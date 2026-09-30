# Elite Academy Hammamet, centre de formation : « cahier ». Marine profond, jaune électrique, papier quadrillé. Titre Bricolage Grotesque surligné au feutre (animé),
# photo scotchée inclinée + post-it, marquee, pages de cahier « à confirmer » (aucun programme inventé), étapes, galerie, formulaire. Bricolage Grotesque + Inter.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700;12..96,800&family=Inter:wght@300;400;500;600;700'
CSS = '''
:root{--bg:#0B1B3F;--fg:#F2F4FA;--acc:#FFE14D;--onacc:#0B1B3F;--line:rgba(242,244,250,.14);--hbg:rgba(11,27,63,.88);--disp:'Bricolage Grotesque',system-ui,sans-serif;--sans:Inter,system-ui,sans-serif;--r:12px;--mapbg:#12275A;--fbg:rgba(255,255,255,.05)}
h1,h2,h3{font-weight:800;letter-spacing:-.035em}.brand .mono{width:44px;height:44px;border-radius:12px;display:grid;place-items:center;background:var(--acc);color:var(--bg);font:800 1rem var(--disp);transform:rotate(-6deg)}
.grid{background-image:linear-gradient(rgba(242,244,250,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(242,244,250,.06) 1px,transparent 1px);background-size:32px 32px}
.hero{min-height:100svh;display:grid;grid-template-columns:1.05fr .95fr;gap:4rem;align-items:center;padding:9rem 0 4rem}
.hero h1{font-size:clamp(3.4rem,8.6vw,8.8rem);line-height:.9}.hl{position:relative;display:inline-block;z-index:0;color:var(--bg)}.hl:before{content:'';position:absolute;inset:.12em -.08em .02em;background:var(--acc);z-index:-1;transform:skew(-6deg) scaleX(0);transform-origin:left;animation:hl 1s cubic-bezier(.7,0,.2,1) .7s forwards;border-radius:6px}
@keyframes hl{to{transform:skew(-6deg) scaleX(1)}}.lede{max-width:33rem;font-size:1.1rem;margin:2rem 0 2.4rem;opacity:.85}.acts{display:flex;gap:1rem;flex-wrap:wrap}
.pol{position:relative;width:100%;background:#fff;padding:14px 14px 56px;transform:rotate(3deg);box-shadow:0 40px 80px rgba(0,0,0,.4);border-radius:4px;max-width:580px;justify-self:center;transition:transform .8s var(--ease)}.pol:hover{transform:rotate(0)}
.pol img{aspect-ratio:4/3.4;object-fit:cover;width:100%}.pol figcaption{position:absolute;left:14px;bottom:18px;color:#0B1B3F;font:600 .8rem var(--disp)}
.pol:before{content:'';position:absolute;top:-16px;left:40%;width:120px;height:34px;background:rgba(255,225,77,.75);transform:rotate(-4deg)}
.note2{position:absolute;right:-18px;top:-34px;width:190px;background:var(--acc);color:var(--bg);padding:1.1rem;font:700 1rem/1.25 var(--disp);transform:rotate(-5deg);box-shadow:0 20px 40px rgba(0,0,0,.35)}.note2 small{display:block;font:500 .72rem var(--sans);margin-top:.4rem}
.mq{border-block:1px solid var(--line);padding:1.3rem 0;font:800 clamp(2rem,4vw,3.4rem)/1 var(--disp);--mqs:30s}.mq span:nth-child(odd){color:var(--acc)}
.sec{padding:8rem 0}.sec h2{font-size:clamp(2.4rem,5vw,4.8rem);line-height:.96}
.facts{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin-top:3.6rem}.facts div{border:1px solid var(--line);border-radius:16px;padding:1.6rem;background:rgba(11,27,63,.6)}
.facts small{display:block;font:600 .64rem/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--acc);margin-bottom:.8rem}.facts p{margin:0;font:600 1.3rem/1.25 var(--disp)}
.paper{background:#F7F5EE;color:#0B1B3F;--line:rgba(11,27,63,.14)}.pages{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem;margin-top:4rem}
.pg{background:#fff repeating-linear-gradient(transparent 0 33px,rgba(29,78,216,.18) 33px 34px);border-radius:6px;padding:2.2rem 2rem 2.2rem 3rem;position:relative;box-shadow:0 20px 50px rgba(11,27,63,.1);transition:transform .6s var(--ease)}
.pg:hover{transform:translateY(-6px) rotate(-.6deg)}.pg:before{content:'';position:absolute;left:1.8rem;top:0;bottom:0;width:1px;background:#F08080}.pg svg{width:52px;height:52px;color:#1D4ED8;margin-bottom:1.6rem}
.pg h3{font-size:1.7rem;margin-bottom:.8rem}.pg p{font-size:.95rem;line-height:34px;margin:0 0 1rem}.paper .kick{color:#1D4ED8}.paper .btn.p{background:#0B1B3F;color:var(--acc)}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:0;margin-top:4rem;counter-reset:s}.steps li{list-style:none;padding:2rem 2rem 0 0;border-top:3px solid var(--acc);margin-right:2rem}.steps li:before{counter-increment:s;content:'0' counter(s);font:800 3.6rem/1 var(--disp);color:var(--acc);display:block;margin-bottom:1.2rem}
.steps h3{font-size:1.6rem;margin-bottom:.5rem}.steps p{opacity:.75;margin:0}
.gal{display:grid;grid-template-columns:1.4fr 1fr;grid-template-rows:260px 260px;gap:1rem}.gal figure{margin:0;border-radius:16px;overflow:hidden;position:relative}.gal figure:first-child{grid-row:span 2}
.gal img{width:100%;height:100%;object-fit:cover;transition:transform 1.4s var(--ease)}.gal figure:hover img{transform:scale(1.05)}.gal figcaption{position:absolute;left:.8rem;bottom:.8rem;background:var(--acc);color:var(--bg);font:600 .72rem var(--sans);padding:.3rem .6rem;border-radius:6px}
.info{display:grid;grid-template-columns:1fr 1fr;gap:1.4rem}.box{border:1px solid var(--line);border-radius:20px;padding:2.4rem;background:rgba(11,27,63,.7)}.box h3{font-size:1.8rem;margin-bottom:1rem}
.rdv{display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem}.rdv .box{background:#F7F5EE;color:#0B1B3F;--line:rgba(11,27,63,.15);--fln:rgba(11,27,63,.25);--acc:#0B1B3F;--onacc:#FFE14D}
.mapw{border-radius:20px}
@media(max-width:960px){.hero{grid-template-columns:1fr;padding-top:8rem}.pol{max-width:88%}.note2{right:-4px;top:-40px;width:150px;font-size:.9rem}.facts,.pages,.steps,.info,.rdv{grid-template-columns:1fr}.steps li{margin:0 0 2rem}.gal{grid-template-columns:1fr 1fr;grid-template-rows:200px 200px}.gal figure:first-child{grid-column:span 2;grid-row:auto}}
@media(max-width:760px){.sec{padding:5.5rem 0}.box{padding:1.6rem}.gal{grid-template-rows:220px 160px 160px}.gal figure:first-child{grid-column:span 2}}
'''
NOTE = "Démo : aucune donnée n'est enregistrée. Le bouton ouvre WhatsApp avec votre message ; le centre vous répond directement."
def build(F, M):
    msg = 'Bonjour, je souhaite des informations sur les formations d’Elite Academy.'
    brand = '<span class="mono">EA</span><span><b>Elite Academy</b><small>Centre de formation · Hammamet</small></span>'
    links = [('Le centre', '#centre'), ('Formations', '#formations'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    pages = [('book', 'Intitulés des formations', 'Liste des formations proposées par le centre.'), ('cal', 'Durées et rythmes', 'Calendrier, durée des sessions, horaires des cours.'), ('doc', 'Inscription', 'Conditions, pièces à fournir et modalités.')]
    pgh = ''.join(f'<article class="pg" data-rv style="--d:{i*.12:.2f}s">{IC[k]}<h3>{t}</h3><p>{p}</p>{ph()}</article>' for i, (k, t, p) in enumerate(pages))
    mq = ''.join(f'<span>{w}</span>' for w in ['Elite Academy', 'Formation', 'Hammamet', 'Inscriptions'] * 2)
    spec = [('text', 'Nom et prénom'), ('tel', 'Téléphone'), ('full', 'Formation souhaitée'), ('textarea', 'Message (facultatif)')]
    body = f'''{lux.header(brand, links, ('S’informer', '#rdv'))}<main id="main"><div class="grid">
<section class="w hero" id="top"><div><p class="kick rise">Centre de formation · Hammamet</p><h1 class="rise d1">Se <span class="hl">former</span> à Hammamet.</h1>
<p class="lede rise d2">Elite Academy est un centre de formation installé à Hammamet. Programmes, niveaux et calendrier sont communiqués par le centre sur simple demande.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Demander le programme {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div></div>
<figure class="pol rise d2">{M.img('hero', 'Salle de lecture d’une bibliothèque (photo d’illustration)', sizes='(max-width: 960px) 88vw, 520px', lazy=False)}<figcaption>Photo d'illustration · ne montre pas le centre</figcaption>
<div class="note2">Jeudi : ouverture à 08h00<small>relevé Google · autres horaires à confirmer</small></div></figure></section>
<div class="mq" aria-hidden="true"><div>{mq}{mq}</div></div>
<section class="sec" id="centre"><div class="w"><p class="kick" data-rv>Le centre</p><h2 data-rv>Elite Academy,<br>en bref.</h2>
<div class="facts"><div data-rv><small>Type</small><p>Centre de formation</p></div><div data-rv style="--d:.1s"><small>Ville</small><p>Hammamet</p></div><div data-rv style="--d:.2s"><small>Téléphone</small><p><a href="{K.telhref(F['tel'])}">{F['tel']}</a></p></div>
<div data-rv><small>Formations</small><p>{ph()}</p></div><div data-rv style="--d:.1s"><small>Publics et niveaux</small><p>{ph()}</p></div><div data-rv style="--d:.2s"><small>Adresse exacte</small><p>{ph()}</p></div></div></div></section></div>
<section class="sec paper" id="formations"><div class="w"><p class="kick" data-rv>Formations</p><h2 data-rv>Le catalogue, page par page.</h2>
<p data-rv style="max-width:38rem;margin-top:1.2rem;opacity:.75">Aucune formation n'est inventée ici : ces pages seront complétées avec les informations fournies par Elite Academy.</p>
<div class="pages">{pgh}</div><p data-rv style="margin-top:3rem"><a class="btn p" href="#rdv">Demander le programme {IC['arrow']}</a></p></div></section>
<section class="sec grid"><div class="w"><p class="kick" data-rv>S'informer</p><h2 data-rv>Trois étapes.</h2><ol class="steps" style="padding:0">
<li data-rv><h3>Prendre contact</h3><p>Par téléphone ou WhatsApp, en indiquant la formation qui vous intéresse.</p></li><li data-rv style="--d:.12s"><h3>Recevoir les informations</h3><p>Le centre vous communique le programme, le calendrier et les modalités.</p></li>
<li data-rv style="--d:.24s"><h3>S'inscrire</h3><p>L'inscription se finalise directement auprès du centre.</p></li></ol></div></section>
<section class="sec" style="padding-top:0"><div class="w gal"><figure data-rv>{M.img('bancs', 'Bancs et pupitres (photo d’illustration)', sizes='(max-width: 960px) 92vw, 700px')}<figcaption>Illustration</figcaption></figure>
<figure data-rv style="--d:.1s">{M.img('carnet', 'Carnet et stylo (photo d’illustration)', sizes='(max-width: 960px) 46vw, 480px')}<figcaption>Illustration</figcaption></figure>
<figure data-rv style="--d:.2s">{M.img('medina', 'Remparts de la médina de Hammamet (photo d’illustration)', sizes='(max-width: 960px) 46vw, 480px')}<figcaption>Hammamet · illustration</figcaption></figure></div></section>
<section class="sec grid" id="horaires" style="padding-top:0"><div class="w info"><div class="box" data-rv><h3>Horaires</h3>{lux.hours(F)}</div>
<div class="box" data-rv style="--d:.1s"><h3>Contact</h3>{lux.contacts(F, 'WhatsApp · demande d’informations', msg, [('Facebook', f'<a href="{F["fb"]}" target="_blank" rel="noopener">facebook.com/EliteAcademy.Hammamet</a>')])}</div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w rdv"><div data-rv><p class="kick">Contact</p><h2>Demander le programme.</h2><p style="margin-top:1.4rem;opacity:.8">Votre demande s'ouvre dans WhatsApp, prête à être envoyée au centre.</p>
<figure style="margin:2rem 0 0;max-width:340px;border-radius:14px;overflow:hidden" data-rv>{M.img('stylo', 'Stylo (photo d’illustration)', sizes='340px')}</figure></div>
<div class="box" data-rv style="--d:.1s">{lux.form(F, 'Bonjour, je souhaite des informations sur vos formations.', spec, 'Envoyer la demande', NOTE)}</div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Hammamet.</h2><p data-rv>Adresse exacte {ph()} · <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Voir la fiche Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F, 'S’informer', '#rdv', 'wa')}'''
    return lux.page(F, 'Elite Academy · Centre de formation à Hammamet (démo)', 'Elite Academy, centre de formation à Hammamet : contact, horaires et demande de programme.', FONTS, CSS, body, '#0B1B3F', lux.fav('#FFE14D', '#0B1B3F', 'EA', 'Arial', 'rect'))
