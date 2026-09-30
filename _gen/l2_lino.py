# Lino, garderie scolaire (Nabeul) : univers enfantin doux, formes « blob » pastel, séparateurs ondulés, cartes autocollants inclinées, nom arabe, note Google (autorisée hors santé), lien Instagram.
# Fredoka + Quicksand ; pêche / menthe / lilas / bleu nuit.
import gen_lot2 as K
FONTS = 'family=Fredoka:wght@500;600;700&family=Quicksand:wght@500;600;700'
CSS = '''
:root{--pe:#FFD8C2;--mi:#BDEBD7;--li:#D9CCFF;--sk:#C8E6FF;--nv:#2B2D5C;--mut:#5d6085;--cr:#FFFAF3;--or:#FF8A5B}
body{background:var(--cr);color:var(--nv);font:500 1rem/1.65 Quicksand,system-ui,sans-serif}h1,h2,h3{font-family:Fredoka,sans-serif;font-weight:700;line-height:1;margin:0 0 .6rem}
.w{width:min(1120px,100% - 2rem);margin-inline:auto}.ph{font:700 .72rem/1 Quicksand;color:var(--nv);background:#fff;border:2px dashed var(--nv);border-radius:99px;padding:.18rem .5rem;white-space:nowrap}
.rb{background:var(--nv);color:#cfd0ef;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:#fff}
.hd .w{display:flex;justify-content:space-between;align-items:center;height:76px}.lg{font:700 1.9rem Fredoka;text-decoration:none;color:var(--or);display:flex;gap:.6rem;align-items:baseline}.lg small{font:600 1rem 'Noto Kufi Arabic',Fredoka,sans-serif;color:var(--nv)}
.bt{display:inline-flex;gap:.5rem;align-items:center;background:var(--nv);color:#fff;text-decoration:none;font:600 1rem Fredoka;padding:.85rem 1.3rem;border-radius:99px;box-shadow:0 5px 0 #15163a}.bt svg{width:18px}.bt.o{background:var(--or);box-shadow:0 5px 0 #c9562d}
.hero{position:relative;padding:2.5rem 0 5rem;overflow:hidden}.blob{position:absolute;border-radius:42% 58% 63% 37%/45% 38% 62% 55%;z-index:0}
.b1{width:420px;height:420px;background:var(--pe);right:-80px;top:-60px}.b2{width:260px;height:260px;background:var(--mi);left:-90px;bottom:0}.b3{width:160px;height:160px;background:var(--li);right:30%;bottom:10px}
.hero .w{position:relative;z-index:1;display:grid;gap:2rem;align-items:center}.hero h1{font-size:clamp(3rem,8vw,5.6rem)}.hero h1 span{color:var(--or)}.hero .ar{font:700 1.6rem 'Noto Kufi Arabic',sans-serif;margin:.2rem 0 1rem}.hero p{font-size:1.12rem;max-width:30rem}
.acts{display:flex;gap:.8rem;flex-wrap:wrap;margin-top:1.4rem}.stk{position:relative}.stk .ph1{border-radius:36px;overflow:hidden;transform:rotate(2.5deg);border:10px solid #fff;box-shadow:0 20px 40px -20px rgba(43,45,92,.4)}.stk .ph1 img{width:100%;aspect-ratio:4/3;object-fit:cover}
.star{position:absolute;left:-10px;bottom:-24px;background:#fff;border-radius:22px;padding:.8rem 1.1rem;transform:rotate(-6deg);box-shadow:0 12px 24px -12px rgba(43,45,92,.5);font:700 1.5rem Fredoka}.star small{display:block;font:600 .76rem Quicksand;color:var(--mut)}
.wave{display:block;width:100%;height:60px}.sec{padding:3.5rem 0}.sec h2{font-size:clamp(2.2rem,5vw,3.2rem);text-align:center}.sec .lead{text-align:center;color:var(--mut);max-width:36rem;margin:0 auto 2rem}
.cards{display:grid;gap:1.4rem}.cd{border-radius:28px;padding:1.5rem;transform:rotate(-1.5deg)}.cd:nth-child(2){transform:rotate(1.5deg)}.cd:nth-child(3){transform:rotate(-.8deg)}.cd h3{font-size:1.5rem}
.cd.a{background:var(--pe)}.cd.b{background:var(--mi)}.cd.c{background:var(--li)}.cd .ic{width:56px;height:56px;border-radius:18px;background:#fff;display:grid;place-items:center;margin-bottom:.8rem}.cd .ic svg{width:28px;color:var(--or)}
.gal{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}.gal figure{margin:0;border-radius:28px;overflow:hidden;border:8px solid #fff;box-shadow:0 14px 30px -18px rgba(43,45,92,.5)}.gal figure:nth-child(2){transform:translateY(22px) rotate(2deg)}.gal img{width:100%;aspect-ratio:1;object-fit:cover}
.mint{background:var(--mi)}.two{display:grid;gap:2rem}.tb{width:100%;border-collapse:separate;border-spacing:0 .4rem}.tb td{background:#fff;padding:.7rem 1rem}.tb td:first-child{border-radius:16px 0 0 16px;font-family:Fredoka;font-weight:600}.tb td+td{text-align:right;border-radius:0 16px 16px 0}.tb .today td{background:var(--nv);color:#fff}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.8rem;background:#fff;border-radius:28px;padding:1.5rem}.form label{display:grid;gap:.3rem;font-weight:700;font-size:.86rem}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;border:2px solid #e6e0f5;border-radius:16px;padding:.75rem;min-height:48px;width:100%;background:var(--cr)}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--or);color:#fff;border:0;border-radius:99px;padding:1rem;font:600 1.1rem Fredoka;cursor:pointer;box-shadow:0 5px 0 #c9562d}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.78rem;color:var(--mut);margin:0}.map{height:340px;border-radius:28px;overflow:hidden;border:8px solid #fff}.note{font-size:.82rem;color:var(--mut)}.ft{padding:2rem 0 3rem;font-size:.82rem;color:var(--mut)}
@media(min-width:880px){.hero .w{grid-template-columns:1.05fr .95fr}.cards{grid-template-columns:repeat(3,1fr)}.two{grid-template-columns:1fr 1fr;align-items:start}}
@media(max-width:600px){.gal{grid-template-columns:1fr 1fr}.gal figure:nth-child(3){display:none}.b1{width:260px;height:260px}.lg small{display:none}}
'''
def wave(top, bot):
    return f'<svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true" style="background:{top}"><path d="M0 30 C240 60 480 0 720 30 S1200 60 1440 30 V60 H0z" fill="{bot}"/></svg>'
