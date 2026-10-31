"""Check the built wheel without importing the source checkout or GPU runtime."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile

env = dict(os.environ)
env.pop("PYTHONPATH", None)
code = """
from pathlib import Path
from importlib.metadata import version
import nnunetv2.paths as paths
assert 'site-packages' in str(Path(paths.__file__).resolve())
assert hasattr(paths.nnUNet_raw, 'is_set')
print('Installed CPU paths import passed:', version('nnunetv2'))
"""
with tempfile.TemporaryDirectory() as tmp:
    subprocess.run([sys.executable, "-c", code], cwd=tmp, env=env, check=True)
