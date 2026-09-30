# Maître Aymen Jouida, avocat (Hammamet) : papier à en-tête sobre, rubriques numérotées à titre collant (marge gauche), sans aucune promotion.
# EB Garamond + IBM Plex Sans ; parchemin / anthracite / bordeaux. Photo en niveaux de gris, formulaire de simple prise de rendez-vous.
import gen_lot2 as K
FONTS = 'family=EB+Garamond:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Sans:wght@400;500;600'
CSS = '''
:root{--parch:#F5F1E8;--char:#262626;--ox:#6B1E23;--mut:#666;--line:#d6cfc0}
body{background:var(--parch);color:var(--char);font:400 1rem/1.7 'IBM Plex Sans',system-ui,sans-serif}
h1,h2,h3{font-family:'EB Garamond',serif;font-weight:400;line-height:1.1;margin:0 0 .6rem}.w{width:min(1080px,100% - 2.4rem);margin-inline:auto}
.ph{font:500 .72rem/1 'IBM Plex Sans';color:var(--ox);border:1px solid #d9b9bb;padding:.15rem .4rem;white-space:nowrap}
.rb{background:var(--char);color:#ccc;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:#fff}
.lh{text-align:center;padding:2rem 0 1.2rem;border-bottom:3px double var(--char)}.lh .n{font:400 clamp(1.8rem,4vw,2.4rem) 'EB Garamond';letter-spacing:.06em}
.lh .t{font-size:.76rem;letter-spacing:.34em;text-transform:uppercase;color:var(--ox)}.lh nav{display:flex;justify-content:center;gap:1.6rem;margin-top:1rem;font-size:.84rem;flex-wrap:wrap}.lh nav a{text-decoration:none}
.hero{display:grid;gap:2rem;padding:3.5rem 0;border-bottom:1px solid var(--line);align-items:center}.hero h1{font-size:clamp(2.6rem,6vw,4.4rem)}.hero h1 i{color:var(--ox)}
.hero p{color:var(--mut);max-width:34rem}.hero img{width:100%;aspect-ratio:4/3;object-fit:cover;filter:grayscale(1) contrast(1.05)}
.bt{display:inline-flex;gap:.5rem;align-items:center;text-decoration:none;font-weight:500;padding:.85rem 1.2rem;border:1px solid var(--char);margin:.3rem .5rem 0 0}.bt svg{width:17px}.bt.d{background:var(--char);color:#fff}
.row{display:grid;gap:.6rem 3rem;padding:3rem 0;border-bottom:1px solid var(--line)}.row>header{align-self:start}.row>header span{font:italic 400 1.1rem 'EB Garamond';color:var(--ox)}
.row h2{font-size:2rem}.kv{margin:0}.kv div{display:grid;grid-template-columns:12rem 1fr;gap:1rem;padding:.7rem 0;border-top:1px solid var(--line)}.kv dt{color:var(--mut);font-size:.88rem}.kv dd{margin:0}
.tb{width:100%;max-width:520px;border-collapse:collapse}.tb td{padding:.55rem 0;border-top:1px solid var(--line)}.tb td+td{text-align:right}.tb .today td{font-weight:600;color:var(--ox)}
.form{display:grid;grid-template-columns:1fr 1fr;gap:1rem;max-width:640px}.form label{display:grid;gap:.25rem;font-size:.8rem;font-weight:500}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;border:1px solid #bdb5a4;background:#fffdf8;padding:.7rem;min-height:46px;width:100%;border-radius:0}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--char);color:#fff;border:0;padding:1rem;font:500 1rem 'IBM Plex Sans';cursor:pointer}.form button svg{width:18px}
.fnote{grid-column:1/-1;font-size:.78rem;color:var(--mut);margin:0}.map{height:320px;filter:grayscale(1)}.note{font-size:.8rem;color:var(--mut)}
.dq{font:italic 1.25rem/1.5 'EB Garamond';border-left:3px solid var(--ox);padding-left:1rem;color:#444}
.ft{padding:2rem 0 3rem;font-size:.8rem;color:var(--mut)}
@media(max-width:560px){.kv div{grid-template-columns:1fr;gap:0}.form{grid-template-columns:1fr}}
@media(min-width:820px){.hero{grid-template-columns:1.1fr .9fr}.row{grid-template-columns:15rem 1fr}.row>header{position:sticky;top:1.5rem}}
'''
def build(F, M):
    hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else K.ph()}</td></tr>' for n, d, v, k in K.hours(F))
    note = "Démo : aucune donnée n'est enregistrée. Ce formulaire sert uniquement à demander un rendez-vous : n'y décrivez pas votre affaire. Aucune consultation n'est donnée par message."
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<header class="lh w"><p class="t">Avocat · Hammamet</p><p class="n">Maître Aymen Jouida</p><nav aria-label="Navigation"><a href="#cabinet">Le cabinet</a><a href="#horaires">Horaires</a><a href="#rdv">Rendez-vous</a><a href="#acces">Accès</a></nav></header>
<main id="main" class="w"><section class="hero"><div><h1>Bureau d'avocat <i>à Hammamet</i></h1><p>Maître Aymen Jouida reçoit sur rendez-vous à son bureau de Hammamet.</p>
<a class="bt d" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a><a class="bt" href="#rdv">{K.I['cal']}Demander un rendez-vous</a></div>
{M.img('hero', 'Rayonnage d’ouvrages de droit (photo d’illustration)', sizes='(max-width: 820px) 100vw, 45vw', lazy=False)}</section>
<section class="row" id="cabinet"><header><span>I.</span><h2>Le cabinet</h2></header><div><dl class="kv"><div><dt>Avocat</dt><dd>Maître Aymen Jouida</dd></div><div><dt>Adresse</dt><dd>{F['addr']}</dd></div>
<div><dt>Téléphone</dt><dd><a href="{K.telhref(F['tel'])}">{F['tel']}</a> · <a href="{K.telhref(F['tel2'])}">{F['tel2']}</a></dd></div><div><dt>Inscription au barreau</dt><dd>{K.ph()}</dd></div>
<div><dt>Diplômes</dt><dd>{K.ph()}</dd></div><div><dt>Domaines d'intervention</dt><dd>{K.ph('à confirmer, selon les diplômes')}</dd></div><div><dt>Langues</dt><dd>{K.ph()}</dd></div></dl></div></section>
<section class="row" id="horaires"><header><span>II.</span><h2>Horaires du bureau</h2></header><div><table class="tb">{hrs}</table><p class="note">{K.HOURS_NOTE}</p></div></section>
<section class="row" id="rdv"><header><span>III.</span><h2>Rendez-vous</h2></header><div><p>Pour un premier rendez-vous, appelez le bureau ou envoyez une demande par WhatsApp. Les échanges sur votre dossier ont lieu au cabinet.</p>
{K.form(F, 'Bonjour Maître, je souhaite prendre rendez-vous à votre bureau :', [('text', 'Nom et prénom'), ('tel', 'Téléphone'), ('date', 'Jour souhaité'), ('select', 'Moment', ['Matin', 'Après-midi', 'Peu importe'])], 'Demander un rendez-vous', note=note)}</div></section>
<section class="row" id="acces"><header><span>IV.</span><h2>Accès</h2></header><div><div class="map">{K.mapframe(F)}</div><p><a class="bt" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire</a></p></div></section>
<section class="row"><header><span>V.</span><h2>Déontologie</h2></header><div><p class="dq">Ce site présente uniquement les coordonnées et l'organisation du bureau, dans le respect du secret professionnel et des règles de la profession d'avocat.</p></div></section></main>
<footer class="ft w">{M.credits()}{K.footer_legal(F)}</footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' fill='#262626'/><text x='32' y='43' font-size='30' text-anchor='middle' fill='#F5F1E8' font-family='Georgia'>AJ</text></svg>"
    return K.page(F, 'Maître Aymen Jouida — Avocat à Hammamet (démo)', 'Bureau de Maître Aymen Jouida, avocat à Hammamet : coordonnées, horaires, accès et demande de rendez-vous.', FONTS, CSS, body, '#262626', fav)
