# Dr Fethi Boukadida, médecin généraliste (Hammamet) : « veilleur de nuit ». Bleu minuit, jaune lampe. Hero nocturne plein écran (Yasmine Hammamet de nuit),
# horloge analogique vivante (heure réelle), italiques Instrument Serif géantes, mention « 24h/24 » donnée comme relevé à confirmer, cartes, formulaire. Instrument Serif + Geist.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Instrument+Serif:ital@0;1&family=Geist:wght@300;400;500;600;700'
CSS = '''
:root{--bg:#0A1230;--fg:#EEF0F7;--acc:#FFC857;--onacc:#0A1230;--line:rgba(238,240,247,.13);--hbg:rgba(10,18,48,.86);--disp:'Instrument Serif',Georgia,serif;--sans:Geist,system-ui,sans-serif;--r:999px;--mapbg:#111B42;--fbg:rgba(255,255,255,.04)}
em{font-style:italic;color:var(--acc)}.brand .mono{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;background:var(--acc);color:#0A1230;font:italic 400 1.2rem var(--disp)}
.hero{position:relative;min-height:100svh;display:flex;align-items:center;overflow:hidden;isolation:isolate}.hero .px{filter:saturate(1.1)}
.hero:after{content:'';position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(10,18,48,.95) 25%,rgba(10,18,48,.4) 70%,rgba(10,18,48,.6)),linear-gradient(0deg,var(--bg),transparent 35%)}
.hg{display:grid;grid-template-columns:1.3fr .7fr;gap:3rem;align-items:center;padding:9rem 0 4rem}
.hero h1{font-size:clamp(3.6rem,8.6vw,8.8rem);line-height:.9;font-weight:400;letter-spacing:-.02em}.hero h1 span{display:block}
.lede{max-width:33rem;font-size:1.08rem;opacity:.82;margin:1.8rem 0 2.2rem}.acts{display:flex;gap:1rem;flex-wrap:wrap}
.clock{width:min(340px,100%);aspect-ratio:1;justify-self:center;border-radius:50%;background:radial-gradient(circle,rgba(255,200,87,.12),rgba(10,18,48,.3) 70%);border:1px solid rgba(255,200,87,.35);box-shadow:0 0 90px rgba(255,200,87,.18);position:relative}
.clock svg{width:100%;height:100%}.clock .hd{transform-origin:100px 100px}.clock .sh{animation:tick 60s steps(60) infinite}@keyframes tick{to{transform:rotate(360deg)}}
.clock p{position:absolute;left:0;right:0;bottom:-3.4rem;text-align:center;font-size:.82rem;opacity:.75;margin:0}
.badge{display:inline-flex;align-items:center;gap:.7rem;border:1px solid rgba(255,200,87,.4);border-radius:99px;padding:.5rem 1rem .5rem .5rem;font-size:.86rem;margin-bottom:1.8rem}.badge b{background:var(--acc);color:#0A1230;border-radius:99px;padding:.3rem .7rem;font-weight:700}
.sec{padding:8rem 0}.sec h2{font-size:clamp(2.6rem,5.6vw,5.4rem);line-height:.98;font-weight:400}
.lamp{background:#FFF7E6;color:#1A1F33;--line:rgba(26,31,51,.12);--acc:#B7791F}.lamp em{color:#B7791F}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem;margin-top:4rem}.three article{background:#fff;border-radius:28px;padding:2.4rem 2rem;box-shadow:0 20px 50px rgba(26,31,51,.06)}.three svg{width:60px;height:60px;color:#B7791F;margin-bottom:2rem}.three h3{font-size:2rem;margin-bottom:.5rem;font-weight:400}.three p{opacity:.75;margin:0}
.nt{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem}.nt figure{margin:0;position:relative;overflow:hidden;border-radius:28px;min-height:480px}.nt img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.6s var(--ease)}.nt figure:hover img{transform:scale(1.05)}
.nt figcaption{position:absolute;left:1rem;bottom:1rem;background:rgba(10,18,48,.7);backdrop-filter:blur(6px);border-radius:99px;padding:.35rem .8rem;font-size:.72rem}
.info{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem}.card{border:1px solid var(--line);border-radius:28px;padding:2.6rem;background:rgba(255,255,255,.03)}.card h3{font-size:2.1rem;margin-bottom:1rem;font-weight:400}
.dl{margin:0}.dl div{display:grid;grid-template-columns:10rem 1fr;gap:1rem;padding:.9rem 0;border-bottom:1px solid var(--line)}.dl dt{font:600 .62rem/1.7 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.55}.dl dd{margin:0}
.alert{display:flex;gap:1rem;align-items:center;border:1px solid rgba(255,200,87,.4);border-radius:20px;padding:1.2rem 1.4rem;margin-top:1.4rem;font-size:.9rem}.alert b{font:italic 400 2.2rem/1 var(--disp);color:var(--acc)}
.rdv{display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem}.form select option{color:#0A1230}
.mapw{border-radius:28px}
@media(max-width:960px){.hg,.nt,.info,.rdv{grid-template-columns:1fr}.clock{width:min(240px,64%);margin-bottom:3rem}.three{grid-template-columns:1fr}.nt figure{min-height:340px}}
@media(max-width:760px){.sec{padding:5.5rem 0}.card{padding:1.6rem}.dl div{grid-template-columns:1fr;gap:.1rem}}
'''
def clock():
    t = ''.join(f'<line x1="100" y1="{14 if i%5==0 else 17}" x2="100" y2="22" transform="rotate({i*6} 100 100)" stroke="{"#FFC857" if i%5==0 else "rgba(238,240,247,.4)"}" stroke-width="{2 if i%5==0 else 1}"/>' for i in range(60))
    return (f'<svg viewBox="0 0 200 200" aria-hidden="true">{t}<g class="hd" data-h><line x1="100" y1="100" x2="100" y2="56" stroke="#EEF0F7" stroke-width="4" stroke-linecap="round"/></g>'
            f'<g class="hd" data-m><line x1="100" y1="100" x2="100" y2="34" stroke="#EEF0F7" stroke-width="2.4" stroke-linecap="round"/></g><g class="hd sh" data-s><line x1="100" y1="112" x2="100" y2="28" stroke="#FFC857" stroke-width="1.2"/></g>'
            f'<circle cx="100" cy="100" r="4" fill="#FFC857"/></svg>')
