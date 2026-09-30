# Dr Ayoub Trabelsi, ORL (Nabeul) : « résonance ». Pétrole encre, menthe, os. Hero scindé, modèle anatomique de l'oreille dans un cercle entouré d'ondes animées,
# triptyque O · N · G en grandes lettres, actes publiés par le cabinet (à confirmer), fiche d'identité, horaires, rendez-vous WhatsApp. Newsreader + Inter Tight.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300;1,6..72,400&family=Inter+Tight:wght@300;400;500;600;700'
CSS = '''
:root{--bg:#0C2226;--fg:#E9EFEA;--acc:#8FE3C8;--onacc:#082024;--line:rgba(233,239,234,.13);--hbg:rgba(12,34,38,.86);--disp:Newsreader,Georgia,serif;--sans:'Inter Tight',system-ui,sans-serif;--r:999px;--mapbg:#12302F;--fbg:rgba(255,255,255,.04)}
em{font-style:italic;color:var(--acc)}.brand .mono{width:42px;height:42px;border-radius:50%;display:grid;place-items:center;border:1px solid var(--acc);color:var(--acc);font:italic 400 1.1rem var(--disp)}
.hero{min-height:100svh;display:grid;grid-template-columns:1.05fr .95fr;align-items:center;gap:3rem;padding:9rem 0 4rem;position:relative;overflow:hidden}
.hero:before{content:'';position:absolute;inset:auto -20% -40% auto;width:70vw;height:70vw;background:radial-gradient(closest-side,rgba(143,227,200,.14),transparent);pointer-events:none}
.hero h1{font-size:clamp(3.4rem,7.6vw,7.4rem);line-height:.92;letter-spacing:-.02em;font-weight:300}.hero h1 span{display:block}
.lede{font-size:1.1rem;max-width:32rem;opacity:.82;margin:2rem 0 2.4rem}.acts{display:flex;gap:1rem;flex-wrap:wrap}
.orb{position:relative;aspect-ratio:1;width:min(600px,100%);justify-self:center}.orb:after{content:'';position:absolute;inset:4%;border-radius:50%;border:1px dashed rgba(143,227,200,.28);animation:spin 60s linear infinite}@keyframes spin{to{transform:rotate(360deg)}}
.orb .ph0{position:absolute;inset:14%;border-radius:50%;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.45)}.orb .ph0 img{width:100%;height:100%;object-fit:cover;object-position:58% 50%;filter:saturate(.92) contrast(1.04)}
.orb i{position:absolute;inset:14%;border-radius:50%;border:1px solid var(--acc);opacity:0;animation:ring 4.8s cubic-bezier(.2,.6,.3,1) infinite}.orb i:nth-of-type(2){animation-delay:1.6s}.orb i:nth-of-type(3){animation-delay:3.2s}
@keyframes ring{0%{transform:scale(1);opacity:.7}100%{transform:scale(1.42);opacity:0}}
.orb .tag{position:absolute;left:0;bottom:8%;background:var(--fg);color:var(--bg);border-radius:18px;padding:1rem 1.2rem;font-size:.8rem;line-height:1.35;box-shadow:0 20px 40px rgba(0,0,0,.3)}.orb .tag b{display:block;font:500 1.3rem var(--disp)}
.strip{border-top:1px solid var(--line);border-bottom:1px solid var(--line);display:grid;grid-template-columns:repeat(3,1fr)}.strip div{padding:1.6rem 1.8rem}.strip div+div{border-left:1px solid var(--line)}
.strip small{display:block;font:600 .62rem/1 var(--sans);letter-spacing:.24em;text-transform:uppercase;opacity:.6;margin-bottom:.6rem}.strip p{margin:0;font:400 1.25rem/1.25 var(--disp)}
.sec{padding:8rem 0}.sec h2{font-size:clamp(2.4rem,4.6vw,4.2rem);letter-spacing:-.015em}
.ong{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem;margin-top:4rem}.ong article{position:relative;border:1px solid var(--line);border-radius:28px;padding:2.4rem 2rem 2rem;overflow:hidden;transition:background .5s,border-color .5s}
.ong article:hover{background:rgba(143,227,200,.06);border-color:rgba(143,227,200,.4)}.ong .L{font:300 9rem/.8 var(--disp);color:transparent;-webkit-text-stroke:1px rgba(143,227,200,.55);position:absolute;right:1.2rem;top:1rem}
.ong svg{width:64px;height:64px;color:var(--acc);margin-bottom:5rem}.ong h3{font-size:1.9rem;margin-bottom:.6rem}.ong p{opacity:.75;font-size:.95rem;margin:0}
.lead2{max-width:40rem;opacity:.78;margin-top:1.4rem}
.bone{background:#EEF1EC;color:#0C2226;--line:rgba(12,34,38,.14);--acc:#0E6B5C;--onacc:#fff}.bone em{color:#0E6B5C}
.acte{display:grid;grid-template-columns:1fr 1.1fr;gap:5rem;align-items:start}
.al{list-style:none;margin:2.4rem 0 0;padding:0;border-top:1px solid var(--line)}.al li{display:grid;grid-template-columns:3rem 1fr auto;align-items:center;gap:1rem;padding:1.5rem 0;border-bottom:1px solid var(--line);font:400 1.6rem/1.2 var(--disp)}
.al li span{font:600 .7rem var(--sans);letter-spacing:.2em;color:var(--acc)}.al .ph{font-size:.6rem}
.duo{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem}.duo figure{margin:0;border-radius:24px;overflow:hidden;position:relative;aspect-ratio:4/5}.duo figure:nth-child(2){margin-top:4rem}
.duo img{width:100%;height:100%;object-fit:cover;transition:transform 1.4s var(--ease)}.duo figure:hover img{transform:scale(1.05)}.duo figcaption{position:absolute;left:1rem;bottom:1rem;right:1rem;font-size:.72rem;background:rgba(238,241,236,.9);border-radius:99px;padding:.4rem .8rem}
.id{display:grid;grid-template-columns:.9fr 1.1fr;gap:5rem}.dl{margin:0}.dl div{display:grid;grid-template-columns:12rem 1fr;gap:1rem;padding:1.1rem 0;border-bottom:1px solid var(--line)}
.dl dt{font:600 .64rem/1.6 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.6}.dl dd{margin:0;font:400 1.15rem/1.4 var(--disp)}
.pan{background:#10292D;border:1px solid var(--line);border-radius:28px;padding:2.4rem}
.rdv{display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem;align-items:start}.rdv .pan{background:#EEF1EC;color:#0C2226;--line:rgba(12,34,38,.15);--acc:#0E6B5C;--onacc:#fff;--fln:rgba(12,34,38,.25)}
.mapw{border-radius:28px;margin-top:4rem}
.ft{border-top:1px solid var(--line)}.band2{position:relative;height:62vh;min-height:380px;overflow:hidden;isolation:isolate;display:flex;align-items:flex-end}.band2:after{content:'';position:absolute;inset:0;z-index:-1;background:linear-gradient(0deg,rgba(12,34,38,.9),rgba(12,34,38,.15) 60%)}.band2 .w{padding-bottom:2.6rem}.band2 h2{font-size:clamp(2.2rem,5vw,4.6rem)}.band2 small{opacity:.7;font-size:.74rem}
@media(max-width:960px){.hero{grid-template-columns:1fr;padding-top:8rem;gap:2rem}.orb{width:min(340px,80%);order:-1}.acte,.id,.rdv{grid-template-columns:1fr;gap:3rem}.ong{grid-template-columns:1fr}.ong svg{margin-bottom:2.4rem}}
@media(max-width:760px){.strip{grid-template-columns:1fr}.strip div+div{border-left:0;border-top:1px solid var(--line)}.sec{padding:5.5rem 0}.dl div{grid-template-columns:1fr;gap:.2rem}.al li{font-size:1.25rem;grid-template-columns:2.4rem 1fr}.al li .ph{grid-column:2}.pan{padding:1.6rem}.duo figure:nth-child(2){margin-top:2rem}}
'''
def build(F, M):
    wa = K.walink(F['wa'], 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet ORL.')
    brand = '<span class="mono">AT</span><span><b>Dr Ayoub Trabelsi</b><small>ORL · Nabeul</small></span>'
    links = [('Le cabinet', '#cabinet'), ('Spécialité', '#specialite'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    ong = [('ear', 'O', 'Oreille', 'L’oreille externe, moyenne et interne, et l’audition.'), ('nose', 'N', 'Nez', 'Les fosses nasales et les sinus.'), ('throat', 'G', 'Gorge', 'Le pharynx, le larynx et la voix, ainsi que le cou.')]
    ongh = ''.join(f'<article data-rv style="--d:{i*.12:.2f}s"><span class="L">{L}</span>{IC[k]}<h3>{t}</h3><p>{p}</p></article>' for i, (k, L, t, p) in enumerate(ong))
    actes = ['Chirurgie de la face et du cou', 'Audiométrie', 'Endoscopie']
    alh = ''.join(f'<li><span>0{i+1}</span>{a}{ph()}</li>' for i, a in enumerate(actes))
    body = f'''{lux.header(brand, links)}<main id="main">
<section class="w hero" id="top"><div><p class="kick rise">Oto-rhino-laryngologie · Nabeul</p><h1 class="rise d1"><span>Dr Ayoub</span><span><em>Trabelsi</em></span></h1>
<p class="lede rise d2">Cabinet d'ORL au Complexe Jasmin Médical, avenue Hédi Nouira, en face de la Clinique El Amen. Consultations sur rendez-vous.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Prendre rendez-vous {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div></div>
<div class="orb rise d2"><i></i><i></i><i></i><div class="ph0">{M.img('hero', 'Modèle anatomique de l’oreille en coupe (photo d’illustration)', sizes='(max-width: 960px) 80vw, 460px', lazy=False)}</div>
<div class="tag"><b>Bureau 203</b>2e étage · Jasmin Médical</div></div></section>
<div class="w strip" data-rv><div><small>Téléphone</small><p><a href="{K.telhref(F['tel'])}">{F['tel']}</a></p></div><div><small>Horaire relevé</small><p>Mercredi, {F['wed']}</p></div><div><small>Adresse</small><p>Av. Hédi Nouira, Nabeul</p></div></div>
<section class="sec" id="specialite"><div class="w"><p class="kick" data-rv>La spécialité</p><h2 data-rv>Oreille, nez, <em>gorge</em>, et chirurgie de la face et du cou.</h2>
<p class="lead2" data-rv>L'oto-rhino-laryngologie concerne les organes de la sphère ORL. Présentation générale de la spécialité, à titre informatif.</p><div class="ong">{ongh}</div></div></section>
<figure class="band2" style="margin:0"><div class="pxw">{M.img('nabeul', 'Plage de Nabeul (photo d’illustration)', cls='px', sizes='100vw', extra=' data-px=".15"')}</div><div class="w" data-rv><h2>Consulter à <em>Nabeul</em></h2><small>Photo d'illustration · ne montre pas le cabinet</small></div></figure>
<section class="sec bone" id="cabinet"><div class="w acte"><div><p class="kick" data-rv>Au cabinet</p><h2 data-rv>Actes mentionnés sur les <em>fiches publiques</em> du cabinet.</h2>
<ul class="al" data-rv>{alh}</ul><p class="note" data-rv>Liste reprise des annuaires médicaux en ligne, à confirmer par le cabinet avant publication.</p></div>
<div class="duo"><figure data-rv>{M.img('oreille', 'Modèle ancien de l’oreille en ivoire (photo d’illustration)', sizes='(max-width: 960px) 46vw, 300px')}<figcaption>Illustration · anatomie de l'oreille</figcaption></figure>
<figure data-rv style="--d:.15s">{M.img('oto', 'Otoscope (photo d’illustration)', sizes='(max-width: 960px) 46vw, 300px')}<figcaption>Illustration · otoscope</figcaption></figure></div></div></section>
<section class="sec" id="horaires"><div class="w id"><div data-rv><p class="kick">Fiche du cabinet</p><h2>Informations <em>pratiques</em></h2>
<dl class="dl" style="margin-top:2.4rem"><div><dt>Médecin</dt><dd>Dr Ayoub Trabelsi</dd></div><div><dt>Spécialité</dt><dd>Oto-rhino-laryngologie (ORL)</dd></div><div><dt>Qualification · Ordre</dt><dd>{ph()}</dd></div><div><dt>Adresse</dt><dd>{F['addr']}</dd></div></dl></div>
<div class="pan" data-rv style="--d:.1s"><h3 style="font-size:1.7rem;margin-bottom:1rem">Horaires</h3>{lux.hours(F)}<div style="margin-top:1.6rem">{lux.contacts(F, wa_msg='Bonjour Docteur, je souhaite prendre rendez-vous au cabinet ORL.')}</div></div></div></section>
<section class="sec bone" id="rdv"><div class="w rdv"><div data-rv><p class="kick">Rendez-vous</p><h2>Demander un <em>rendez-vous</em></h2><p class="lead2">Indiquez le jour et le moment souhaités : le message s'ouvre dans WhatsApp et le cabinet vous confirme le créneau.</p>
<p><a class="btn o" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp direct</a></p></div>
<div class="pan" data-rv style="--d:.1s">{lux.form(F, 'Bonjour Docteur, je souhaite un rendez-vous au cabinet ORL.', lux.MED_FORM)}</div></div></section>
<section class="sec" id="acces" style="padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv>Avenue Hédi Nouira, <em>Nabeul</em></h2><p class="lead2" data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc)">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F)}'''
    return lux.page(F, 'Dr Ayoub Trabelsi · ORL à Nabeul (démo)', 'Cabinet ORL du Dr Ayoub Trabelsi, Complexe Jasmin Médical, Nabeul : coordonnées, horaires et demande de rendez-vous.', FONTS, CSS, body, '#0C2226', lux.fav('#0C2226', '#8FE3C8', 'AT'))
