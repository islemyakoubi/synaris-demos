# NB Language Center (Dar Chaabane) : magazine typographique. Syne + Figtree ; encre / jaune tournesol / papier.
# Structure : hero à mots géants multilingues + photo inclinée, bandeau défilant, 2 cartes-langues XXL, 3 étapes, inscription, horaires | carte.
import gen_lot2 as K
FONTS = 'family=Syne:wght@600;800&family=Figtree:wght@400;600;700'
CSS = '''
:root{--ink:#14213D;--sun:#FCA311;--paper:#FFF8EC;--sky:#E5ECF6;--mut:#5b6478}
body{background:var(--paper);color:var(--ink);font:400 1.02rem/1.6 Figtree,system-ui,sans-serif}
h1,h2,h3{font-family:Syne,sans-serif;font-weight:800;line-height:.95;letter-spacing:-.02em;margin:0 0 .6rem}
.w{width:min(1180px,100% - 2.4rem);margin-inline:auto}.ph{font:600 .72rem/1 Figtree;background:var(--sky);border:1px dashed #9fb0cc;border-radius:5px;padding:.15rem .4rem;white-space:nowrap;color:var(--ink)}
.rb{background:var(--ink);color:#cfd6e4;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:var(--sun)}
.hd{position:sticky;top:0;z-index:30;background:var(--paper);border-bottom:2px solid var(--ink)}.hd .w{display:flex;align-items:center;justify-content:space-between;height:68px;gap:1rem}
.lg{display:flex;align-items:center;gap:.6rem;text-decoration:none;font:800 1.05rem/1 Syne}.lg i{width:40px;height:40px;font-size:.78rem;background:var(--sun);display:grid;place-items:center;font-style:normal;border:2px solid var(--ink);box-shadow:3px 3px 0 var(--ink)}
.nav{display:none;gap:1.6rem}.nav a{text-decoration:none;font-weight:600}.nav a:hover{color:#b36f00}
.bt{display:inline-flex;align-items:center;gap:.5rem;background:var(--ink);color:#fff;text-decoration:none;font-weight:700;padding:.85rem 1.2rem;border:2px solid var(--ink);box-shadow:4px 4px 0 var(--sun);transition:transform .15s}
.bt:hover{transform:translate(-2px,-2px)}.bt svg{width:18px;height:18px}.bt.y{background:var(--sun);color:var(--ink);box-shadow:4px 4px 0 var(--ink)}
.hero{padding:3rem 0 2.5rem;display:grid;gap:2.5rem}.words{font:800 clamp(3.6rem,13vw,9.5rem)/.86 Syne;letter-spacing:-.04em;margin:0}
.words span{display:block}.words span:nth-child(2){color:var(--sun);text-shadow:5px 5px 0 var(--ink)}.words span:nth-child(3){font-family:'Noto Kufi Arabic',Syne;font-size:.8em}
.hero p.l{font-size:1.15rem;max-width:34rem;color:var(--mut)}.acts{display:flex;flex-wrap:wrap;gap:1rem;margin-top:1.4rem}
.ph-card{position:relative;transform:rotate(2.5deg);border:2px solid var(--ink);box-shadow:10px 10px 0 var(--ink);background:#fff;padding:.7rem .7rem 3rem}
.ph-card img{width:100%;aspect-ratio:4/5;object-fit:cover}.ph-card figcaption{position:absolute;bottom:.8rem;left:.9rem;font:600 .9rem Figtree}
.stk{position:absolute;top:-1.4rem;right:-1rem;width:118px;height:118px;border-radius:50%;background:var(--sun);border:2px solid var(--ink);display:grid;place-items:center;text-align:center;font:800 1.5rem/1 Syne;transform:rotate(-10deg)}
.stk small{display:block;font:600 .68rem/1.2 Figtree;margin-top:.2rem}
.mq{border-block:2px solid var(--ink);background:var(--sun);overflow:hidden;white-space:nowrap;padding:.8rem 0;font:800 1.5rem/1 Syne}
.mq div{display:inline-block;animation:mq 26s linear infinite}.mq span{margin:0 1.4rem}@keyframes mq{to{transform:translateX(-50%)}}
.sec{padding:4.5rem 0}.kick{font:700 .8rem/1 Figtree;letter-spacing:.2em;text-transform:uppercase;color:#b36f00}
h2{font-size:clamp(2.3rem,6vw,4.2rem)}
.langs{display:grid;gap:1.4rem;margin-top:2rem}.lc{border:2px solid var(--ink);background:#fff;padding:1.6rem;position:relative;overflow:hidden;min-height:260px}
.lc b{position:absolute;right:-.5rem;bottom:-2.2rem;font:800 11rem/1 Syne;color:var(--sky);z-index:0}.lc>*{position:relative}
.lc h3{font-size:2.4rem}.lc .hi{font:600 1.1rem Figtree;color:#b36f00}.lc ul{padding-left:1.1rem;margin:.8rem 0 0}.lc.alt{background:var(--ink);color:#fff}.lc.alt b{color:#22335a}.lc.alt .hi{color:var(--sun)}
.steps{display:grid;gap:1rem;counter-reset:s;margin-top:2rem}.steps li{list-style:none;counter-increment:s;border-top:2px solid var(--ink);padding-top:1rem}
.steps li:before{content:counter(s,decimal-leading-zero);font:800 3rem/1 Syne;color:var(--sun);text-shadow:3px 3px 0 var(--ink);display:block;margin-bottom:.4rem}
.ins{background:var(--ink);color:#fff}.ins .w{display:grid;gap:2rem}.ins h2{color:#fff}.ins .kick{color:var(--sun)}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.9rem;background:var(--paper);color:var(--ink);padding:1.4rem;border:2px solid var(--sun);box-shadow:8px 8px 0 var(--sun)}
.form label{display:grid;gap:.3rem;font-weight:700;font-size:.85rem}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;border:2px solid var(--ink);background:#fff;padding:.7rem;min-height:46px;width:100%;border-radius:0}
.form button{grid-column:1/-1;display:flex;justify-content:center;align-items:center;gap:.5rem;background:var(--sun);color:var(--ink);border:2px solid var(--ink);font:800 1.05rem Syne;padding:1rem;cursor:pointer}
.form button svg{width:20px}.fnote{grid-column:1/-1;font-size:.78rem;color:var(--mut);margin:0}
.info{display:grid;gap:2rem}.tb{width:100%;border-collapse:collapse}.tb td{padding:.7rem .2rem;border-bottom:1px solid #d9d2c3}.tb tr.today td{font-weight:700;background:#fff1d6}
.tb td:last-child{text-align:right}.note{font-size:.8rem;color:var(--mut)}.map{height:360px;border:2px solid var(--ink)}
.ft{border-top:2px solid var(--ink);padding:2.5rem 0 5rem;font-size:.85rem;color:var(--mut)}.ft a{color:var(--ink)}.legal{max-width:60rem}
.fab{position:fixed;right:1rem;bottom:1rem;z-index:40}
@media(min-width:780px){.hero{grid-template-columns:1.25fr .75fr;align-items:center;padding:4.5rem 0 3.5rem}.langs{grid-template-columns:1fr 1fr}.steps{grid-template-columns:repeat(3,1fr)}
.ins .w{grid-template-columns:.8fr 1.2fr;align-items:start}.info{grid-template-columns:1fr 1fr}.nav{display:flex}.ft{padding-bottom:2.5rem}}
'''
def build(F, M):
    r = F['rating']; wa = K.walink(F['wa'], "Bonjour NB Language Center, je souhaite des informations sur vos cours de langues.")
    hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else K.ph()}</td></tr>' for n, d, v, k in K.hours(F))
    mq = ''.join(f'<span>{w}</span><span>✦</span>' for w in ['Deutsch', 'English', 'Allemand', 'Anglais', 'Dar Chaabane', 'Guten Tag', 'Good morning', 'صباح الخير'])
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<header class="hd"><div class="w"><a class="lg" href="#top"><i>NB</i>Language Center</a>
<nav class="nav" aria-label="Navigation"><a href="#langues">Langues</a><a href="#inscription">Inscription</a><a href="#infos">Horaires et accès</a></nav>
<a class="bt y" href="#inscription">S'inscrire</a></div></header>
<main id="main"><section class="w hero" id="top"><div>
<p class="kick">Institut de langues · {F['city']}</p>
<h1 class="words" aria-label="Hallo, Hello, Marhaba"><span>Hallo.</span><span>Hello.</span><span lang="ar">مرحبا.</span></h1>
<p class="l">Cours d'allemand et d'anglais à Dar Chaabane, au cœur du Cap Bon. Niveaux, groupes et horaires des cours {K.ph()}.</p>
<div class="acts"><a class="bt" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}Écrire sur WhatsApp</a><a class="bt y" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div></div>
<figure class="ph-card">{M.img('hero', 'Pile de livres colorés (photo d’illustration)', sizes='(max-width: 780px) 90vw, 40vw', lazy=False)}<figcaption>Photo d'illustration</figcaption>
<span class="stk">{r[0]}★<small>{r[1]} avis<br>{r[2]}</small></span></figure></section>
<div class="mq" aria-hidden="true"><div>{mq}{mq}</div></div>
<section class="sec w" id="langues"><p class="kick">Les langues</p><h2>Deux langues,<br>un seul centre.</h2>
<div class="langs"><article class="lc"><b>DE</b><p class="hi">Deutsch</p><h3>Allemand</h3><p>Pour les études, le travail ou le voyage.</p><ul><li>Niveaux proposés : {K.ph()}</li><li>Groupes ou cours particuliers : {K.ph()}</li><li>Tarifs : {K.ph()}</li></ul></article>
<article class="lc alt"><b>EN</b><p class="hi">English</p><h3>Anglais</h3><p>Pour l'école, l'université ou le quotidien.</p><ul><li>Niveaux proposés : {K.ph()}</li><li>Enfants / adultes : {K.ph()}</li><li>Tarifs : {K.ph()}</li></ul></article></div>
<p class="note" style="margin-top:1rem">Autres langues éventuelles : {K.ph()}</p></section>
<section class="sec w" style="padding-top:0"><p class="kick">S'inscrire en 3 temps</p><h2>Simple comme bonjour.</h2>
<ol class="steps"><li><h3>Votre demande</h3><p>Choisissez la langue et votre niveau estimé dans le formulaire.</p></li><li><h3>WhatsApp</h3><p>Le message part tout prêt vers le centre, sans appel.</p></li><li><h3>Le centre vous répond</h3><p>Groupe, créneau et démarrage : vous convenez ensemble des détails.</p></li></ol></section>
<section class="sec ins" id="inscription"><div class="w"><div><p class="kick">Inscription</p><h2>Prêt à parler ?</h2><p style="color:#cfd6e4">Envoyez votre demande : elle arrive directement sur le WhatsApp du centre ({F['tel']}).</p></div>
{K.form(F, 'Bonjour NB Language Center, je souhaite m’inscrire :', [('text', 'Nom et prénom'), ('tel', 'Téléphone'), ('select', 'Langue', ['Allemand', 'Anglais', 'Autre']), ('select', 'Niveau estimé', ['Débutant', 'Intermédiaire', 'Avancé', 'Je ne sais pas']), ('select', 'Pour', ['Moi (adulte)', 'Mon enfant', 'Étudiant(e)']), ('textarea', 'Message (facultatif)')], 'Envoyer ma demande', note="Démo : aucune donnée n'est enregistrée. Le bouton ouvre WhatsApp avec votre demande, que vous validez vous-même.")}</div></section>
<section class="sec w info" id="infos"><div><p class="kick">Horaires</p><h2 style="font-size:2.6rem">Quand passer</h2><table class="tb">{hrs}</table><p class="note">{K.HOURS_NOTE}</p>
<p><b>Adresse :</b> {F['addr']}<br><b>Téléphone :</b> <a href="{K.telhref(F['tel'])}">{F['tel']}</a><br><b>Facebook :</b> <a href="{F['fb']}" target="_blank" rel="noopener">page du centre</a></p>
<p class="note">Note {r[0]}/5 sur {r[1]} avis {r[2]}, relevée le {K.CONSULTED}.</p><a class="bt" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire</a></div>{K.mapframe(F)}</section></main>
<footer class="ft"><div class="w">{M.credits()}{K.footer_legal(F)}</div></footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' fill='#FCA311'/><text x='32' y='42' font-size='28' font-weight='800' text-anchor='middle' fill='#14213D' font-family='Arial'>NB</text></svg>"
    return K.page(F, 'NB Language Center — Cours d’allemand et d’anglais à Dar Chaabane (démo)', 'NB Language Center, institut de langues à Dar Chaabane (Cap Bon) : allemand, anglais. Inscription par WhatsApp, horaires et accès.',
                  FONTS + '&family=Noto+Kufi+Arabic:wght@800', CSS, body, '#FCA311', fav)
