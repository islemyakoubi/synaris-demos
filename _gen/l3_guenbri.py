# Dr Salah Guenbri, médecin généraliste (Hammamet) : « lumière du matin ». Sauge, crème, terre cuite. Hero en écran scindé (photo plein cadre en parallaxe / panneau crème),
# chiffres-clés du cabinet, présentation générale, mosaïque médina, horaires prudents (sources contradictoires), formulaire. Young Serif + Instrument Sans.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Young+Serif&family=Instrument+Sans:wght@400;500;600;700'
CSS = '''
:root{--bg:#F4EFE4;--fg:#233127;--acc:#B85A36;--onacc:#fff;--line:rgba(35,49,39,.14);--hbg:rgba(244,239,228,.9);--disp:'Young Serif',Georgia,serif;--sans:'Instrument Sans',system-ui,sans-serif;--r:10px;--sage:#7E9B84;--mapbg:#E6E0D0;--rbg:#233127}
em{font-style:normal;color:var(--acc)}.brand .mono{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;background:var(--sage);color:#fff;font:400 1rem var(--disp)}
.hero{display:grid;grid-template-columns:1fr 1fr;min-height:100svh}.hl{position:relative;overflow:hidden;isolation:isolate;min-height:60vh}.hl .pxw{z-index:0}.hl:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(35,49,39,.25),transparent 40%)}
.hr{display:flex;flex-direction:column;justify-content:center;padding:9rem clamp(1.5rem,5vw,5rem) 4rem}
.hero h1{font-size:clamp(3rem,6.2vw,6.4rem);line-height:.98;letter-spacing:-.02em}.lede{font-size:1.1rem;max-width:30rem;margin:1.8rem 0 2.2rem;opacity:.82}.acts{display:flex;gap:1rem;flex-wrap:wrap}
.chips{display:flex;gap:.6rem;flex-wrap:wrap;margin-top:2.4rem}.chips span{border:1px solid var(--line);border-radius:99px;padding:.5rem .9rem;font-size:.84rem;background:#fff}
.sec{padding:8rem 0}.sec h2{font-size:clamp(2.3rem,4.4vw,4.2rem);letter-spacing:-.015em}
.sage{background:var(--sage);color:#fff;--line:rgba(255,255,255,.28)}.sage .kick{color:#fff}.sage em{color:#FFE2CF}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem;margin-top:4rem}.three article{background:rgba(255,255,255,.12);border:1px solid var(--line);border-radius:22px;padding:2.4rem 2rem;transition:background .5s,transform .6s var(--ease)}
.three article:hover{background:rgba(255,255,255,.2);transform:translateY(-6px)}.three svg{width:64px;height:64px;margin-bottom:2rem}.three h3{font-size:1.6rem;margin-bottom:.6rem}.three p{margin:0;opacity:.88}
.mos{display:grid;grid-template-columns:.8fr 1.2fr;gap:1.2rem;align-items:stretch}.mos .t{display:grid;grid-template-rows:1fr 1fr;gap:1.2rem}.mos figure{margin:0;border-radius:22px;overflow:hidden;position:relative;min-height:260px}
.mos img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.4s var(--ease)}.mos figure:hover img{transform:scale(1.05)}.mos figcaption{position:absolute;left:1rem;bottom:1rem;background:var(--bg);border-radius:99px;padding:.35rem .8rem;font-size:.72rem}
.mos .big{min-height:640px}
.info{display:grid;grid-template-columns:1.1fr .9fr;gap:1.4rem}.card{background:#fff;border-radius:22px;padding:2.6rem;border:1px solid var(--line)}.card h3{font-size:1.8rem;margin-bottom:1.2rem}
.dl{margin:0}.dl div{display:grid;grid-template-columns:10rem 1fr;gap:1rem;padding:.9rem 0;border-bottom:1px solid var(--line)}.dl dt{font:600 .62rem/1.7 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.6}.dl dd{margin:0}
.warn{display:flex;gap:.8rem;background:#FBEADF;border-radius:14px;padding:1rem 1.2rem;margin-top:1.2rem;font-size:.86rem}.warn svg{width:22px;height:22px;flex:none;color:var(--acc)}
.rdv{background:var(--fg);color:#F4EFE4;border-radius:28px;padding:4.5rem;display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem;--line:rgba(244,239,228,.18);--fln:rgba(244,239,228,.3);--fbg:rgba(255,255,255,.05)}.rdv select option{color:#233127}.rdv em{color:#F2B391}
.mapw{border-radius:22px}
@media(max-width:960px){.hero{grid-template-columns:1fr}.hl{min-height:56vh;order:2}.hr{padding-top:8rem}.three,.info,.rdv,.mos{grid-template-columns:1fr}.mos .big{min-height:420px}.rdv{padding:2.4rem 1.4rem}}
@media(max-width:760px){.sec{padding:5.5rem 0}.card{padding:1.6rem}.dl div{grid-template-columns:1fr;gap:.1rem}.hl{min-height:44vh}}
'''
def build(F, M):
    msg = 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet.'
    brand = '<span class="mono">SG</span><span><b>Dr Salah Guenbri</b><small>Médecine générale · Hammamet</small></span>'
    links = [('Le cabinet', '#cabinet'), ('Médecine générale', '#mg'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    three = [('steth', 'Consultation', 'Consultation de médecine générale au cabinet, sur rendez-vous.'), ('doc', 'Suivi', 'Le médecin généraliste assure le suivi de ses patients dans la durée.'), ('arrow2', 'Orientation', 'Si nécessaire, il oriente vers un médecin spécialiste.')]
    IC2 = dict(IC, arrow2=IC['shield'])
    th = ''.join(f'<article data-rv style="--d:{i*.12:.2f}s">{IC2[k]}<h3>{t}</h3><p>{p}</p></article>' for i, (k, t, p) in enumerate(three))
    body = f'''{lux.header(brand, links)}<main id="main">
<section class="hero" id="top"><div class="hl"><div class="pxw">{M.img('hero', 'Stéthoscope et carnet sur un bureau, lumière du matin (photo d’illustration)', cls='px', sizes='(max-width: 960px) 100vw, 50vw', lazy=False, extra=' data-px=".12"')}</div></div>
<div class="hr"><p class="kick rise">Médecin généraliste · Hammamet</p><h1 class="rise d1">Dr Salah <em>Guenbri</em></h1>
<p class="lede rise d2">Cabinet de médecine générale avenue de la Libération (Ettahrir), à côté de la banque STB, à Hammamet. Consultations sur rendez-vous.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Prendre rendez-vous {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div>
<div class="chips rise d4"><span>Mercredi : {F['wed']}</span><span>Av. de la Libération</span><span>Hammamet</span></div></div></section>
<section class="sec" id="cabinet"><div class="w info"><div data-rv><p class="kick">Le cabinet</p><h2>Au centre de <em>Hammamet</em>.</h2>
<p style="font-size:1.15rem;margin-top:1.6rem;max-width:34rem">Le cabinet du Dr Salah Guenbri se trouve avenue de la Libération, au rez-de-chaussée, à côté de la banque STB. Il est joignable sur deux numéros de téléphone et via WhatsApp.</p></div>
<div class="card" data-rv style="--d:.1s"><h3>Fiche</h3><dl class="dl"><div><dt>Médecin</dt><dd>Dr Salah Guenbri</dd></div><div><dt>Exercice</dt><dd>Médecine générale</dd></div><div><dt>Qualification</dt><dd>{ph()}</dd></div><div><dt>Adresse</dt><dd>{F['addr']}</dd></div></dl></div></div></section>
<section class="sec sage" id="mg"><div class="w"><p class="kick" data-rv>La médecine générale</p><h2 data-rv>Le médecin de <em>premier recours</em>.</h2><div class="three">{th}</div>
<p class="note" data-rv style="margin-top:2rem">Présentation générale de la médecine générale, à titre informatif.</p></div></section>
<section class="sec"><div class="w mos"><div class="t"><figure data-rv>{M.img('minaret', 'Minaret de Hammamet (photo d’illustration)', sizes='(max-width: 960px) 92vw, 480px')}<figcaption>Hammamet · illustration</figcaption></figure>
<figure data-rv style="--d:.1s">{M.img('porte', 'Médina de Hammamet au bord de la mer (photo d’illustration)', sizes='(max-width: 960px) 92vw, 480px')}<figcaption>Médina · illustration</figcaption></figure></div>
<figure class="big" data-rv style="--d:.15s">{M.img('ruelle', 'Ruelle de la médina de Hammamet (photo d’illustration)', sizes='(max-width: 960px) 92vw, 720px')}<figcaption>Ruelle de la médina · illustration, ne montre pas le cabinet</figcaption></figure></div></section>
<section class="sec" id="horaires" style="padding-top:0"><div class="w info"><div class="card" data-rv><h3>Horaires</h3>{lux.hours(F)}<div class="warn">{K.I['clock']}<span>Les horaires publiés diffèrent selon les sources en ligne : seul l'horaire du mercredi relevé sur Google est affiché, le reste est à confirmer par le cabinet.</span></div></div>
<div class="card" data-rv style="--d:.1s"><h3>Contact</h3>{lux.contacts(F, wa_msg=msg, extra=[('Facebook', f'<a href="{F["fb"]}" target="_blank" rel="noopener">facebook.com/DocGuenbri</a>')])}</div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w"><div class="rdv"><div data-rv><p class="kick" style="color:#F2B391">Rendez-vous</p><h2>Demander un <em>rendez-vous</em></h2><p style="margin-top:1.4rem;opacity:.8">Le message s'ouvre dans WhatsApp ; le cabinet confirme le créneau.</p></div>
<div data-rv style="--d:.1s">{lux.form(F, 'Bonjour Docteur, je souhaite un rendez-vous au cabinet.', lux.MED_FORM)}</div></div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Avenue de la Libération.</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F)}'''
    return lux.page(F, 'Dr Salah Guenbri · Médecin généraliste à Hammamet (démo)', 'Cabinet de médecine générale du Dr Salah Guenbri, avenue de la Libération, Hammamet : coordonnées, horaires et demande de rendez-vous.', FONTS, CSS, body, '#F4EFE4', lux.fav('#7E9B84', '#fff', 'SG'))
