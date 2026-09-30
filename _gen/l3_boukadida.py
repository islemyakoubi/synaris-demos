# Cabinet Ahmed Boukadida, kinésithérapie et réadaptation fonctionnelle (Hammamet) : « performance ». Noir, vert acide. Typographie condensée géante Anton,
# portrait cadré vert acide (kinésiotaping sur la nuque et les épaules), compteurs, cartes numérotées, bandeau en défilement, formulaire. Anton + Archivo. Informatif uniquement.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Anton&family=Archivo:wght@300;400;500;600;700;800'
CSS = '''
:root{--bg:#0A0A0A;--fg:#F2F2EE;--acc:#D4FF3A;--onacc:#0A0A0A;--line:rgba(242,242,238,.13);--hbg:rgba(10,10,10,.86);--disp:Anton,Impact,sans-serif;--sans:Archivo,system-ui,sans-serif;--r:0;--mapbg:#161616;--fbg:rgba(255,255,255,.04)}
h1,h2,h3{text-transform:uppercase;letter-spacing:.005em}.brand .mono{width:44px;height:44px;display:grid;place-items:center;background:var(--acc);color:#0A0A0A;font:400 1.1rem var(--disp);clip-path:polygon(0 0,100% 0,100% 72%,72% 100%,0 100%)}
.hero .kick{max-width:60%;margin-bottom:2.2rem}.hero{position:relative;min-height:100svh;padding:9rem 0 3rem;overflow:hidden;display:flex;flex-direction:column;justify-content:flex-end}
.hero h1{font-size:clamp(4rem,12.5vw,13rem);line-height:.84;position:relative;z-index:2}.hero h1 span{display:block}.hero h1 .s{color:transparent;-webkit-text-stroke:2px var(--acc)}
.elas{position:absolute;right:clamp(1.5rem,5vw,5rem);top:16%;width:min(24vw,350px);aspect-ratio:3/4;z-index:1;margin:0}.elas:before{content:'';position:absolute;inset:18px -18px -18px 18px;border:2px solid var(--acc);z-index:-1}.elas .i{width:100%;height:100%;overflow:hidden;box-shadow:0 40px 80px rgba(0,0,0,.6)}.elas img{width:100%;height:100%;object-fit:cover;object-position:50% 35%;animation:zoom 16s ease-in-out infinite alternate}
@keyframes zoom{to{transform:scale(1.06)}}.elas figcaption{position:absolute;left:0;bottom:-2.2rem;font-size:.7rem;opacity:.6;letter-spacing:.06em}
.hrow{display:grid;grid-template-columns:1.2fr 1fr;gap:3rem;align-items:end;margin-top:2.4rem;position:relative;z-index:2}.lede{max-width:34rem;font-size:1.08rem;margin:0;opacity:.85}.acts{display:flex;gap:1rem;flex-wrap:wrap;justify-content:flex-end}
.tick{display:flex;border-block:1px solid var(--line);margin-top:3rem;position:relative;z-index:2}.tick div{flex:1;padding:1.2rem 1.4rem}.tick div+div{border-left:1px solid var(--line)}.tick small{display:block;font:700 .62rem/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--acc);margin-bottom:.5rem}
.mq{background:var(--acc);color:#0A0A0A;padding:1.1rem 0;font:400 clamp(2rem,4.4vw,3.8rem)/1 var(--disp);text-transform:uppercase;--mqs:26s;transform:rotate(-1.5deg);margin:-1rem 0 0;width:104%;margin-left:-2%}
.sec{padding:8rem 0}.sec h2{font-size:clamp(3rem,7vw,6.6rem);line-height:.9}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);margin-top:4rem;border:1px solid var(--line)}.cards article{background:var(--bg);padding:2.6rem 2.2rem;position:relative;overflow:hidden;transition:background .5s}
.cards article:hover{background:#141414}.cards .n{font:400 5rem/1 var(--disp);color:transparent;-webkit-text-stroke:1px var(--acc);display:block;margin-bottom:2.2rem}.cards h3{font-size:1.9rem;margin-bottom:.8rem}.cards p{opacity:.72;margin:0 0 1rem}
.cards article:after{content:'';position:absolute;left:0;bottom:0;height:3px;width:0;background:var(--acc);transition:width .7s var(--ease)}.cards article:hover:after{width:100%}
.dual{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem}.dual figure{margin:0;position:relative;overflow:hidden;min-height:560px}.dual img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.1);transition:filter .8s,transform 1.4s var(--ease)}
.dual figure:hover img{filter:none;transform:scale(1.04)}.dual figcaption{position:absolute;left:0;bottom:0;background:var(--acc);color:#0A0A0A;font:700 .7rem var(--sans);letter-spacing:.1em;text-transform:uppercase;padding:.5rem .8rem}
.info{display:grid;grid-template-columns:1fr 1fr 1fr;gap:1px;background:var(--line);border:1px solid var(--line)}.info>div{background:var(--bg);padding:2.4rem}.info h3{font-size:1.7rem;margin-bottom:1rem;color:var(--acc)}
.dl{margin:0}.dl div{padding:.85rem 0;border-bottom:1px solid var(--line)}.dl dt{font:700 .62rem/1.6 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.6}.dl dd{margin:0}
.rdv{display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem}.rdv .f{background:var(--fg);color:#0A0A0A;padding:2.6rem;--line:rgba(10,10,10,.15);--fln:rgba(10,10,10,.25);--acc:#0A0A0A;--onacc:#D4FF3A}
.mapw{filter:grayscale(.2)}
@media(max-width:960px){.elas{position:relative;right:auto;top:auto;width:min(78vw,380px);margin:0 0 3.4rem}.hero{justify-content:flex-start}.hrow,.dual,.rdv{grid-template-columns:1fr}.acts{justify-content:flex-start}.cards,.info{grid-template-columns:1fr}.dual figure{min-height:380px}}
@media(max-width:760px){.sec{padding:5.5rem 0}.tick{flex-direction:column}.tick div+div{border-left:0;border-top:1px solid var(--line)}.info>div,.rdv .f{padding:1.6rem}.hero h1 .s{-webkit-text-stroke:1.4px var(--acc)}}
'''
def build(F, M):
    msg = 'Bonjour, je souhaite prendre rendez-vous au cabinet de kinésithérapie.'
    brand = '<span class="mono">AB</span><span><b>Ahmed Boukadida</b><small>Kinésithérapie · Hammamet</small></span>'
    links = [('Domaines', '#domaines'), ('Le cabinet', '#cabinet'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    cards = [('Kinésithérapie', 'Rééducation par le mouvement et les techniques manuelles.', 'fiche Google'), ('Réadaptation fonctionnelle', 'Retrouver l’usage d’une articulation ou d’une fonction.', 'fiche Google'),
             ('Genou · LCA', 'Rééducation après reconstruction du ligament croisé antérieur : thème abordé par le praticien sur son profil professionnel.', 'à confirmer')]
    ch = ''.join(f'<article data-rv style="--d:{i*.1:.1f}s"><span class="n">0{i+1}</span><h3>{t}</h3><p>{p}</p>{ph(s)}</article>' for i, (t, p, s) in enumerate(cards))
    mq = ''.join(f'<span>{w}</span>' for w in ['Rééducation', '◆', 'Réadaptation', '◆', 'Hammamet', '◆'] * 2)
    body = f'''{lux.header(brand, links)}<main id="main">
<section class="hero" id="top"><figure class="elas rise d2"><div class="i">{M.img('hero', 'Bandes de kinésiotaping sur la nuque et les épaules (photo d’illustration)', sizes='(max-width: 960px) 78vw, 420px', lazy=False)}</div><figcaption>Kinésiotaping · photo d'illustration</figcaption></figure>
<div class="w"><p class="kick rise">Kinésithérapie et réadaptation fonctionnelle · Hammamet</p><h1 class="rise d1"><span>Rééduca</span><span class="s">tion.</span></h1>
<div class="hrow"><p class="lede rise d2">Cabinet d'Ahmed Boukadida, kinésithérapeute, rue Assad Ibn El Fourat, dans la zone touristique de Hammamet. Séances sur rendez-vous.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Prendre rendez-vous {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div></div>
<div class="tick rise d4"><div><small>Horaire relevé</small>Mercredi, {F['wed']}</div><div><small>Adresse</small>Rue Assad Ibn El Fourat</div><div><small>Téléphone</small>{F['tel']}</div></div></div></section>
<div class="mq" aria-hidden="true"><div>{mq}{mq}</div></div>
<section class="sec" id="domaines"><div class="w"><p class="kick" data-rv>Domaines</p><h2 data-rv>Remettre<br>en mouvement.</h2><div class="cards">{ch}</div>
<p class="note" data-rv style="margin-top:2rem">Liste indicative reprise des informations publiques, à confirmer par le praticien avant publication.</p></div></section>
<section class="sec" id="cabinet" style="padding-top:0"><div class="w dual"><figure data-rv>{M.img('genou', 'Séance de rééducation du genou (photo d’illustration)', sizes='(max-width: 960px) 92vw, 600px')}<figcaption>Illustration · ne montre pas le cabinet</figcaption></figure>
<figure data-rv style="--d:.12s">{M.img('radio', 'Radiographie du genou (image d’illustration)', sizes='(max-width: 960px) 92vw, 600px')}<figcaption>Illustration · radiographie</figcaption></figure></div></section>
<section class="sec" id="horaires" style="padding-top:0"><div class="w"><div class="info" data-rv><div><h3>Fiche</h3><dl class="dl"><div><dt>Praticien</dt><dd>Ahmed Boukadida</dd></div><div><dt>Profession</dt><dd>Kinésithérapeute</dd></div><div><dt>Diplômes</dt><dd>{ph()}</dd></div><div><dt>Adresse</dt><dd>{F['addr']}</dd></div></dl></div>
<div><h3>Horaires</h3>{lux.hours(F)}</div><div><h3>Contact</h3>{lux.contacts(F, wa_msg=msg)}</div></div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w rdv"><div data-rv><p class="kick">Rendez-vous</p><h2>Réserver<br>une séance.</h2><p style="margin-top:1.4rem;opacity:.8">Le message s'ouvre dans WhatsApp ; le cabinet confirme le créneau.</p></div>
<div class="f" data-rv style="--d:.1s">{lux.form(F, 'Bonjour, je souhaite un rendez-vous au cabinet de kinésithérapie.', lux.MED_FORM)}</div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><figure class="dual" style="display:block;margin:0 0 3rem;position:relative;min-height:320px;overflow:hidden" data-rv>{M.img('plage', 'Plage de Hammamet (photo d’illustration)', sizes='100vw', extra=' style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"')}</figure>
<p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Zone touristique.</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F)}'''
    return lux.page(F, 'Cabinet Ahmed Boukadida · Kinésithérapie à Hammamet (démo)', 'Cabinet de kinésithérapie et réadaptation fonctionnelle d’Ahmed Boukadida, zone touristique de Hammamet : coordonnées, horaires et demande de rendez-vous.', FONTS, CSS, body, '#0A0A0A', lux.fav('#D4FF3A', '#0A0A0A', 'AB', 'Impact', 'rect'))
