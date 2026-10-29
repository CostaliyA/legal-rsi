import sys, tempfile, shutil, subprocess, os
from pathlib import Path
src=Path(sys.argv[1]).absolute(); dst=Path(sys.argv[2]).absolute()
work=Path(tempfile.mkdtemp())
shutil.copy(src, work/"in.docx")
profile=tempfile.mkdtemp(prefix="soprof-")
macro_dir=work/"user"/"basic"/"Standard"; macro_dir.mkdir(parents=True)
shutil.copy("/tmp/lo/upd.bas", macro_dir/"Module1.xba")
script=macro_dir/"script.xlb"
script.write_text('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE library:library PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "library.dtd">\n<library:library xmlns:library="http://openoffice.org/2000/library" library:name="Standard" library:readonly="false" library:passwordprotected="false">\n <library:element library:name="Module1"/>\n</library:library>\n')
(macro_dir.parent/"script.xlc").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE library:libraries PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "libraries.dtd">\n<library:libraries xmlns:library="http://openoffice.org/2000/library" xmlns:xlink="http://www.w3.org/1999/xlink">\n <library:library library:name="Standard" xlink:href="$(USER)/basic/Standard/script.xlb/" xlink:type="simple" library:link="false"/>\n</library:libraries>\n')
cmd=["soffice","--headless","--norestore","--nologo",f"-env:UserInstallation=file://{profile}",
     f"macro:///Standard.Module1.UpdateIndexes", str(work/"in.docx")]
r=subprocess.run(cmd,capture_output=True,text=True,timeout=300)
print("rc",r.returncode, r.stderr[-500:])
shutil.copy(work/"in.docx", dst)
print("wrote",dst)
