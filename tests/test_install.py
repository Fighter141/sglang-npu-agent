"""Installer regression tests: CPU only, isolated files, no user configuration."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", ROOT / "scripts/install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / "source"
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        self.source = self.repo / ".agents/skills"
        self.project = self.root / "project"
        self.target = self.project / ".agents/skills"
        self.global_target = self.root / "global/skills"
        self.patch = mock.patch.multiple(
            installer, ROOT=self.repo, SOURCE=self.source, GLOBAL_TARGET=self.global_target
        )
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def run_cli(self, *args, stdin="", interactive=False):
        class Input(io.StringIO):
            def isatty(self):
                return interactive

        output = io.StringIO()
        with mock.patch.object(sys, "argv", ["install.py", *map(str, args)]), \
                mock.patch.object(sys, "stdin", Input(stdin)), \
                contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            try:
                code = installer.main()
            except SystemExit as exc:
                code = exc.code
        return code, output.getvalue()

    def install(self, *names, **kwargs):
        return self.run_cli("install", *names, "--target", self.project, **kwargs)

    def fixture_skill(self, path):
        path.mkdir(parents=True)
        (path / "SKILL.md").write_text("unrelated skill\n", encoding="utf-8")
        return path

    def test_install_all_and_status(self):
        self.assertEqual(self.install("--all")[0], 0)
        expected = {p.name for p in self.source.iterdir()}
        self.assertEqual({p.name for p in self.target.iterdir()}, expected)
        code, output = self.run_cli("status", "--target", self.project)
        self.assertEqual(code, 0)
        for name in expected:
            self.assertIn(name, output)

    def test_portable_project_references(self):
        self.assertEqual(self.install("sglang-npu-project")[0], 0)
        bundle = self.target / "sglang-npu-project/references/project"
        for name in ["AGENTS.md", "docs/architecture.md", "knowledge/index.md",
                     "reference/templates/experiment.yaml", "skills/README.md", "LICENSE"]:
            self.assertEqual((bundle / name).read_bytes(), (self.repo / name).read_bytes())
        shutil.rmtree(self.repo)
        self.assertTrue((bundle / "docs/roadmap.md").is_file())
        self.assertFalse((self.project / "AGENTS.md").exists())

    def test_force_self_install_preserves_source(self):
        skill = self.source / "sglang-npu-project/SKILL.md"
        original = skill.read_bytes()
        code, _ = self.run_cli("install", "sglang-npu-project", "--target", self.repo, "--force")
        self.assertNotEqual(code, 0)
        self.assertEqual(skill.read_bytes(), original)

    def test_uninstall_all_preserves_other_skills(self):
        self.assertEqual(self.install("sglang-npu-project")[0], 0)
        unrelated = self.fixture_skill(self.target / "another-project-skill")
        # An untracked legacy skill with a known name is also preserved.
        legacy = self.fixture_skill(self.target / "sglang-benchmark")
        code, _ = self.run_cli("uninstall", "--all", "--target", self.project)
        self.assertEqual(code, 0)
        self.assertFalse((self.target / "sglang-npu-project").exists())
        self.assertTrue((unrelated / "SKILL.md").exists())
        self.assertTrue((legacy / "SKILL.md").exists())

    def test_unknown_skill_fails_before_partial_install(self):
        code, _ = self.install("sglang-npu-project", "does-not-exist")
        self.assertNotEqual(code, 0)
        self.assertFalse(self.target.exists())

    def test_global_install_is_isolated_and_removable(self):
        self.assertEqual(self.run_cli("install", "sglang-benchmark", "--global")[0], 0)
        self.assertTrue((self.global_target / "sglang-benchmark/SKILL.md").is_file())
        self.assertEqual(self.run_cli("uninstall", "sglang-benchmark", "--global")[0], 0)
        self.assertFalse((self.global_target / "sglang-benchmark").exists())

    def test_existing_install_is_preserved_without_force(self):
        self.install("sglang-benchmark")
        skill = self.target / "sglang-benchmark/SKILL.md"
        skill.write_text("local edits", encoding="utf-8")
        self.assertEqual(self.install("sglang-benchmark")[0], 0)
        self.assertEqual(skill.read_text(), "local edits")
        self.assertEqual(self.install("sglang-benchmark", "--force")[0], 0)
        self.assertEqual(skill.read_bytes(), (self.source / "sglang-benchmark/SKILL.md").read_bytes())

    def test_copy_failure_preserves_previous_install(self):
        self.install("sglang-benchmark")
        skill = self.target / "sglang-benchmark/SKILL.md"
        skill.write_text("previous working version", encoding="utf-8")
        with mock.patch.object(installer.shutil, "copytree", side_effect=OSError("disk full")):
            code, output = self.install("sglang-benchmark", "--force")
        self.assertNotEqual(code, 0)
        self.assertIn("disk full", output)
        self.assertEqual(skill.read_text(), "previous working version")
        self.assertFalse(list(self.target.glob(".sglang-install-*")))

    def test_publish_failure_rolls_back_previous_install(self):
        self.install("sglang-benchmark")
        skill = self.target / "sglang-benchmark/SKILL.md"
        skill.write_text("previous working version", encoding="utf-8")
        rename = Path.rename

        def fail_publish(path, target):
            if path.name == "prepared":
                raise OSError("publish failed")
            return rename(path, target)

        with mock.patch.object(Path, "rename", fail_publish):
            code, _ = self.install("sglang-benchmark", "--force")
        self.assertNotEqual(code, 0)
        self.assertEqual(skill.read_text(), "previous working version")
        self.assertFalse(list(self.target.glob(".sglang-install-*")))

    def test_rollback_failure_preserves_backup_for_recovery(self):
        self.install("sglang-benchmark")
        original = (self.target / "sglang-benchmark/SKILL.md").read_bytes()
        rename = Path.rename

        def fail_publish_and_restore(path, target):
            if path.name in {"prepared", "previous"}:
                raise OSError("rename failed")
            return rename(path, target)

        with mock.patch.object(Path, "rename", fail_publish_and_restore):
            code, output = self.install("sglang-benchmark", "--force")
        self.assertNotEqual(code, 0)
        backups = list(self.target.glob(".sglang-install-*/previous/SKILL.md"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_bytes(), original)
        self.assertIn(str(backups[0].parent), output)

    def test_uninstall_source_is_rejected(self):
        for selection in [("--all",), ("sglang-benchmark",)]:
            code, _ = self.run_cli("uninstall", *selection, "--target", self.repo)
            self.assertNotEqual(code, 0)
        self.assertEqual(len(list(self.source.glob("*/SKILL.md"))), 11)

    def test_non_force_self_install_is_noop(self):
        self.assertEqual(self.run_cli("install", "--all", "--target", self.repo)[0], 0)
        self.assertFalse(list(self.source.glob("*/" + installer.MARKER)))

    def test_named_uninstall_preserves_unmanaged_skill(self):
        skill = self.fixture_skill(self.target / "sglang-benchmark")
        code, _ = self.run_cli("uninstall", "sglang-benchmark", "--target", self.project)
        self.assertNotEqual(code, 0)
        self.assertTrue((skill / "SKILL.md").exists())
        self.assertEqual(self.install("sglang-benchmark", "--force")[0], 0)
        self.assertEqual(self.run_cli("uninstall", "sglang-benchmark", "--target", self.project)[0], 0)

    def test_uninstall_preflights_entire_selection(self):
        self.install("sglang-npu-project")
        self.fixture_skill(self.target / "unmanaged")
        code, _ = self.run_cli("uninstall", "sglang-npu-project", "unmanaged", "--target", self.project)
        self.assertNotEqual(code, 0)
        self.assertTrue((self.target / "sglang-npu-project/SKILL.md").exists())

    def test_corrupt_or_foreign_marker_is_not_owned(self):
        self.install("sglang-benchmark")
        skill = self.target / "sglang-benchmark"
        marker = skill / installer.MARKER
        for contents in ["{bad json", "null", json.dumps({
                "schema_version": 1, "repository": "other/project", "skill": skill.name})]:
            marker.write_text(contents, encoding="utf-8")
            self.assertEqual(self.run_cli("uninstall", "--all", "--target", self.project)[0], 0)
            self.assertTrue((skill / "SKILL.md").exists())

    def test_path_arguments_do_not_escape_target(self):
        victim = self.fixture_skill(self.root / "victim")
        for command in ["install", "uninstall"]:
            for name in [str(victim), "../../../victim", "../victim", ".", ".."]:
                code, _ = self.run_cli(command, name, "--target", self.project)
                self.assertNotEqual(code, 0)
                self.assertTrue((victim / "SKILL.md").exists())

    def test_skill_symlink_does_not_delete_external_files(self):
        victim = self.fixture_skill(self.root / "victim")
        self.target.mkdir(parents=True)
        (self.target / "sglang-benchmark").symlink_to(victim, target_is_directory=True)
        self.assertNotEqual(self.install("sglang-benchmark", "--force")[0], 0)
        self.assertNotEqual(self.run_cli("uninstall", "sglang-benchmark", "--target", self.project)[0], 0)
        self.assertTrue((victim / "SKILL.md").exists())

    def test_broken_target_symlink_is_rejected(self):
        self.target.mkdir(parents=True)
        link = self.target / "sglang-benchmark"
        link.symlink_to(self.root / "missing")
        self.assertNotEqual(self.install("sglang-benchmark", "--force")[0], 0)
        self.assertTrue(link.is_symlink())

    def test_symlinked_target_parent_is_rejected(self):
        self.project.mkdir()
        external = self.root / "external"
        external.mkdir()
        (self.project / ".agents").symlink_to(external, target_is_directory=True)
        self.assertNotEqual(self.install("sglang-benchmark")[0], 0)
        self.assertEqual(list(external.iterdir()), [])

    def test_symlinked_source_is_not_copied(self):
        victim = self.root / "private.txt"
        victim.write_text("do not distribute", encoding="utf-8")
        (self.source / "sglang-benchmark/linked.txt").symlink_to(victim)
        self.assertNotEqual(self.install("sglang-benchmark")[0], 0)
        self.assertFalse(self.target.exists())

    def test_target_inside_source_is_rejected(self):
        code, _ = self.run_cli("install", "sglang-benchmark", "--target", self.source / "sglang-benchmark/nested")
        self.assertNotEqual(code, 0)
        self.assertFalse((self.source / "sglang-benchmark/nested").exists())

    def test_missing_bundle_source_fails_before_install(self):
        shutil.rmtree(self.repo / "knowledge")
        self.assertNotEqual(self.install("--all")[0], 0)
        self.assertFalse(self.target.exists())

    def test_doctor_finds_missing_installed_reference(self):
        self.install("sglang-npu-project")
        self.assertEqual(self.run_cli("doctor", "--target", self.project)[0], 0)
        (self.target / "sglang-npu-project/references/project/docs/architecture.md").unlink()
        self.assertNotEqual(self.run_cli("doctor", "--target", self.project)[0], 0)

    def test_empty_source_fails_without_creating_target(self):
        shutil.rmtree(self.source)
        self.source.mkdir()
        for command in ["list", "doctor"]:
            self.assertNotEqual(self.run_cli(command, "--target", self.project)[0], 0)
        self.assertNotEqual(self.install("--all")[0], 0)
        self.assertFalse(self.target.exists())

    def test_noninteractive_install_requires_selection(self):
        self.assertNotEqual(self.install()[0], 0)
        self.assertFalse(self.target.exists())

    def test_interactive_selection_and_cancel(self):
        self.assertEqual(self.install(stdin="1,2\n", interactive=True)[0], 0)
        self.assertEqual(len(list(self.target.glob("*/SKILL.md"))), 2)
        self.assertEqual(self.install(stdin="\n", interactive=True)[0], 0)
        self.assertNotEqual(self.install(stdin="999\n", interactive=True)[0], 0)
        self.assertNotEqual(self.install(stdin="", interactive=True)[0], 0)

    def test_incompatible_options_fail(self):
        for args in [("install", "--all", "sglang-benchmark"),
                     ("install", "--all", "--global", "--target", self.project),
                     ("uninstall", "--all", "--force"), ("doctor", "--all")]:
            self.assertNotEqual(self.run_cli(*args)[0], 0)
        self.assertFalse(self.target.exists())


if __name__ == "__main__":
    unittest.main()