CJS = '''<script>(function(){var n=new Date(),h=document.querySelector('[data-h]'),m=document.querySelector('[data-m]'),s=document.querySelector('[data-s]');if(!h)return;
function u(){var d=new Date();h.style.transform='rotate('+((d.getHours()%12)*30+d.getMinutes()/2)+'deg)';m.style.transform='rotate('+(d.getMinutes()*6)+'deg)'}u();setInterval(u,30000);
s.style.animationDelay='-'+n.getSeconds()+'s'})();</script>'''
def build(F, M):
    msg = 'Bonjour Docteur, je souhaite venir consulter au cabinet.'
    brand = '<span class="mono">FB</span><span><b>Dr Fethi Boukadida</b><small>Médecine générale · Hammamet</small></span>'
    links = [('Le cabinet', '#cabinet'), ('Médecine générale', '#mg'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    three = [('steth', 'Consultation', 'Consultation de médecine générale au cabinet.'), ('doc', 'Suivi', 'Le suivi des patients dans la durée.'), ('shield', 'Orientation', 'Vers un médecin spécialiste si nécessaire.')]
    th = ''.join(f'<article data-rv style="--d:{i*.12:.2f}s">{IC[k]}<h3>{t}</h3><p>{p}</p></article>' for i, (k, t, p) in enumerate(three))
    body = f'''{lux.header(brand, links, ('Contact', '#rdv'))}<main id="main">
<section class="hero" id="top"><div class="pxw">{M.img('hero', 'Yasmine Hammamet de nuit (photo d’illustration)', cls='px', sizes='100vw', lazy=False, extra=' data-px=".14"')}</div>
<div class="w hg"><div><p class="badge rise"><b>24h/24</b>Mention relevée sur la fiche Google, à confirmer</p><h1 class="rise d1"><span>Dr Fethi</span><span><em>Boukadida</em></span></h1>
<p class="lede rise d2">Cabinet de médecine générale au 27 avenue de la Libération, au rond-point Julia, en face de la banque STB, à Hammamet.</p>
<div class="acts rise d3"><a class="btn p" href="{K.telhref(F['tel'])}">{K.I['phone']}Appeler le {F['tel']}</a><a class="btn o" href="#rdv">Écrire au cabinet {IC['arrow']}</a></div></div>
<div class="clock rise d2">{clock()}<p>Heure locale</p></div></div></section>
<section class="sec" id="cabinet"><div class="w info"><div data-rv><p class="kick">Le cabinet</p><h2>Au rond-point <em>Julia</em>.</h2><p style="font-size:1.12rem;margin-top:1.6rem;max-width:34rem;opacity:.85">Le cabinet du Dr Fethi Boukadida se trouve avenue de la Libération (Ettahrir), face à la banque STB. La fiche Google du cabinet le signale également dans la catégorie des services d'urgence.</p>
<div class="alert"><b>190</b><span>En cas d'urgence vitale, appelez le SAMU au 190.</span></div></div>
<div class="card" data-rv style="--d:.1s"><h3>Fiche</h3><dl class="dl"><div><dt>Médecin</dt><dd>Dr Fethi Boukadida</dd></div><div><dt>Exercice</dt><dd>Médecine générale</dd></div><div><dt>Qualification</dt><dd>{ph()}</dd></div><div><dt>Adresse</dt><dd>{F['addr']}</dd></div></dl></div></div></section>
<section class="sec lamp" id="mg"><div class="w"><p class="kick" data-rv>La médecine générale</p><h2 data-rv>Le médecin de <em>premier recours</em>.</h2><div class="three">{th}</div><p class="note" data-rv style="margin-top:2rem">Présentation générale, à titre informatif.</p></div></section>
<section class="sec"><div class="w nt"><figure data-rv>{M.img('marina', 'Marina de Yasmine Hammamet au crépuscule (photo d’illustration)', sizes='(max-width: 960px) 92vw, 600px')}<figcaption>Hammamet · illustration</figcaption></figure>
<figure data-rv style="--d:.12s">{M.img('sacoche', 'Sacoche de médecin (photo d’illustration)', sizes='(max-width: 960px) 92vw, 600px')}<figcaption>Illustration · ne montre pas le cabinet</figcaption></figure></div></section>
<section class="sec" id="horaires" style="padding-top:0"><div class="w info"><div class="card" data-rv><h3>Horaires</h3>{lux.hours(F)}</div><div class="card" data-rv style="--d:.1s"><h3>Contact</h3>{lux.contacts(F, 'WhatsApp · message au cabinet', msg)}</div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w rdv"><div data-rv><p class="kick">Contact</p><h2>Écrire au <em>cabinet</em>.</h2><p style="margin-top:1.4rem;opacity:.8">Le message s'ouvre dans WhatsApp. Pour une urgence vitale, appelez le 190.</p>
<figure style="margin:2rem 0 0;border-radius:24px;overflow:hidden;max-width:420px" data-rv>{M.img('aube', 'Côte de Hammamet à l’aube (photo d’illustration)', sizes='420px')}</figure></div>
<div class="card" data-rv style="--d:.1s">{lux.form(F, 'Bonjour Docteur, je souhaite venir consulter au cabinet.', lux.MED_FORM)}</div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Avenue de la <em>Libération</em>.</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F, 'Écrire', '#rdv', 'wa')}{CJS}'''
    return lux.page(F, 'Dr Fethi Boukadida · Médecin généraliste à Hammamet (démo)', 'Cabinet de médecine générale du Dr Fethi Boukadida, avenue de la Libération, Hammamet : coordonnées et contact.', FONTS, CSS, body, '#0A1230', lux.fav('#FFC857', '#0A1230', 'FB'))
