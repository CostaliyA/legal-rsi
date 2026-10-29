"""Install the grouped release into a VERL checkout without changing module imports."""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess

def install(target: Path, apply: bool = False) -> dict:
    source = Path(__file__).resolve().parent
    target = target.expanduser().resolve()
    if not (target/'verl/trainer/main_ppo.py').is_file():
        raise ValueError('Target must be a VERL checkout containing verl/trainer/main_ppo.py')
    entries = json.loads((source/'install_manifest.json').read_text())
    pending=[]
    for item in entries:
        src=(source/item['source']).resolve();dst=(target/item['destination']).resolve()
        if not src.is_relative_to(source) or not dst.is_relative_to(target):
            raise ValueError('Manifest path escapes its root')
        if hashlib.sha256(src.read_bytes()).hexdigest()!=item['sha256']:
            raise ValueError(f'Release source hash mismatch: {src}')
        if dst.exists():
            if not dst.is_file() or hashlib.sha256(dst.read_bytes()).hexdigest()!=item['sha256']:
                raise ValueError(f'Existing file differs; back it up before installing: {dst}')
        else:pending.append((src,dst,item['executable']))
    patch=source/'verl_core.patch'
    def check(reverse=False):
        return subprocess.run(['git','apply','--check',*(['--reverse'] if reverse else []),str(patch)],cwd=target,capture_output=True).returncode==0
    if check(True):state='already_applied'
    elif check():state='apply_needed'
    else:raise ValueError('VERL core does not match the base or the supplied patch')
    if apply:
        if state=='apply_needed':subprocess.run(['git','apply',str(patch)],cwd=target,check=True)
        for src,dst,executable in pending:
            dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
            if executable:dst.chmod(0o755)
    return {'verl_root':str(target),'core_patch':state,'new_source_files':len(pending),'applied':apply}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--verl-root',type=Path,required=True)
    p.add_argument('--apply',action='store_true',help='Apply after validation; default checks only')
    a=p.parse_args();print(json.dumps(install(a.verl_root,a.apply),indent=2))
