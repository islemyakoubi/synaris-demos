# Centre Soliman Informatique & Langues Vivantes : grille « bento » techno, ligne de terminal, tuiles-langues avec « bonjour » en 5 langues.
# Space Grotesk + JetBrains Mono ; blanc bleuté / bleu électrique / citron vert / encre.
import gen_lot2 as K
FONTS = 'family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;600'
CSS = '''
:root{--bg:#F4F6FC;--blue:#2B59FF;--lime:#C6F432;--ink:#0E1330;--mut:#5a6180;--card:#fff}
body{background:var(--bg);color:var(--ink);font:400 1rem/1.6 'Space Grotesk',system-ui,sans-serif}h1,h2,h3{line-height:1;margin:0 0 .6rem;font-weight:700;letter-spacing:-.02em}
.w{width:min(1200px,100% - 2rem);margin-inline:auto}.mono{font-family:'JetBrains Mono',monospace}.ph{font:600 .7rem/1 'JetBrains Mono';background:#e6ebff;color:var(--blue);border-radius:6px;padding:.2rem .45rem;white-space:nowrap}
.rb{background:var(--ink);color:#b8c0e0;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:var(--lime)}
.hd .w{display:flex;justify-content:space-between;align-items:center;height:70px}.lg{display:flex;gap:.6rem;align-items:center;text-decoration:none;font-weight:700}.lg i{font-style:normal;background:var(--blue);color:#fff;border-radius:10px;padding:.35rem .5rem;font:600 .9rem 'JetBrains Mono'}
.bt{display:inline-flex;gap:.5rem;align-items:center;background:var(--blue);color:#fff;text-decoration:none;font-weight:700;padding:.85rem 1.2rem;border-radius:12px}.bt svg{width:18px}.bt.l{background:var(--lime);color:var(--ink)}
.bento{display:grid;gap:.8rem;grid-template-columns:repeat(2,1fr);padding:1rem 0 3rem}.t{background:var(--card);border-radius:22px;padding:1.3rem;position:relative;overflow:hidden;min-height:140px}
.t.hero{grid-column:1/-1;background:var(--ink);color:#fff;padding:2rem 1.5rem}.t.hero h1{font-size:clamp(2.4rem,6vw,4.4rem)}.t.hero h1 span{color:var(--lime)}
.term{font:400 .88rem 'JetBrains Mono';color:var(--lime);margin-bottom:1rem}.term:after{content:'_';animation:bl 1s steps(1) infinite}@keyframes bl{50%{opacity:0}}
.t.hero p{color:#b8c0e0;max-width:34rem}.acts{display:flex;gap:.7rem;flex-wrap:wrap;margin-top:1.2rem}
.lang{display:flex;flex-direction:column;justify-content:space-between}.lang b{font:700 2.6rem/1 'Space Grotesk'}.lang span{font:400 .95rem 'JetBrains Mono';color:var(--mut)}
.lang.fr{background:#e6ebff}.lang.en{background:var(--lime)}.lang.de{background:#ffe3dc}.lang.it{background:#dcf6ea}.lang.es{background:#fff1c7}.lang.it b,.lang.es b{color:var(--ink)}
.code{background:var(--blue);color:#fff;grid-column:1/-1}.code b{font:600 2.4rem 'JetBrains Mono'}.code p{margin:.3rem 0 0;color:#dfe6ff}
.pic{padding:0;min-height:200px}.pic img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.pic span{position:absolute;left:.8rem;bottom:.8rem;background:#fff;border-radius:8px;padding:.2rem .5rem;font:600 .72rem 'JetBrains Mono'}
.rate b{font-size:3rem;display:block}.rate small{color:var(--mut)}.facts ul{list-style:none;padding:0;margin:0}.facts li{padding:.35rem 0;border-bottom:1px dashed #d5dbef;font-size:.92rem}
.sec{padding:3rem 0}h2{font-size:clamp(2rem,5vw,3.2rem)}.ins{display:grid;gap:1.5rem}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.8rem;background:#fff;border-radius:22px;padding:1.4rem}.form label{display:grid;gap:.3rem;font:600 .78rem 'JetBrains Mono';color:var(--mut)}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;font-family:'Space Grotesk';font-size:1rem;color:var(--ink);border:1.5px solid #dfe4f3;border-radius:12px;padding:.75rem;min-height:48px;width:100%;background:var(--bg)}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--ink);color:var(--lime);border:0;border-radius:12px;padding:1rem;font:700 1rem 'Space Grotesk';cursor:pointer}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.78rem;color:var(--mut);margin:0}.tb{width:100%;border-collapse:collapse;font-size:.92rem}.tb td{padding:.45rem 0;border-bottom:1px dashed #d5dbef}.tb td+td{text-align:right;font-family:'JetBrains Mono';font-size:.82rem}.tb .today td{color:var(--blue);font-weight:700}
.map{height:100%;min-height:300px;border-radius:22px;overflow:hidden}.note{font-size:.78rem;color:var(--mut)}.ft{padding:2rem 0 3rem;font-size:.8rem;color:var(--mut)}
@media(min-width:900px){.bento{grid-template-columns:repeat(6,1fr);grid-auto-rows:minmax(150px,auto)}.t.hero{grid-column:span 4;grid-row:span 2;padding:2.6rem}.lang{grid-column:span 1}
.pic.a{grid-column:span 2;grid-row:span 2}.code{grid-column:span 2}.rate{grid-column:span 1}.facts{grid-column:span 3}.pic.b{grid-column:span 2}.ins{grid-template-columns:1fr 1fr}}
'''
def build(F, M):
    CODE = K.esc('</>'); r = F['rating']; hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else "à confirmer"}</td></tr>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour, je souhaite des informations sur vos formations (langues / informatique).')
    L = [('fr', 'FR', 'Bonjour'), ('en', 'EN', 'Hello'), ('de', 'DE', 'Hallo'), ('it', 'IT', 'Ciao'), ('es', 'ES', 'Hola')]
    langs = ''.join(f'<div class="t lang {c}"><b>{b}</b><span>{h}</span></div>' for c, b, h in L)
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<header class="hd"><div class="w"><a class="lg" href="#top"><i>{CODE}</i>Soliman Informatique et Langues</a><a class="bt" href="#inscription">S'inscrire</a></div></header>
<main id="main" class="w"><div class="bento" id="top">
<div class="t hero"><p class="term">$ soliman --langues --informatique</p><h1>Langues vivantes<br>et <span>informatique</span>, à Soliman.</h1><p>Centre de formation privé agréé, créé en 2022. Français, anglais, allemand, italien, espagnol et informatique.</p>
<div class="acts"><a class="bt l" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a><a class="bt" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div></div>
<div class="t pic a">{M.img('hero', 'Salle informatique (photo d’illustration)', sizes='(max-width: 900px) 100vw, 33vw', lazy=False)}<span>salle_info.jpg · illustration</span></div>
{langs}<div class="t code"><b>{CODE}</b><p>Informatique : modules et niveaux {K.ph()}</p></div>
<div class="t rate"><b>{r[0]}</b><small>/5 · {r[1]} avis {r[2]}<br>relevé le {K.CONSULTED}</small></div>
<div class="t facts"><ul><li>✔ Centre privé agréé · créé en 2022</li><li>✔ 5 langues + informatique</li><li>✔ Mercredi {F['wed']}</li><li>✔ Tarifs et calendrier : {K.ph()}</li></ul></div>
<div class="t pic b">{M.img('classe', 'Salle de cours de langues (photo d’illustration)', sizes='(max-width: 900px) 50vw, 33vw')}<span>classe.jpg · illustration</span></div></div>
<section class="sec ins" id="inscription"><div><p class="mono" style="color:var(--blue)">// inscription</p><h2>Réservez votre place</h2><p style="color:var(--mut)">Choisissez la formation : la demande part sur le WhatsApp du centre ({F['tel']}).</p>
<div class="t pic" style="min-height:260px;margin-top:1rem">{M.img('livres', 'Méthodes de langues (photo d’illustration)', sizes='(max-width: 900px) 100vw, 50vw')}<span>methodes.jpg · illustration</span></div></div>
{K.form(F, 'Bonjour, je souhaite m’inscrire au Centre Soliman Informatique et Langues Vivantes :', [('text', 'Nom et prénom'), ('tel', 'Téléphone'), ('select', 'Formation', ['Français', 'Anglais', 'Allemand', 'Italien', 'Espagnol', 'Informatique']), ('select', 'Niveau', ['Débutant', 'Intermédiaire', 'Avancé', 'Je ne sais pas']), ('select', 'Pour', ['Adulte', 'Élève', 'Étudiant(e)']), ('textarea', 'Message (facultatif)')], 'Envoyer ma demande', note="Démo : aucune donnée n'est enregistrée. Le bouton ouvre WhatsApp avec votre demande.")}</section>
<section class="sec ins"><div class="t"><h3>Horaires</h3><table class="tb">{hrs}</table><p class="note">{K.HOURS_NOTE}</p><p><b>Adresse :</b> {F['addr']}<br><b>Tél. :</b> {F['tel']} · {F['tel2']}</p><a class="bt" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire</a></div><div class="map">{K.mapframe(F)}</div></section></main>
<footer class="ft w">{M.credits()}{K.footer_legal(F)}</footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='16' fill='#2B59FF'/><text x='32' y='41' font-size='22' text-anchor='middle' fill='#C6F432' font-family='monospace'>SL</text></svg>"
    return K.page(F, 'Centre Soliman Informatique & Langues Vivantes — Formations à Soliman (démo)', 'Centre Soliman Informatique et Langues Vivantes : français, anglais, allemand, italien, espagnol et informatique à Soliman. Inscription par WhatsApp.', FONTS, CSS, body, '#2B59FF', fav)
