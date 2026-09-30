# Dr Mohamed Khelif, ophtalmologue (Grombalia) : « iris ». Noir profond, dégradé ambre/sarcelle de l'iris. Hero : iris en médaillon qui « respire »,
# anneaux gradués en rotation (bague d'objectif), grands titres Sora, spécialité en 3 cercles, diptyque instruments, rendez-vous sur fond d'éclipse. Sora + Hanken Grotesk.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Sora:wght@300;400;500;600;700&family=Hanken+Grotesk:wght@300;400;500;600;700'
CSS = '''
:root{--bg:#07080A;--fg:#EEF0EE;--acc:#F2B25C;--onacc:#07080A;--line:rgba(238,240,238,.12);--hbg:rgba(7,8,10,.86);--disp:Sora,system-ui,sans-serif;--sans:'Hanken Grotesk',system-ui,sans-serif;--r:999px;--tl:#3FB6A8;--mapbg:#111417;--fbg:rgba(255,255,255,.04)}
h1,h2,h3{font-weight:300;letter-spacing:-.04em}.grad{background:linear-gradient(100deg,var(--acc),#E88A3A 40%,var(--tl));-webkit-background-clip:text;background-clip:text;color:transparent}
.brand .mono{width:44px;height:44px;border-radius:50%;background:conic-gradient(from 0deg,var(--acc),var(--tl),var(--acc));display:grid;place-items:center}.brand .mono i{width:16px;height:16px;border-radius:50%;background:#07080A}
.hero{min-height:100svh;display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:2rem;padding:8rem 0 3rem;position:relative}
.hero h1{font-size:clamp(3.2rem,7vw,7rem);line-height:.95}.hero h1 span{display:block}.lede{max-width:31rem;font-size:1.08rem;opacity:.78;margin:2rem 0 2.4rem}.acts{display:flex;gap:1rem;flex-wrap:wrap}
.eye{position:relative;aspect-ratio:1;width:min(600px,100%);justify-self:center}.eye .m{position:absolute;inset:16%;border-radius:50%;overflow:hidden;box-shadow:0 0 120px rgba(242,178,92,.25)}
.eye .m img{width:100%;height:100%;object-fit:cover;animation:breathe 7s ease-in-out infinite}@keyframes breathe{50%{transform:scale(1.12)}}
.eye svg.ring{position:absolute;inset:0;width:100%;height:100%;animation:spin 80s linear infinite;color:rgba(238,240,238,.4)}.eye svg.ring.r2{inset:6%;width:88%;height:88%;animation-direction:reverse;animation-duration:50s;color:var(--acc)}@keyframes spin{to{transform:rotate(360deg)}}
.hmeta{display:grid;grid-template-columns:repeat(3,auto);gap:2.4rem;margin-top:3rem;justify-content:start}.hmeta small{display:block;font:600 .62rem/1 var(--sans);letter-spacing:.22em;text-transform:uppercase;opacity:.55;margin-bottom:.5rem}.hmeta p{margin:0;font:400 1rem var(--disp)}
.sec{padding:8rem 0}.sec h2{font-size:clamp(2.4rem,5vw,4.8rem);line-height:1}
.circles{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem;margin-top:4.5rem}.circles article{aspect-ratio:1;border-radius:50%;border:1px solid var(--line);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:2.8rem;transition:border-color .6s,background .6s;position:relative}
.circles article:hover{border-color:var(--acc);background:radial-gradient(circle,rgba(242,178,92,.1),transparent 70%)}.circles svg{width:64px;height:64px;color:var(--acc);margin-bottom:1.4rem}.circles h3{font-size:1.7rem;margin-bottom:.5rem}.circles p{opacity:.7;margin:0;font-size:.93rem;max-width:16rem}
.dip{display:grid;grid-template-columns:1.3fr 1fr;gap:1.2rem}.dip figure{margin:0;position:relative;overflow:hidden;border-radius:28px;min-height:520px}.dip img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.6s var(--ease)}.dip figure:hover img{transform:scale(1.05)}
.dip figcaption{position:absolute;left:1rem;bottom:1rem;background:rgba(7,8,10,.7);backdrop-filter:blur(6px);border-radius:99px;padding:.4rem .8rem;font-size:.72rem}
.info{display:grid;grid-template-columns:1fr 1fr;gap:1.4rem}.card{border:1px solid var(--line);border-radius:28px;padding:2.6rem;background:linear-gradient(160deg,rgba(255,255,255,.04),rgba(255,255,255,.01))}.card h3{font-size:1.8rem;margin-bottom:1.2rem}
.dl{margin:0}.dl div{display:grid;grid-template-columns:10rem 1fr;gap:1rem;padding:.9rem 0;border-bottom:1px solid var(--line)}.dl dt{font:600 .62rem/1.7 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.55}.dl dd{margin:0}
.rdvw{position:relative;overflow:hidden;isolation:isolate}.rdvw:before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,var(--bg) 35%,rgba(7,8,10,.6));z-index:-1}
.rdv{display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem}.rdv .card{background:rgba(7,8,10,.72);backdrop-filter:blur(10px)}.form select option{color:#07080A}.form button{border-radius:999px}
.mapw{border-radius:28px}
@media(max-width:960px){.hero{grid-template-columns:1fr;padding-top:7.5rem}.eye{width:min(440px,92%);order:-1}.circles{grid-template-columns:1fr;max-width:380px;margin-inline:auto}.dip,.info,.rdv{grid-template-columns:1fr}.dip figure{min-height:380px}}
@media(max-width:760px){.sec{padding:5.5rem 0}.hmeta{grid-template-columns:1fr 1fr;gap:1.4rem}.card{padding:1.6rem}.dl div{grid-template-columns:1fr;gap:.1rem}}
'''
def ring(n=120, r=46, cls='ring'):
    t = ''.join(f'<line x1="50" y1="{50-r}" x2="50" y2="{50-r+(2.6 if i%10==0 else 1.2)}" transform="rotate({i*360/n:.2f} 50 50)"/>' for i in range(n))
    return f'<svg class="{cls}" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width=".25" aria-hidden="true"><circle cx="50" cy="50" r="{r+3}" stroke-width=".15"/>{t}</svg>'
