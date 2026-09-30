# Lot 2 : 20 sites de démo sur mesure (un gabarit par établissement : l2_*.py), construits après gen_v2.py.
# Faits : lot2_facts.json (repris du fichier prospects, rien d'inventé). Photos : titles_lot2.json (Wikimedia Commons, licences libres).
# Médecins / dentistes : site informatif (Charte web CNOM) : pas d'avis, pas de témoignages, pas de promotion.
import json, os, re, io, sys, time, html, importlib, urllib.request, urllib.parse
from urllib.parse import quote
GEN = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, GEN)
ROOT = os.environ.get('DEMOS_ROOT', '/workspace/demos')
UA = {'User-Agent': 'SynarisDemos/1.0 (https://github.com/islemyakoubi/synaris-demos) build-bot'}
CONSULTED = '30/09/2026'
NB = '\u00a0'
RIBBON = "<b>Démo</b> — maquette non officielle réalisée par Synaris Labs à partir d'informations publiques, à valider par l'établissement."
MODS = {'nb-language-center-dar-chaabane': 'l2_nb', 'dr-manel-attia-hammamet': 'l2_attia', 'dr-nawel-nacef-kelibia': 'l2_nacef',
        'dr-aymen-boujneh-hammamet': 'l2_boujneh', 'dr-mohamed-ghalleb-nabeul': 'l2_ghalleb', 'avocat-aymen-jouida-hammamet': 'l2_jouida',
        'soliman-informatique-langues': 'l2_soliman', 'dr-hend-ben-mustapha-soliman': 'l2_hend', 'dr-yasmine-damergi-nabeul': 'l2_damergi',
        'dr-sarra-haouet-mrezga': 'l2_haouet', 'dr-ichrak-hammami-nabeul': 'l2_hammami', 'dr-houssem-el-manaa-menzel-temime': 'l2_elmanaa',
        'dr-ghada-bassoumi-hammamet': 'l2_bassoumi', 'oralion-dental-clinic-hammamet': 'l2_oralion', 'dr-hamadi-regaieg-hammamet': 'l2_regaieg',
        'dr-obay-becem-kelibia': 'l2_obay', 'dr-imen-kdous-kelibia': 'l2_kdous', 'my-smile-ridene-kelibia': 'l2_mysmile',
        'dr-souha-khefifi-grombalia': 'l2_khefifi', 'lino-garderie-nabeul': 'l2_lino'}

def get(url):
    for a in range(6):
        try: return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except Exception as e: print('retry', url[:90], e); time.sleep(8 * (a + 1))
    raise SystemExit('failed ' + url)
strip = lambda s: re.sub('<[^>]+>', '', s or '').strip()
esc = lambda s: html.escape(s, quote=True)
def walink(wa, msg=''): return f'https://wa.me/{wa}' + ('?text=' + quote(msg) if msg else '')
def telhref(t): return 'tel:' + re.sub(r'[^+0-9]', '', t.split('·')[0])
def ph(t='à confirmer', cls='ph'): return f'<span class="{cls}">{t}</span>'

I = dict(
 wa='<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>',
 phone='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
 pin='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 clock='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 mail='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
 cal='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
 globe='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>',
 tooth='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" aria-hidden="true"><path d="M7 3c-2.5 0-4 2-4 4.5 0 2 .8 3.4 1.4 5 .6 1.8.8 4 1.4 6.2.4 1.6 1.2 2.3 2 2.3 1.6 0 1.4-4.5 2.4-6.4.5-.9 1.1-.9 1.6 0 1 1.9.8 6.4 2.4 6.4.8 0 1.6-.7 2-2.3.6-2.2.8-4.4 1.4-6.2.6-1.6 1.4-3 1.4-5C21 5 19.5 3 17 3c-2 0-3 1-5 1S9 3 7 3z"/></svg>',
 eye='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3.2"/></svg>',
 heart='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M12 20s-7.5-4.6-9.3-9.2C1.4 7.4 3.6 4 7 4c2.1 0 3.6 1.2 5 3 1.4-1.8 2.9-3 5-3 3.4 0 5.6 3.4 4.3 6.8C19.5 15.4 12 20 12 20z"/><path d="M3 12h4l2-3 3 6 2-3h7"/></svg>',
)

DAYS = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
def hours(F):
    """[(n, jour, valeur, connu)] : seul le jour relevé sur la fiche Google (30/09/2026) est renseigné."""
    known = {3: F.get('wed'), 4: F.get('thu')}
    return [(i + 1, d, known.get(i + 1) or 'à confirmer', bool(known.get(i + 1))) for i, d in enumerate(DAYS)]
HOURS_NOTE = f"Horaire relevé sur la fiche Google le {CONSULTED}. Autres jours et horaires complets à confirmer avec l'établissement."
def hours_short(F):
    if F.get('wed'): return f"Mercredi {F['wed']}, autres jours à confirmer"
    if F.get('thu'): return f"Jeudi {F['thu']}, autres jours à confirmer"
    return 'Horaires à confirmer'

