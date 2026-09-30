# V2 — two hand-crafted demo designs (one bespoke template per business), built AFTER data_lot1.py:
#   dar-mrad-nabeul (v2_darmrad.py), haouaria-beach (v2_haouaria.py). (royal-palace-beni-khalled removed 30/09/2026.)
# Replaces ONLY the generic lot-1 output of these 2 slugs. Images: free-licence Wikimedia Commons photos
# listed in titles_v2.json, fetched at build time and resized to WebP (1280 + 640 px).
import json, os, re, io, sys, time, shutil, html, urllib.request, urllib.parse
from urllib.parse import quote
GEN = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, GEN)
ROOT = os.environ.get('DEMOS_ROOT', '/workspace/demos')
UA = {'User-Agent': 'SynarisDemos/1.0 (https://github.com/islemyakoubi/synaris-demos) build-bot'}
CONSULTED = '30/09/2026'
RIBBON = "<b>Démo</b> — maquette non officielle réalisée par Synaris Labs à partir d'informations publiques, à valider par l'établissement."

def get(url):
    for a in range(6):
        try: return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except Exception as e: print('retry', url[:90], e); time.sleep(8 * (a + 1))
    raise SystemExit('failed ' + url)
strip = lambda s: re.sub('<[^>]+>', '', s or '').strip()
esc = lambda s: html.escape(s, quote=True)
WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>'
PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>'
PIN_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>'
def walink(wa, msg): return f'https://wa.me/{wa}?text=' + quote(msg)

