# Dr Manel Attia, médecin dentiste (Hammamet) : composition symétrique à arcades (médina de Hammamet).
# Instrument Serif + Manrope ; chaux / menthe / sarcelle profonde / sable. Hero centré à arche, bandeau 4 pastilles, arches partout.
import gen_lot2 as K
FONTS = 'family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;600;700'
CSS = '''
:root{--lime:#FBFAF7;--mint:#DDF3EE;--teal:#0F5E59;--sand:#E9DCC6;--ink:#17302E;--mut:#5d716e}
body{background:var(--lime);color:var(--ink);font:400 1rem/1.65 Manrope,system-ui,sans-serif}
h1,h2,h3{font-family:'Instrument Serif',serif;font-weight:400;line-height:1.02;margin:0 0 .6rem}
.w{width:min(1120px,100% - 2.4rem);margin-inline:auto}.ph{font:600 .72rem/1 Manrope;color:var(--teal);background:var(--mint);border-radius:99px;padding:.2rem .55rem;white-space:nowrap}
.rb{background:var(--teal);color:#d6ece8;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:#fff}
.hd .w{display:flex;justify-content:space-between;align-items:center;height:74px}.lg{text-decoration:none;font:400 1.5rem/1 'Instrument Serif'}.lg small{display:block;font:600 .66rem/1.4 Manrope;letter-spacing:.18em;text-transform:uppercase;color:var(--mut)}
.nav{display:none;gap:1.8rem;font-weight:600;font-size:.92rem}.nav a{text-decoration:none}
.bt{display:inline-flex;align-items:center;gap:.5rem;background:var(--teal);color:#fff;text-decoration:none;font-weight:700;padding:.9rem 1.4rem;border-radius:99px}.bt svg{width:18px;height:18px}.bt.o{background:transparent;color:var(--teal);box-shadow:inset 0 0 0 1.5px var(--teal)}
.hero{text-align:center;padding:2.5rem 0 0}.hero .k{font-weight:700;font-size:.78rem;letter-spacing:.24em;text-transform:uppercase;color:var(--mut)}
.hero h1{font-size:clamp(3.2rem,9vw,6.6rem);margin:.6rem 0}.hero h1 i{color:var(--teal)}.hero p{max-width:36rem;margin:0 auto 1.6rem;color:var(--mut);font-size:1.08rem}
.acts{display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap}
.arch{margin:2.6rem auto 0;width:min(560px,86%);aspect-ratio:4/5;border-radius:999px 999px 0 0;overflow:hidden;border:10px solid #fff;box-shadow:0 30px 60px -30px rgba(15,94,89,.5)}
.arch img{width:100%;height:100%;object-fit:cover}
.pills{display:grid;gap:1px;background:var(--sand);border:1px solid var(--sand);border-radius:22px;overflow:hidden;margin:-2.4rem auto 0;position:relative;width:min(1000px,100% - 2.4rem)}
.pills div{background:#fff;padding:1.2rem 1.3rem}.pills small{display:block;font-size:.7rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--mut)}.pills b{font-weight:600}
.sec{padding:5rem 0}.ey{font-weight:700;font-size:.76rem;letter-spacing:.22em;text-transform:uppercase;color:var(--teal)}h2{font-size:clamp(2.4rem,5vw,3.6rem)}
.duo{display:grid;gap:3rem;align-items:center}.arch2{border-radius:999px 999px 24px 24px;overflow:hidden;aspect-ratio:3/4;max-width:420px}.arch2 img{width:100%;height:100%;object-fit:cover}
.facts{list-style:none;padding:0;margin:1.2rem 0}.facts li{display:flex;justify-content:space-between;gap:1rem;padding:.85rem 0;border-bottom:1px solid var(--sand)}.facts li span:first-child{color:var(--mut)}
.rdv{background:var(--mint)}.card{background:#fff;border-radius:999px 999px 28px 28px;padding:5rem 1.4rem 1.6rem;max-width:760px;margin:2rem auto 0;text-align:left}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.9rem}.form label{display:grid;gap:.3rem;font-weight:600;font-size:.85rem}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;border:1.5px solid var(--sand);border-radius:14px;padding:.75rem .9rem;min-height:48px;background:var(--lime);width:100%}
.form button{grid-column:1/-1;display:flex;justify-content:center;gap:.5rem;align-items:center;background:var(--teal);color:#fff;border:0;border-radius:99px;padding:1rem;font:700 1rem Manrope;cursor:pointer}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.78rem;color:var(--mut);margin:0}
.acc{display:grid;gap:2rem}.tb{width:100%;border-collapse:collapse}.tb td{padding:.7rem 0;border-bottom:1px solid var(--sand)}.tb td+td{text-align:right}.tb .today td{color:var(--teal);font-weight:700}
.map{height:100%;min-height:380px;border-radius:999px 999px 24px 24px;overflow:hidden}.note{font-size:.8rem;color:var(--mut)}
.ft{border-top:1px solid var(--sand);padding:2.5rem 0 3rem;font-size:.84rem;color:var(--mut);text-align:center}.ft .credits{text-align:left;max-width:760px;margin:0 auto 1rem}
@media(min-width:800px){.nav{display:flex}.pills{grid-template-columns:repeat(4,1fr)}.duo{grid-template-columns:.8fr 1.2fr}.acc{grid-template-columns:1fr 1fr}.card{padding:5.5rem 3rem 2.4rem}}
'''
def build(F, M):
    hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else K.ph()}</td></tr>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet.')
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<header class="hd"><div class="w"><a class="lg" href="#top">Dr Manel Attia<small>Médecin dentiste · Hammamet</small></a>
<nav class="nav" aria-label="Navigation"><a href="#cabinet">Le cabinet</a><a href="#rdv">Rendez-vous</a><a href="#acces">Horaires et accès</a></nav><a class="bt" href="#rdv">Rendez-vous</a></div></header>
<main id="main"><section class="hero" id="top"><div class="w"><p class="k">Cabinet dentaire · {F['city']}</p><h1>Dr Manel <i>Attia</i></h1>
<p>Médecin dentiste à Hammamet. Consultations sur rendez-vous, par téléphone ou WhatsApp.</p>
<div class="acts"><a class="bt" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a><a class="bt o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div>
<div class="arch">{M.img('hero', 'Porte ancienne de la médina de Hammamet (photo d’illustration)', sizes='(max-width: 800px) 86vw, 560px', lazy=False)}</div></div></section>
<div class="pills"><div><small>Qualification</small><b>{F['sector']}</b></div><div><small>Adresse</small><b>{F['addr']}</b></div><div><small>Mercredi</small><b>{F['wed']}</b></div><div><small>E-mail</small><b><a href="mailto:{F['email']}">{F['email']}</a></b></div></div>
<section class="sec" id="cabinet"><div class="w duo"><div class="arch2">{M.img('cabinet', 'Fauteuil dentaire (photo d’illustration, ne montre pas le cabinet)', sizes='(max-width: 800px) 90vw, 420px')}</div>
<div><p class="ey">Le cabinet</p><h2>Informations pratiques</h2><ul class="facts">
<li><span>Praticienne</span><span>Dr Manel Attia</span></li><li><span>Qualification</span><span>{F['sector']}</span></li><li><span>N° d'inscription à l'Ordre</span><span>{K.ph()}</span></li>
<li><span>Langues parlées</span><span>{K.ph()}</span></li><li><span>CNAM / assurances</span><span>{K.ph()}</span></li><li><span>Accès et parking</span><span>{K.ph()}</span></li></ul>
<p class="note">Pensez à apporter votre carte CNAM ou d'assurance et vos radios récentes éventuelles.</p></div></div></section>
<section class="sec rdv" id="rdv"><div class="w" style="text-align:center"><p class="ey">Rendez-vous</p><h2>Demander un rendez-vous</h2><p style="color:var(--mut)">Le message part sur le WhatsApp du cabinet ({F['tel']}) ; le cabinet vous confirme le créneau.</p>
<div class="card">{K.form(F, 'Bonjour, je souhaite prendre rendez-vous au cabinet du Dr Manel Attia :', K.MED_FORM, 'Envoyer sur WhatsApp')}</div></div></section>
<section class="sec" id="acces"><div class="w acc"><div><p class="ey">Horaires</p><h2>Consultations</h2><table class="tb">{hrs}</table><p class="note">{K.HOURS_NOTE}</p>
<p><b>{F['addr']}</b><br><a href="{K.telhref(F['tel'])}">{F['tel']}</a> · <a href="mailto:{F['email']}">{F['email']}</a></p><a class="bt o" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire</a></div>
<div class="map">{K.mapframe(F, 'map')}</div></div></section></main>
<footer class="ft"><div class="w">{M.credits()}{K.footer_legal(F)}</div></footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='14' fill='#0F5E59'/><path d='M16 54V30a16 16 0 0 1 32 0v24' fill='none' stroke='#DDF3EE' stroke-width='5'/></svg>"
    return K.page(F, 'Dr Manel Attia — Médecin dentiste à Hammamet (démo)', 'Cabinet dentaire du Dr Manel Attia à Hammamet : coordonnées, horaires, accès et demande de rendez-vous par WhatsApp.', FONTS, CSS, body, '#0F5E59', fav)