def build(F, M):
    msg = 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet d’ophtalmologie.'
    brand = '<span class="mono"><i></i></span><span><b>Dr Mohamed Khelif</b><small>Ophtalmologie · Grombalia</small></span>'
    links = [('Spécialité', '#specialite'), ('Le cabinet', '#cabinet'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    ci = [('eye', 'La vision', 'L’acuité visuelle et les troubles de la réfraction.'), ('lens', 'L’avant de l’œil', 'Paupières, cornée, cristallin.'), ('prism', 'Le fond d’œil', 'La rétine et le nerf optique.')]
    cih = ''.join(f'<article data-rv="s" style="--d:{i*.12:.2f}s">{IC[k]}<h3>{t}</h3><p>{p}</p></article>' for i, (k, t, p) in enumerate(ci))
    body = f'''{lux.header(brand, links)}<main id="main">
<section class="w hero" id="top"><div><p class="kick rise">Ophtalmologie · Grombalia</p><h1 class="rise d1"><span>Dr Mohamed</span><span class="grad">Khelif</span></h1>
<p class="lede rise d2">Cabinet d'ophtalmologie au 6e étage du Centre Hermès Médical, avenue Habib Bourguiba, en face de Carrefour Market. Consultations sur rendez-vous.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Prendre rendez-vous {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div>
<div class="hmeta rise d4"><div><small>Mercredi</small><p>{F['wed']}</p></div><div><small>Étage</small><p>6e · Hermès Médical</p></div><div><small>Ville</small><p>Grombalia</p></div></div></div>
<div class="eye rise d1">{ring()}{ring(72, 44, 'ring r2')}<div class="m">{M.img('hero', 'Iris d’un œil humain en gros plan (photo d’illustration)', sizes='(max-width: 960px) 70vw, 400px', lazy=False)}</div></div></section>
<section class="sec" id="specialite"><div class="w" style="text-align:center"><p class="kick" data-rv style="justify-content:center">La spécialité</p><h2 data-rv>L'ophtalmologie, <span class="grad">en trois regards</span>.</h2><div class="circles">{cih}</div>
<p class="note" data-rv style="margin-top:2.4rem">Présentation générale de la spécialité, à titre informatif. Examens et actes réalisés au cabinet : {ph()}</p></div></section>
<section class="sec" id="cabinet" style="padding-top:0"><div class="w dip"><figure data-rv>{M.img('refracteur', 'Réfracteur d’ophtalmologie (photo d’illustration)', sizes='(max-width: 960px) 92vw, 700px')}<figcaption>Illustration · ne montre pas le cabinet</figcaption></figure>
<figure data-rv style="--d:.12s">{M.img('lampe', 'Lampe à fente (photo d’illustration)', sizes='(max-width: 960px) 92vw, 520px')}<figcaption>Illustration · lampe à fente</figcaption></figure></div></section>
<section class="sec" id="horaires" style="padding-top:0"><div class="w info"><div class="card" data-rv><h3>Fiche du cabinet</h3><dl class="dl"><div><dt>Médecin</dt><dd>Dr Mohamed Khelif</dd></div><div><dt>Spécialité</dt><dd>Ophtalmologie</dd></div><div><dt>Qualification</dt><dd>{ph()}</dd></div><div><dt>Adresse</dt><dd>{F['addr']}</dd></div></dl>
<div style="margin-top:1rem">{lux.contacts(F, wa_msg=msg)}</div></div><div class="card" data-rv style="--d:.12s"><h3>Horaires</h3>{lux.hours(F)}</div></div></section>
<section class="sec rdvw" id="rdv"><div class="pxw">{M.img('eclipse', 'Iris en gros plan (photo d’illustration)', cls='px', sizes='100vw', extra=' data-px=".12" style="opacity:.55"')}</div><div class="w rdv"><div data-rv><p class="kick">Rendez-vous</p><h2>Demander un <span class="grad">rendez-vous</span></h2><p style="margin-top:1.4rem;opacity:.8">Le message s'ouvre dans WhatsApp ; le cabinet confirme le créneau.</p></div>
<div class="card" data-rv style="--d:.1s">{lux.form(F, 'Bonjour Docteur, je souhaite un rendez-vous au cabinet d’ophtalmologie.', lux.MED_FORM)}</div></div></section>
<section class="sec" id="acces" style="padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Centre Hermès Médical.</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F)}'''
    return lux.page(F, 'Dr Mohamed Khelif · Ophtalmologue à Grombalia (démo)', 'Cabinet d’ophtalmologie du Dr Mohamed Khelif, Centre Hermès Médical, Grombalia : coordonnées, horaires et demande de rendez-vous.', FONTS, CSS, body, '#07080A', lux.fav('#07080A', '#F2B25C', 'MK', 'Arial'))
