# Dr Obay Becem, ophtalmologue (Kélibia) : grille suisse stricte, hero = planche d'acuité typographique (lettres décroissantes), filets noirs, accent vert.
# Archivo + Archivo Narrow ; blanc / noir / vert #00A676.
import gen_lot2 as K
FONTS = 'family=Archivo:wght@400;600;800;900&family=Archivo+Narrow:wght@400;600'
CSS = '''
:root{--bk:#0d0d0d;--g:#00A676;--mut:#5f5f5f;--line:#0d0d0d}
body{background:#fff;color:var(--bk);font:400 1rem/1.6 Archivo,system-ui,sans-serif}h1,h2,h3{font-weight:900;line-height:.95;margin:0 0 .6rem;letter-spacing:-.03em}.nar{font-family:'Archivo Narrow',sans-serif}
.w{width:min(1240px,100% - 2rem);margin-inline:auto}.ph{font:600 .72rem/1 'Archivo Narrow';color:#fff;background:var(--g);padding:.22rem .45rem;white-space:nowrap}
.rb{background:var(--bk);color:#bbb;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:#fff}
.hd{display:grid;grid-template-columns:1fr auto;border-bottom:3px solid var(--bk);padding:1rem 0;align-items:end}.hd b{font-weight:900;font-size:1.2rem;text-transform:uppercase}.hd span{font:600 .85rem 'Archivo Narrow';text-transform:uppercase}
.g12{display:grid;gap:0}.hero{border-bottom:1px solid var(--line)}.chart{text-align:center;padding:2.5rem 1rem;border-bottom:1px solid var(--line);font-weight:800;line-height:1.05;letter-spacing:.25em}
.chart div:nth-child(1){font-size:clamp(5rem,14vw,10rem);letter-spacing:0}.chart div:nth-child(2){font-size:clamp(2.6rem,7vw,5rem)}.chart div:nth-child(3){font-size:clamp(1.8rem,4.5vw,3.2rem)}.chart div:nth-child(4){font-size:clamp(1.2rem,3vw,2rem);color:var(--g)}.chart div:nth-child(5){font-size:1rem}
.chart small{display:block;font:400 .72rem 'Archivo Narrow';letter-spacing:.1em;color:var(--mut);margin-top:1rem;text-transform:uppercase}
.id{padding:2rem 1rem}.id h1{font-size:clamp(3rem,7vw,5.6rem);text-transform:uppercase}.id p{max-width:28rem;color:var(--mut)}.id .k{font:600 .8rem 'Archivo Narrow';text-transform:uppercase;letter-spacing:.14em;color:var(--g)}
.bt{display:inline-flex;gap:.5rem;align-items:center;background:var(--bk);color:#fff;text-decoration:none;font-weight:800;padding:.9rem 1.2rem;text-transform:uppercase;font-size:.85rem}.bt svg{width:18px}.bt.g{background:var(--g)}
.acts{display:flex;gap:0;flex-wrap:wrap;margin-top:1.2rem}.acts .bt{border-right:1px solid #fff}
.cell{padding:1.6rem 1rem;border-bottom:1px solid var(--line)}.cell .n{font:600 .75rem 'Archivo Narrow';color:var(--g);letter-spacing:.14em}.cell h2{font-size:2rem;text-transform:uppercase}
.im img{width:100%;height:100%;min-height:260px;object-fit:cover;filter:grayscale(1) contrast(1.1)}.im{border-bottom:1px solid var(--line);overflow:hidden}
.dl{display:grid;grid-template-columns:1fr 1.4fr;margin:0}.dl dt,.dl dd{margin:0;padding:.55rem 0;border-top:1px solid #ddd}.dl dt{font:600 .8rem 'Archivo Narrow';text-transform:uppercase;letter-spacing:.08em;color:var(--mut)}
.tb{width:100%;border-collapse:collapse}.tb td{padding:.55rem 0;border-top:1px solid #ddd;font-family:'Archivo Narrow'}.tb td+td{text-align:right}.tb .today td{font-weight:600;color:var(--g)}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}.form label{display:grid;gap:.25rem;font:600 .78rem 'Archivo Narrow';text-transform:uppercase;letter-spacing:.06em}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:1rem Archivo;border:2px solid var(--bk);border-radius:0;padding:.7rem;min-height:46px;width:100%;background:#fff}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--g);color:#fff;border:0;padding:1rem;font:800 1rem Archivo;text-transform:uppercase;cursor:pointer}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.76rem;color:var(--mut);margin:0}.map{height:100%;min-height:340px}.note{font-size:.8rem;color:var(--mut)}.ft{padding:1.5rem 0 3rem;font-size:.82rem;color:var(--mut)}
@media(min-width:900px){.g12{grid-template-columns:repeat(12,1fr)}.hero .chart{grid-column:1/6;border-bottom:0;border-right:1px solid var(--line);display:flex;flex-direction:column;justify-content:center}.hero .id{grid-column:6/13;padding:3rem 2.5rem;align-self:center}
.c4{grid-column:span 4;border-right:1px solid var(--line)}.c4:last-child{border-right:0}.c5{grid-column:span 5;border-right:1px solid var(--line)}.c7{grid-column:span 7}.c6{grid-column:span 6;border-right:1px solid var(--line)}.c6+.c6{border-right:0}.cell{padding:2rem}}
'''
def build(F, M):
    hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else "à confirmer"}</td></tr>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour Docteur, je souhaite prendre rendez-vous en ophtalmologie.')
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<header class="w hd"><b>Dr Obay Becem</b><span>Ophtalmologie — Kélibia</span></header>
<main id="main" class="w"><section class="g12 hero"><div class="chart" aria-hidden="true"><div>E</div><div>O B</div><div>A Y B</div><div>E C E M</div><div>K É L I B I A</div><small>Planche d'acuité · décor typographique, pas un test</small></div>
<div class="id"><p class="k">Médecin ophtalmologue</p><h1>Dr Obay<br>Becem</h1><p>Cabinet d'ophtalmologie à Kélibia. Consultations sur rendez-vous, par téléphone ou WhatsApp.</p>
<div class="acts"><a class="bt" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a><a class="bt g" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a></div></div></section>
<section class="g12"><div class="cell c4"><p class="n">01 — CABINET</p><h2>Identité</h2><dl class="dl"><dt>Médecin</dt><dd>Dr Obay Becem</dd><dt>Spécialité</dt><dd>{F['sector']}</dd><dt>N° d'Ordre</dt><dd>{K.ph()}</dd><dt>Langues</dt><dd>{K.ph()}</dd><dt>CNAM</dt><dd>{K.ph()}</dd></dl></div>
<div class="im c4">{M.img('hero', 'Réfracteur d’ophtalmologie (photo d’illustration)', sizes='(max-width: 900px) 100vw, 33vw', lazy=False)}</div>
<div class="cell c4"><p class="n">02 — HORAIRES</p><h2>Semaine</h2><table class="tb">{hrs}</table><p class="note">Horaires non publiés sur la fiche Google au 30/09/2026 : à confirmer avec le cabinet.</p></div></section>
<section class="g12"><div class="cell c5"><p class="n">03 — PRÉPARER</p><h2>Avant la visite</h2><p>Apportez votre carte CNAM ou d'assurance, vos lunettes ou lentilles actuelles, et vos ordonnances ou comptes rendus récents.</p><p class="note">Urgence vitale : 190 (SAMU).</p>
<div class="im" style="border:0;margin-top:1rem">{M.img('lampe', 'Lampe à fente d’ophtalmologie (photo d’illustration)', sizes='(max-width: 900px) 100vw, 40vw')}</div></div>
<div class="cell c7" id="rdv"><p class="n">04 — RENDEZ-VOUS</p><h2>Demande</h2>{K.form(F, 'Bonjour, je souhaite un rendez-vous chez le Dr Obay Becem (ophtalmologie) :', K.MED_FORM, 'Envoyer sur WhatsApp')}</div></section>
<section class="g12"><div class="cell c6"><p class="n">05 — ACCÈS</p><h2>Kélibia</h2><p>{F['addr']}</p><a class="bt" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire</a><div class="im" style="border:0;margin-top:1.2rem">{M.img('porte', 'Porte traditionnelle à Kélibia (photo d’illustration)', sizes='(max-width: 900px) 100vw, 50vw')}</div></div>
<div class="c6">{K.mapframe(F)}</div></section></main>
<footer class="ft w">{M.credits()}{K.footer_legal(F)}</footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' fill='#fff'/><text x='32' y='52' font-size='54' text-anchor='middle' fill='#0d0d0d' font-family='Arial' font-weight='900'>E</text><rect y='58' width='64' height='6' fill='#00A676'/></svg>"
    return K.page(F, 'Dr Obay Becem — Ophtalmologue à Kélibia (démo)', 'Cabinet d’ophtalmologie du Dr Obay Becem à Kélibia : informations, horaires, accès et demande de rendez-vous.', FONTS, CSS, body, '#0d0d0d', fav)
