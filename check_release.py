"""Check grouped source hashes, data paths, reward arithmetic and retained gains."""
from pathlib import Path
import hashlib,json,math
root=Path(__file__).resolve().parent
for x in json.loads((root/'code/install_manifest.json').read_text()):
 p=root/'code'/x['source'];assert hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256'],str(p)
for name,count in [('01_gain_epoch1',7),('02_no_gain_latest',20)]:
 data=root/'data'/name;index=json.loads((data/'DATA_INDEX.json').read_text());assert len(index['runs'])==count
 old=[];new=[];feedback=0
 for row in index['runs']:
  d=data/row['run'];s=json.loads((d/'scores.json').read_text());m=json.loads((d/'rollout_metadata.json').read_text())
  assert (data/row['transcript']).is_file()
  assert m['task_id']==s['task_id']==row['task_id'] and s['n_grading_errors']==0
  q=s['n_passed']/s['n_criteria'];u=int(s['n_passed']==s['n_criteria'])+s.get('beta',.2)*q
  assert math.isclose(u,s['reward_task'],abs_tol=1e-10)
  if s.get('rubric_feedback_file'):
   p=d/s['rubric_feedback_file'];assert hashlib.sha256(p.read_bytes()).hexdigest()==s['rubric_feedback_sha256'];feedback+=1
  parts=Path(row['run']).parts
  if name=='01_gain_epoch1' and parts[0]=='validation':
   (old if parts[-1]=='old' else new).append(u)
  elif name=='02_no_gain_latest' and parts[0] in ('test_old','test_new'):
   (old if parts[0]=='test_old' else new).append(u)
 assert math.isclose(sum(new)/len(new)-sum(old)/len(old),index['mean_gain'],abs_tol=1e-10)
 print(name,':',count,'scored trajectories;',feedback,'feedback hashes checked; gain=',index['mean_gain'])
print('Release checks passed')