def compliance(F):
    k = F['kind']
    if k == 'med': return ("Site d'information du cabinet, conçu selon la Charte web du Conseil national de l'Ordre des médecins : identité, qualification, "
                           "coordonnées, horaires et accès uniquement. Aucun avis de patient, aucun témoignage, aucune publicité. À déclarer au Conseil régional de l'Ordre avant mise en ligne.")
    if k == 'dent': return ("Site d'information du cabinet dentaire, conçu dans l'esprit du Code de déontologie des médecins dentistes et de la Charte Internet du CNOMDT : "
                            "informations pratiques uniquement, aucun avis de patient, aucun témoignage, aucune publicité. À déclarer au Conseil de l'Ordre avant mise en ligne.")
    if k == 'law': return ("Site d'information du cabinet : coordonnées, horaires et accès. Pas de liste de clients, pas de publicité. La création du site est à signaler "
                           "au Conseil de l'Ordre national des avocats. Aucune consultation juridique n'est donnée par ce site ni par WhatsApp : le formulaire sert uniquement à demander un rendez-vous.")
    return ''

def mapframe(F, cls='map'):
    q = quote(F['q'])
    return f'<iframe class="{cls}" title="Carte : {esc(F["name"])}, {esc(F["city"])}" src="https://maps.google.com/maps?q={q}&z=15&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'

def fields(spec):
    """spec : liste de (type, libellé, [options]) -> champs de formulaire (le message WhatsApp reprend libellé : valeur)."""
    out = []
    for f in spec:
        t, lab = f[0], f[1]; n = re.sub(r'[^a-z]', '', lab.lower())[:12] or 'x'
        full = ' class="full"' if t in ('textarea', 'full', 'fulltel') else ''
        if t == 'select': w = f'<select name="{n}" data-label="{esc(lab)}">' + ''.join(f'<option>{esc(o)}</option>' for o in f[2]) + '</select>'
        elif t == 'textarea': w = f'<textarea name="{n}" data-label="{esc(lab)}" rows="3"></textarea>'
        elif t == 'date': w = f'<input type="date" name="{n}" data-label="{esc(lab)}">'
        elif t in ('tel', 'fulltel'): w = f'<input type="tel" name="{n}" data-label="{esc(lab)}" inputmode="tel" autocomplete="tel" required>'
        else: w = f'<input name="{n}" data-label="{esc(lab)}" autocomplete="name" required>'
        out.append(f'<label{full}><span>{esc(lab)}</span>{w}</label>')
    return ''.join(out)
MED_FORM = [('text', 'Nom et prénom'), ('tel', 'Téléphone'), ('date', 'Jour souhaité'), ('select', 'Moment', ['Matin', 'Après-midi', 'Peu importe']),
            ('select', 'Première visite au cabinet', ['Oui', 'Non']), ('textarea', 'Message (facultatif)')]
FORM_NOTE = "Démo : aucune donnée n'est enregistrée. Le bouton ouvre WhatsApp avec votre message ; le cabinet confirme le rendez-vous. En cas d'urgence, appelez le 190 (SAMU)."
def form(F, intro, spec, btn, cls='form', note=None):
    return (f'<form class="{cls}" data-wa="{F["wa"]}" data-intro="{esc(intro)}" novalidate>{fields(spec)}'
            f'<button type="submit">{I["wa"]}<span>{btn}</span></button><p class="fnote">{note or FORM_NOTE}</p></form>')

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
    """Photos du site dans <slug>/media/ : nom.webp (1280) + nom-640.webp ; garde crédits et dimensions."""
    def __init__(self, slug, items, info):
        from PIL import Image
        self.dims, self.cr = {}, []
        d = os.path.join(ROOT, slug, 'media'); os.makedirs(d, exist_ok=True)
        for name, title in items:
            it = info[title]; self.cr.append((name, it))
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
        c = f' class="{cls}"' if cls else ''
        ld = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
        return (f'<img{c} src="media/{name}-640.webp" srcset="media/{name}-640.webp 640w, media/{name}.webp {w}w" '
                f'sizes="{sizes}" width="{w}" height="{h}" alt="{esc(alt)}"{ld}{extra}>')
    def credits(self, extra=''):
        li = ''.join(f'<li>{esc(n)} — « {esc(x["title"][:80])} » par {esc(x["artist"] or "auteur Wikimedia")}, '
                     f'<a href="{esc(x["license_url"] or x["source"])}" target="_blank" rel="noopener">{esc(x["license"])}</a>, via '
                     f'<a href="{esc(x["source"])}" target="_blank" rel="noopener">Wikimedia Commons</a></li>' for n, x in self.cr)
        return f'<details class="credits"><summary>Crédits photos (licences libres, Wikimedia Commons)</summary><ul>{li}<li>Photos d\'illustration : elles ne montrent pas l\'établissement. {extra}</li></ul></details>'

