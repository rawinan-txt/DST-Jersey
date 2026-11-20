import base64,json
s=open('src.html').read()
s=s.replace("const slots = Math.max(0, 3 - S.designs.length);","const shown = S.designs.filter(x=>x.status!=='hidden'); const slots = Math.max(0, 3 - shown.length);")
s=s.replace("${S.designs.map(x=>`<button class=\"dcard","${shown.map(x=>`<button class=\"dcard")
s=s.replace("แบบที่ ${S.designs.length+i+1}","แบบที่ ${shown.length+i+1}")
imgs={f'{k}-{n}':'data:image/webp;base64,'+base64.b64encode(open(f'img/{k}-{n}.webp','rb').read()).decode() for k in ['black','green'] for n in ['front','back','collar','fabric','sleeve','blank']}
from PIL import Image
dims={f'{k}-blank':'%d/%d'%Image.open(f'img/{k}-blank.webp').size for k in ['black','green']}
open('index.html','w').write(s.replace('%%IMAGES%%',json.dumps(imgs)).replace('%%DIMS%%',json.dumps(dims)))
