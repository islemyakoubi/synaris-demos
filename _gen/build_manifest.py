# Builds images.json (credits + 1280px URLs) from titles.json via the Wikimedia Commons API, then downloads images.
import json, os, re, time, urllib.request, urllib.parse
GEN=os.path.dirname(os.path.abspath(__file__)); ROOT=os.environ.get('DEMOS_ROOT','/workspace/demos')
UA={'User-Agent':'SynarisDemos/1.0 (https://github.com/islemyakoubi/synaris-demos) build-bot'}
def get(url):
    for a in range(6):
        try: return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read()
        except Exception as e: print('retry',url[:90],e); time.sleep(10*(a+1))
    raise SystemExit('failed '+url)
strip=lambda s: re.sub('<[^>]+>','',s or '').strip()
T=json.load(open(os.path.join(GEN,'titles.json')))
allt=sorted({t for v in T.values() for _,t in v}); info={}
for i in range(0,len(allt),20):
    chunk=allt[i:i+20]
    q={'action':'query','format':'json','titles':'|'.join('File:'+t for t in chunk),'prop':'imageinfo','iiprop':'url|extmetadata','iiurlwidth':1280}
    d=json.loads(get('https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(q)))
    norm={n['to']:n['from'] for n in d['query'].get('normalized',[])}
    for pg in d['query']['pages'].values():
        ii=pg['imageinfo'][0]; m=ii.get('extmetadata',{})
        key=norm.get(pg['title'],pg['title'])[5:]
        info[key]={'url':ii['thumburl'],'title':pg['title'][5:],'artist':strip(m.get('Artist',{}).get('value',''))[:60],
                   'license':m.get('LicenseShortName',{}).get('value',''),'license_url':m.get('LicenseUrl',{}).get('value',''),'source':ii['descriptionurl']}
man={s:[dict(file=f'img/{n}.jpg',**info[t]) for n,t in v] for s,v in T.items()}
json.dump(man,open(os.path.join(GEN,'images.json'),'w'),ensure_ascii=False,separators=(',',':'))
for slug,items in man.items():
    os.makedirs(os.path.join(ROOT,slug,'img'),exist_ok=True)
    for it in items:
        fn=os.path.join(ROOT,slug,it['file'])
        if os.path.exists(fn): continue
        b=get(it['url'])
        try:
            import io; from PIL import Image
            im=Image.open(io.BytesIO(b)).convert('RGB'); im.thumbnail((1600,1600)); im.save(fn,quality=78,optimize=True,progressive=True)
        except ImportError: open(fn,'wb').write(b)
        print(slug,it['file']); time.sleep(0.5)
