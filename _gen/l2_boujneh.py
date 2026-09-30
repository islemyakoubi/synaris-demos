# Dr Aymen Boujneh, gynécologue obstétricien (Hammamet) : écran partagé, image de jasmin fixe à gauche, contenu qui défile à droite.
# Libre Caslon Text + Karla ; poudre / prune / sauge. Rubriques numérotées en marge, grille d'infos à filets fins.
import gen_lot2 as K
FONTS = 'family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&family=Karla:wght@400;500;700'
CSS = '''
:root{--blush:#F7EDEA;--plum:#5B2A4A;--sage:#8AA39B;--ink:#2b1f27;--mut:#6f6068;--line:#e3d3cf}
body{background:var(--blush);color:var(--ink);font:400 1.02rem/1.7 Karla,system-ui,sans-serif}
h1,h2,h3{font-family:'Libre Caslon Text',serif;font-weight:400;line-height:1.1;margin:0 0 .7rem}.ph{font:500 .72rem/1 Karla;color:var(--plum);background:#efdcd8;border-radius:3px;padding:.2rem .45rem;white-space:nowrap}
.rb{background:var(--plum);color:#ecd9e3;font-size:.74rem;text-align:center;padding:.4rem 1rem;position:relative;z-index:5}.rb b{color:#fff}
.split{display:grid}.side{position:relative;min-height:62vh;overflow:hidden}.side img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.side:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(43,31,39,.1),rgba(43,31,39,.72))}
.side .id{position:absolute;left:1.6rem;right:1.6rem;bottom:1.8rem;z-index:2;color:#fff}.side .id p{margin:0;font-size:.8rem;letter-spacing:.24em;text-transform:uppercase;opacity:.85}
.side h1{font-size:clamp(2.6rem,5vw,4.2rem);margin:.5rem 0 .3rem}.side h1 i{color:#f0c9d8}.side .q{font-style:italic;font-family:'Libre Caslon Text';opacity:.9}
.main{padding:0 1.4rem}.top{display:flex;justify-content:space-between;align-items:center;gap:1rem;padding:1.2rem 0;border-bottom:1px solid var(--line)}
.top nav{display:none;gap:1.2rem;font-size:.88rem;font-weight:500;flex-wrap:wrap}.top a{text-decoration:none}
.bt{display:inline-flex;gap:.5rem;align-items:center;background:var(--plum);color:#fff;text-decoration:none;font-weight:700;padding:.85rem 1.3rem;border-radius:2px}.bt svg{width:18px}.bt.l{background:transparent;color:var(--plum);border:1px solid var(--plum)}
.rub{display:grid;grid-template-columns:3rem 1fr;gap:0 1rem;padding:3.2rem 0;border-bottom:1px solid var(--line)}.rub>span{font:italic 1.6rem 'Libre Caslon Text';color:var(--sage)}
.rub h2{font-size:clamp(1.9rem,3.4vw,2.6rem);color:var(--plum)}.rub>div{min-width:0}.lead{font-size:1.15rem;color:var(--mut)}
.grid{display:grid;grid-template-columns:1fr;border-top:1px solid var(--line);border-left:1px solid var(--line);margin-top:1.4rem}
.grid div{padding:1rem 1.1rem;border-right:1px solid var(--line);border-bottom:1px solid var(--line)}.grid small{display:block;font-size:.7rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--sage)}
.act{list-style:none;padding:0;margin:1rem 0}.act li{padding:.8rem 0 .8rem 1.8rem;border-bottom:1px solid var(--line);position:relative}.act li:before{content:'';position:absolute;left:0;top:1.25rem;width:.8rem;height:1px;background:var(--plum)}
.tb{width:100%;border-collapse:collapse}.tb td{padding:.6rem 0;border-bottom:1px solid var(--line)}.tb td+td{text-align:right}.tb .today td{color:var(--plum);font-weight:700}
.fig{margin:1.4rem 0 0;overflow:hidden;border-radius:2px}.fig img{width:100%;aspect-ratio:16/9;object-fit:cover}.fig figcaption{font-size:.78rem;color:var(--mut);padding-top:.4rem}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.9rem;margin-top:1.2rem}.form label{display:grid;gap:.3rem;font-size:.85rem;font-weight:700;color:var(--plum)}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;border:1px solid var(--line);background:#fffaf8;padding:.75rem;min-height:48px;width:100%;border-radius:2px}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--plum);color:#fff;border:0;padding:1rem;font:700 1rem Karla;cursor:pointer}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.78rem;color:var(--mut);margin:0}.map{height:320px;margin-top:1.2rem}.note{font-size:.8rem;color:var(--mut)}
.ft{padding:2rem 0 3rem;font-size:.82rem;color:var(--mut)}
@media(min-width:560px){.grid{grid-template-columns:1fr 1fr}.top nav{display:flex}}@media(min-width:960px){.split{grid-template-columns:44% 1fr}.side{position:sticky;top:0;height:100vh;min-height:0}.main{padding:0 3.5rem}.rub{grid-template-columns:4.5rem 1fr}}
'''
def build(F, M):
    hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else K.ph()}</td></tr>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet.')
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<div class="split"><aside class="side">{M.img('hero', 'Fleurs de jasmin (photo d’illustration)', sizes='(max-width: 960px) 100vw, 44vw', lazy=False)}
<div class="id"><p>Cabinet de gynécologie · Hammamet</p><h1>Dr Aymen <i>Boujneh</i></h1><p class="q">Gynécologue obstétricien</p></div></aside>
<main class="main" id="main"><div class="top"><nav aria-label="Navigation"><a href="#cabinet">Cabinet</a><a href="#consultations">Consultations</a><a href="#rdv">Rendez-vous</a><a href="#acces">Accès</a></nav><a class="bt" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a></div>
<section class="rub" id="cabinet"><span>i.</span><div><h2>Le cabinet</h2><p class="lead">Cabinet de gynécologie et d'obstétrique du Dr Aymen Boujneh à Hammamet. Consultations sur rendez-vous.</p>
<div class="grid"><div><small>Qualification</small>{F['sector']}</div><div><small>N° d'Ordre</small>{K.ph()}</div><div><small>Langues</small>{K.ph()}</div><div><small>Conventionnement</small>CNAM {K.ph()}</div></div></div></section>
<section class="rub" id="consultations"><span>ii.</span><div><h2>Consultations</h2><p>D'après la fiche publique du cabinet sur med.tn :</p><ul class="act"><li>{F['extra'][0]}</li><li>{F['extra'][1]}</li><li>Suivi de grossesse et gynécologie : détail des consultations {K.ph()}</li></ul>
<figure class="fig">{M.img('echo', 'Appareil d’échographie (photo d’illustration, ne montre pas le cabinet)', sizes='(max-width: 960px) 100vw, 50vw')}<figcaption>Photo d'illustration.</figcaption></figure>
<h3 style="margin-top:2rem;font-size:1.5rem">Horaires</h3><table class="tb">{hrs}</table><p class="note">{K.HOURS_NOTE}</p></div></section>
<section class="rub" id="rdv"><span>iii.</span><div><h2>Prendre rendez-vous</h2><p>Par téléphone au <a href="{K.telhref(F['tel'])}"><b>{F['tel']}</b></a> ou par WhatsApp avec le formulaire ci-dessous.</p>
{K.form(F, 'Bonjour, je souhaite prendre rendez-vous au cabinet du Dr Aymen Boujneh :', K.MED_FORM, 'Envoyer sur WhatsApp')}</div></section>
<section class="rub" id="acces"><span>iv.</span><div><h2>Accès</h2><p>{F['addr']}</p><div class="map">{K.mapframe(F)}</div><p style="margin-top:1rem"><a class="bt l" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire</a></p>
<figure class="fig">{M.img('medina', 'Rue de la médina de Hammamet (photo d’illustration)', sizes='(max-width: 960px) 100vw, 50vw')}<figcaption>Hammamet, médina (photo d'illustration).</figcaption></figure></div></section>
<footer class="ft">{M.credits()}{K.footer_legal(F)}</footer></main></div>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' fill='#5B2A4A'/><g fill='#F7EDEA'><circle cx='32' cy='22' r='7'/><circle cx='22' cy='34' r='7'/><circle cx='42' cy='34' r='7'/><circle cx='27' cy='45' r='7'/><circle cx='37' cy='45' r='7'/></g></svg>"
    return K.page(F, 'Dr Aymen Boujneh — Gynécologue obstétricien à Hammamet (démo)', 'Cabinet du Dr Aymen Boujneh, gynécologue obstétricien à Hammamet : consultations, horaires, accès et demande de rendez-vous par WhatsApp.', FONTS, CSS, body, '#5B2A4A', fav)
