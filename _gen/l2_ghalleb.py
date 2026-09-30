# Dr Mohamed Ghalleb, gynécologue (Nabeul, depuis 1988) : carte de visite typographique (letterpress), colonne étroite centrée.
# Playfair Display + Lato ; crème / vert forêt / laiton. Sceau circulaire « depuis 1988 », filets doubles, horaires à points de conduite, rubriques en petites capitales.
import gen_lot2 as K
FONTS = 'family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Lato:wght@400;700'
CSS = '''
:root{--cream:#F4EFE3;--forest:#1F3B2D;--brass:#A67C3D;--ink:#22302a;--mut:#6a6f66}
body{background:var(--cream);color:var(--ink);font:400 1.02rem/1.75 Lato,system-ui,sans-serif}
h1,h2,h3{font-family:'Playfair Display',serif;font-weight:400;line-height:1.1;margin:0 0 .6rem;color:var(--forest)}
.col{width:min(780px,100% - 2.4rem);margin-inline:auto}.ph{font:700 .68rem/1 Lato;letter-spacing:.06em;color:var(--brass);border-bottom:1px dotted var(--brass);white-space:nowrap}
.rb{background:var(--forest);color:#d9e2d9;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:#e8d3a6}
.top{display:flex;justify-content:center;gap:2rem;padding:1.1rem 0;font-size:.74rem;letter-spacing:.24em;text-transform:uppercase;border-bottom:1px solid #d8cfb9}.top a{text-decoration:none}
.card{margin:3rem auto 0;background:#fbf8f0;padding:3rem 1.6rem 2.6rem;text-align:center;position:relative;box-shadow:0 1px 0 #d8cfb9,0 30px 50px -35px rgba(31,59,45,.45)}
.card:before{content:'';position:absolute;inset:10px;border:1px solid var(--brass);outline:1px solid var(--brass);outline-offset:-6px;pointer-events:none}
.seal{width:124px;height:124px;margin:0 auto 1.2rem;color:var(--brass)}.card .sc{font-size:.74rem;letter-spacing:.3em;text-transform:uppercase;color:var(--brass)}
.card h1{font-size:clamp(2.5rem,7vw,4.2rem);margin:.4rem 0}.card .spec{font:italic 1.35rem 'Playfair Display';color:var(--mut)}
.orn{display:flex;align-items:center;gap:.8rem;justify-content:center;color:var(--brass);margin:1.2rem 0}.orn:before,.orn:after{content:'';width:60px;height:1px;background:currentColor}
.acts{display:flex;justify-content:center;gap:.8rem;flex-wrap:wrap;margin-top:1.4rem}.bt{display:inline-flex;gap:.5rem;align-items:center;text-decoration:none;font-weight:700;font-size:.82rem;letter-spacing:.14em;text-transform:uppercase;padding:.9rem 1.3rem;border:1px solid var(--forest)}
.bt svg{width:17px}.bt.f{background:var(--forest);color:var(--cream)}
.band{margin:3rem 0;height:300px;position:relative;overflow:hidden}.band img{width:100%;height:100%;object-fit:cover;filter:sepia(.35) saturate(.8)}
.rub{padding:2.4rem 0;border-top:1px solid #d8cfb9}.rub h2{font-size:.84rem;font-family:Lato;font-weight:700;letter-spacing:.3em;text-transform:uppercase;color:var(--brass);margin-bottom:1.2rem}
.lead{font:400 1.45rem/1.45 'Playfair Display';color:var(--forest)}
.dl{margin:0}.dl div{display:flex;align-items:baseline;gap:.6rem;padding:.35rem 0}.dl dt{white-space:nowrap}.dl dd{margin:0;text-align:right;white-space:nowrap}
.dl div:after{content:'';order:1;flex:1;border-bottom:1px dotted #a9a08a}.dl dd{order:2}.dl .today dt,.dl .today dd{font-weight:700;color:var(--forest)}
.two{display:grid;gap:2rem}.two figure{margin:0}.two img{width:100%;aspect-ratio:4/5;object-fit:cover;filter:sepia(.25)}.two figcaption{font-size:.76rem;color:var(--mut)}
.form{display:grid;grid-template-columns:1fr 1fr;gap:1rem}.form label{display:grid;gap:.25rem;font-size:.72rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--brass)}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:400 1rem Lato;letter-spacing:0;text-transform:none;border:0;border-bottom:1px solid var(--forest);background:transparent;padding:.6rem 0;min-height:44px;width:100%;color:var(--ink)}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--forest);color:var(--cream);border:0;padding:1rem;font:700 .85rem Lato;letter-spacing:.16em;text-transform:uppercase;cursor:pointer}.form button svg{width:18px}
.fnote{grid-column:1/-1;font-size:.78rem;color:var(--mut);margin:0}.map{height:320px;filter:sepia(.3)}.note{font-size:.8rem;color:var(--mut)}
.ft{padding:2rem 0 3rem;font-size:.8rem;color:var(--mut);border-top:1px solid #d8cfb9;text-align:center}.ft .credits{text-align:left}
@media(min-width:760px){.card{padding:4rem 3rem 3.2rem}.two{grid-template-columns:1fr 1fr;align-items:center}}
'''
SEAL = '''<svg class="seal" viewBox="0 0 124 124" aria-hidden="true"><defs><path id="c" d="M62 62m-48 0a48 48 0 1 1 96 0a48 48 0 1 1-96 0"/></defs><circle cx="62" cy="62" r="60" fill="none" stroke="currentColor"/><circle cx="62" cy="62" r="38" fill="none" stroke="currentColor"/>
<text font-family="Lato" font-size="10.5" letter-spacing="3.2" fill="currentColor"><textPath href="#c">CABINET DE GYNÉCOLOGIE · NABEUL ·</textPath></text><text x="62" y="58" text-anchor="middle" font-family="Playfair Display" font-size="11" fill="currentColor">depuis</text><text x="62" y="78" text-anchor="middle" font-family="Playfair Display" font-size="22" fill="currentColor">1988</text></svg>'''
def build(F, M):
    dl = ''.join(f'<div data-d="{n}"><dt>{d}</dt><dd>{v if k else K.ph()}</dd></div>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet.')
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<nav class="top" aria-label="Navigation"><a href="#cabinet">Cabinet</a><a href="#horaires">Horaires</a><a href="#rdv">Rendez-vous</a></nav>
<main id="main"><div class="col"><div class="card">{SEAL}<p class="sc">Nabeul</p><h1>Dr Mohamed Ghalleb</h1><p class="spec">{F['sector']}</p><div class="orn">✦</div>
<p>{F['addr']}<br><a href="{K.telhref(F['tel'])}">{F['tel']}</a></p><div class="acts"><a class="bt f" href="{K.telhref(F['tel'])}">{K.I['phone']}Appeler</a><a class="bt" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a></div></div></div>
<div class="band">{M.img('hero', 'Porte bleue et bougainvilliers (photo d’illustration)', sizes='100vw', lazy=False)}</div>
<div class="col"><section class="rub" id="cabinet"><h2>Le cabinet</h2><p class="lead">Le Dr Mohamed Ghalleb reçoit ses patientes à Nabeul, sur rendez-vous.</p>
<dl class="dl"><div><dt>Qualification</dt><dd>{F['sector']}</dd></div><div><dt>Installation</dt><dd>1988 {K.ph()}</dd></div><div><dt>N° d'inscription à l'Ordre</dt><dd>{K.ph()}</dd></div><div><dt>Langues parlées</dt><dd>{K.ph()}</dd></div><div><dt>CNAM / assurances</dt><dd>{K.ph()}</dd></div></dl></section>
<section class="rub" id="horaires"><h2>Horaires de consultation</h2><dl class="dl">{dl}</dl><p class="note">Horaire relevé sur la fiche Google le {K.CONSULTED} (ouverture le jeudi à 9h00). Autres jours à confirmer.</p></section>
<section class="rub"><div class="two"><figure>{M.img('attente', 'Salle d’attente (photo d’illustration, ne montre pas le cabinet)', sizes='(max-width: 760px) 90vw, 380px')}<figcaption>Photo d'illustration.</figcaption></figure>
<div><h2>Votre rendez-vous</h2><p>Munissez-vous de votre carte CNAM ou d'assurance, ainsi que de vos derniers examens et ordonnances éventuels.</p><p>Pour annuler ou déplacer un rendez-vous, prévenez le cabinet par téléphone ou WhatsApp.</p></div></div></section>
<section class="rub" id="rdv"><h2>Demande de rendez-vous</h2>{K.form(F, 'Bonjour, je souhaite prendre rendez-vous au cabinet du Dr Mohamed Ghalleb :', K.MED_FORM, 'Envoyer sur WhatsApp')}</section>
<section class="rub"><h2>Accès</h2><div class="map">{K.mapframe(F)}</div><p><a href="{F['maps']}" target="_blank" rel="noopener">Ouvrir l'itinéraire dans Google Maps →</a></p></section></div></main>
<footer class="ft"><div class="col">{M.credits()}{K.footer_legal(F)}</div></footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' fill='#1F3B2D'/><circle cx='32' cy='32' r='22' fill='none' stroke='#A67C3D' stroke-width='2'/><text x='32' y='41' font-size='24' text-anchor='middle' fill='#F4EFE3' font-family='Georgia'>G</text></svg>"
    return K.page(F, 'Dr Mohamed Ghalleb — Gynécologue à Nabeul (démo)', 'Cabinet du Dr Mohamed Ghalleb, gynécologue à Nabeul : coordonnées, horaires, accès et demande de rendez-vous par WhatsApp.', FONTS, CSS, body, '#1F3B2D', fav)
