# Dr Nawel Nacef, médecin dentiste (Kélibia) : carte postale de Kélibia.
# Fraunces + Work Sans ; bleu Kélibia / blanc / sable / rouge timbre. Hero = carte postale recto-verso avec timbre, fiches bristol inclinées, horaires en ticket, carte en polaroïd.
import gen_lot2 as K
FONTS = 'family=Fraunces:opsz,wght@9..144,400;9..144,700&family=Work+Sans:wght@400;500;600'
CSS = '''
:root{--blue:#1C4E80;--sand:#F3E9D8;--red:#C8553D;--ink:#1d2a36;--mut:#5f6b76}
body{background:var(--sand);color:var(--ink);font:400 1rem/1.65 'Work Sans',system-ui,sans-serif;background-image:radial-gradient(rgba(28,78,128,.07) 1px,transparent 1px);background-size:18px 18px}
h1,h2,h3{font-family:Fraunces,serif;line-height:1.05;margin:0 0 .6rem}.w{width:min(1140px,100% - 2.4rem);margin-inline:auto}
.ph{font:500 .72rem/1 'Work Sans';color:var(--red);border:1px dashed var(--red);border-radius:4px;padding:.15rem .4rem;white-space:nowrap}
.rb{background:var(--blue);color:#d7e3f0;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:#fff}
.hd .w{display:flex;justify-content:space-between;align-items:center;height:70px}.lg{text-decoration:none;font:700 1.25rem Fraunces;color:var(--blue)}.lg span{color:var(--red)}
.nav{display:none;gap:1.5rem;font-weight:500}.nav a{text-decoration:none}.bt{display:inline-flex;gap:.5rem;align-items:center;background:var(--red);color:#fff;text-decoration:none;font-weight:600;padding:.85rem 1.2rem;border-radius:6px}.bt svg{width:18px}
.bt.b{background:var(--blue)}.pc{background:#fff;margin:2rem auto 0;display:grid;box-shadow:0 30px 60px -30px rgba(28,78,128,.45),0 0 0 1px #e6dccb;transform:rotate(-1deg)}
.pc .ph-img{position:relative;min-height:320px}.pc .ph-img img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.pc .ph-img span{position:absolute;left:1rem;bottom:1rem;background:#fff;font:italic 700 1.4rem Fraunces;color:var(--blue);padding:.3rem .8rem}
.back{padding:1.6rem;position:relative;display:flex;flex-direction:column;gap:1rem}.back .msg{font:400 1.05rem/1.6 Fraunces;color:var(--mut);padding-right:6.5rem}
.back h1{font-size:clamp(2.3rem,5vw,3.4rem);color:var(--blue)}.lines{border-top:1.5px solid #cfd8e2}.lines p{margin:0;padding:.65rem 0;border-bottom:1.5px solid #cfd8e2;font-weight:500}
.stamp{position:absolute;top:1.4rem;right:1.4rem;width:92px;height:108px;border:2px dashed var(--red);display:grid;place-items:center;text-align:center;color:var(--red);font:700 .78rem/1.2 Fraunces;transform:rotate(4deg);background:#fff7f1}
.stamp b{display:block;font-size:1.5rem}.acts{display:flex;gap:.7rem;flex-wrap:wrap}
.sec{padding:4.5rem 0}.ey{font-weight:600;letter-spacing:.2em;text-transform:uppercase;font-size:.75rem;color:var(--red)}h2{font-size:clamp(2.2rem,5vw,3.3rem);color:var(--blue)}
.cards{display:grid;gap:1.4rem;margin-top:2rem}.cd{background:#fffdf8;padding:1.6rem;border-top:6px solid var(--blue);box-shadow:0 12px 30px -18px rgba(0,0,0,.35)}
.cd:nth-child(1){transform:rotate(-1.2deg)}.cd:nth-child(2){transform:rotate(.8deg);border-color:var(--red)}.cd:nth-child(3){transform:rotate(-.5deg)}
.cd h3{font-size:1.5rem;color:var(--blue)}.cd ul{list-style:none;padding:0;margin:0}.cd li{padding:.45rem 0;border-bottom:1px dotted #c9c0ae}
.tk{background:#fff;max-width:520px;padding:1.6rem;position:relative;border-radius:10px;-webkit-mask:radial-gradient(circle at 0 50%,transparent 14px,#000 15px) left/51% 100% no-repeat,radial-gradient(circle at 100% 50%,transparent 14px,#000 15px) right/51% 100% no-repeat;mask:radial-gradient(circle at 0 50%,transparent 14px,#000 15px) left/51% 100% no-repeat,radial-gradient(circle at 100% 50%,transparent 14px,#000 15px) right/51% 100% no-repeat}
.tb{width:100%;border-collapse:collapse;font-family:Fraunces}.tb td{padding:.55rem 0;border-bottom:1.5px dashed #d5ccb9}.tb td+td{text-align:right;font-family:'Work Sans'}.tb .today td{color:var(--red);font-weight:700}
.duo{display:grid;gap:2.5rem;align-items:start}.form{display:grid;grid-template-columns:1fr 1fr;gap:.8rem;background:#fff;padding:1.5rem;border-left:6px solid var(--red)}
.form label{display:grid;gap:.3rem;font-size:.84rem;font-weight:600}.form .full{grid-column:1/-1}.form input,.form select,.form textarea{font:inherit;border:0;border-bottom:1.5px solid #b9c4cf;background:#f8f5ee;padding:.7rem;min-height:46px;width:100%}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--blue);color:#fff;border:0;padding:1rem;font:600 1rem 'Work Sans';border-radius:6px;cursor:pointer}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.78rem;color:var(--mut);margin:0}.pola{background:#fff;padding:.8rem .8rem 3rem;box-shadow:0 20px 40px -24px rgba(0,0,0,.45);transform:rotate(1.2deg);position:relative}
.pola .map{height:340px}.pola p{position:absolute;bottom:.6rem;left:1rem;margin:0;font:italic 1.1rem Fraunces;color:var(--blue)}.note{font-size:.8rem;color:var(--mut)}
.ft{padding:2rem 0 3rem;font-size:.84rem;color:var(--mut);border-top:1.5px dashed #c9c0ae}
@media(min-width:820px){.nav{display:flex}.pc{grid-template-columns:1.1fr 1fr}.pc .ph-img{min-height:520px}.back{padding:2.4rem 2.2rem;border-left:1.5px solid #e2d9c8}.cards{grid-template-columns:repeat(3,1fr)}.duo{grid-template-columns:1fr 1fr}}
'''
def build(F, M):
    hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else K.ph()}</td></tr>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet.')
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<header class="hd"><div class="w"><a class="lg" href="#top">Dr Nawel <span>Nacef</span></a><nav class="nav" aria-label="Navigation"><a href="#cabinet">Le cabinet</a><a href="#horaires">Horaires</a><a href="#rdv">Rendez-vous</a></nav><a class="bt" href="#rdv">Rendez-vous</a></div></header>
<main id="main"><div class="w"><article class="pc" id="top"><div class="ph-img">{M.img('hero', 'Fort byzantin de Kélibia et la mer (photo d’illustration)', sizes='(max-width: 820px) 100vw, 55vw', lazy=False)}<span>Kélibia</span></div>
<div class="back"><span class="stamp" aria-hidden="true">Cabinet<b>2023</b>Kélibia</span><p class="ey">Cabinet dentaire</p><h1>Dr Nawel Nacef</h1>
<p class="msg">Médecin dentiste à Kélibia. Rendez-vous par téléphone ou WhatsApp.</p>
<div class="lines"><p>{F['sector']}</p><p>{F['addr']}</p><p><a href="{K.telhref(F['tel'])}">{F['tel']}</a> · <a href="mailto:{F['email']}">{F['email']}</a></p></div>
<div class="acts"><a class="bt" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a><a class="bt b" href="{K.telhref(F['tel'])}">{K.I['phone']}Appeler</a></div></div></article></div>
<section class="sec" id="cabinet"><div class="w"><p class="ey">Le cabinet</p><h2>En bref</h2><div class="cards">
<div class="cd"><h3>Identité</h3><ul><li>Dr Nawel Nacef</li><li>{F['sector']}</li><li>{F['extra'][0]}</li><li>N° d'Ordre : {K.ph()}</li></ul></div>
<div class="cd"><h3>Au cabinet</h3><ul><li>Langues parlées : {K.ph()}</li><li>CNAM / assurances : {K.ph()}</li><li>Accessibilité : {K.ph()}</li><li>Paiement : {K.ph()}</li></ul></div>
<div class="cd"><h3>Votre visite</h3><ul><li>Sur rendez-vous</li><li>Carte CNAM ou d'assurance</li><li>Radios récentes éventuelles</li></ul></div></div></div></section>
<section class="sec" id="horaires" style="padding-top:0"><div class="w duo"><div><p class="ey">Horaires</p><h2>Jours de consultation</h2><div class="tk"><table class="tb">{hrs}</table></div><p class="note">{K.HOURS_NOTE}</p></div>
<div class="pola">{K.mapframe(F)}<p>{F['addr']}</p></div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w duo"><div><p class="ey">Rendez-vous</p><h2>Écrire au cabinet</h2><p>Votre demande part sur le WhatsApp du cabinet ({F['tel']}). Le cabinet vous répond pour fixer l'heure.</p>
<a class="bt b" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire Google Maps</a></div>{K.form(F, 'Bonjour, je souhaite prendre rendez-vous au cabinet du Dr Nawel Nacef :', K.MED_FORM, 'Envoyer sur WhatsApp')}</div></section></main>
<footer class="ft"><div class="w">{M.credits()}{K.footer_legal(F)}</div></footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' fill='#1C4E80'/><rect x='10' y='10' width='44' height='44' fill='none' stroke='#fff' stroke-dasharray='4 3' stroke-width='3'/><text x='32' y='41' font-size='22' text-anchor='middle' fill='#fff' font-family='Georgia'>N</text></svg>"
    return K.page(F, 'Dr Nawel Nacef — Médecin dentiste à Kélibia (démo)', 'Cabinet dentaire du Dr Nawel Nacef à Kélibia : coordonnées, horaires, accès et demande de rendez-vous par WhatsApp.', FONTS, CSS, body, '#1C4E80', fav)
