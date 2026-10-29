import subprocess, json, re, sys
pdf = sys.argv[1] if len(sys.argv)>1 else "pass1.pdf"
n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo",pdf],capture_output=True,text=True).stdout).group(1))
pages = {}
for i in range(3, n+1):
    txt = subprocess.run(["pdftotext","-f",str(i),"-l",str(i),"-layout",pdf,"-"],capture_output=True,text=True).stdout
    for line in txt.splitlines():
        s = line.strip()
        m = re.match(r"^(ARTICLE\s+(\d+))\s*[—\-]", s)
        if m:
            key = "ARTICLE "+m.group(2)
            if key not in pages: pages[key]=i
        if s == "RECITALS" and "RECITALS" not in pages: pages["RECITALS"]=i
        if s.startswith("SIGNATURE PAGE") and "SIGNATURE" not in pages: pages["SIGNATURE"]=i
        if s.startswith("NOTARY ACKNOWLEDGMENT") and "NOTARY" not in pages: pages["NOTARY"]=i
        m2 = re.match(r"^(EXHIBIT\s+([A-F]))\s*[—\-]", s)
        if m2:
            key = "# EXHIBIT "+m2.group(2)
            if key not in pages: pages[key]=i
print(json.dumps(pages, indent=1))
print("TOTAL PAGES", n, file=sys.stderr)
