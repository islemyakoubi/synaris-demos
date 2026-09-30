# Dr Houssem El Manaa, cardiologue (Menzel Temime, Centre médical El Amen) : thème sombre « moniteur ». Tracé ECG SVG animé plein écran, cartes vitrées, fiche en grille de données monospace.
# Plus Jakarta Sans + JetBrains Mono ; marine nuit / rouge pouls / vert moniteur.
import gen_lot2 as K
FONTS = 'family=Plus+Jakarta+Sans:wght@400;600;800&family=JetBrains+Mono:wght@400;600'
CSS = '''
:root{--bg:#0B1B3A;--bg2:#10244a;--red:#FF4D5E;--grn:#3DFFA8;--txt:#e8eefc;--mut:#98a6c7;--gl:rgba(255,255,255,.06);--bd:rgba(255,255,255,.12)}
body{background:var(--bg);color:var(--txt);font:400 1rem/1.65 'Plus Jakarta Sans',system-ui,sans-serif}h1,h2,h3{font-weight:800;line-height:1.02;margin:0 0 .6rem;letter-spacing:-.03em}
.mono{font-family:'JetBrains Mono',monospace}.w{width:min(1180px,100% - 2rem);margin-inline:auto}a{color:inherit}
.ph{font:600 .7rem/1 'JetBrains Mono';color:var(--grn);background:rgba(61,255,168,.1);border:1px solid rgba(61,255,168,.3);border-radius:4px;padding:.2rem .45rem;white-space:nowrap}
.rb{background:#07122a;color:var(--mut);font-size:.74rem;text-align:center;padding:.4rem 1rem;border-bottom:1px solid var(--bd)}.rb b{color:#fff}
.hd .w{display:flex;justify-content:space-between;align-items:center;height:70px}.lg{font-weight:800;text-decoration:none;display:flex;gap:.5rem;align-items:center}.lg svg{width:22px;color:var(--red)}
.nav{display:none;gap:1.6rem;font-size:.9rem;color:var(--mut)}.nav a{text-decoration:none}
.bt{display:inline-flex;gap:.5rem;align-items:center;background:var(--red);color:#fff;text-decoration:none;font-weight:800;padding:.85rem 1.2rem;border-radius:12px}.bt svg{width:18px}.bt.g{background:var(--gl);border:1px solid var(--bd)}
.hero{position:relative;padding:4rem 0 3rem;overflow:hidden}.ecg{position:absolute;left:0;right:0;top:48%;height:160px;width:100%;opacity:.3;pointer-events:none}
.ecg path{fill:none;stroke:var(--red);stroke-width:2.5;stroke-dasharray:1400;stroke-dashoffset:1400;animation:tr 4s linear infinite}@keyframes tr{to{stroke-dashoffset:0}}
@media(prefers-reduced-motion:reduce){.ecg path{animation:none;stroke-dashoffset:0}}
.hero .w{position:relative}.hero .k{font:600 .78rem 'JetBrains Mono';color:var(--grn);letter-spacing:.1em}.hero h1{font-size:clamp(3rem,8vw,6.2rem)}.hero h1 span{color:var(--red)}
.hero p{color:var(--mut);max-width:34rem;font-size:1.1rem}.acts{display:flex;gap:.7rem;flex-wrap:wrap;margin-top:1.4rem}
.vit{display:grid;grid-template-columns:repeat(2,1fr);gap:.7rem;margin-top:3rem}.vit div{background:var(--gl);border:1px solid var(--bd);border-radius:16px;padding:1rem;backdrop-filter:blur(6px)}
.vit small{display:block;font:400 .68rem 'JetBrains Mono';color:var(--mut);text-transform:uppercase;letter-spacing:.12em}.vit b{font-size:1.05rem}
.sec{padding:4.5rem 0}.sec h2{font-size:clamp(2rem,4.5vw,3.2rem)}.ey{font:600 .74rem 'JetBrains Mono';color:var(--grn);letter-spacing:.14em;text-transform:uppercase}
.two{display:grid;gap:2rem}.gl{background:var(--gl);border:1px solid var(--bd);border-radius:22px;padding:1.5rem}.im{border-radius:22px;overflow:hidden;border:1px solid var(--bd)}.im img{width:100%;aspect-ratio:4/3;object-fit:cover;filter:saturate(.85)}
.dl{display:grid;grid-template-columns:auto 1fr;gap:.55rem 1.2rem;margin:0}.dl dt{font:400 .78rem 'JetBrains Mono';color:var(--mut)}.dl dd{margin:0}
.tb{width:100%;border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:.9rem}.tb td{padding:.6rem 0;border-bottom:1px solid var(--bd)}.tb td+td{text-align:right}.tb .today td{color:var(--grn)}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}.form label{display:grid;gap:.3rem;font-weight:600;font-size:.84rem}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;border:1px solid var(--bd);border-radius:10px;padding:.75rem;min-height:48px;width:100%;background:var(--bg2);color:var(--txt);color-scheme:dark}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--red);color:#fff;border:0;border-radius:12px;padding:1rem;font:800 1rem 'Plus Jakarta Sans';cursor:pointer}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.76rem;color:var(--mut);margin:0}.map{height:360px;border-radius:22px;overflow:hidden;border:1px solid var(--bd);filter:invert(.9) hue-rotate(180deg)}.note{font-size:.8rem;color:var(--mut)}
.ft{padding:2rem 0 3rem;font-size:.82rem;color:var(--mut);border-top:1px solid var(--bd)}.ft a{color:var(--txt)}
@media(min-width:900px){.nav{display:flex}.two{grid-template-columns:1fr 1fr;align-items:start}.vit{grid-template-columns:repeat(4,1fr)}}
'''
ECG = '<svg class="ecg" viewBox="0 0 1400 160" preserveAspectRatio="none" aria-hidden="true"><path d="M0 90 H180 l20 -10 20 10 H300 l12 12 18 -90 18 120 14 -42 H520 l24 -18 26 18 H700 l20 -10 20 10 H820 l12 12 18 -90 18 120 14 -42 H1040 l24 -18 26 18 H1400"/></svg>'
def build(F, M):
    hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else "à confirmer"}</td></tr>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour Docteur, je souhaite prendre rendez-vous en consultation de cardiologie.')
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<header class="hd"><div class="w"><a class="lg" href="#top">{K.I['heart']}Dr Houssem El Manaa</a><nav class="nav" aria-label="Navigation"><a href="#cabinet">Cabinet</a><a href="#horaires">Horaires</a><a href="#rdv">Rendez-vous</a><a href="#acces">Accès</a></nav><a class="bt" href="{K.telhref(F['tel'])}">{K.I['phone']}Appeler</a></div></header>
<main id="main"><section class="hero" id="top">{ECG}<div class="w"><p class="k">CARDIOLOGIE · MENZEL TEMIME</p><h1>Dr Houssem<br><span>El Manaa</span></h1><p>Cardiologue, Centre médical El Amen à Menzel Temime. Consultations sur rendez-vous, par téléphone ou WhatsApp.</p>
<div class="acts"><a class="bt" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a><a class="bt g" href="#horaires">{K.I['clock']}Horaires</a></div>
<div class="vit mono"><div><small>Spécialité</small><b>Cardiologue</b></div><div><small>Lieu</small><b>Centre médical El Amen</b></div><div><small>Téléphones</small><b>{F['tel']}</b></div><div><small>Aujourd'hui</small><b>{K.hours_short(F)}</b></div></div></div></section>
<section class="sec" id="cabinet"><div class="w two"><div class="gl"><p class="ey">Fiche du cabinet</p><h2>Informations</h2><dl class="dl"><dt>Médecin</dt><dd>Dr Houssem El Manaa</dd><dt>Spécialité</dt><dd>Cardiologie · cardiologie interventionnelle (selon annuaires publics, {K.ph()})</dd>
<dt>Adresse</dt><dd>{F['addr']}</dd><dt>Téléphones</dt><dd><a href="{K.telhref(F['tel'])}">{F['tel']}</a> · <a href="{K.telhref(F['tel2'])}">{F['tel2']}</a></dd><dt>N° d'Ordre</dt><dd>{K.ph()}</dd><dt>Langues</dt><dd>{K.ph()}</dd><dt>CNAM</dt><dd>{K.ph()}</dd></dl>
<p class="note" style="margin-top:1.2rem">Pour votre consultation : apportez votre carte CNAM ou d'assurance, vos ordonnances en cours et vos examens récents (ECG, bilans, comptes rendus).</p></div>
<div class="im">{M.img('hero', 'Tracé d’électrocardiogramme (image d’illustration)', sizes='(max-width: 900px) 100vw, 50vw', lazy=False)}</div></div></section>
<section class="sec" id="horaires" style="padding-top:0"><div class="w two"><div><p class="ey">Horaires</p><h2>Consultations</h2><table class="tb">{hrs}</table><p class="note">{K.HOURS_NOTE}</p></div><div class="im">{M.img('outils', 'Instruments médicaux de cardiologie (photo d’illustration)', sizes='(max-width: 900px) 100vw, 50vw')}</div></div></section>
<section class="sec" id="rdv" style="background:var(--bg2)"><div class="w two"><div><p class="ey">Rendez-vous</p><h2>Demander un créneau</h2><p style="color:var(--mut)">Le formulaire prépare un message WhatsApp pour le cabinet. Aucune question médicale n'est traitée par message : le cabinet vous rappelle pour fixer l'heure.</p></div>
<div class="gl">{K.form(F, 'Bonjour, je souhaite un rendez-vous en cardiologie chez le Dr Houssem El Manaa :', K.MED_FORM, 'Envoyer sur WhatsApp')}</div></div></section>
<section class="sec" id="acces"><div class="w two"><div class="map">{K.mapframe(F)}</div><div><p class="ey">Accès</p><h2>Menzel Temime</h2><p>{F['addr']}</p><a class="bt g" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire Google Maps</a>
<div class="im" style="margin-top:1.4rem">{M.img('ville', 'Menzel Temime (photo d’illustration)', sizes='(max-width: 900px) 100vw, 50vw')}</div></div></div></section></main>
<footer class="ft"><div class="w">{M.credits()}{K.footer_legal(F)}</div></footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='14' fill='#0B1B3A'/><path d='M6 36h14l5-12 7 24 6-16 4 4h16' fill='none' stroke='#FF4D5E' stroke-width='4' stroke-linejoin='round'/></svg>"
    return K.page(F, 'Dr Houssem El Manaa — Cardiologue à Menzel Temime (démo)', 'Cabinet de cardiologie du Dr Houssem El Manaa, Centre médical El Amen à Menzel Temime : informations, horaires, accès et demande de rendez-vous.', FONTS, CSS, body, '#0B1B3A', fav)
