# Dr Fethi Boukadida, médecin généraliste (Hammamet) : « la garde ». Bleu minuit, jaune lampe. Hero bleu nuit à halo doré : grand médaillon lumineux
# (stéthoscope, blouse blanche) souligné d'un tracé de pouls animé, italiques Instrument Serif géantes, mention « 24h/24 » donnée comme relevé à confirmer, cartes, formulaire. Instrument Serif + Geist.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Instrument+Serif:ital@0;1&family=Geist:wght@300;400;500;600;700'
CSS = '''
:root{--bg:#0A1230;--fg:#EEF0F7;--acc:#FFC857;--onacc:#0A1230;--line:rgba(238,240,247,.13);--hbg:rgba(10,18,48,.86);--disp:'Instrument Serif',Georgia,serif;--sans:Geist,system-ui,sans-serif;--r:999px;--mapbg:#111B42;--fbg:rgba(255,255,255,.04)}
em{font-style:italic;color:var(--acc)}.brand .mono{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;background:var(--acc);color:#0A1230;font:italic 400 1.2rem var(--disp)}
.hero{position:relative;min-height:100svh;display:flex;align-items:center;overflow:hidden;isolation:isolate;background:radial-gradient(45% 60% at 74% 48%,rgba(255,200,87,.16),transparent 70%),radial-gradient(60% 60% at 10% 100%,rgba(60,90,200,.18),transparent 70%),var(--bg)}
.hg{display:grid;grid-template-columns:1.1fr .9fr;gap:3rem;align-items:center;padding:9rem 0 4rem}
.hero h1{font-size:clamp(3.6rem,8.6vw,8.8rem);line-height:.9;font-weight:400;letter-spacing:-.02em}.hero h1 span{display:block}
.lede{max-width:33rem;font-size:1.08rem;opacity:.82;margin:1.8rem 0 2.2rem}.acts{display:flex;gap:1rem;flex-wrap:wrap}
.medal{position:relative;margin:0;justify-self:center;width:min(420px,100%)}.medal .i{border-radius:50%;overflow:hidden;aspect-ratio:1;border:1px solid rgba(255,200,87,.5);box-shadow:0 0 0 14px rgba(255,200,87,.06),0 0 120px rgba(255,200,87,.25)}.medal img{width:100%;height:100%;object-fit:cover;object-position:50% 50%}
.medal:before{content:'';position:absolute;inset:-34px;border-radius:50%;border:1px dashed rgba(255,200,87,.28);animation:rot 80s linear infinite}@keyframes rot{to{transform:rotate(360deg)}}
.pulse{display:block;width:100%;height:56px;margin-top:1.6rem;color:var(--acc)}.pulse path{stroke-dasharray:640;stroke-dashoffset:640;animation:ecg 3.2s linear infinite}@keyframes ecg{60%,100%{stroke-dashoffset:0}}@media(prefers-reduced-motion:reduce){.pulse path{animation:none;stroke-dashoffset:0}.medal:before{animation:none}}
.medal figcaption{text-align:center;font-size:.74rem;opacity:.65;margin-top:.4rem}
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
@media(max-width:960px){.hg,.nt,.info,.rdv{grid-template-columns:1fr}.medal{width:min(300px,76%);order:-1;margin-top:1rem}.three{grid-template-columns:1fr}.nt figure{min-height:340px}}
@media(max-width:760px){.sec{padding:5.5rem 0}.card{padding:1.6rem}.dl div{grid-template-columns:1fr;gap:.1rem}}
'''
PULSE = '<svg class="pulse" viewBox="0 0 400 56" aria-hidden="true"><path d="M0 30h120l10-14 12 30 14-44 12 46 10-18h222" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>'
def build(F, M):
    msg = 'Bonjour Docteur, je souhaite venir consulter au cabinet.'
    brand = '<span class="mono">FB</span><span><b>Dr Fethi Boukadida</b><small>Médecine générale · Hammamet</small></span>'
    links = [('Le cabinet', '#cabinet'), ('Médecine générale', '#mg'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    three = [('steth', 'Consultation', 'Consultation de médecine générale au cabinet.'), ('doc', 'Suivi', 'Le suivi des patients dans la durée.'), ('shield', 'Orientation', 'Vers un médecin spécialiste si nécessaire.')]
    th = ''.join(f'<article data-rv style="--d:{i*.12:.2f}s">{IC[k]}<h3>{t}</h3><p>{p}</p></article>' for i, (k, t, p) in enumerate(three))
    body = f'''{lux.header(brand, links, ('Contact', '#rdv'))}<main id="main">
<section class="hero" id="top">
<div class="w hg"><div><p class="badge rise"><b>24h/24</b>Mention relevée sur la fiche Google, à confirmer</p><h1 class="rise d1"><span>Dr Fethi</span><span><em>Boukadida</em></span></h1>
<p class="lede rise d2">Cabinet de médecine générale au 27 avenue de la Libération, au rond-point Julia, en face de la banque STB, à Hammamet.</p>
<div class="acts rise d3"><a class="btn p" href="{K.telhref(F['tel'])}">{K.I['phone']}Appeler le {F['tel']}</a><a class="btn o" href="#rdv">Écrire au cabinet {IC['arrow']}</a></div></div>
<figure class="medal rise d2"><div class="i">{M.img('hero', 'Mains d’un médecin en blouse blanche tenant un stéthoscope (photo d’illustration)', sizes='(max-width: 960px) 76vw, 420px', lazy=False)}</div>{PULSE}<figcaption>Médecine générale · photo d'illustration</figcaption></figure></div></section>
<section class="sec" id="cabinet"><div class="w info"><div data-rv><p class="kick">Le cabinet</p><h2>Au rond-point <em>Julia</em>.</h2><p style="font-size:1.12rem;margin-top:1.6rem;max-width:34rem;opacity:.85">Le cabinet du Dr Fethi Boukadida se trouve avenue de la Libération (Ettahrir), face à la banque STB. La fiche Google du cabinet le signale également dans la catégorie des services d'urgence.</p>
<div class="alert"><b>190</b><span>En cas d'urgence vitale, appelez le SAMU au 190.</span></div></div>
<div class="card" data-rv style="--d:.1s"><h3>Fiche</h3><dl class="dl"><div><dt>Médecin</dt><dd>Dr Fethi Boukadida</dd></div><div><dt>Exercice</dt><dd>Médecine générale</dd></div><div><dt>Qualification</dt><dd>{ph()}</dd></div><div><dt>Adresse</dt><dd>{F['addr']}</dd></div></dl></div></div></section>
<section class="sec lamp" id="mg"><div class="w"><p class="kick" data-rv>La médecine générale</p><h2 data-rv>Le médecin de <em>premier recours</em>.</h2><div class="three">{th}</div><p class="note" data-rv style="margin-top:2rem">Présentation générale, à titre informatif.</p></div></section>
<section class="sec"><div class="w nt"><figure data-rv>{M.img('marina', 'Marina de Yasmine Hammamet au crépuscule (photo d’illustration)', sizes='(max-width: 960px) 92vw, 600px')}<figcaption>Hammamet · illustration</figcaption></figure>
<figure data-rv style="--d:.12s">{M.img('sacoche', 'Sacoche de médecin (photo d’illustration)', sizes='(max-width: 960px) 92vw, 600px')}<figcaption>Illustration · ne montre pas le cabinet</figcaption></figure></div></section>
<section class="sec" id="horaires" style="padding-top:0"><div class="w info"><div class="card" data-rv><h3>Horaires</h3>{lux.hours(F)}</div><div class="card" data-rv style="--d:.1s"><h3>Contact</h3>{lux.contacts(F, 'WhatsApp · message au cabinet', msg)}</div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w rdv"><div data-rv><p class="kick">Contact</p><h2>Écrire au <em>cabinet</em>.</h2><p style="margin-top:1.4rem;opacity:.8">Le message s'ouvre dans WhatsApp. Pour une urgence vitale, appelez le 190.</p>
<figure style="margin:2rem 0 0;border-radius:24px;overflow:hidden;max-width:420px" data-rv>{M.img('thermo', 'Thermomètre médical (photo d’illustration)', sizes='420px')}</figure></div>
<div class="card" data-rv style="--d:.1s">{lux.form(F, 'Bonjour Docteur, je souhaite venir consulter au cabinet.', lux.MED_FORM)}</div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Avenue de la <em>Libération</em>.</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F, 'Écrire', '#rdv', 'wa')}'''
    return lux.page(F, 'Dr Fethi Boukadida · Médecin généraliste à Hammamet (démo)', 'Cabinet de médecine générale du Dr Fethi Boukadida, avenue de la Libération, Hammamet : coordonnées et contact.', FONTS, CSS, body, '#0A1230', lux.fav('#FFC857', '#0A1230', 'FB'))
