import os
import shutil
import logging
import importlib.util
from typing import Optional

class SelfModificationError(Exception):
    pass

class SelfModification:
    """
    Provides safe, auditable self-modification for Athena.
    Allows proposing, validating, and applying code/config changes with rollback and logging.
    """
    def __init__(self, backup_dir: str = "selfmod_backups"):
        self.backup_dir = backup_dir
        os.makedirs(self.backup_dir, exist_ok=True)
        self.log_file = os.path.join(self.backup_dir, "selfmod.log")

    def backup_file(self, file_path: str) -> str:
        base = os.path.basename(file_path)
        backup_path = os.path.join(self.backup_dir, f"{base}.bak")
        shutil.copy2(file_path, backup_path)
        self._log(f"Backup created: {backup_path}")
        return backup_path

    def validate_python_code(self, code: str) -> bool:
        try:
            compile(code, '<string>', 'exec')
            return True
        except Exception as e:
            self._log(f"Validation failed: {e}")
            return False

    def propose_change(self, file_path: str, new_code: str) -> bool:
        if not os.path.isfile(file_path):
            self._log(f"File not found: {file_path}")
            raise SelfModificationError(f"File not found: {file_path}")
        if not self.validate_python_code(new_code):
            raise SelfModificationError("Proposed code did not pass validation.")
        self.backup_file(file_path)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_code)
        self._log(f"Applied change to {file_path}")
        return True

    def rollback(self, file_path: str) -> bool:
        base = os.path.basename(file_path)
        backup_path = os.path.join(self.backup_dir, f"{base}.bak")
        if not os.path.isfile(backup_path):
            self._log(f"No backup found for {file_path}")
            return False
        shutil.copy2(backup_path, file_path)
        self._log(f"Rolled back {file_path} to backup")
        return True

    def _log(self, message: str):
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(message + "\n")
        logging.info(f"[SelfMod] {message}")

    def reload_module(self, module_name: str) -> Optional[object]:
        try:
            if module_name in globals():
                importlib.reload(globals()[module_name])
            else:
                importlib.import_module(module_name)
            self._log(f"Reloaded module: {module_name}")
            return globals().get(module_name)
        except Exception as e:
            self._log(f"Failed to reload module {module_name}: {e}")
            return None
