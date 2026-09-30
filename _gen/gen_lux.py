# Lots 3 et suivants : sites premium sur mesure (un gabarit par établissement : l3_*.py, l4_*.py...), moteur commun lux.py.
# Faits : lot<N>_facts.json (repris des fiches publiques, rien d'inventé ; inconnu = « à confirmer »). Photos : titles_lot<N>.json (Wikimedia Commons, licences libres).
import json, os, io, sys, glob, re, importlib, time
GEN = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, GEN)
import gen_lot2 as K
class Media(K.Media):
    """Comme K.Media, plus une variante 1920 px du hero (plein écran net) quand l'original est assez grand."""
    def __init__(self, slug, items, info):
        super().__init__(slug, items, info)
        from PIL import Image
        self.xl = None
        p = os.path.join(K.ROOT, slug, 'media', 'hero-1920.webp')
        if not os.path.exists(p) and self.dims.get('hero', (0, 0))[0] >= 1280:
            url = dict(self.cr)['hero']['url']
            if '/1280px-' in url:
                try:
                    im = Image.open(io.BytesIO(K.get(url.replace('/1280px-', '/1920px-')))).convert('RGB')
                    if im.width >= 1600: im.thumbnail((1920, 1920)); im.save(p, 'WEBP', quality=70, method=6)
                except SystemExit: pass
        if os.path.exists(p):
            with Image.open(p) as im: self.xl = im.size
    def img(self, name, alt, cls='', sizes='(max-width: 700px) 100vw, 50vw', lazy=True, extra=''):
        h = super().img(name, alt, cls, sizes, lazy, extra)
        if name == 'hero' and self.xl: h = h.replace(f'media/hero.webp {self.dims["hero"][0]}w"', f'media/hero.webp {self.dims["hero"][0]}w, media/hero-1920.webp {self.xl[0]}w"')
        return h
def build_all(only=None):
    for ff in sorted(glob.glob(os.path.join(GEN, 'lot*_facts.json'))):
        n = int(re.findall(r'lot(\d+)_facts', ff)[0])
        if n < 3: continue
        FA = json.load(open(ff)); T = json.load(open(os.path.join(GEN, f'titles_lot{n}.json')))
        slugs = [s for s in FA if not only or s in only]
        if not slugs: continue
        info = K.commons_info(sorted({t for s in slugs for _, t in T[s]}))
        for slug in slugs:
            F = FA[slug]; mod = importlib.import_module(F['mod'])
            M = Media(slug, T[slug], info)
            open(os.path.join(K.ROOT, slug, 'index.html'), 'w').write(mod.build(F, M)); print('built lot', n, slug)
if __name__ == '__main__':
    build_all(sys.argv[1:] or None)
