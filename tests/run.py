#!/usr/bin/env python3
"""Build and run luce-psd's test blocks in native and C modes."""
import os, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent / "luce-base/build/luce-base"
MODES = [["--native"], ["--backend=c"]]
env = dict(os.environ, LUCE_BASE=str(BASE.resolve()))
for flags in MODES:
    subprocess.run([str(BASE.resolve()), "test", str(ROOT / "src/luce_psd/psd.lucb"), *flags],
                   env=env, check=True, timeout=180)
print("PASS luce-psd parser")