def footer_legal(F):
    c = compliance(F)
    return (f'<p class="legal">{c + " " if c else ""}Site de démonstration non officiel réalisé à partir d\'informations publiques ; contenus à valider par l\'établissement. '
            f'© <span data-year>2026</span> {esc(F["name"])} · Démo réalisée par <a href="https://github.com/islemyakoubi" target="_blank" rel="noopener">Synaris Labs</a>, Menzel Temime.</p>')

BASE = ('*,*:before,*:after{box-sizing:border-box}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}body{margin:0}img{max-width:100%;height:auto;display:block}'
        'a{color:inherit}.skip{position:absolute;left:-999px;top:0}.skip:focus{left:1rem;top:1rem;z-index:99;background:#fff;color:#000;padding:.5rem 1rem}'
        'iframe{border:0;display:block;width:100%}form [hidden]{display:none}details summary{cursor:pointer}.credits ul{padding-left:1.1rem}'
        '.lb{position:fixed;inset:0;z-index:90;background:rgba(0,0,0,.9);display:none;place-items:center;padding:1rem}.lb.open{display:grid}.lb img{max-height:88vh;width:auto}'
        '.lb button{position:absolute;top:1rem;right:1rem;width:46px;height:46px;border-radius:50%;border:0;font-size:1.5rem;cursor:pointer}'
        '[data-panel][hidden]{display:none}@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}')

JS = r'''(function(){var d=document;d.documentElement.classList.add('js');
d.querySelectorAll('[data-year]').forEach(function(y){y.textContent=new Date().getFullYear()});
var hb=d.querySelector('[data-menu]'),nav=d.querySelector('[data-nav]');
if(hb&&nav){hb.addEventListener('click',function(){var o=nav.classList.toggle('open');hb.setAttribute('aria-expanded',o)});
nav.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){nav.classList.remove('open');hb.setAttribute('aria-expanded','false')})})}
var hd=d.querySelector('[data-header]');if(hd){var f=function(){hd.classList.toggle('scrolled',window.scrollY>30)};f();window.addEventListener('scroll',f,{passive:true})}
var t=(new Date().getDay()+6)%7+1;d.querySelectorAll('[data-d="'+t+'"]').forEach(function(r){r.classList.add('today')});
d.querySelectorAll('form[data-wa]').forEach(function(fm){fm.addEventListener('submit',function(e){e.preventDefault();
if(!fm.reportValidity())return;var L=[fm.getAttribute('data-intro')];
fm.querySelectorAll('[name]').forEach(function(el){if(el.disabled||!el.value)return;var l=el.getAttribute('data-label')||el.name;
var v=el.value;if(el.type==='date'){var p=v.split('-');v=p[2]+'/'+p[1]+'/'+p[0]}L.push('- '+l+' : '+v)});
window.open('https://wa.me/'+fm.getAttribute('data-wa')+'?text='+encodeURIComponent(L.join('\n')),'_blank','noopener')})});
d.querySelectorAll('[data-tabs]').forEach(function(g){var bs=g.querySelectorAll('[data-tab]');bs.forEach(function(b){b.addEventListener('click',function(){
bs.forEach(function(x){x.setAttribute('aria-selected',x===b)});g.querySelectorAll('[data-panel]').forEach(function(p){p.hidden=p.getAttribute('data-panel')!==b.getAttribute('data-tab')})})})});
d.querySelectorAll('[data-fs]').forEach(function(b){b.addEventListener('click',function(){var r=d.documentElement,s=parseFloat(getComputedStyle(r).fontSize);
r.style.fontSize=Math.max(14,Math.min(26,s+parseFloat(b.getAttribute('data-fs'))))+'px'})});
var lb=d.querySelector('.lb');if(lb){var li=lb.querySelector('img');d.querySelectorAll('[data-full]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();
li.src=a.getAttribute('data-full');li.alt=(a.querySelector('img')||{}).alt||'';lb.classList.add('open')})});
var c=function(){lb.classList.remove('open');li.removeAttribute('src')};lb.addEventListener('click',function(e){if(e.target!==li)c()});d.addEventListener('keydown',function(e){if(e.key==='Escape')c()})}
})();'''

def page(F, title, desc, fonts, css, body, theme, favicon, lang='fr', dir_='ltr'):
    return f'''<!doctype html>
<html lang="{lang}" dir="{dir_}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="noindex,nofollow">
<meta name="theme-color" content="{theme}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:image" content="media/hero.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,{quote(favicon)}">
<style>{BASE}{css}</style>
</head>
<body>
{body}
<script>{JS}</script>
</body>
</html>'''

def build_all(only=None):
    FA = json.load(open(os.path.join(GEN, 'lot2_facts.json')))
    T = json.load(open(os.path.join(GEN, 'titles_lot2.json')))
    slugs = [s for s in MODS if not only or s in only]
    info = commons_info(sorted({t for s in slugs for _, t in T[s]}))
    for slug in slugs:
        mod = importlib.import_module(MODS[slug])
        M = Media(slug, T[slug], info)
        h = mod.build(FA[slug], M)
        open(os.path.join(ROOT, slug, 'index.html'), 'w').write(h); print('built lot2', slug, len(h))

if __name__ == '__main__':
    build_all(sys.argv[1:] or None)
