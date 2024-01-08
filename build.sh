#!/usr/bin/env nix-shell
#! nix-shell -i python3.11 -p python3

import subprocess
import glob
import os
from pathlib import Path
import ycppc

def set_cwd_to_script_dir():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
set_cwd_to_script_dir()

os.makedirs("build", exist_ok=True)

res = subprocess.run(["git", "ls-files"], check=True, capture_output=True, text=True)
files = res.stdout.splitlines()
def do_not_apply(file_path):
    _, ext = os.path.splitext(file_path)
    return ext == '.sh' or ext == '.py'
files = filter(lambda file: not do_not_apply(file), files)

for file in files:
    content = None
    with open(file, 'r') as fin:
        content = fin.read()
    
    content = ycppc.apply(content)

    output_path = Path(f'build/{file}')
    output_path.parent.mkdir(exist_ok=True, parents=True)
    with open(output_path, 'w') as fout:
        fout.write(content)