def build(F, M):
    hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else "à confirmer"}</td></tr>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour, je souhaite des informations sur la garderie Lino pour mon enfant.')
    r = F['rating']
    spec = [('text', 'Nom du parent'), ('tel', 'Téléphone'), ('text', "Âge ou classe de l'enfant"), ('select', 'Je souhaite', ['Une information', 'Visiter la garderie', 'Une inscription']), ('textarea', 'Message (facultatif)')]
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<header class="hd"><div class="w"><a class="lg" href="#top">Lino <small lang="ar" dir="rtl">{F['ar']}</small></a><a class="bt" href="{K.telhref(F['tel'])}">{K.I['phone']}Appeler</a></div></header>
<main id="main"><section class="hero" id="top"><span class="blob b1"></span><span class="blob b2"></span><span class="blob b3"></span><div class="w"><div><h1>Garderie <span>Lino</span></h1><p class="ar" lang="ar" dir="rtl">{F['ar']}</p><p>Garderie scolaire à Nabeul. Pour les horaires, les places et l'inscription, appelez-nous ou écrivez sur WhatsApp.</p>
<div class="acts"><a class="bt o" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a><a class="bt" href="{F['ig']}" target="_blank" rel="noopener">Instagram</a></div></div>
<div class="stk"><div class="ph1">{M.img('hero', 'Crayons de couleur (photo d’illustration)', sizes='(max-width: 880px) 100vw, 520px', lazy=False)}</div><div class="star">★ {r[0]}<small>{r[1]} avis sur {r[2]}</small></div></div></div></section>
{wave('var(--cr)', '#fff')}<section class="sec" style="background:#fff"><div class="w"><h2>La garderie</h2><p class="lead">Les informations ci-dessous sont à compléter avec l'équipe de Lino.</p>
<div class="cards"><div class="cd a"><div class="ic">{K.I['heart']}</div><h3>Accueil des écoliers</h3><p>Âges accueillis, avant et après l'école, mercredi après-midi : {K.ph()}</p></div>
<div class="cd b"><div class="ic">{K.I['cal']}</div><h3>Activités</h3><p>Aide aux devoirs, jeux, activités manuelles : programme {K.ph()}</p></div>
<div class="cd c"><div class="ic">{K.I['pin']}</div><h3>À Nabeul</h3><p>{F['addr']}. Transport et repas : {K.ph()}</p></div></div>
<div class="gal" style="margin-top:3rem"><figure>{M.img('dessin', 'Enfant qui dessine (photo d’illustration, ne montre pas la garderie)', sizes='(max-width: 600px) 50vw, 33vw')}</figure><figure>{M.img('jouets', 'Jouets en bois (photo d’illustration)', sizes='(max-width: 600px) 50vw, 33vw')}</figure><figure>{M.img('crayons', 'Pot de crayons de couleur (photo d’illustration)', sizes='33vw')}</figure></div></div></section>
{wave('#fff', 'var(--mi)')}<section class="sec mint" id="horaires"><div class="w two"><div><h2 style="text-align:left">Horaires</h2><table class="tb">{hrs}</table><p class="note">{K.HOURS_NOTE}</p></div>
<div id="contact"><h2 style="text-align:left">Nous écrire</h2>{K.form(F, 'Bonjour Lino, je vous écris au sujet de mon enfant :', spec, 'Envoyer sur WhatsApp', note="Démo : aucune donnée n'est enregistrée. Le bouton ouvre WhatsApp avec votre message pour la garderie.")}</div></div></section>
{wave('var(--mi)', 'var(--cr)')}<section class="sec"><div class="w two"><div class="map">{K.mapframe(F)}</div><div><h2 style="text-align:left">Nous trouver</h2><p>{F['addr']}</p><p>Téléphone : <a href="{K.telhref(F['tel'])}">{F['tel']}</a></p><div class="acts"><a class="bt" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire</a><a class="bt o" href="{F['ig']}" target="_blank" rel="noopener">@garderielino</a></div></div></div></section></main>
<footer class="ft w">{M.credits()}{K.footer_legal(F)}</footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><path d='M32 4c16 0 28 10 28 26S48 60 30 60 4 48 4 32 16 4 32 4z' fill='#FF8A5B'/><text x='32' y='44' font-size='30' text-anchor='middle' fill='#fff' font-family='Arial' font-weight='700'>L</text></svg>"
    return K.page(F, 'Lino — Garderie scolaire à Nabeul | محضنة لينو المدرسية (démo)', 'Lino, garderie scolaire à Nabeul : informations, horaires, accès et contact par WhatsApp.', FONTS + '&family=Noto+Kufi+Arabic:wght@600;700', CSS, body, '#FF8A5B', fav)
