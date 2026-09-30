# Auto École Moderne (Grombalia) : « signalisation ». Blanc, bleu signal, rouge panneau. Hero route plein cadre, lignes de marquage animées au sol,
# titres Barlow Condensed en panneaux, parcours en 4 étapes sur tracé routier, bloc tableau de bord, formulaire « permis souhaité ». Barlow Condensed + Barlow.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Barlow+Condensed:wght@500;600;700;800&family=Barlow:wght@400;500;600;700'
CSS = '''
:root{--bg:#FFFFFF;--fg:#0E1B2C;--acc:#0047BB;--onacc:#fff;--line:rgba(14,27,44,.12);--hbg:rgba(255,255,255,.92);--disp:'Barlow Condensed',system-ui,sans-serif;--sans:Barlow,system-ui,sans-serif;--r:6px;--red:#D7263D;--mapbg:#EEF1F5;--rbg:#0E1B2C}
h1,h2,h3{font-weight:800;text-transform:uppercase;letter-spacing:-.005em}.brand .mono{width:44px;height:44px;border-radius:8px;display:grid;place-items:center;background:var(--acc);color:#fff;font:800 1.3rem var(--disp);border:3px solid #fff;box-shadow:0 0 0 2px var(--acc)}
.hdr{color:#fff}.hdr.scrolled{color:var(--fg)}
.hero{position:relative;min-height:100svh;display:flex;align-items:flex-end;overflow:hidden;isolation:isolate;color:#fff}.hero .px{object-position:50% 70%}
.hero:before{content:'';position:absolute;inset:0;z-index:-1;background:linear-gradient(0deg,rgba(14,27,44,.95) 0%,rgba(0,40,110,.45) 55%,rgba(14,27,44,.6) 100%)}
.lanes{position:absolute;left:50%;bottom:0;width:18px;height:52%;transform:translateX(-50%) perspective(300px) rotateX(58deg);transform-origin:bottom;z-index:-1;background:repeating-linear-gradient(0deg,#fff 0 40px,transparent 40px 80px);animation:lane 1.1s linear infinite;opacity:.9}
@keyframes lane{to{background-position:0 80px}}
.hin{padding:10rem 0 4rem}.signs{display:flex;gap:.7rem;margin-bottom:1.6rem}.signs span{display:grid;place-items:center;width:46px;height:46px;font:800 1.2rem var(--disp)}
.signs .b{background:var(--acc);border-radius:6px;border:3px solid #fff}.signs .r{border-radius:50%;background:#fff;border:6px solid var(--red);color:var(--fg);font-size:1rem}.signs .t{width:0;height:0;border-left:26px solid transparent;border-right:26px solid transparent;border-bottom:46px solid var(--red);position:relative}
.signs .t:after{content:'!';position:absolute;left:-4px;top:14px;color:#fff;font:800 1.1rem var(--disp)}
.hero h1{font-size:clamp(4rem,11vw,11.5rem);line-height:.84}.hero h1 span{display:block;color:#7FB0FF}
.hrow{display:grid;grid-template-columns:1.1fr .9fr;gap:3rem;align-items:end;margin-top:2rem}.lede{font-size:1.12rem;max-width:34rem;margin:0;opacity:.9}.acts{display:flex;gap:1rem;flex-wrap:wrap;justify-content:flex-end}.hero .btn.o{color:#fff}
.sec{padding:8rem 0}.sec h2{font-size:clamp(3rem,6.4vw,6rem);line-height:.9}
.road{position:relative;margin-top:5rem;display:grid;grid-template-columns:repeat(4,1fr);gap:1.4rem}.road:before{content:'';position:absolute;left:0;right:0;top:34px;height:12px;background:#2B3542;border-radius:6px}
.road:after{content:'';position:absolute;left:0;right:0;top:39px;height:2px;background:repeating-linear-gradient(90deg,#fff 0 24px,transparent 24px 44px);animation:rl 1.6s linear infinite}@keyframes rl{to{background-position:44px 0}}
.road li{list-style:none;position:relative;z-index:1}.road .dot{width:80px;height:80px;border-radius:50%;background:#fff;border:6px solid var(--acc);display:grid;place-items:center;font:800 1.8rem var(--disp);color:var(--acc);margin-bottom:1.6rem;box-shadow:0 10px 30px rgba(0,71,187,.2)}
.road li:nth-child(4) .dot{border-color:var(--red);color:var(--red)}.road h3{font-size:1.7rem;margin-bottom:.4rem}.road p{opacity:.72;margin:0}
.blue{background:var(--acc);color:#fff;--line:rgba(255,255,255,.25)}.blue .kick{color:#fff}
.dash{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center}.dash figure{margin:0;border-radius:18px;overflow:hidden;position:relative;aspect-ratio:4/3}.dash img{width:100%;height:100%;object-fit:cover}
.dash figcaption{position:absolute;left:1rem;bottom:1rem;background:#fff;color:var(--fg);font:600 .72rem var(--sans);padding:.35rem .7rem;border-radius:4px}
.pl{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:2.4rem}.pl div{border:2px solid rgba(255,255,255,.5);border-radius:10px;padding:1.2rem 1.4rem}.pl small{display:block;font:700 .64rem/1 var(--sans);letter-spacing:.18em;text-transform:uppercase;opacity:.75;margin-bottom:.5rem}.pl p{margin:0;font:700 1.4rem/1.2 var(--disp);text-transform:uppercase}
.pl .ph{color:#fff}
.info{display:grid;grid-template-columns:1fr 1fr;gap:1.4rem}.card{border:2px solid var(--fg);border-radius:14px;padding:2.4rem;position:relative}.card h3{font-size:2rem;margin-bottom:1rem}.card:before{content:'';position:absolute;right:1.4rem;top:1.4rem;width:26px;height:26px;background:var(--red);border-radius:50%;box-shadow:-34px 0 0 #F5B700,-68px 0 0 #2BA84A}
.rdv{display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem}.rdv .card:before{display:none}
.mapw{border-radius:14px;border:2px solid var(--fg)}
@media(max-width:960px){.hrow,.dash,.info,.rdv{grid-template-columns:1fr}.acts{justify-content:flex-start}.road{grid-template-columns:1fr 1fr;gap:2.4rem 1.4rem}.road:before,.road:after{display:none}}
@media(max-width:760px){.sec{padding:5.5rem 0}.road{grid-template-columns:1fr}.pl{grid-template-columns:1fr}.card{padding:1.6rem}.card:before{transform:scale(.7);transform-origin:right top}}
'''
NOTE = "Démo : aucune donnée n'est enregistrée. Le bouton ouvre WhatsApp avec votre message ; l'auto-école vous répond directement."
def build(F, M):
    msg = 'Bonjour, je souhaite des informations pour passer le permis avec Auto École Moderne.'
    brand = '<span class="mono">M</span><span><b>Auto École Moderne</b><small>Grombalia</small></span>'
    links = [('Parcours', '#parcours'), ('L’école', '#ecole'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    steps = [('Inscription', 'Au bureau, rue Mohamed V : pièces et modalités communiquées par l’école.'), ('Code de la route', 'Apprentissage des règles et de la signalisation.'), ('Conduite', 'Leçons de conduite avec un moniteur.'), ('Examen', 'Passage des épreuves du permis.')]
    st = ''.join(f'<li data-rv style="--d:{i*.12:.2f}s"><div class="dot">{i+1}</div><h3>{t}</h3><p>{p}</p></li>' for i, (t, p) in enumerate(steps))
    spec = [('text', 'Nom et prénom'), ('tel', 'Téléphone'), ('full', 'Permis souhaité'), ('textarea', 'Message (facultatif)')]
    body = f'''{lux.header(brand, links, ('S’inscrire', '#rdv'))}<main id="main">
<section class="hero" id="top"><div class="pxw">{M.img('hero', 'Route en Tunisie (photo d’illustration)', cls='px', sizes='100vw', lazy=False, extra=' data-px=".16"')}</div><div class="lanes" aria-hidden="true"></div>
<div class="w hin"><div class="signs rise" aria-hidden="true"><span class="b">P</span><span class="r">50</span><span class="t"></span></div><h1 class="rise d1">Auto École<span>Moderne</span></h1>
<div class="hrow"><p class="lede rise d2">Auto-école au 10 rue Mohamed V, à Grombalia. Inscriptions, code et conduite : renseignez-vous directement auprès de l'école.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Se renseigner {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div></div></div></section>
<section class="sec" id="parcours"><div class="w"><p class="kick" data-rv>Le parcours</p><h2 data-rv>Du code<br>au permis.</h2><ol class="road" style="padding:0">{st}</ol>
<p class="note" data-rv style="margin-top:3rem">Étapes générales du permis de conduire. Catégories enseignées, tarifs et calendrier : {ph()}</p></div></section>
<section class="sec blue" id="ecole"><div class="w dash"><figure data-rv>{M.img('volant', 'Tableau de bord et volant d’une voiture ancienne (photo d’illustration)', sizes='(max-width: 960px) 92vw, 600px')}<figcaption>Illustration · ne montre pas l'école</figcaption></figure>
<div><p class="kick" data-rv>L'école</p><h2 data-rv>Rue Mohamed V,<br>Grombalia.</h2><div class="pl" data-rv><div><small>Adresse</small><p>10 rue Mohamed V</p></div><div><small>Horaire relevé</small><p>Mer. {F['wed']}</p></div>
<div><small>Catégories de permis</small><p>{ph()}</p></div><div><small>Véhicules</small><p>{ph()}</p></div></div></div></div></section>
<section class="sec" id="horaires"><div class="w info"><div class="card" data-rv><h3>Horaires</h3>{lux.hours(F)}</div>
<div class="card" data-rv style="--d:.1s"><h3>Contact</h3>{lux.contacts(F, 'WhatsApp · renseignements', msg, [('Facebook', f'<a href="{F["fb"]}" target="_blank" rel="noopener">facebook.com/Auto.ecole.moderne</a>')])}</div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w rdv"><div data-rv><p class="kick">Inscription</p><h2>Se renseigner.</h2><p style="margin-top:1.4rem;opacity:.75">Indiquez le permis qui vous intéresse : le message s'ouvre dans WhatsApp, prêt à être envoyé.</p>
<figure style="margin:2rem 0 0;border-radius:14px;overflow:hidden;max-width:420px" data-rv>{M.img('route', 'Route de Matmata (photo d’illustration)', sizes='420px')}</figure></div>
<div class="card" data-rv style="--d:.1s">{lux.form(F, 'Bonjour, je souhaite des informations pour le permis.', spec, 'Envoyer la demande', NOTE)}</div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Grombalia.</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F, 'Écrire', '#rdv', 'wa')}'''
    return lux.page(F, 'Auto École Moderne · Grombalia (démo)', 'Auto École Moderne, 10 rue Mohamed V, Grombalia : contact, horaires et demande d’inscription.', FONTS, CSS, body, '#0E1B2C', lux.fav('#0047BB', '#fff', 'M', 'Arial', 'rect'))
