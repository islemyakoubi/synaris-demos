# Villa Verde (Bir Bou Rekba, Hammamet Nord) : « chaux et oliviers ». Vert profond, blanc de chaux, terre cuite. Hero plein écran (olivier, zoom lent Ken Burns),
# titre Marcellus très espacé, arches, équipements en liste éditoriale, distances en grands chiffres, feu de camp, réservation WhatsApp (arrivée/départ). Marcellus + Jost.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Marcellus&family=Jost:wght@300;400;500;600'
CSS = '''
:root{--bg:#F5F1E8;--fg:#1F3A2B;--acc:#B5553C;--onacc:#fff;--line:rgba(31,58,43,.14);--hbg:rgba(245,241,232,.9);--disp:Marcellus,Georgia,serif;--sans:Jost,system-ui,sans-serif;--r:0;--mapbg:#E8E1D1;--rbg:#1F3A2B}
body{font-weight:300}h1,h2,h3{letter-spacing:.02em}.brand .mono{width:44px;height:44px;border-radius:50% 50% 0 0;background:var(--fg);display:grid;place-items:center;color:#F5F1E8;font:400 1.1rem var(--disp)}
.hdr{color:#fff}.hdr.scrolled{color:var(--fg)}
.hero{position:relative;min-height:100svh;display:flex;align-items:flex-end;overflow:hidden;isolation:isolate;color:#fff}.kb{position:absolute;inset:0;z-index:-2;overflow:hidden}.kb img{width:100%;height:100%;object-fit:cover;animation:kb 26s ease-in-out infinite alternate}
@keyframes kb{from{transform:scale(1)}to{transform:scale(1.14) translate(-2%,-2%)}}.hero:after{content:'';position:absolute;inset:0;z-index:-1;background:linear-gradient(0deg,rgba(20,38,28,.85),rgba(20,38,28,.1) 55%,rgba(20,38,28,.45))}
.hin{padding:10rem 0 4rem;text-align:center}.hero .kick{justify-content:center;color:#F1C9A5}.hero .kick:after{content:'';width:34px;height:1px;background:currentColor}
.hero h1{font-size:clamp(3.8rem,11vw,11rem);line-height:.9;letter-spacing:.12em;text-transform:uppercase;margin-right:-.12em}.lede{max-width:36rem;margin:1.6rem auto 2.2rem;font-size:1.1rem;opacity:.9}.acts{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}.hero .btn.o{color:#fff}
.sec{padding:8rem 0}.sec h2{font-size:clamp(2.4rem,5vw,4.8rem);line-height:1.02}
.intro{display:grid;grid-template-columns:1fr 1fr;gap:6rem;align-items:center}.arch{margin:0;border-radius:999px 999px 0 0;overflow:hidden;aspect-ratio:3/4;position:relative}.arch img{width:100%;height:100%;object-fit:cover}
.arch figcaption{position:absolute;left:0;right:0;bottom:1rem;text-align:center;color:#fff;font-size:.72rem;text-shadow:0 1px 6px rgba(0,0,0,.5)}
.intro p.big{font-size:1.22rem;line-height:1.8;margin-top:1.6rem}
.dist{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--line);margin-top:3rem}.dist div{padding:1.6rem 0}.dist div+div{border-left:1px solid var(--line);padding-left:2rem}.dist b{display:block;font:400 4rem/1 var(--disp);color:var(--acc)}.dist span{font-size:.9rem;opacity:.8}
.green{background:var(--fg);color:#F5F1E8;--line:rgba(245,241,232,.16)}.green .kick{color:#F1C9A5}
.eq{display:grid;grid-template-columns:repeat(3,1fr);gap:0;margin-top:4rem;border-top:1px solid var(--line)}.eq article{padding:2.6rem 2.2rem 2.4rem 0;border-right:1px solid var(--line);margin-right:2.2rem}.eq article:last-child{border:0;margin:0}
.eq svg{width:60px;height:60px;color:#F1C9A5;margin-bottom:1.8rem}.eq h3{font-size:1.8rem;margin-bottom:1rem}.eq ul{list-style:none;margin:0;padding:0}.eq li{padding:.55rem 0;border-bottom:1px solid var(--line);font-size:.98rem}
.fire{display:grid;grid-template-columns:1.2fr .8fr;min-height:560px}.fire figure{margin:0;position:relative;overflow:hidden}.fire img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.fire .tx{background:var(--acc);color:#fff;padding:5rem clamp(1.5rem,4vw,4rem);display:flex;flex-direction:column;justify-content:center}
.fire .tx h2{font-size:clamp(2.2rem,4vw,3.8rem)}.fire .tx .kick{color:#FFE3D2}
.two{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem}.card{background:#fff;padding:2.6rem;border:1px solid var(--line)}.card h3{font-size:1.9rem;margin-bottom:1rem}
.rdv{display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem}.rdv .card{background:#FBF8F2}
@media(max-width:960px){.intro,.two,.rdv,.fire{grid-template-columns:1fr;gap:3rem}.eq{grid-template-columns:1fr}.eq article{margin:0;border-right:0;border-bottom:1px solid var(--line);padding:2rem 0}.fire{gap:0}.fire figure{min-height:340px}.arch{max-width:460px}}
@media(max-width:760px){.sec{padding:5.5rem 0}.hero h1{letter-spacing:.06em}.card{padding:1.6rem}.dist b{font-size:3rem}}
'''
NOTE = "Démo : aucune donnée n'est enregistrée. Le bouton ouvre WhatsApp avec votre demande ; la maison d'hôtes confirme disponibilités et conditions."
def build(F, M):
    msg = 'Bonjour, je souhaite une information sur un séjour à Villa Verde.'
    brand = '<span class="mono">V</span><span><b>Villa Verde</b><small>Maison d’hôtes · Bir Bou Rekba</small></span>'
    links = [('La maison', '#maison'), ('Chambres', '#chambres'), ('Infos', '#infos'), ('Réserver', '#rdv')]
    eq = [('bed', 'Chambres', ['Wi-Fi et télévision', 'Balcon', 'Nécessaire à thé et café', 'Salle de bain privative', 'Certaines chambres dans un bâtiment en bois']),
          ('house', 'Suites et villa', ['Suites avec salon', 'Une villa également proposée', 'Configuration et capacité à confirmer']),
          ('pool', 'Extérieurs', ['Piscine extérieure', 'Coin feu de camp', 'Parking', 'Petit-déjeuner offert, autres repas sur demande'])]
    eqh = ''.join(f'<article data-rv style="--d:{i*.12:.2f}s">{IC[k]}<h3>{t}</h3><ul>{"".join(f"<li>{x}</li>" for x in L)}</ul></article>' for i, (k, t, L) in enumerate(eq))
    spec = [('text', 'Nom et prénom'), ('tel', 'Téléphone'), ('date', 'Arrivée'), ('date', 'Départ'), ('select', 'Personnes', ['1', '2', '3', '4', '5', '6', 'Plus de 6']), ('textarea', 'Message (facultatif)')]
    w, h = M.dims['hero']
    body = f'''{lux.header(brand, links, ('Réserver', '#rdv'))}<main id="main">
<section class="hero" id="top"><div class="kb">{M.img('hero', 'Olivier dans la campagne tunisienne (photo d’illustration)', sizes='100vw', lazy=False)}</div>
<div class="w hin"><p class="kick rise">Maison d'hôtes · Bir Bou Rekba · Hammamet Nord</p><h1 class="rise d1">Villa Verde</h1>
<p class="lede rise d2">Une villa blanchie à la chaux dans les collines au nord de Hammamet, avec piscine extérieure et petit-déjeuner offert.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Demander une disponibilité {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div></div></section>
<section class="sec" id="maison"><div class="w intro"><figure class="arch" data-rv>{M.img('piscine', 'Piscine sous les palmiers à Yasmine Hammamet (photo d’illustration)', sizes='(max-width: 960px) 90vw, 520px')}<figcaption>Illustration · ne montre pas Villa Verde</figcaption></figure>
<div><p class="kick" data-rv>La maison</p><h2 data-rv>Chaux blanche,<br>collines et oliviers.</h2><p class="big" data-rv>Villa Verde est une maison d'hôtes de Bir Bou Rekba, sur les hauteurs au nord de Hammamet. Chambres, suites et une villa entourent une piscine extérieure.</p>
<div class="dist" data-rv><div><b>6 km</b><span>du golf Yasmine</span></div><div><b>12 km</b><span>de la plage de Lambouka</span></div></div>
<p class="note" data-rv>Description et distances reprises de la fiche publiée sur kharjet.tn, à confirmer par l'établissement.</p></div></div></section>
<section class="sec green" id="chambres"><div class="w"><p class="kick" data-rv>Chambres et équipements</p><h2 data-rv>Tout ce que mentionne la fiche.</h2><div class="eq">{eqh}</div>
<p class="note" data-rv style="margin-top:2rem">Équipements repris de la fiche kharjet.tn. Tarifs, capacités et conditions : {ph()}</p></div></section>
<section class="fire"><figure data-rv="c">{M.img('feu', 'Feu de camp la nuit (photo d’illustration)', sizes='(max-width: 960px) 100vw, 60vw')}</figure><div class="tx" data-rv><p class="kick">Le soir</p><h2>Un coin feu de camp, sous les étoiles.</h2><p style="margin-top:1.2rem;opacity:.9">La maison dispose d'un espace feu de camp à l'extérieur, d'après sa fiche publique.</p></div></section>
<section class="sec" id="infos"><div class="w two"><div class="card" data-rv><h3>Contact</h3>{lux.contacts(F, 'WhatsApp · demande de séjour', msg)}</div><div class="card" data-rv style="--d:.1s"><h3>Accueil</h3>{lux.hours(F)}
<figure style="margin:1.6rem 0 0;max-width:280px;overflow:hidden">{M.img('olives', 'Rameau d’olivier (photo d’illustration)', sizes='280px')}</figure></div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w rdv"><div data-rv><p class="kick">Réserver</p><h2>Demander une disponibilité.</h2><p style="margin-top:1.4rem;opacity:.8">Indiquez vos dates et le nombre de personnes : la demande s'ouvre dans WhatsApp.</p></div>
<div class="card" data-rv style="--d:.1s">{lux.form(F, 'Bonjour, je souhaite une disponibilité à Villa Verde.', spec, 'Envoyer la demande', NOTE)}</div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Bir Bou Rekba.</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Rechercher sur Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F, 'Réserver', '#rdv', 'wa')}'''
    return lux.page(F, 'Villa Verde · Maison d’hôtes à Bir Bou Rekba (démo)', 'Villa Verde, maison d’hôtes à Bir Bou Rekba, au nord de Hammamet : chambres, piscine, contact et demande de disponibilité.', FONTS, CSS, body, '#1F3A2B', lux.fav('#1F3A2B', '#F5F1E8', 'V'))
