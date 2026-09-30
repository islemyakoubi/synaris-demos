# Dr Emira Fenina Chtourou, gynécologue-obstétricienne (Hammamet) : « crépuscule, attente ». Mauve du soir, grès, ivoire. Hero scindé : titre Italiana
# aligné à gauche, grande arche cerclée d'or (silhouette de grossesse) à droite ; pieds de nouveau-né ; panorama de la Kasbah en défilement ; cartes ; nouveau-né au panier ; formulaire. Italiana + Josefin Sans.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Italiana&family=Josefin+Sans:wght@300;400;500;600;700'
CSS = '''
:root{--bg:#1E1826;--fg:#F3ECE3;--acc:#D9B98C;--onacc:#1E1826;--line:rgba(243,236,227,.14);--hbg:rgba(30,24,38,.86);--disp:Italiana,Georgia,serif;--sans:'Josefin Sans',system-ui,sans-serif;--r:0;--mapbg:#2A2234;--fbg:rgba(255,255,255,.04)}
body{font-weight:300}h1,h2,h3{letter-spacing:.02em}.brand .mono{width:44px;height:44px;border:1px solid var(--acc);transform:rotate(45deg);display:grid;place-items:center}.brand .mono i{transform:rotate(-45deg);font:400 1rem var(--disp);color:var(--acc);font-style:normal}
.hero{position:relative;min-height:100svh;display:flex;align-items:center;overflow:hidden;isolation:isolate;padding-bottom:4.5rem}
.dusk{position:absolute;inset:0;z-index:-1;background:radial-gradient(55% 70% at 75% 40%,rgba(91,74,107,.55),transparent 70%),radial-gradient(40% 50% at 20% 80%,rgba(217,185,140,.12),transparent 70%)}
.hin{padding:9rem 0 4rem;display:grid;grid-template-columns:1.15fr .85fr;gap:4rem;align-items:center}.hero .kick:after{content:'';width:34px;height:1px;background:currentColor}
.harch{position:relative;margin:0;justify-self:center;width:min(32vw,440px)}.harch .i{border-radius:999px 999px 0 0;overflow:hidden;aspect-ratio:3/4.2;box-shadow:0 40px 100px rgba(0,0,0,.5)}.harch img{width:100%;height:100%;object-fit:cover;object-position:50% 50%}
.harch:before{content:'';position:absolute;inset:-16px -16px 16px 16px;border:1px solid var(--acc);border-radius:999px 999px 0 0;z-index:-1}.harch figcaption{font-size:.7rem;letter-spacing:.1em;opacity:.6;margin-top:1.4rem;text-align:right}
.hero h1{font-size:clamp(2.8rem,5.6vw,6rem);line-height:1;letter-spacing:.05em;text-transform:uppercase}.hero h1 span{display:block}.hero h1 small{display:block;font:300 clamp(.9rem,1.6vw,1.2rem)/1.6 var(--sans);letter-spacing:.5em;margin-top:1.4rem;color:var(--acc)}
.lede{max-width:34rem;margin:2rem 0 2.4rem;font-size:1.08rem;opacity:.85}.acts{display:flex;gap:1rem;flex-wrap:wrap}
.hbar{position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:center;gap:3rem;padding:1.4rem;border-top:1px solid var(--line);font-size:.86rem;letter-spacing:.08em;flex-wrap:wrap}.hbar b{color:var(--acc);font-weight:600;margin-right:.5rem}
.sec{padding:8rem 0}.sec h2{font-size:clamp(2.4rem,5vw,4.8rem);line-height:1}
.ab{display:grid;grid-template-columns:1fr 1fr;gap:0;align-items:stretch;background:#000}.ab figure{margin:0;position:relative;min-height:620px;overflow:hidden}.ab img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ab .tx{padding:6rem clamp(1.5rem,5vw,5rem);display:flex;flex-direction:column;justify-content:center;background:var(--bg)}.ab h2{font-size:clamp(2.6rem,5vw,4.8rem);line-height:1}.ab p.big{font-size:1.2rem;line-height:1.75;margin-top:1.6rem;opacity:.88}
.cap{position:absolute;left:1rem;bottom:1rem;font-size:.7rem;letter-spacing:.1em;opacity:.7}
.pano{height:62vh;min-height:360px;position:relative;overflow:hidden}.pano img{height:100%;width:auto;max-width:none;animation:pan 60s linear infinite alternate}@keyframes pan{to{transform:translateX(calc(-100% + 100vw))}}
.pano:after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,var(--bg),transparent 15%,transparent 85%,var(--bg))}.pt{position:absolute;inset:0;z-index:2;display:grid;place-items:center}.pano h2{text-align:center;font-size:clamp(2.4rem,6vw,5.6rem);text-shadow:0 4px 30px rgba(0,0,0,.5);white-space:nowrap}
.sp{display:grid;grid-template-columns:repeat(3,1fr);border:1px solid var(--line);margin-top:4rem}.sp article{padding:3rem 2.4rem;text-align:center;transition:background .6s}.sp article+article{border-left:1px solid var(--line)}.sp article:hover{background:rgba(217,185,140,.06)}
.sp svg{width:64px;height:64px;color:var(--acc);margin:0 auto 1.8rem}.sp h3{font-size:2rem;margin-bottom:.8rem}.sp p{opacity:.75;margin:0}
.info{display:grid;grid-template-columns:1fr 1fr;gap:1.4rem}.card{border:1px solid var(--line);padding:2.6rem;background:rgba(255,255,255,.02)}.card h3{font-size:2rem;margin-bottom:1.2rem;color:var(--acc)}
.dl{margin:0}.dl div{display:grid;grid-template-columns:10rem 1fr;gap:1rem;padding:.9rem 0;border-bottom:1px solid var(--line)}.dl dt{font:600 .62rem/1.7 var(--sans);letter-spacing:.24em;text-transform:uppercase;opacity:.6}.dl dd{margin:0}
.rdv{display:grid;grid-template-columns:.9fr 1.1fr;gap:0;border:1px solid var(--line)}.rdv figure{margin:0;position:relative;min-height:520px;overflow:hidden}.rdv figure img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.rdv .f{padding:3.4rem}.rdv .f h2{margin-bottom:1.8rem}.form select option{color:#1E1826}
@media(max-width:960px){.hin{grid-template-columns:1fr;gap:3rem}.hero{flex-direction:column;align-items:stretch;padding-bottom:0}.hero>.w{width:100%}.harch{order:-1;width:min(72vw,300px)}.harch figcaption{text-align:center}.ab,.info,.rdv{grid-template-columns:1fr}.ab figure{min-height:420px}.sp{grid-template-columns:1fr}.sp article+article{border-left:0;border-top:1px solid var(--line)}.rdv figure{min-height:300px}}
@media(max-width:760px){.sec{padding:5.5rem 0}.hbar{position:relative;gap:.6rem;flex-direction:column;align-items:center}.hero{min-height:auto}.hin{padding-top:8.5rem}.hero h1{font-size:clamp(2.4rem,11vw,3.2rem)}.hero h1 small{letter-spacing:.3em}.card,.rdv .f{padding:1.6rem}.dl div{grid-template-columns:1fr;gap:.1rem}.pano h2{white-space:normal;}}
'''
def build(F, M):
    msg = 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet.'
    brand = '<span class="mono"><i>EF</i></span><span><b>Dr Emira Fenina Chtourou</b><small>Gynécologie-obstétrique</small></span>'
    links = [('Le cabinet', '#cabinet'), ('Spécialité', '#specialite'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    sp = [('flower', 'Gynécologie', 'La santé gynécologique de la femme, à chaque âge.'), ('baby', 'Obstétrique', 'Le suivi de la grossesse et de l’accouchement.'), ('echo', 'Échographie', 'L’imagerie utilisée en gynécologie et en obstétrique.')]
    sph = ''.join(f'<article data-rv style="--d:{i*.12:.2f}s">{IC[k]}<h3>{t}</h3><p>{p}</p></article>' for i, (k, t, p) in enumerate(sp))
    pw, phh = M.dims['panorama']
    body = f'''{lux.header(brand, links)}<main id="main">
<section class="hero" id="top"><div class="dusk"></div>
<div class="w hin"><div><p class="kick rise">Hammamet · Souk Lekhmis</p><h1 class="rise d1"><span>Dr Emira</span><span>Fenina</span><span>Chtourou</span><small>Gynécologie · Obstétrique</small></h1>
<p class="lede rise d2">Cabinet de gynécologie-obstétrique, immeuble Les Oliviers, 2e étage, bureau B1. Consultations sur rendez-vous.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Prendre rendez-vous {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div></div>
<figure class="harch rise d2"><div class="i">{M.img('hero', 'Silhouette d’une femme enceinte devant une fenêtre (photo d’illustration)', sizes='(max-width: 960px) 72vw, 440px', lazy=False)}</div><figcaption>Grossesse · photo d'illustration</figcaption></figure></div>
<div class="hbar rise d4"><span><b>Mercredi</b>{F['wed']}</span><span><b>Adresse</b>Immeuble Les Oliviers, bureau B1</span><span><b>E-mail</b>{F['email']}</span></div></section>
<section class="ab" id="cabinet"><figure data-rv="c">{M.img('bebe', 'Pieds d’un nouveau-né (photo d’illustration)', sizes='(max-width: 960px) 100vw, 50vw')}<figcaption class="cap">Illustration · ne montre pas le cabinet</figcaption></figure>
<div class="tx"><p class="kick" data-rv>Le cabinet</p><h2 data-rv>Immeuble<br>Les Oliviers.</h2><p class="big" data-rv>Le Dr Emira Fenina Chtourou, gynécologue-obstétricienne, reçoit à Souk Lekhmis, Hammamet, au 2e étage de l'immeuble Les Oliviers. Le cabinet est joignable par téléphone, par e-mail et via WhatsApp.</p>
<p class="note" data-rv>Parcours et qualifications {ph()}</p></div></section>
<section class="sec" id="specialite"><div class="w" style="text-align:center"><p class="kick" data-rv style="justify-content:center">La spécialité</p><h2 data-rv>Gynécologie et obstétrique</h2><div class="sp" style="text-align:center">{sph}</div>
<p class="note" data-rv style="margin-top:2rem">Présentation générale de la spécialité, à titre informatif. Les actes pratiqués au cabinet sont {ph()}</p></div></section>
<figure class="pano" style="margin:0" aria-label="Panorama de la Kasbah de Hammamet (photo d’illustration)"><img src="media/panorama.webp" width="{pw}" height="{phh}" alt="Panorama de la Kasbah de Hammamet (photo d’illustration)" loading="lazy" decoding="async"><div class="pt"><h2 data-rv>Hammamet</h2></div></figure>
<section class="sec" id="horaires"><div class="w info"><div class="card" data-rv><h3>Fiche du cabinet</h3><dl class="dl"><div><dt>Médecin</dt><dd>Dr Emira Fenina Chtourou</dd></div><div><dt>Spécialité</dt><dd>Gynécologie-obstétrique</dd></div><div><dt>Adresse</dt><dd>{F['addr']}</dd></div></dl>
<div style="margin-top:1rem">{lux.contacts(F, wa_msg=msg)}</div></div><div class="card" data-rv style="--d:.12s"><h3>Horaires</h3>{lux.hours(F)}</div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w"><div class="rdv" data-rv><figure>{M.img('panier', 'Nouveau-né endormi dans un panier (photo d’illustration)', sizes='(max-width: 960px) 100vw, 520px')}<figcaption class="cap">Illustration · ne montre pas le cabinet</figcaption></figure>
<div class="f"><p class="kick">Rendez-vous</p><h2>Demander un rendez-vous</h2>{lux.form(F, 'Bonjour Docteur, je souhaite un rendez-vous au cabinet.', lux.MED_FORM)}</div></div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Souk Lekhmis, Hammamet</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F)}'''
    return lux.page(F, 'Dr Emira Fenina Chtourou · Gynécologue à Hammamet (démo)', 'Cabinet de gynécologie-obstétrique du Dr Emira Fenina Chtourou, immeuble Les Oliviers, Hammamet : coordonnées, horaires et demande de rendez-vous.', FONTS, CSS, body, '#1E1826', lux.fav('#1E1826', '#D9B98C', 'EF'))
