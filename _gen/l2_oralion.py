# Oralion Dental Clinic (Hammamet) : hero photo plein cadre avec carte flottante en verre, puis grille bento de tuiles d'info, bande Hammamet (fort + plage). Praticiens à confirmer.
# Onest + Fraunces ; océan profond / glace / cyan.
import gen_lot2 as K
FONTS = 'family=Onest:wght@400;500;700&family=Fraunces:opsz,wght@9..144,300;9..144,600'
CSS = '''
:root{--oc:#0A2540;--ice:#EAF6FB;--cy:#12B5CB;--ink:#0A2540;--mut:#58708a;--line:#d3e6ef}
body{background:var(--ice);color:var(--ink);font:400 1rem/1.65 Onest,system-ui,sans-serif}h1,h2,h3{font-family:Fraunces,serif;font-weight:600;line-height:1;margin:0 0 .6rem;letter-spacing:-.02em}
.w{width:min(1220px,100% - 2rem);margin-inline:auto}.ph{font:500 .7rem/1 Onest;color:#0b7f90;background:#d6f3f7;border-radius:99px;padding:.22rem .55rem;white-space:nowrap}
.rb{background:var(--oc);color:#a9c3d8;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:#fff}
.hero{position:relative;min-height:88vh;display:flex;align-items:flex-end;padding:1rem}.hero>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.hero:before{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,37,64,.55),transparent 30%,rgba(10,37,64,.4));z-index:1}
.top{position:absolute;left:0;right:0;top:0;z-index:2;display:flex;justify-content:space-between;align-items:center;padding:1.2rem 1.4rem;color:#fff}.top .lg{font:600 1.35rem Fraunces;text-decoration:none;display:flex;gap:.5rem;align-items:center}.top .lg svg{width:24px}
.card{position:relative;z-index:2;background:rgba(255,255,255,.86);backdrop-filter:blur(14px);border-radius:28px;padding:1.6rem;max-width:560px;box-shadow:0 30px 60px -30px rgba(10,37,64,.6)}
.card .k{font-weight:700;font-size:.76rem;letter-spacing:.18em;text-transform:uppercase;color:#0b7f90}.card h1{font-size:clamp(2.6rem,6vw,4.4rem);font-weight:300}.card h1 b{font-weight:600}.card p{color:var(--mut)}
.bt{display:inline-flex;gap:.5rem;align-items:center;background:var(--oc);color:#fff;text-decoration:none;font-weight:700;padding:.85rem 1.2rem;border-radius:99px}.bt svg{width:18px}.bt.c{background:var(--cy);color:var(--oc)}.bt.l{background:rgba(255,255,255,.2);color:#fff;border:1px solid rgba(255,255,255,.4)}
.acts{display:flex;gap:.6rem;flex-wrap:wrap;margin-top:1rem}
.bento{display:grid;gap:.9rem;padding:3rem 0}.t{background:#fff;border-radius:24px;padding:1.4rem;border:1px solid var(--line);min-width:0}.t small{display:block;font-weight:700;font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:#0b7f90;margin-bottom:.4rem}
.t.dk{background:var(--oc);color:#fff}.t.dk small{color:var(--cy)}.t.cy{background:var(--cy)}.t.cy small{color:var(--oc)}.t h2{font-size:2rem}.big{font:300 1.9rem/1.1 Fraunces;white-space:nowrap}
.t.im{padding:0;overflow:hidden;min-height:240px;position:relative}.t.im img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.tb{width:100%;border-collapse:collapse}.tb td{padding:.45rem 0;border-bottom:1px solid rgba(255,255,255,.14)}.tb td+td{text-align:right}.tb .today td{color:var(--cy);font-weight:700}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.7rem}.form label{display:grid;gap:.25rem;font-weight:500;font-size:.84rem}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;border:1px solid var(--line);border-radius:14px;padding:.7rem;min-height:46px;width:100%;background:var(--ice)}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--oc);color:#fff;border:0;border-radius:99px;padding:1rem;font:700 1rem Onest;cursor:pointer}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.76rem;color:var(--mut);margin:0}.map{height:100%;min-height:320px;border-radius:0}.t.mp{padding:0;overflow:hidden}.note{font-size:.78rem;opacity:.8}
.ft{padding:1rem 0 3rem;font-size:.82rem;color:var(--mut)}
@media(min-width:960px){.hero{padding:2.4rem}.bento{grid-template-columns:repeat(4,1fr);grid-auto-rows:minmax(150px,auto)}.s2{grid-column:span 2}.r2{grid-row:span 2}}
@media(min-width:600px) and (max-width:959px){.bento{grid-template-columns:1fr 1fr}.s2{grid-column:span 2}}
@media(max-width:560px){.top .bt{display:none}.hero{min-height:92vh}}
'''
def build(F, M):
    hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else "à confirmer"}</td></tr>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour, je souhaite prendre rendez-vous à Oralion Dental Clinic.')
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<main id="main"><section class="hero" id="top">{M.img('hero', 'Salle de soins dentaires moderne (photo d’illustration, ne montre pas la clinique)', sizes='100vw', lazy=False)}
<div class="top"><a class="lg" href="#top">{K.I['tooth']}Oralion</a><a class="bt l" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div>
<div class="card"><p class="k">Cabinet dentaire · Hammamet</p><h1>Oralion <b>Dental Clinic</b></h1><p>Cabinet dentaire à Hammamet. Rendez-vous par téléphone ou WhatsApp.</p><div class="acts"><a class="bt" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a><a class="bt c" href="#rdv">{K.I['cal']}Rendez-vous</a></div></div></section>
<div class="w bento"><div class="t dk r2"><small>Horaires</small><h2>La semaine</h2><table class="tb">{hrs}</table><p class="note">{K.HOURS_NOTE}</p></div>
<div class="t"><small>Téléphone</small><p class="big"><a href="{K.telhref(F['tel'])}">{F['tel']}</a></p></div><div class="t cy"><small>Aujourd'hui</small><p style="font-weight:700;margin:0">{K.hours_short(F)}</p></div>
<div class="t im r2">{M.img('fort', 'La kasbah de Hammamet (photo d’illustration)', sizes='(max-width: 960px) 50vw, 25vw')}</div><div class="t s2"><small>La clinique</small><p style="margin:0">Praticien(s) : {K.ph()} · N° d'Ordre : {K.ph()} · Langues : {K.ph()} · CNAM : {K.ph()}</p><p class="note" style="margin-top:.5rem">Adresse : {F['addr']}</p></div>
<div class="t s2 r2" id="rdv"><small>Demande de rendez-vous</small>{K.form(F, 'Bonjour, je souhaite prendre rendez-vous à Oralion Dental Clinic :', K.MED_FORM, 'Envoyer sur WhatsApp')}</div>
<div class="t im">{M.img('plage', 'Plage de Hammamet (photo d’illustration)', sizes='(max-width: 960px) 50vw, 25vw')}</div><div class="t dk"><small>Préparer sa visite</small><p style="margin:0">Apportez votre carte CNAM ou d'assurance et vos radiographies récentes s'il y en a. Pour une urgence vitale : 190 (SAMU).</p><div class="acts"><a class="bt c" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire</a></div></div>
<div class="t mp s2" id="acces">{K.mapframe(F)}</div></div></main>
<footer class="ft w">{M.credits()}{K.footer_legal(F)}</footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='20' fill='#0A2540'/><circle cx='32' cy='32' r='14' fill='none' stroke='#12B5CB' stroke-width='6'/></svg>"
    return K.page(F, 'Oralion Dental Clinic — Cabinet dentaire à Hammamet (démo)', 'Oralion Dental Clinic à Hammamet : informations pratiques, horaires, accès et demande de rendez-vous par WhatsApp.', FONTS, CSS, body, '#0A2540', fav)
