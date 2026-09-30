# Dr Sarra Haouet, médecin dentiste (Mrezga + Nabeul centre) : « carte d'abord ». Hero moitié carte avec sélecteur des 2 cabinets, bande photo, horaires + formulaire côte à côte.
# Urbanist + Merriweather ; bleu mer / sable / marine.
import gen_lot2 as K
FONTS = 'family=Urbanist:wght@400;600;800&family=Merriweather:ital,wght@0,400;1,400'
CSS = '''
:root{--sea:#0E7490;--sand:#F6EFE4;--navy:#0B2A3A;--mut:#5e6f76;--line:#e4dccd}
body{background:var(--sand);color:var(--navy);font:400 1rem/1.65 Urbanist,system-ui,sans-serif}h1,h2,h3{font-family:Urbanist;font-weight:800;line-height:1;margin:0 0 .6rem;letter-spacing:-.02em}
.ser{font-family:Merriweather,serif}.w{width:min(1200px,100% - 2rem);margin-inline:auto}.ph{font:600 .72rem/1 Urbanist;color:var(--sea);background:#dff0f3;border-radius:4px;padding:.2rem .45rem;white-space:nowrap}
.rb{background:var(--navy);color:#bcd3dc;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:#fff}
.hero{display:grid;min-height:calc(100vh - 32px)}.left{padding:2rem 1.2rem;display:flex;flex-direction:column;justify-content:center;gap:1rem}
.left .k{font-weight:600;letter-spacing:.2em;text-transform:uppercase;font-size:.75rem;color:var(--sea)}.left h1{font-size:clamp(2.8rem,6vw,4.8rem)}.left .ser{color:var(--mut);font-style:italic}
.sw{display:grid;grid-template-columns:1fr 1fr;gap:.5rem}.sw button{font:600 1rem Urbanist;border:2px solid var(--navy);background:transparent;color:var(--navy);border-radius:12px;padding:.9rem;cursor:pointer;text-align:left}
.sw button small{display:block;font-weight:400;font-size:.78rem;color:var(--mut)}.sw button[aria-selected=true]{background:var(--navy);color:#fff}.sw button[aria-selected=true] small{color:#bcd3dc}
.cab{background:#fff;border-radius:16px;padding:1.2rem;border:1px solid var(--line)}.cab p{margin:.2rem 0}.cab .t{font-weight:800;font-size:1.3rem}
.bt{display:inline-flex;gap:.5rem;align-items:center;background:var(--sea);color:#fff;text-decoration:none;font-weight:700;padding:.8rem 1.1rem;border-radius:12px;margin:.6rem .4rem 0 0}.bt svg{width:18px}.bt.n{background:var(--navy)}
.right{position:relative;min-height:420px}.right .map{position:absolute;inset:0;height:100%}.right .pin{position:absolute;left:1rem;bottom:2.2rem;background:#fff;border-radius:12px;padding:.5rem .8rem;font-weight:700;font-size:.85rem;box-shadow:0 10px 30px -12px rgba(0,0,0,.4);display:flex;gap:.4rem;align-items:center;z-index:2}.right .pin svg{width:18px;color:var(--sea)}
.strip{display:grid;grid-template-columns:repeat(3,1fr);gap:.5rem;padding:.5rem}.strip figure{margin:0;position:relative;height:220px;overflow:hidden;border-radius:14px}.strip img{width:100%;height:100%;object-fit:cover}
.strip figcaption{position:absolute;left:.6rem;bottom:.6rem;background:rgba(255,255,255,.92);border-radius:8px;padding:.2rem .5rem;font-size:.74rem;font-weight:600}
.sec{padding:4rem 0}.two{display:grid;gap:2rem}.sec h2{font-size:clamp(2rem,4.5vw,3rem)}.ey{font-weight:600;letter-spacing:.2em;text-transform:uppercase;font-size:.74rem;color:var(--sea)}
.tb{width:100%;border-collapse:collapse}.tb td{padding:.65rem 0;border-bottom:1px solid var(--line)}.tb td+td{text-align:right}.tb .today td{color:var(--sea);font-weight:800}
.kv{display:grid;grid-template-columns:1fr 1fr;gap:.6rem;margin-top:1.4rem}.kv div{background:#fff;border-radius:12px;padding:.8rem;border:1px solid var(--line)}.kv small{display:block;font-size:.7rem;color:var(--mut);letter-spacing:.12em;text-transform:uppercase}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.8rem;background:var(--navy);color:#fff;border-radius:20px;padding:1.5rem}.form label{display:grid;gap:.3rem;font-weight:600;font-size:.84rem}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;border:0;border-radius:10px;padding:.75rem;min-height:48px;width:100%;background:#16384b;color:#fff}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:#fff;color:var(--navy);border:0;border-radius:10px;padding:1rem;font:800 1rem Urbanist;cursor:pointer}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.76rem;color:#9fb9c4;margin:0}.note{font-size:.8rem;color:var(--mut)}.ft{padding:2rem 0 3rem;font-size:.82rem;color:var(--mut)}
@media(min-width:900px){.hero{grid-template-columns:.95fr 1.05fr}.left{padding:3rem 3rem 3rem max(1.2rem,calc((100vw - 1200px)/2))}.two{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.strip{grid-template-columns:1fr 1fr}.strip figure:first-child{grid-column:1/-1}}
'''
def build(F, M):
    hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else K.ph()}</td></tr>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet.')
    F2 = dict(F, q='Nabeul centre, Tunisie', name='Cabinet de Nabeul centre')
    spec = K.MED_FORM[:2] + [('select', 'Cabinet', ['Mrezga', 'Nabeul centre', 'Peu importe'])] + K.MED_FORM[2:]
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<main id="main"><section class="hero" data-tabs><div class="left"><p class="k">Médecin dentiste · Mrezga et Nabeul</p><h1>Dr Sarra Haouet</h1><p class="ser">Deux cabinets, à Mrezga et au centre de Nabeul. Choisissez le plus proche :</p>
<div class="sw" role="tablist"><button type="button" role="tab" data-tab="m" aria-selected="true">Mrezga<small>Cabinet principal</small></button><button type="button" role="tab" data-tab="n" aria-selected="false">Nabeul centre<small>Second cabinet</small></button></div>
<div class="cab" data-panel="m"><p class="t">Cabinet de Mrezga</p><p>{F['addr']}</p><p><a href="{K.telhref(F['tel'])}">{F['tel']}</a></p><a class="bt" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a><a class="bt n" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire</a></div>
<div class="cab" data-panel="n" hidden><p class="t">Cabinet de Nabeul centre</p><p>{F['addr2']}</p><p><a href="{K.telhref(F['tel2'])}">{F['tel2']}</a></p><a class="bt n" href="{K.telhref(F['tel2'])}">{K.I['phone']}Appeler ce cabinet</a></div></div>
<div class="right"><div data-panel="m"><span class="pin">{K.I['pin']}Mrezga</span>{K.mapframe(F)}</div><div data-panel="n" hidden><span class="pin">{K.I['pin']}Nabeul centre (position approximative)</span>{K.mapframe(F2)}</div></div></section>
<div class="strip"><figure>{M.img('hero', 'Palmier à Mrezga (photo d’illustration)', sizes='(max-width: 600px) 100vw, 33vw', lazy=False)}<figcaption>Mrezga</figcaption></figure><figure>{M.img('cabinet', 'Fauteuil dentaire (photo d’illustration, ne montre pas le cabinet)', sizes='33vw')}<figcaption>Illustration</figcaption></figure><figure>{M.img('nabeul', 'Nabeul (photo d’illustration)', sizes='33vw')}<figcaption>Nabeul</figcaption></figure></div>
<section class="sec"><div class="w two"><div><p class="ey">Horaires</p><h2>Consultations</h2><table class="tb">{hrs}</table><p class="note">{K.HOURS_NOTE} Horaires propres à chaque cabinet : à confirmer.</p>
<div class="kv"><div><small>Qualification</small>{F['sector']}</div><div><small>N° d'Ordre</small>{K.ph()}</div><div><small>Langues</small>{K.ph()}</div><div><small>CNAM</small>{K.ph()}</div></div></div>
<div id="rdv"><p class="ey">Rendez-vous</p><h2>Écrire au cabinet</h2>{K.form(F, 'Bonjour, je souhaite prendre rendez-vous chez le Dr Sarra Haouet :', spec, 'Envoyer sur WhatsApp')}</div></div></section></main>
<footer class="ft w">{M.credits()}{K.footer_legal(F)}</footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='32' fill='#0E7490'/><path d='M32 14c-8 0-14 6-14 14 0 10 14 22 14 22s14-12 14-22c0-8-6-14-14-14z' fill='#F6EFE4'/></svg>"
    return K.page(F, 'Dr Sarra Haouet — Médecin dentiste à Mrezga et Nabeul (démo)', 'Cabinets dentaires du Dr Sarra Haouet à Mrezga et Nabeul centre : adresses, horaires, accès et demande de rendez-vous par WhatsApp.', FONTS, CSS, body, '#0E7490', fav)
