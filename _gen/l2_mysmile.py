# MY SMILE, centre dentaire du Dr Marouen Ridene (Kélibia) : identité de marque ronde et joyeuse, grande courbe « sourire » SVG sous le hero, sections en zigzag image/texte alternées.
# Baloo 2 + Nunito ; jaune #FFD60A / marine #1D3557 / blanc.
import gen_lot2 as K
FONTS = 'family=Baloo+2:wght@500;700;800&family=Nunito:wght@400;600;700'
CSS = '''
:root{--y:#FFD60A;--nv:#1D3557;--mut:#566478;--sky:#EAF1FB}
body{background:#fff;color:var(--nv);font:400 1rem/1.65 Nunito,system-ui,sans-serif}h1,h2,h3{font-family:'Baloo 2',sans-serif;font-weight:800;line-height:1;margin:0 0 .5rem}
.w{width:min(1120px,100% - 2rem);margin-inline:auto}.ph{font:700 .72rem/1 Nunito;color:var(--nv);background:#fff3b0;border-radius:99px;padding:.22rem .55rem;white-space:nowrap}
.rb{background:var(--nv);color:#c5d0e0;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:#fff}
.hd .w{display:flex;justify-content:space-between;align-items:center;height:74px}.lg{font:800 1.6rem 'Baloo 2';text-decoration:none;display:flex;align-items:center;gap:.4rem}.lg i{font-style:normal;background:var(--y);border-radius:12px;padding:0 .4rem}
.bt{display:inline-flex;gap:.5rem;align-items:center;background:var(--nv);color:#fff;text-decoration:none;font-weight:700;padding:.85rem 1.3rem;border-radius:99px}.bt svg{width:18px}.bt.y{background:var(--y);color:var(--nv)}
.hero{background:var(--y);position:relative;padding:3rem 0 7rem;text-align:center}.hero h1{font-size:clamp(3rem,9vw,6.4rem)}.hero p{font-size:1.15rem;max-width:34rem;margin:0 auto 1.4rem}
.hero .acts{display:flex;gap:.6rem;justify-content:center;flex-wrap:wrap}.curve{position:absolute;left:0;right:0;bottom:-1px;width:100%;height:120px;display:block}
.face{width:min(560px,90%);margin:-5rem auto 0;position:relative;z-index:1;border-radius:32px;overflow:hidden;border:8px solid #fff;box-shadow:0 30px 60px -30px rgba(29,53,87,.5)}.face img{width:100%;aspect-ratio:16/10;object-fit:cover}
.zz{padding:3.5rem 0}.zr{display:grid;gap:2rem;align-items:center;margin:2.5rem 0}.zr .pic{border-radius:40px 40px 40px 8px;overflow:hidden}.zr .pic img{width:100%;aspect-ratio:4/3;object-fit:cover}
.zr h2{font-size:clamp(2.2rem,5vw,3.2rem)}.zr .n{display:inline-grid;place-items:center;width:44px;height:44px;border-radius:50%;background:var(--y);font:800 1.2rem 'Baloo 2';margin-bottom:.6rem}
.card{background:var(--sky);border-radius:28px;padding:1.5rem}.kv{display:grid;grid-template-columns:auto 1fr;gap:.5rem 1rem;margin:0}.kv dt{font-weight:700;color:var(--mut)}.kv dd{margin:0}
.tb{width:100%;border-collapse:collapse}.tb td{padding:.5rem 0;border-bottom:2px dotted #cfdbeb}.tb td+td{text-align:right}.tb .today td{font-weight:700;background:#fff3b0}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.7rem}.form label{display:grid;gap:.25rem;font-weight:700;font-size:.84rem}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;border:2px solid #d6e0ee;border-radius:16px;padding:.7rem;min-height:46px;width:100%;background:#fff}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--nv);color:#fff;border:0;border-radius:99px;padding:1rem;font:800 1.05rem 'Baloo 2';cursor:pointer}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.76rem;color:var(--mut);margin:0}.map{height:340px;border-radius:28px;overflow:hidden}.note{font-size:.8rem;color:var(--mut)}.ft{padding:2rem 0 3rem;font-size:.82rem;color:var(--mut)}
@media(min-width:880px){.zr{grid-template-columns:1fr 1fr}.zr.rv .pic{order:2}.zr.rv .pic{border-radius:40px 40px 8px 40px}}
'''
SMILE = '<svg class="curve" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true"><path d="M0 0 Q720 200 1440 0 V120 H0z" fill="#fff"/></svg>'
def build(F, M):
    hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else K.ph()}</td></tr>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour, je souhaite prendre rendez-vous au centre dentaire My Smile.')
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<header class="hd"><div class="w"><a class="lg" href="#top"><i>MY</i>SMILE</a><a class="bt" href="{K.telhref(F['tel'])}">{K.I['phone']}Appeler</a></div></header>
<main id="main"><section class="hero" id="top"><div class="w"><h1>My Smile</h1><p>Centre dentaire du Dr Marouen Ridene à Kélibia. Rendez-vous par téléphone ou WhatsApp.</p><div class="acts"><a class="bt" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a><a class="bt y" style="background:#fff" href="#rdv">{K.I['cal']}Rendez-vous</a></div></div>{SMILE}</section>
<div class="face">{M.img('hero', 'Brosse à dents et dentifrice (photo d’illustration)', sizes='(max-width: 620px) 90vw, 560px', lazy=False)}</div>
<div class="w zz"><div class="zr"><div class="pic">{M.img('vue', 'Le fort de Kélibia (photo d’illustration)', sizes='(max-width: 880px) 100vw, 540px')}</div><div><span class="n">1</span><h2>Le centre</h2><div class="card"><dl class="kv"><dt>Nom</dt><dd>My Smile, centre dentaire</dd><dt>Praticien</dt><dd>Dr Marouen Ridene, médecin dentiste</dd><dt>Ville</dt><dd>Kélibia</dd><dt>Adresse</dt><dd>{K.ph()}</dd><dt>Téléphone</dt><dd><a href="{K.telhref(F['tel'])}">{F['tel']}</a></dd><dt>N° d'Ordre</dt><dd>{K.ph()}</dd><dt>Langues</dt><dd>{K.ph()}</dd><dt>CNAM</dt><dd>{K.ph()}</dd></dl></div></div></div>
<div class="zr rv"><div class="pic">{M.img('porte', 'Porte traditionnelle à Kélibia (photo d’illustration)', sizes='(max-width: 880px) 100vw, 540px')}</div><div><span class="n">2</span><h2>Horaires</h2><div class="card"><table class="tb">{hrs}</table></div><p class="note">Horaires non publiés sur la fiche Google au 30/09/2026 : à confirmer avec le centre.</p></div></div>
<div class="zr" id="rdv"><div class="map">{K.mapframe(F)}</div><div><span class="n">3</span><h2>Rendez-vous</h2>{K.form(F, 'Bonjour, je souhaite prendre rendez-vous au centre dentaire My Smile (Dr Marouen Ridene) :', K.MED_FORM, 'Envoyer sur WhatsApp')}<p><a class="bt y" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire</a></p></div></div></div></main>
<footer class="ft w">{M.credits()}{K.footer_legal(F)}</footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><circle cx='32' cy='32' r='32' fill='#FFD60A'/><path d='M16 34 Q32 54 48 34' fill='none' stroke='#1D3557' stroke-width='6' stroke-linecap='round'/></svg>"
    return K.page(F, 'My Smile — Centre dentaire Dr Marouen Ridene à Kélibia (démo)', 'My Smile, centre dentaire du Dr Marouen Ridene à Kélibia : informations, horaires, accès et demande de rendez-vous.', FONTS, CSS, body, '#FFD60A', fav)
