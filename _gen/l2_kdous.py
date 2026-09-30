# Dr Imen Kdous, médecin dentiste (Kélibia) : bandes de couleur pleine largeur empilées, titres de section surdimensionnés en filigrane, photo du port de Kélibia.
# Red Hat Display + Red Hat Text ; marine / ocre / écume.
import gen_lot2 as K
FONTS = 'family=Red+Hat+Display:wght@500;700;900&family=Red+Hat+Text:wght@400;500;700'
CSS = '''
:root{--nv:#12264A;--oc:#D98E2B;--foam:#EEF4F2;--ink:#12264A;--mut:#5c6a7e}
body{background:var(--foam);color:var(--ink);font:400 1rem/1.65 'Red Hat Text',system-ui,sans-serif}h1,h2,h3{font-family:'Red Hat Display',sans-serif;font-weight:900;line-height:.95;margin:0 0 .6rem;letter-spacing:-.03em}
.w{width:min(1160px,100% - 2.2rem);margin-inline:auto}.ph{font:700 .7rem/1 'Red Hat Text';color:var(--nv);background:rgba(217,142,43,.22);border-radius:4px;padding:.2rem .45rem;white-space:nowrap}
.rb{background:#0a1832;color:#b3bfd4;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:#fff}
.band{position:relative;overflow:hidden;padding:4.5rem 0}.band .wm{position:absolute;left:-.05em;top:-.12em;font:900 clamp(6rem,19vw,16rem)/1 'Red Hat Display';opacity:.08;white-space:nowrap;pointer-events:none;letter-spacing:-.05em}
.band .w{position:relative}.nv{background:var(--nv);color:#fff}.oc{background:var(--oc);color:var(--nv)}.fm{background:var(--foam)}.wh{background:#fff}
.top{display:flex;justify-content:space-between;align-items:center;padding:1.2rem 0}.top b{font:900 1.2rem 'Red Hat Display'}.top a{color:#fff}
.bt{display:inline-flex;gap:.5rem;align-items:center;background:var(--oc);color:var(--nv);text-decoration:none;font-weight:700;padding:.85rem 1.2rem;border-radius:8px}.bt svg{width:18px}.bt.n{background:var(--nv);color:#fff}.bt.w2{background:#fff;color:var(--nv)}
.hero{padding:0 0 0}.hero .grid{display:grid;gap:2rem;align-items:end;padding:2rem 0 0}.hero h1{font-size:clamp(3.4rem,10vw,8rem)}.hero h1 span{color:var(--oc)}.hero p{color:#c7d2e4;max-width:30rem;font-size:1.1rem}
.hero .ph2{margin-top:2rem;height:clamp(240px,40vw,460px);border-radius:14px 14px 0 0;overflow:hidden}.hero .ph2 img{width:100%;height:100%;object-fit:cover}.acts{display:flex;gap:.6rem;flex-wrap:wrap;margin-top:1.3rem}
.band h2{font-size:clamp(2.4rem,6vw,4.4rem)}.cols{display:grid;gap:2rem}.facts{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem 2rem}.facts small{display:block;font-weight:700;font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;opacity:.7}.facts p{margin:0;font-size:1.1rem;font-weight:500}
.days{display:grid;grid-template-columns:repeat(7,1fr);gap:0;border:2px solid var(--nv);border-radius:12px;overflow:hidden}.days div{padding:1rem .3rem;text-align:center;border-right:2px solid var(--nv);font:700 .9rem 'Red Hat Display'}.days div:last-child{border-right:0}
.days div.today{background:var(--nv);color:var(--oc)}.days small{display:block;font:500 .72rem 'Red Hat Text';margin-top:.3rem}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}.form label{display:grid;gap:.3rem;font-weight:700;font-size:.84rem}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;border:0;border-radius:8px;padding:.75rem;min-height:48px;width:100%;background:#fff;color:var(--nv)}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--oc);color:var(--nv);border:0;border-radius:8px;padding:1rem;font:900 1rem 'Red Hat Display';cursor:pointer}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.76rem;color:#b3bfd4;margin:0}.map{height:360px;border-radius:14px;overflow:hidden}.note{font-size:.8rem;opacity:.75}.sq{border-radius:14px;overflow:hidden}.sq img{width:100%;aspect-ratio:4/3;object-fit:cover}
.ft{padding:2rem 0 3rem;font-size:.82rem;color:var(--mut)}
@media(min-width:900px){.cols{grid-template-columns:1fr 1fr;align-items:start}.hero .grid{grid-template-columns:1.3fr .7fr}}
@media(max-width:640px){.days{grid-template-columns:repeat(4,1fr)}.days div{border-bottom:2px solid var(--nv)}.facts{grid-template-columns:1fr}}
'''
def build(F, M):
    ab = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim']
    days = ''.join(f'<div data-d="{n}">{ab[n - 1]}<small>{v if k else "à confirmer"}</small></div>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet.')
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<main id="main"><section class="band nv hero"><div class="w"><div class="top"><b>Dr Imen Kdous</b><a href="{K.telhref(F['tel'])}">{F['tel']}</a></div>
<div class="grid"><div><h1>Cabinet dentaire,<br><span>Kélibia.</span></h1></div><div><p>Dr Imen Kdous, médecin dentiste à Kélibia. Rendez-vous par téléphone ou WhatsApp.</p><div class="acts"><a class="bt" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a><a class="bt w2" href="#horaires">{K.I['clock']}Horaires</a></div></div></div>
<div class="ph2">{M.img('hero', 'Le port de Kélibia (photo d’illustration)', sizes='(max-width: 1160px) 100vw, 1160px', lazy=False)}</div></div></section>
<section class="band oc"><span class="wm" aria-hidden="true">CABINET</span><div class="w cols"><h2>Le cabinet</h2><div class="facts"><div><small>Praticienne</small><p>Dr Imen Kdous</p></div><div><small>Qualification</small><p>{F['sector']}</p></div><div><small>Adresse</small><p>{F['addr']}</p></div><div><small>Téléphone</small><p><a href="{K.telhref(F['tel'])}">{F['tel']}</a></p></div><div><small>N° d'Ordre</small><p>{K.ph()}</p></div><div><small>Langues · CNAM</small><p>{K.ph()} · {K.ph()}</p></div></div></div></section>
<section class="band wh" id="horaires"><span class="wm" aria-hidden="true">HORAIRES</span><div class="w"><h2>Horaires</h2><div class="days">{days}</div><p class="note" style="margin-top:1rem">{K.HOURS_NOTE}</p></div></section>
<section class="band nv" id="rdv"><span class="wm" aria-hidden="true">RENDEZ-VOUS</span><div class="w cols"><div><h2>Rendez-vous</h2><p style="color:#c7d2e4">Le formulaire ouvre WhatsApp avec votre demande pour le cabinet. Pensez à votre carte CNAM et à vos radiographies récentes.</p><div class="sq">{M.img('outils', 'Instruments dentaires (photo d’illustration)', sizes='(max-width: 900px) 100vw, 560px')}</div></div>
{K.form(F, 'Bonjour, je souhaite prendre rendez-vous au cabinet du Dr Imen Kdous :', K.MED_FORM, 'Envoyer sur WhatsApp')}</div></section>
<section class="band fm" id="acces"><span class="wm" aria-hidden="true">KÉLIBIA</span><div class="w cols"><div><h2>Accès</h2><p>{F['addr']}</p><a class="bt n" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire</a><div class="sq" style="margin-top:1.4rem">{M.img('plage', 'Plage de Kélibia (photo d’illustration)', sizes='(max-width: 900px) 100vw, 560px')}</div></div><div class="map">{K.mapframe(F)}</div></div></section></main>
<footer class="ft w">{M.credits()}{K.footer_legal(F)}</footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='32' fill='#12264A'/><rect y='32' width='64' height='32' fill='#D98E2B'/><text x='32' y='44' font-size='28' text-anchor='middle' fill='#fff' font-family='Arial' font-weight='900'>IK</text></svg>"
    return K.page(F, 'Dr Imen Kdous — Médecin dentiste à Kélibia (démo)', 'Cabinet dentaire du Dr Imen Kdous à Kélibia : informations, horaires, accès et demande de rendez-vous par WhatsApp.', FONTS, CSS, body, '#12264A', fav)