def commons_info(titles):
    info = {}
    for i in range(0, len(titles), 20):
        chunk = titles[i:i + 20]
        q = {'action': 'query', 'format': 'json', 'titles': '|'.join('File:' + t for t in chunk), 'prop': 'imageinfo', 'iiprop': 'url|extmetadata', 'iiurlwidth': 1280}
        d = json.loads(get('https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(q)))
        norm = {n['to']: n['from'] for n in d['query'].get('normalized', [])}
        for pg in d['query']['pages'].values():
            if 'imageinfo' not in pg: raise SystemExit('missing on Commons: ' + pg['title'])
            ii = pg['imageinfo'][0]; m = ii.get('extmetadata', {})
            info[norm.get(pg['title'], pg['title'])[5:]] = {'url': ii['thumburl'], 'title': pg['title'][5:], 'artist': strip(m.get('Artist', {}).get('value', ''))[:60],
                'license': m.get('LicenseShortName', {}).get('value', ''), 'license_url': m.get('LicenseUrl', {}).get('value', ''), 'source': ii['descriptionurl']}
    return info

class Media:
    """Downloads the slug's photos into <slug>/media/ as name.webp (1280) + name-640.webp; keeps credits + sizes."""
    def __init__(self, slug, items, info):
        from PIL import Image
        self.slug, self.dims, self.credits = slug, {}, []
        d = os.path.join(ROOT, slug, 'media'); os.makedirs(d, exist_ok=True)
        for name, title in items:
            it = info[title]; self.credits.append((name, it))
            big, small = os.path.join(d, name + '.webp'), os.path.join(d, name + '-640.webp')
            if not (os.path.exists(big) and os.path.exists(small)):
                im = Image.open(io.BytesIO(get(it['url']))).convert('RGB')
                im.thumbnail((1280, 1280)); im.save(big, 'WEBP', quality=74, method=6)
                s = im.copy(); s.thumbnail((640, 640)); s.save(small, 'WEBP', quality=72, method=6)
                if name == 'hero': im.save(os.path.join(d, 'hero.jpg'), 'JPEG', quality=76, optimize=True, progressive=True)
                print(slug, name); time.sleep(0.4)
            with Image.open(big) as im: self.dims[name] = im.size
    def img(self, name, alt, cls='', sizes='(max-width: 700px) 100vw, 50vw', lazy=True, extra=''):
        w, h = self.dims[name]
        c = ' class="%s"' % cls if cls else ''
        ld = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
        return (f'<img{c} src="media/{name}-640.webp" srcset="media/{name}-640.webp 640w, media/{name}.webp {w}w" '
                f'sizes="{sizes}" width="{w}" height="{h}" alt="{esc(alt)}"{ld}{extra}>')
    def credits_html(self):
        return ''.join(f'<li>{esc(n)} — « {esc(x["title"][:80])} » par {esc(x["artist"] or "auteur Wikimedia")}, '
                       f'<a href="{esc(x["license_url"] or x["source"])}" target="_blank" rel="noopener">{esc(x["license"])}</a>, via '
                       f'<a href="{esc(x["source"])}" target="_blank" rel="noopener">Wikimedia Commons</a></li>' for n, x in self.credits)

def clean_old(slug):
    """Remove the generic lot-1 files of this slug (the v2 page uses its own media/ + inline CSS/JS)."""
    base = os.path.join(ROOT, slug)
    for f in ('site.css', 'site.js', 'index.html'):
        if os.path.exists(os.path.join(base, f)): os.remove(os.path.join(base, f))
    if os.path.isdir(os.path.join(base, 'img')): shutil.rmtree(os.path.join(base, 'img'))

# Shared tiny JS: mobile menu, header state, WhatsApp pre-filled forms, lightbox, tabs.
JS = r'''(function(){var d=document;d.documentElement.classList.add('js');
var y=d.getElementById('year');if(y)y.textContent=new Date().getFullYear();
var hb=d.querySelector('[data-menu]'),nav=d.querySelector('[data-nav]');
if(hb&&nav){hb.addEventListener('click',function(){var o=nav.classList.toggle('open');hb.setAttribute('aria-expanded',o)});
nav.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){nav.classList.remove('open');hb.setAttribute('aria-expanded','false')})})}
var hd=d.querySelector('[data-header]');if(hd){var f=function(){hd.classList.toggle('scrolled',window.scrollY>40)};f();window.addEventListener('scroll',f,{passive:true})}
d.querySelectorAll('form[data-wa]').forEach(function(fm){fm.addEventListener('submit',function(e){e.preventDefault();
if(!fm.reportValidity())return;var L=[fm.getAttribute('data-intro')];
fm.querySelectorAll('[name]').forEach(function(el){if(el.disabled||!el.value)return;var l=el.getAttribute('data-label')||el.name;
var v=el.value;if(el.type==='date'){var p=v.split('-');v=p[2]+'/'+p[1]+'/'+p[0]}L.push('• '+l+' : '+v)});
window.open('https://wa.me/'+fm.getAttribute('data-wa')+'?text='+encodeURIComponent(L.join('\n')),'_blank','noopener')})});
d.querySelectorAll('[data-tabs]').forEach(function(t){var bs=t.querySelectorAll('[role=tab]');bs.forEach(function(b){b.addEventListener('click',function(){
bs.forEach(function(x){x.setAttribute('aria-selected',x===b)});var fm=t.querySelector('form');fm.setAttribute('data-intro',b.getAttribute('data-intro'));
fm.querySelectorAll('[data-only]').forEach(function(el){var on=el.getAttribute('data-only')===b.getAttribute('data-mode');el.hidden=!on;el.querySelectorAll('input,select,textarea').forEach(function(i){i.disabled=!on})});
var s=fm.querySelector('[type=submit] span');if(s)s.textContent=b.getAttribute('data-cta')})})});
var lb=d.querySelector('.lb');if(lb){var li=lb.querySelector('img');d.querySelectorAll('[data-full]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();
li.src=a.getAttribute('data-full');li.alt=a.querySelector('img').alt;lb.classList.add('open');lb.querySelector('button').focus()})});
var c=function(){lb.classList.remove('open');li.removeAttribute('src')};lb.addEventListener('click',function(e){if(e.target!==li)c()});d.addEventListener('keydown',function(e){if(e.key==='Escape')c()})}
})();'''

def page(S, M, fonts_url, css, body, theme_color):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(S['title'])}</title>
<meta name="description" content="{esc(S['desc'])}">
<meta name="robots" content="noindex,nofollow">
<meta name="theme-color" content="{theme_color}">
<meta property="og:title" content="{esc(S['title'])}"><meta property="og:description" content="{esc(S['desc'])}"><meta property="og:image" content="media/hero.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts_url}" rel="stylesheet">
<link rel="preload" as="image" href="media/hero-640.webp" imagesrcset="media/hero-640.webp 640w, media/hero.webp 1280w" imagesizes="100vw">
<link rel="icon" href="{S['favicon']}">
<style>{css}</style>
</head>
<body>
{body}
<script>{JS}</script>
</body>
</html>'''

def write(slug, h):
    open(os.path.join(ROOT, slug, 'index.html'), 'w').write(h); print('built v2', slug, len(h))

if __name__ == '__main__':
    T = json.load(open(os.path.join(GEN, 'titles_v2.json')))
    info = commons_info(sorted({t for v in T.values() for _, t in v}))
    import v2_darmrad, v2_haouaria
    for mod in (v2_darmrad, v2_haouaria):
        slug = mod.SLUG; clean_old(slug)
        M = Media(slug, T[slug], info)
        write(slug, mod.build(M))
