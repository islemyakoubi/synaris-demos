# Cabinet d'orthoptie Amina Romane (Nabeul) : « échelle de lecture ». Blanc optique, accents spectraux. Hero : lettres géantes d'échelle d'acuité
# (tailles décroissantes, reflet spectral animé), prisme en médaillon, bande du spectre, profession en quatre cartes, formulaire. Epilogue + Public Sans.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Epilogue:wght@300;400;600;700;800;900&family=Public+Sans:wght@300;400;500;600;700'
CSS = '''
:root{--bg:#FFFFFF;--fg:#111318;--acc:#5B3DF5;--onacc:#fff;--line:rgba(17,19,24,.1);--hbg:rgba(255,255,255,.9);--disp:Epilogue,system-ui,sans-serif;--sans:'Public Sans',system-ui,sans-serif;--r:12px;--mapbg:#F1F1F4;--rbg:#111318;
--spec:linear-gradient(90deg,#FF3D57,#FF9F1C,#FFE14D,#2EC4B6,#3A86FF,#8338EC)}
h1,h2,h3{font-weight:800;letter-spacing:-.04em}.brand .mono{width:44px;height:44px;border-radius:12px;background:var(--spec);display:grid;place-items:center;color:#fff;font:900 1.1rem var(--disp)}
.hero{min-height:100svh;display:grid;grid-template-columns:1.1fr .9fr;gap:3rem;align-items:center;padding:8rem 0 3rem}
.chart{font:900 1px/1 var(--disp);text-align:center;margin:0 0 2rem;user-select:none}.chart span{display:block;letter-spacing:.18em;background:linear-gradient(90deg,#111318 40%,#FF3D57,#FFE14D,#2EC4B6,#3A86FF,#8338EC,#111318 60%);background-size:300% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:sheen 8s ease-in-out infinite}
.chart span:nth-child(1){font-size:clamp(6rem,13vw,13rem)}.chart span:nth-child(2){font-size:clamp(3.4rem,7vw,7rem);animation-delay:.3s}.chart span:nth-child(3){font-size:clamp(2rem,4.2vw,4.2rem);animation-delay:.6s}.chart span:nth-child(4){font-size:clamp(1.2rem,2.4vw,2.4rem);animation-delay:.9s}.chart span:nth-child(5){font-size:clamp(.8rem,1.3vw,1.3rem);animation-delay:1.2s}
@keyframes sheen{0%,100%{background-position:100% 0}50%{background-position:0 0}}
.hero h1{font-size:clamp(2.2rem,3.8vw,3.6rem);line-height:1}.lede{opacity:.75;max-width:32rem;margin:1.2rem 0 2rem}.acts{display:flex;gap:1rem;flex-wrap:wrap}
.pr{position:relative;border-radius:36px;overflow:hidden;aspect-ratio:4/5;box-shadow:0 40px 80px rgba(91,61,245,.18)}.pr img{width:100%;height:100%;object-fit:cover}
.pr:after{content:'';position:absolute;left:0;right:0;bottom:0;height:6px;background:var(--spec)}.pr figcaption{position:absolute;left:1rem;top:1rem;background:#fff;border-radius:99px;padding:.35rem .8rem;font-size:.72rem}
.spec{height:140px;position:relative;overflow:hidden}.spec img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.sec{padding:8rem 0}.sec h2{font-size:clamp(2.4rem,5vw,4.8rem);line-height:.98}.sec h2 span{background:var(--spec);-webkit-background-clip:text;background-clip:text;color:transparent}
.four{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin-top:4rem}.four article{border:1px solid var(--line);border-radius:24px;padding:2.2rem 1.8rem;position:relative;overflow:hidden;transition:transform .6s var(--ease),box-shadow .6s}
.four article:before{content:'';position:absolute;left:0;top:0;right:0;height:4px;background:var(--spec);transform:scaleX(0);transform-origin:left;transition:transform .7s var(--ease)}.four article:hover{transform:translateY(-6px);box-shadow:0 30px 60px rgba(17,19,24,.08)}.four article:hover:before{transform:scaleX(1)}
.four svg{width:60px;height:60px;color:var(--acc);margin-bottom:2.2rem}.four h3{font-size:1.4rem;margin-bottom:.5rem}.four p{opacity:.7;margin:0;font-size:.95rem}
.gl{display:grid;grid-template-columns:1fr 1.4fr;gap:1rem}.gl figure{margin:0;border-radius:24px;overflow:hidden;position:relative;min-height:480px;background:#f4f4f6}.gl img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.gl figure:first-child img{object-fit:contain;padding:2rem}
.gl figcaption{position:absolute;left:1rem;bottom:1rem;background:#fff;border-radius:99px;padding:.35rem .8rem;font-size:.72rem;box-shadow:0 4px 20px rgba(0,0,0,.08)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:1rem}.card{border:1px solid var(--line);border-radius:24px;padding:2.6rem}.card h3{font-size:1.7rem;margin-bottom:1.2rem}
.dl{margin:0}.dl div{display:grid;grid-template-columns:10rem 1fr;gap:1rem;padding:.9rem 0;border-bottom:1px solid var(--line)}.dl dt{font:700 .62rem/1.7 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.55}.dl dd{margin:0}
.rdv{background:#111318;color:#fff;border-radius:36px;padding:4.5rem;display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem;--line:rgba(255,255,255,.14);--fln:rgba(255,255,255,.25);--fbg:rgba(255,255,255,.05);--acc:#8C7BFF;position:relative;overflow:hidden}
.rdv:before{content:'';position:absolute;left:0;right:0;top:0;height:6px;background:var(--spec)}.rdv select option{color:#111318}
.mapw{border-radius:24px}
@media(max-width:1020px){.four{grid-template-columns:1fr 1fr}}
@media(max-width:960px){.hero,.gl,.two,.rdv{grid-template-columns:1fr}.pr{aspect-ratio:4/3}.rdv{padding:2.4rem 1.4rem}.gl figure{min-height:340px}}
@media(max-width:760px){.four{grid-template-columns:1fr}.sec{padding:5.5rem 0}.card{padding:1.6rem}.dl div{grid-template-columns:1fr;gap:.1rem}.spec{height:90px}}
'''
def build(F, M):
    msg = 'Bonjour, je souhaite prendre rendez-vous au cabinet d’orthoptie.'
    brand = '<span class="mono">A</span><span><b>Amina Romane</b><small>Orthoptiste · Nabeul</small></span>'
    links = [('L’orthoptie', '#orthoptie'), ('Le cabinet', '#cabinet'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    four = [('eye', 'Bilan orthoptique', 'L’évaluation de la vision binoculaire et de la motricité des yeux.'), ('lens', 'Vision binoculaire', 'La coordination des deux yeux.'), ('prism', 'Rééducation', 'La rééducation orthoptique, par des exercices visuels.'), ('book', 'Basse vision', 'L’accompagnement des personnes malvoyantes.')]
    fh = ''.join(f'<article data-rv style="--d:{i*.1:.1f}s">{IC[k]}<h3>{t}</h3><p>{p}</p></article>' for i, (k, t, p) in enumerate(four))
    body = f'''{lux.header(brand, links)}<main id="main">
<section class="w hero" id="top"><div><p class="chart rise" aria-hidden="true"><span>E</span><span>FP</span><span>TOZ</span><span>LPED</span><span>PECFD</span></p>
<p class="kick rise d1">Cabinet d'orthoptie · Nabeul</p><h1 class="rise d1">Amina Romane, orthoptiste</h1><p class="lede rise d2">Cabinet au 1er étage de l'immeuble Essalama, appartement 208, avenue Habib Thameur, près de Carrefour Market. Séances sur rendez-vous.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Prendre rendez-vous {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div></div>
<figure class="pr rise d2" style="margin:0">{M.img('hero', 'Prisme décomposant la lumière (photo d’illustration)', sizes='(max-width: 960px) 92vw, 520px', lazy=False)}<figcaption>Illustration · prisme</figcaption></figure></section>
<div class="spec" aria-hidden="true">{M.img('spectre', '', sizes='100vw')}</div>
<section class="sec" id="orthoptie"><div class="w"><p class="kick" data-rv>La profession</p><h2 data-rv>L'orthoptie, <span>en quatre points</span>.</h2><div class="four">{fh}</div>
<p class="note" data-rv style="margin-top:2rem">Présentation générale de la profession, à titre informatif. Les prises en charge proposées au cabinet sont {ph()}</p></div></section>
<section class="sec" id="cabinet" style="padding-top:0"><div class="w gl"><figure data-rv>{M.img('echelle', 'Échelle d’acuité visuelle (photo d’illustration)', sizes='(max-width: 960px) 92vw, 480px')}<figcaption>Illustration · échelle de lecture</figcaption></figure>
<figure data-rv style="--d:.12s">{M.img('lunettes', 'Paires de lunettes (photo d’illustration)', sizes='(max-width: 960px) 92vw, 700px')}<figcaption>Illustration · ne montre pas le cabinet</figcaption></figure></div></section>
<section class="sec" id="horaires" style="padding-top:0"><div class="w two"><div class="card" data-rv><h3>Fiche du cabinet</h3><dl class="dl"><div><dt>Praticienne</dt><dd>Amina Romane</dd></div><div><dt>Profession</dt><dd>Orthoptiste</dd></div><div><dt>Diplômes</dt><dd>{ph()}</dd></div><div><dt>Adresse</dt><dd>{F['addr']}</dd></div></dl>
<div style="margin-top:1rem">{lux.contacts(F, wa_msg=msg)}</div></div><div class="card" data-rv style="--d:.1s"><h3>Horaires</h3>{lux.hours(F)}</div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w"><div class="rdv"><div data-rv><p class="kick">Rendez-vous</p><h2 style="color:#fff">Demander un rendez-vous.</h2><p style="margin-top:1.4rem;opacity:.8">Le message s'ouvre dans WhatsApp ; le cabinet confirme le créneau.</p></div>
<div data-rv style="--d:.1s">{lux.form(F, 'Bonjour, je souhaite un rendez-vous au cabinet d’orthoptie.', lux.MED_FORM)}</div></div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Immeuble <span>Essalama</span>.</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F)}'''
    return lux.page(F, 'Cabinet d’orthoptie Amina Romane · Nabeul (démo)', 'Cabinet d’orthoptie d’Amina Romane, immeuble Essalama, avenue Habib Thameur, Nabeul : coordonnées, horaires et demande de rendez-vous.', FONTS, CSS, body, '#FFFFFF', lux.fav('#5B3DF5', '#fff', 'A', 'Arial', 'rect'))
