# Dr Khalil Houissa, cardiologue (Nabeul) : « signal ». Blanc clinique, rouge signal, graphite. Typographie géante « Cardio » traversée par un tracé ECG animé,
# cœur anatomique en fusion multiply, grille technique, sections en cartes à coins nets, bandeau graphite, rendez-vous. Space Grotesk + IBM Plex Sans.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@300;400;500;600'
CSS = '''
:root{--bg:#FAFAF8;--fg:#17181B;--acc:#E0262F;--onacc:#fff;--line:rgba(23,24,27,.12);--hbg:rgba(250,250,248,.9);--disp:'Space Grotesk',system-ui,sans-serif;--sans:'IBM Plex Sans',system-ui,sans-serif;--r:2px;--mapbg:#EEEEEA;--rbg:#17181B}
h1,h2,h3{font-weight:500;letter-spacing:-.035em}.brand .mono{width:44px;height:44px;display:grid;place-items:center;background:var(--acc);color:#fff;font:700 .95rem var(--disp)}
.hero{position:relative;min-height:100svh;padding:8.5rem 0 3rem;overflow:hidden;background-image:linear-gradient(var(--line) 1px,transparent 1px),linear-gradient(90deg,var(--line) 1px,transparent 1px);background-size:64px 64px;background-position:-1px -1px}
.hero:after{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 70% 50%,transparent 20%,var(--bg) 75%);pointer-events:none}
.hero .w{position:relative;z-index:2}.giant{font:600 clamp(5rem,19vw,19rem)/.8 var(--disp);letter-spacing:-.06em;margin:0;color:var(--fg);position:relative;z-index:1}
.giant span{color:var(--acc)}.ecg{position:absolute;left:0;width:100%;top:clamp(9rem,17vw,16rem);height:clamp(120px,16vw,220px);z-index:3;pointer-events:none}
.ecg path{fill:none;stroke:var(--acc);stroke-width:3;stroke-linejoin:round;stroke-dasharray:2600;stroke-dashoffset:2600;animation:trace 4.5s cubic-bezier(.5,0,.3,1) .4s infinite}
@keyframes trace{0%{stroke-dashoffset:2600}55%{stroke-dashoffset:0}85%{stroke-dashoffset:0;opacity:1}100%{stroke-dashoffset:0;opacity:0}}
.hgrid{display:grid;grid-template-columns:1.1fr .9fr;gap:3rem;align-items:end;margin-top:1rem}
.hgrid h1{font-size:clamp(2.2rem,4vw,3.6rem);line-height:1}.lede{max-width:32rem;font-size:1.05rem;margin:1.2rem 0 2rem;opacity:.8}.acts{display:flex;gap:1rem;flex-wrap:wrap}
.heart{position:absolute;right:4%;top:6.5rem;width:min(34vw,470px);z-index:0;mix-blend-mode:multiply;opacity:.95}.heart img{width:100%;height:auto;-webkit-mask-image:radial-gradient(closest-side,#000 62%,transparent 100%);mask-image:radial-gradient(closest-side,#000 62%,transparent 100%)}
.live{display:inline-flex;align-items:center;gap:.6rem;font:500 .74rem/1 var(--disp);letter-spacing:.14em;text-transform:uppercase}.live i{width:9px;height:9px;border-radius:50%;background:var(--acc);animation:beat 1.1s infinite}
@keyframes beat{0%,100%{transform:scale(1)}15%{transform:scale(1.6)}30%{transform:scale(1)}45%{transform:scale(1.35)}}
.kpis{display:grid;grid-template-columns:repeat(3,1fr);border:1px solid var(--fg);background:var(--bg)}.kpis div{padding:1.3rem 1.4rem}.kpis div+div{border-left:1px solid var(--fg)}
.kpis small{display:block;font:500 .64rem/1 var(--disp);letter-spacing:.2em;text-transform:uppercase;opacity:.6;margin-bottom:.5rem}.kpis p{margin:0;font:500 1.1rem/1.25 var(--disp)}
.sec{padding:8rem 0}.sec h2{font-size:clamp(2.4rem,5vw,4.8rem);line-height:.98}
.dark{background:var(--fg);color:#F4F4F1;--line:rgba(244,244,241,.14)}
.ex{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin-top:4rem;border-top:1px solid var(--line)}.ex article{padding:2.2rem 1.6rem 2rem 0;border-right:1px solid var(--line);margin-right:1.6rem}.ex article:last-child{border:0;margin:0}
.ex svg{width:60px;height:60px;color:var(--acc);margin-bottom:3rem}.ex h3{font-size:1.45rem;margin-bottom:.6rem}.ex p{opacity:.7;font-size:.92rem;margin:0 0 1rem}
.duo{display:grid;grid-template-columns:1.3fr 1fr;gap:1.4rem}.duo figure{margin:0;position:relative;overflow:hidden;min-height:440px;background:#eee}.duo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.4s var(--ease)}.duo figure:hover img{transform:scale(1.04)}
.duo figcaption{position:absolute;left:0;bottom:0;background:var(--bg);padding:.5rem .9rem;font:500 .7rem var(--disp);letter-spacing:.08em}
.info{display:grid;grid-template-columns:1fr 1fr 1fr;border:1px solid var(--fg)}.info>div{padding:2.4rem}.info>div+div{border-left:1px solid var(--fg)}.info h3{font-size:1.6rem;margin-bottom:1.2rem}
.dl{margin:0}.dl div{padding:.85rem 0;border-bottom:1px solid var(--line)}.dl dt{font:500 .62rem/1.6 var(--disp);letter-spacing:.2em;text-transform:uppercase;opacity:.6}.dl dd{margin:0}
.rdv{display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem}.rdv .f{border:1px solid var(--fg);padding:2.4rem;background:#fff}
@media(max-width:960px){.heart{position:relative;right:auto;top:auto;width:62%;margin:-2rem 0 0 auto}.hgrid,.duo,.rdv{grid-template-columns:1fr}.ex{grid-template-columns:1fr 1fr}.ex article{margin:0;padding:2rem 1.2rem;border-bottom:1px solid var(--line)}
.info{grid-template-columns:1fr}.info>div+div{border-left:0;border-top:1px solid var(--fg)}}
@media(max-width:760px){.kpis{grid-template-columns:1fr}.kpis div+div{border-left:0;border-top:1px solid var(--fg)}.sec{padding:5.5rem 0}.ex{grid-template-columns:1fr}.info>div,.rdv .f{padding:1.6rem}.duo figure{min-height:320px}.ecg{top:8.6rem}}
'''
ECG = '<svg class="ecg" viewBox="0 0 1440 200" preserveAspectRatio="none" aria-hidden="true"><path d="M0 120 H250 l18 -14 16 14 H340 l12 18 22 -128 22 150 16 -40 H520 l30 -22 30 22 H760 l18 -14 16 14 H850 l12 18 22 -128 22 150 16 -40 H1030 l30 -22 30 22 H1440"/></svg>'
def build(F, M):
    msg = 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet de cardiologie.'
    brand = '<span class="mono">KH</span><span><b>Dr Khalil Houissa</b><small>Cardiologie · Nabeul</small></span>'
    links = [('Spécialité', '#specialite'), ('Le cabinet', '#cabinet'), ('Infos', '#infos'), ('Accès', '#acces')]
    ex = [('heart', 'Le cœur', 'Le muscle cardiaque, ses valves et son rythme.'), ('pulse', 'Le rythme', 'L’activité électrique du cœur.'), ('drop', 'Les vaisseaux', 'Artères, veines et tension artérielle.'), ('steth', 'La consultation', 'Examen clinique au cabinet, sur rendez-vous.')]
    exh = ''.join(f'<article data-rv style="--d:{i*.1:.1f}s">{IC[k]}<h3>{t}</h3><p>{p}</p></article>' for i, (k, t, p) in enumerate(ex))
    body = f'''{lux.header(brand, links)}<main id="main">
<section class="hero" id="top"><div class="heart rise d2">{M.img('hero', 'Illustration anatomique du cœur (image d’illustration)', sizes='(max-width: 960px) 60vw, 470px', lazy=False)}</div>{ECG}
<div class="w"><p class="live rise"><i></i>Cabinet de cardiologie · Nabeul</p><p class="giant rise d1" aria-hidden="true">Cardio<span>.</span></p>
<div class="hgrid"><div><h1 class="rise d2">Dr Khalil Houissa, cardiologue</h1><p class="lede rise d3">Cabinet 402 du centre Le Jasmin Médical, avenue Hédi Nouira à Nabeul. Consultations sur rendez-vous.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Prendre rendez-vous {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div></div>
<div class="kpis rise d4"><div><small>Cabinet</small><p>402</p></div><div><small>Centre</small><p>Le Jasmin Médical</p></div><div><small>Horaires</small><p>à confirmer</p></div></div></div></div></section>
<section class="sec dark" id="specialite"><div class="w"><p class="kick" data-rv>La spécialité</p><h2 data-rv>La cardiologie,<br>en quelques mots.</h2><div class="ex">{exh}</div>
<p class="note" data-rv style="margin-top:2rem">Présentation générale de la spécialité, à titre informatif. Les examens réalisés au cabinet sont {ph()}</p></div></section>
<section class="sec" id="cabinet"><div class="w duo"><figure data-rv>{M.img('echo', 'Appareil d’échocardiographie (photo d’illustration)', sizes='(max-width: 960px) 92vw, 700px')}<figcaption>Illustration · ne montre pas le cabinet</figcaption></figure>
<figure data-rv style="--d:.12s">{M.img('ecg', 'Tracé d’électrocardiogramme (image d’illustration)', sizes='(max-width: 960px) 92vw, 520px')}<figcaption>Illustration · électrocardiogramme</figcaption></figure></div></section>
<section class="sec" id="infos" style="padding-top:0"><div class="w"><div class="info" data-rv><div><h3>Fiche</h3><dl class="dl"><div><dt>Médecin</dt><dd>Dr Khalil Houissa</dd></div><div><dt>Spécialité</dt><dd>Cardiologie</dd></div><div><dt>Qualification</dt><dd>{ph()}</dd></div><div><dt>Adresse</dt><dd>{F['addr']}</dd></div></dl></div>
<div><h3>Horaires</h3>{lux.hours(F)}</div><div><h3>Contact</h3>{lux.contacts(F, wa_msg=msg)}</div></div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w rdv"><div data-rv><p class="kick">Rendez-vous</p><h2>Demander un rendez-vous.</h2><p style="margin-top:1.4rem;opacity:.8">Le formulaire prépare un message WhatsApp ; le cabinet confirme le créneau.</p>
<figure data-rv style="margin:2rem 0 0;max-width:360px">{M.img('stetho', 'Stéthoscope (photo d’illustration)', sizes='360px')}</figure></div>
<div class="f" data-rv style="--d:.1s">{lux.form(F, 'Bonjour Docteur, je souhaite un rendez-vous au cabinet de cardiologie.', lux.MED_FORM)}</div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Le Jasmin Médical.</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F)}'''
    return lux.page(F, 'Dr Khalil Houissa · Cardiologue à Nabeul (démo)', 'Cabinet de cardiologie du Dr Khalil Houissa, Le Jasmin Médical, Nabeul : coordonnées et demande de rendez-vous.', FONTS, CSS, body, '#FAFAF8', lux.fav('#E0262F', '#fff', 'KH', 'Arial', 'rect'))
