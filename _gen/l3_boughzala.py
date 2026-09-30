# Dr Wieme Boughzala, ORL et chirurgie cervico-faciale (Nabeul) : « faïence de Nabeul ». Ivoire, cobalt, émail turquoise. Hero éditorial centré :
# assiette de Nabeul en rotation lente traversée par une onde sonore animée ; motif de carreaux en CSS ; arches ; formulaire sur panneau cobalt. Playfair Display + Karla.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Karla:wght@300;400;500;600;700'
CSS = '''
:root{--bg:#F6F1E7;--fg:#14213D;--acc:#1D4ED8;--onacc:#fff;--line:rgba(20,33,61,.14);--hbg:rgba(246,241,231,.88);--disp:'Playfair Display',Georgia,serif;--sans:Karla,system-ui,sans-serif;--r:4px;--mapbg:#E9E1D0;--tq:#0F8B8D;--rbg:#14213D}
em{font-style:italic;color:var(--acc)}.brand .mono{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;background:var(--fg);color:#F6F1E7;font:italic 500 1.05rem var(--disp)}
.hero{padding:10rem 0 0;text-align:center;position:relative;overflow:hidden}
.hero h1{font-size:clamp(3.2rem,8.4vw,8.2rem);line-height:.95;letter-spacing:-.02em;font-weight:400}.hero .kick{justify-content:center}.hero .kick:after{content:'';width:34px;height:1px;background:currentColor}
.hero .lede{max-width:36rem;margin:1.8rem auto 2.2rem;font-size:1.1rem;opacity:.78}.acts{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}
.stage{position:relative;height:clamp(300px,42vw,560px);margin-top:3.5rem}
.plate{position:absolute;left:50%;top:0;width:clamp(340px,48vw,680px);aspect-ratio:1;transform:translateX(-50%);border-radius:50%;overflow:hidden;box-shadow:0 40px 90px rgba(20,33,61,.28)}
.plate img{width:100%;height:100%;object-fit:cover;animation:spin 90s linear infinite}@keyframes spin{to{transform:rotate(360deg)}}
.wave{position:absolute;left:0;right:0;top:34%;width:100%;height:140px;z-index:2;pointer-events:none}.wave path{fill:none;stroke:#fff;stroke-width:2;stroke-dasharray:14 10;animation:dash 6s linear infinite;mix-blend-mode:difference}
.wave path+path{stroke:var(--acc);stroke-dasharray:none;stroke-width:1.2;opacity:.8;animation:none}
@keyframes dash{to{stroke-dashoffset:-240}}
.facts{position:relative;z-index:3;background:var(--fg);color:#F6F1E7;display:grid;grid-template-columns:repeat(3,1fr);text-align:left}.facts div{padding:1.8rem 2rem}.facts div+div{border-left:1px solid rgba(246,241,231,.14)}
.facts small{display:block;font:700 .62rem/1 var(--sans);letter-spacing:.22em;text-transform:uppercase;color:#8FB3FF;margin-bottom:.6rem}.facts p{margin:0;font:400 1.2rem/1.3 var(--disp)}
.sec{padding:8rem 0}.sec h2{font-size:clamp(2.4rem,4.6vw,4.4rem);letter-spacing:-.01em}
.ed{display:grid;grid-template-columns:1.1fr .9fr;gap:6rem;align-items:center}.ed p.big{font:400 1.35rem/1.6 var(--disp);margin-top:2rem}.ed p.big:first-letter{float:left;font-size:4.6rem;line-height:.8;padding:.35rem .6rem 0 0;color:var(--acc)}
.arch{margin:0;border-radius:999px 999px 6px 6px;overflow:hidden;aspect-ratio:4/5;border:10px solid #fff;box-shadow:0 30px 60px rgba(20,33,61,.16)}.arch img{width:100%;height:100%;object-fit:cover}
.cap{font-size:.74rem;opacity:.6;margin-top:1rem;text-align:center}
.tiles{background-color:#14213D;color:#F6F1E7;--line:rgba(246,241,231,.16);position:relative;overflow:hidden}
.tiles:before{content:'';position:absolute;inset:0;opacity:.14;background:radial-gradient(circle at 50% 50%,transparent 38%,#8FB3FF 39%,#8FB3FF 41%,transparent 42%),conic-gradient(from 45deg,#0F8B8D 0 25%,transparent 0 50%,#0F8B8D 0 75%,transparent 0);background-size:90px 90px}
.tiles .w{position:relative}.tiles em{color:#8FB3FF}.tiles .kick{color:#8FB3FF}
.dom{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem;margin-top:4rem}.dom article{background:rgba(20,33,61,.72);border:1px solid rgba(143,179,255,.35);border-radius:999px 999px 18px 18px;padding:3.4rem 2rem 2.4rem;text-align:center;backdrop-filter:blur(4px);transition:transform .6s var(--ease),background .5s}
.dom article:hover{transform:translateY(-8px);background:rgba(246,241,231,.1)}.dom svg{width:84px;height:84px;color:#8FB3FF;margin:0 auto 1.6rem}.dom h3{font-size:1.8rem;margin-bottom:.6rem}.dom p{opacity:.75;margin:0 0 1rem;font-size:.95rem}
.gal{display:grid;grid-template-columns:1fr 1.3fr 1fr;gap:1.4rem;align-items:end}.gal figure{margin:0}.gal .a{border-radius:999px 999px 6px 6px;overflow:hidden;aspect-ratio:3/4}.gal .a img{width:100%;height:100%;object-fit:cover;transition:transform 1.4s var(--ease)}.gal figure:hover img{transform:scale(1.05)}
.gal figure:nth-child(2) .a{aspect-ratio:1;border-radius:50%}.gal figcaption{font-size:.74rem;opacity:.6;margin-top:.8rem;text-align:center}
.info{display:grid;grid-template-columns:1fr 1fr;gap:1.6rem}.card{background:#fff;border:1px solid var(--line);border-top:4px solid var(--acc);padding:2.4rem;border-radius:6px}
.card h3{font-size:1.8rem;margin-bottom:1.2rem}.dl{margin:0}.dl div{display:grid;grid-template-columns:10rem 1fr;gap:1rem;padding:.95rem 0;border-bottom:1px solid var(--line)}.dl dt{font:700 .62rem/1.7 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.6}.dl dd{margin:0}
.rdv{background:var(--acc);color:#fff;--line:rgba(255,255,255,.3);--fln:rgba(255,255,255,.4);--fbg:rgba(255,255,255,.08);border-radius:6px;padding:4.5rem;display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem}
.rdv .kick,.rdv em{color:#fff}.rdv .form button{background:#fff;color:var(--acc)}.rdv .form select option{color:#14213D}
.mapw{border-radius:6px;border:10px solid #fff;box-shadow:0 20px 50px rgba(20,33,61,.12)}
.ft{background:#EFE7D8}
@media(max-width:960px){.ed,.info,.rdv{grid-template-columns:1fr;gap:3rem}.dom{grid-template-columns:1fr}.gal{grid-template-columns:1fr 1fr}.gal figure:nth-child(3){display:none}.rdv{padding:2.4rem 1.4rem}}
@media(max-width:760px){.facts{grid-template-columns:1fr}.facts div+div{border-left:0;border-top:1px solid rgba(246,241,231,.14)}.sec{padding:5.5rem 0}.dl div{grid-template-columns:1fr;gap:.1rem}.card{padding:1.6rem}.stage{height:300px}.wave{top:22%}}
'''
WAVE = '<svg class="wave" viewBox="0 0 1440 140" preserveAspectRatio="none" aria-hidden="true"><path d="M0 70 C 60 70 80 20 120 20 S 180 120 240 120 300 30 360 30 420 110 480 110 540 40 600 40 660 100 720 100 780 10 840 10 900 130 960 130 1020 30 1080 30 1140 110 1200 110 1260 50 1320 50 1380 70 1440 70"/><path d="M0 70 C 120 70 160 40 240 40 S 360 100 480 100 600 50 720 50 840 90 960 90 1080 55 1200 55 1320 70 1440 70"/></svg>'
def build(F, M):
    msg = 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet ORL.'
    brand = '<span class="mono">WB</span><span><b>Dr Wieme Boughzala</b><small>ORL · Nabeul</small></span>'
    links = [('Le cabinet', '#cabinet'), ('Spécialité', '#specialite'), ('Infos', '#infos'), ('Accès', '#acces')]
    dom = [('ear', 'Otologie', 'L’oreille et l’audition.'), ('nose', 'Rhinologie', 'Le nez et les sinus.'), ('throat', 'Cervico-facial', 'La gorge, le larynx, le cou et la face.')]
    domh = ''.join(f'<article data-rv style="--d:{i*.12:.2f}s">{IC[k]}<h3>{t}</h3><p>{p}</p>{ph("indicatif")}</article>' for i, (k, t, p) in enumerate(dom))
    body = f'''{lux.header(brand, links)}<main id="main">
<section class="hero" id="top"><div class="w"><p class="kick rise">ORL et chirurgie cervico-faciale · Nabeul</p><h1 class="rise d1">Dr Wieme <em>Boughzala</em></h1>
<p class="lede rise d2">Cabinet d'oto-rhino-laryngologie, immeuble Melek, avenue Hédi Nouira à Oued Souhil, en face de Topnet. Consultations sur rendez-vous.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Prendre rendez-vous {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div></div>
<div class="stage rise d2"><div class="plate">{M.img('hero', 'Assiette en céramique de Nabeul (photo d’illustration)', sizes='(max-width: 760px) 340px, 680px', lazy=False)}</div>{WAVE}</div>
<div class="facts"><div><small>Téléphone</small><p><a href="{K.telhref(F['tel'])}">{F['tel']}</a></p></div><div><small>Horaire relevé</small><p>Mercredi, {F['wed']}</p></div><div><small>Adresse</small><p>Immeuble Melek, 2e étage</p></div></div></section>
<section class="sec" id="cabinet"><div class="w ed"><div><p class="kick" data-rv>Le cabinet</p><h2 data-rv>Un cabinet d'ORL <em>au cœur de Nabeul</em>.</h2>
<p class="big" data-rv>Le Dr Wieme Boughzala exerce l'oto-rhino-laryngologie et la chirurgie cervico-faciale au 2e étage de l'immeuble Melek, bureau n°01. Les patients sont reçus sur rendez-vous, pris par téléphone ou via WhatsApp.</p>
<p class="note" data-rv>Informations reprises des fiches publiques du cabinet ; parcours et qualifications {ph()}</p></div>
<figure data-rv="r" style="margin:0"><div class="arch">{M.img('faience', 'Nature morte aux faïences de Nabeul (photo d’illustration)', sizes='(max-width: 960px) 90vw, 460px')}</div><figcaption class="cap">Faïences de Nabeul · illustration, ne montre pas le cabinet</figcaption></figure></div></section>
<section class="sec tiles" id="specialite"><div class="w"><p class="kick" data-rv>La spécialité</p><h2 data-rv>Oreille, nez, gorge, <em>face et cou</em>.</h2><div class="dom">{domh}</div></div></section>
<section class="sec"><div class="w gal"><figure data-rv>{'<div class="a">'+M.img('diapason', 'Diapason (photo d’illustration)', sizes='(max-width: 960px) 45vw, 340px')+'</div>'}<figcaption>Diapason · illustration</figcaption></figure>
<figure data-rv style="--d:.12s"><div class="a">{M.img('tasse', 'Tasse en céramique tunisienne (photo d’illustration)', sizes='(max-width: 960px) 45vw, 440px')}</div><figcaption>Céramique tunisienne · illustration</figcaption></figure>
<figure data-rv style="--d:.24s"><div class="a">{M.img('onde', 'Vibrations d’un diapason (photo d’illustration)', sizes='340px')}</div><figcaption>Ondes sonores · illustration</figcaption></figure></div></section>
<section class="sec" id="infos" style="padding-top:0"><div class="w info"><div class="card" data-rv><h3>Fiche du cabinet</h3><dl class="dl"><div><dt>Médecin</dt><dd>Dr Wieme Boughzala</dd></div><div><dt>Spécialité</dt><dd>ORL et chirurgie cervico-faciale</dd></div>
<div><dt>Qualification</dt><dd>{ph()}</dd></div><div><dt>Adresse</dt><dd>{F['addr']} (en face de Topnet)</dd></div></dl><div style="margin-top:1rem">{lux.contacts(F, wa_msg=msg)}</div></div>
<div class="card" data-rv style="--d:.12s"><h3>Horaires</h3>{lux.hours(F)}</div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w"><div class="rdv"><div data-rv><p class="kick">Rendez-vous</p><h2>Demander un <em>rendez-vous</em></h2><p style="margin-top:1.4rem;opacity:.85">Le formulaire prépare un message WhatsApp ; le cabinet confirme le créneau.</p></div>
<div data-rv style="--d:.1s">{lux.form(F, 'Bonjour Docteur, je souhaite un rendez-vous au cabinet ORL.', lux.MED_FORM)}</div></div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Oued Souhil, <em>Nabeul</em></h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F)}'''
    return lux.page(F, 'Dr Wieme Boughzala · ORL à Nabeul (démo)', 'Cabinet ORL et chirurgie cervico-faciale du Dr Wieme Boughzala à Nabeul : coordonnées, horaires et demande de rendez-vous.', FONTS, CSS, body, '#F6F1E7', lux.fav('#1D4ED8', '#fff', 'WB'))
