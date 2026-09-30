# Auto-école Abdel Kraim Hajri (Hammamet) : « piste ». Asphalte, orange sécurité. Hero plein cadre moto sur plateau, bandes de chantier obliques animées,
# catégories en plaques (à confirmer), marquages au sol géants, parcours en slalom de plots, formulaire « permis souhaité ». Oswald + Rubik.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Oswald:wght@400;500;600;700&family=Rubik:wght@300;400;500;600;700'
CSS = '''
:root{--bg:#1C1F23;--fg:#F4F2EE;--acc:#FF6B00;--onacc:#111;--line:rgba(244,242,238,.13);--hbg:rgba(28,31,35,.88);--disp:Oswald,Impact,sans-serif;--sans:Rubik,system-ui,sans-serif;--r:4px;--mapbg:#24282D;--fbg:rgba(255,255,255,.04)}
h1,h2,h3{text-transform:uppercase;font-weight:600;letter-spacing:.01em}.brand .mono{width:44px;height:44px;background:var(--acc);color:#111;display:grid;place-items:center;font:700 1.2rem var(--disp);border-radius:4px}
.haz{height:18px;background:repeating-linear-gradient(-45deg,var(--acc) 0 22px,#111 22px 44px);background-size:62px 62px;animation:hz 2s linear infinite}@keyframes hz{to{background-position:62px 0}}
.hero{position:relative;min-height:100svh;display:flex;align-items:flex-end;overflow:hidden;isolation:isolate}.hero:after{content:'';position:absolute;inset:0;z-index:-1;background:linear-gradient(0deg,#1C1F23 2%,rgba(28,31,35,.5) 45%,rgba(28,31,35,.35) 100%),linear-gradient(90deg,rgba(28,31,35,.85),transparent 60%)}
.hin{padding:10rem 0 3.4rem}.hero h1{font-size:clamp(3.6rem,10vw,10.4rem);line-height:.86}.hero h1 span{display:block;color:var(--acc)}
.lede{max-width:34rem;font-size:1.08rem;margin:1.6rem 0 2.2rem;opacity:.88}.acts{display:flex;gap:1rem;flex-wrap:wrap}
.plates{display:flex;gap:.8rem;margin-top:2.4rem;flex-wrap:wrap;align-items:center}.plate{background:#F4F2EE;color:#111;border:3px solid #111;outline:2px solid #F4F2EE;border-radius:6px;padding:.3rem .9rem;font:700 1.5rem/1 var(--disp)}.plates .ph{border-color:var(--acc)}
.sec{padding:8rem 0}.sec h2{font-size:clamp(3rem,6.6vw,6.2rem);line-height:.9}
.mk{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;align-items:stretch}.mk figure{margin:0;position:relative;overflow:hidden;min-height:540px}.mk img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.6s var(--ease)}.mk figure:hover img{transform:scale(1.05)}
.mk figcaption{position:absolute;left:0;bottom:0;background:var(--acc);color:#111;font:600 .72rem var(--sans);padding:.45rem .8rem;text-transform:uppercase;letter-spacing:.08em}
.cats{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem;margin-top:4rem}.cats article{background:#23272C;border-top:6px solid var(--acc);padding:2.4rem 2rem;position:relative;overflow:hidden}
.cats .big{font:700 6rem/.9 var(--disp);color:transparent;-webkit-text-stroke:1.5px var(--acc);display:block;margin-bottom:1.4rem}.cats h3{font-size:1.6rem;margin-bottom:.5rem}.cats p{opacity:.72;margin:0 0 1rem}.cats svg{position:absolute;right:1.4rem;top:1.6rem;width:64px;height:64px;color:rgba(255,107,0,.5)}
.slalom{position:relative;margin-top:4.5rem;display:grid;grid-template-columns:repeat(4,1fr);gap:1.6rem}.slalom li{list-style:none;padding:2rem 0 0;border-top:2px dashed rgba(244,242,238,.3);position:relative}
.slalom li:before{content:'';position:absolute;top:-22px;left:0;width:0;height:0;border-left:14px solid transparent;border-right:14px solid transparent;border-bottom:40px solid var(--acc)}.slalom b{font:700 1rem var(--disp);color:var(--acc);display:block;margin-bottom:.6rem;letter-spacing:.1em}
.slalom h3{font-size:1.6rem;margin-bottom:.4rem}.slalom p{opacity:.72;margin:0}
.info{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem}.card{background:#23272C;padding:2.6rem;border-left:6px solid var(--acc)}.card h3{font-size:1.9rem;margin-bottom:1rem}
.rdv{display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem}.rdv .f{background:var(--fg);color:#111;padding:2.6rem;--line:rgba(0,0,0,.14);--fln:rgba(0,0,0,.25);--acc:#FF6B00}.form select option{color:#111}
@media(max-width:960px){.mk,.info,.rdv{grid-template-columns:1fr}.mk figure{min-height:360px}.cats{grid-template-columns:1fr}.slalom{grid-template-columns:1fr 1fr;row-gap:3.4rem}}
@media(max-width:760px){.sec{padding:5.5rem 0}.slalom{grid-template-columns:1fr}.card,.rdv .f{padding:1.6rem}}
'''
NOTE = "Démo : aucune donnée n'est enregistrée. Le bouton ouvre WhatsApp avec votre message ; l'auto-école vous répond directement."
def build(F, M):
    msg = 'Bonjour, je souhaite des informations pour passer le permis.'
    brand = '<span class="mono">H</span><span><b>Auto-école Hajri</b><small>Abdel Kraim Hajri · Hammamet</small></span>'
    links = [('Permis', '#permis'), ('Parcours', '#parcours'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    cats = [('AA', 'moto', 'Permis AA', 'Catégorie moto mentionnée sur un annuaire en ligne.'), ('B', 'car', 'Permis B', 'Voiture, catégorie mentionnée sur un annuaire en ligne.'), ('H', 'sign', 'Permis H', 'Catégorie mentionnée sur un annuaire en ligne.')]
    ch = ''.join(f'<article data-rv style="--d:{i*.12:.2f}s">{IC[ic]}<span class="big">{b}</span><h3>{t}</h3><p>{p}</p>{ph()}</article>' for i, (b, ic, t, p) in enumerate(cats))
    steps = [('Inscription', 'Au bureau, rue du 20 Mars 1956.'), ('Code', 'Les règles et la signalisation.'), ('Plateau et circulation', 'Leçons pratiques avec un moniteur.'), ('Examen', 'Passage des épreuves du permis.')]
    sh = ''.join(f'<li data-rv style="--d:{i*.12:.2f}s"><b>Étape 0{i+1}</b><h3>{t}</h3><p>{p}</p></li>' for i, (t, p) in enumerate(steps))
    spec = [('text', 'Nom et prénom'), ('tel', 'Téléphone'), ('full', 'Permis souhaité'), ('textarea', 'Message (facultatif)')]
    body = f'''{lux.header(brand, links, ('S’inscrire', '#rdv'))}<main id="main">
<section class="hero" id="top"><div class="pxw">{M.img('hero', 'Moto sur un plateau d’apprentissage entre des plots (photo d’illustration)', cls='px', sizes='100vw', lazy=False, extra=' data-px=".16"')}</div>
<div class="w hin"><p class="kick rise">Auto-école · Hammamet</p><h1 class="rise d1">Auto-école<span>Hajri</span></h1>
<p class="lede rise d2">L'auto-école d'Abdel Kraim Hajri se trouve rue du 20 Mars 1956, à Hammamet. Renseignements et inscriptions directement auprès de l'école.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Se renseigner {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div>
<div class="plates rise d4"><span class="plate">AA</span><span class="plate">B</span><span class="plate">H</span>{ph('catégories à confirmer')}</div></div></section>
<div class="haz" aria-hidden="true"></div>
<section class="sec" id="permis"><div class="w"><p class="kick" data-rv>Permis</p><h2 data-rv>Deux roues,<br>quatre roues.</h2><div class="cats">{ch}</div>
<p class="note" data-rv style="margin-top:2rem">Catégories relevées sur un annuaire en ligne : liste, tarifs et calendrier à confirmer par l'auto-école.</p></div></section>
<section class="sec" style="padding-top:0"><div class="w mk"><figure data-rv>{M.img('plateau', 'Exercice de maniabilité à moto entre des plots (photo d’illustration)', sizes='(max-width: 960px) 92vw, 600px')}<figcaption>Illustration · ne montre pas l'école</figcaption></figure>
<figure data-rv style="--d:.12s">{M.img('marquage', 'Marquage au sol « 20 » (photo d’illustration)', sizes='(max-width: 960px) 92vw, 600px')}<figcaption>Illustration · marquage au sol</figcaption></figure></div></section>
<section class="sec" id="parcours" style="padding-top:2rem"><div class="w"><p class="kick" data-rv>Le parcours</p><h2 data-rv>Plot après plot.</h2><ol class="slalom" style="padding:0">{sh}</ol></div></section>
<section class="sec" id="horaires" style="padding-top:0"><div class="w info"><div class="card" data-rv><h3>Horaires</h3>{lux.hours(F)}</div><div class="card" data-rv style="--d:.1s"><h3>Contact</h3>{lux.contacts(F, 'WhatsApp · renseignements', msg)}</div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w rdv"><div data-rv><p class="kick">Inscription</p><h2>Se<br>renseigner.</h2><p style="margin-top:1.4rem;opacity:.8">Indiquez le permis qui vous intéresse : le message s'ouvre dans WhatsApp.</p>
<figure style="margin:2rem 0 0;max-width:380px;overflow:hidden" data-rv>{M.img('fleche', 'Flèche peinte au sol (photo d’illustration)', sizes='380px')}</figure></div>
<div class="f" data-rv style="--d:.1s">{lux.form(F, 'Bonjour, je souhaite des informations pour le permis.', spec, 'Envoyer la demande', NOTE)}</div></div></section>
<div class="haz" aria-hidden="true"></div>
<section class="sec" id="acces" style="padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Rue du 20 Mars 1956.</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F, 'Écrire', '#rdv', 'wa')}'''
    return lux.page(F, 'Auto-école Abdel Kraim Hajri · Hammamet (démo)', 'Auto-école Abdel Kraim Hajri, rue du 20 Mars 1956, Hammamet : contact, horaires et demande d’inscription.', FONTS, CSS, body, '#1C1F23', lux.fav('#FF6B00', '#111', 'H', 'Impact', 'rect'))
