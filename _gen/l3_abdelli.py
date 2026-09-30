# Auto-école Anis Abdelli (Hammamet) : « tableau de bord de nuit ». Bleu nuit, cyan néon, ambre compteur. Hero HUD : compteur SVG dont l'aiguille balaie,
# panneaux vitrés d'informations, photo du tableau de bord en fond, étapes en voyants, rétroviseur, formulaire. Chakra Petch + Albert Sans.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Chakra+Petch:wght@400;500;600;700&family=Albert+Sans:wght@300;400;500;600;700'
CSS = '''
:root{--bg:#070C1F;--fg:#E8F1FF;--acc:#3CF2FF;--onacc:#04101E;--line:rgba(60,242,255,.16);--hbg:rgba(7,12,31,.86);--disp:'Chakra Petch',system-ui,sans-serif;--sans:'Albert Sans',system-ui,sans-serif;--r:6px;--amb:#FF9F3A;--mapbg:#0D1530;--fbg:rgba(60,242,255,.04)}
h1,h2,h3{font-weight:600;letter-spacing:-.01em;text-transform:uppercase}.brand .mono{width:44px;height:44px;border:1px solid var(--acc);border-radius:6px;display:grid;place-items:center;color:var(--acc);font:700 1rem var(--disp);box-shadow:0 0 18px rgba(60,242,255,.35),inset 0 0 12px rgba(60,242,255,.2)}
.hero{position:relative;min-height:100svh;display:flex;align-items:center;overflow:hidden;isolation:isolate}.hero .px{opacity:.4;filter:blur(1px) saturate(1.2)}
.hero:after{content:'';position:absolute;inset:0;z-index:-1;background:radial-gradient(ellipse at 70% 50%,transparent,rgba(7,12,31,.92) 70%),linear-gradient(0deg,var(--bg),transparent 30%)}
.hg{display:grid;grid-template-columns:1.1fr .9fr;gap:3rem;align-items:center;padding:9rem 0 4rem}
.hero h1{font-size:clamp(3rem,7.4vw,7.4rem);line-height:.9;text-shadow:0 0 40px rgba(60,242,255,.25)}.hero h1 span{display:block;color:var(--acc)}.lede{max-width:32rem;opacity:.8;margin:1.8rem 0 2.2rem;font-size:1.06rem}.acts{display:flex;gap:1rem;flex-wrap:wrap}
.btn.p{box-shadow:0 0 30px rgba(60,242,255,.35)}
.gauge{position:relative;width:min(480px,100%);justify-self:center}.gauge svg{width:100%;height:auto;overflow:visible}.gauge .nd{transform-origin:200px 200px;animation:sweep 5s cubic-bezier(.6,0,.3,1) infinite alternate}@keyframes sweep{from{transform:rotate(-120deg)}to{transform:rotate(60deg)}}
.gauge .rd{position:absolute;left:0;right:0;top:56%;text-align:center;font:600 .74rem var(--disp);letter-spacing:.3em;color:var(--amb)}
.hud{display:grid;grid-template-columns:repeat(3,1fr);gap:.8rem;margin-top:1.4rem}.hud div{border:1px solid var(--line);background:rgba(60,242,255,.05);backdrop-filter:blur(8px);border-radius:6px;padding:.9rem 1rem;font-size:.86rem}.hud small{display:block;font:600 .6rem/1 var(--disp);letter-spacing:.24em;color:var(--acc);margin-bottom:.4rem;text-transform:uppercase}
.sec{padding:8rem 0}.sec h2{font-size:clamp(2.6rem,5.6vw,5.4rem);line-height:.92}
.lights{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin-top:4rem}.lights article{border:1px solid var(--line);border-radius:10px;padding:2rem 1.6rem;background:linear-gradient(180deg,rgba(60,242,255,.06),transparent);position:relative}
.lights i{display:block;width:14px;height:14px;border-radius:50%;background:var(--acc);box-shadow:0 0 16px var(--acc);margin-bottom:2.6rem;animation:blink 2.4s infinite}.lights article:nth-child(2) i{animation-delay:.6s}.lights article:nth-child(3) i{animation-delay:1.2s}.lights article:nth-child(4) i{animation-delay:1.8s;background:var(--amb);box-shadow:0 0 16px var(--amb)}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.25}}.lights b{font:600 .72rem var(--disp);letter-spacing:.24em;color:var(--acc)}.lights h3{font-size:1.5rem;margin:.4rem 0 .5rem}.lights p{opacity:.72;margin:0}
.mir{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center}.mir figure{margin:0;border-radius:999px 999px 999px 999px/340px 340px 340px 340px;overflow:hidden;aspect-ratio:2.1/1;border:10px solid #1A2240;box-shadow:0 30px 70px rgba(0,0,0,.5),0 0 0 1px var(--line)}.mir img{width:100%;height:100%;object-fit:cover}
.dl{margin:1.6rem 0 0}.dl div{display:grid;grid-template-columns:10rem 1fr;gap:1rem;padding:.9rem 0;border-bottom:1px solid var(--line)}.dl dt{font:600 .62rem/1.7 var(--disp);letter-spacing:.2em;text-transform:uppercase;color:var(--acc)}.dl dd{margin:0}
.duo{display:grid;grid-template-columns:1fr 1fr;gap:1rem}.duo figure{margin:0;position:relative;overflow:hidden;border-radius:10px;min-height:380px}.duo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.duo figcaption{position:absolute;left:.8rem;bottom:.8rem;background:rgba(7,12,31,.75);border:1px solid var(--line);border-radius:4px;padding:.3rem .6rem;font-size:.7rem}
.info{display:grid;grid-template-columns:1fr 1fr;gap:1rem}.card{border:1px solid var(--line);border-radius:10px;padding:2.4rem;background:rgba(60,242,255,.03)}.card h3{font-size:1.6rem;margin-bottom:1rem;color:var(--acc)}
.rdv{display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem}.form select option{color:#070C1F}
.mapw{border-radius:10px;border:1px solid var(--line)}
@media(max-width:960px){.hg,.mir,.info,.rdv,.duo{grid-template-columns:1fr}.gauge{width:min(360px,86%)}.lights{grid-template-columns:1fr 1fr}}
@media(max-width:760px){.sec{padding:5.5rem 0}.hud{grid-template-columns:1fr}.lights{grid-template-columns:1fr}.card{padding:1.6rem}.dl div{grid-template-columns:1fr;gap:.1rem}.duo figure{min-height:280px}}
'''
def gauge():
    t = ''
    for i in range(0, 25):
        a = -120 + i * 7.5; big = i % 4 == 0
        t += f'<line x1="200" y1="{38 if big else 46}" x2="200" y2="62" transform="rotate({a} 200 200)" stroke="{"#3CF2FF" if i < 19 else "#FF9F3A"}" stroke-width="{3 if big else 1.4}"/>'
    return (f'<svg viewBox="0 0 400 400" aria-hidden="true"><circle cx="200" cy="200" r="170" fill="none" stroke="rgba(60,242,255,.12)" stroke-width="1"/>'
            f'<path d="M 52.8 285 A 170 170 0 1 1 347.2 285" fill="none" stroke="rgba(60,242,255,.35)" stroke-width="2" stroke-dasharray="2 6"/>{t}'
            f'<g class="nd"><line x1="200" y1="200" x2="200" y2="70" stroke="#FF9F3A" stroke-width="4" stroke-linecap="round"/><circle cx="200" cy="200" r="12" fill="#070C1F" stroke="#FF9F3A" stroke-width="3"/></g></svg>')
NOTE = "Démo : aucune donnée n'est enregistrée. Le bouton ouvre WhatsApp avec votre message ; l'auto-école vous répond directement."
def build(F, M):
    msg = 'Bonjour, je souhaite des informations pour passer le permis avec l’auto-école Anis Abdelli.'
    brand = '<span class="mono">AA</span><span><b>Auto-école Anis Abdelli</b><small>Hammamet</small></span>'
    links = [('Parcours', '#parcours'), ('L’école', '#ecole'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    L = [('Inscription', 'Au bureau, rue Chedly Mrad.'), ('Code', 'Règles de circulation et signalisation.'), ('Conduite', 'Leçons pratiques avec un moniteur.'), ('Examen', 'Passage des épreuves du permis.')]
    lh = ''.join(f'<article data-rv style="--d:{i*.1:.1f}s"><i></i><b>0{i+1}</b><h3>{t}</h3><p>{p}</p></article>' for i, (t, p) in enumerate(L))
    spec = [('text', 'Nom et prénom'), ('tel', 'Téléphone'), ('full', 'Permis souhaité'), ('textarea', 'Message (facultatif)')]
    body = f'''{lux.header(brand, links, ('S’inscrire', '#rdv'))}<main id="main">
<section class="hero" id="top"><div class="pxw">{M.img('hero', 'Tableau de bord éclairé (photo d’illustration)', cls='px', sizes='100vw', lazy=False, extra=' data-px=".1"')}</div>
<div class="w hg"><div><p class="kick rise">Auto-école · Hammamet</p><h1 class="rise d1">Anis<span>Abdelli</span></h1><p class="lede rise d2">Auto-école rue Chedly Mrad, à Hammamet. Code, conduite et inscriptions : renseignez-vous directement auprès de l'école.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Se renseigner {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div>
<div class="hud rise d4"><div><small>Mercredi</small>{F['wed']}</div><div><small>Adresse</small>Rue Chedly Mrad</div><div><small>Téléphone</small>{F['tel']}</div></div></div>
<div class="gauge rise d2">{gauge()}<div class="rd">Hammamet</div></div></div></section>
<section class="sec" id="parcours"><div class="w"><p class="kick" data-rv>Le parcours</p><h2 data-rv>Quatre voyants<br>au vert.</h2><div class="lights">{lh}</div>
<p class="note" data-rv style="margin-top:2rem">Étapes générales du permis de conduire. Catégories, tarifs et calendrier : {ph()}</p></div></section>
<section class="sec" id="ecole" style="padding-top:0"><div class="w mir"><figure data-rv="s">{M.img('retro', 'Rétroviseur intérieur (photo d’illustration)', sizes='(max-width: 960px) 92vw, 600px')}</figure>
<div data-rv><p class="kick">L'école</p><h2>Rue Chedly Mrad.</h2><dl class="dl"><div><dt>Auto-école</dt><dd>Anis Abdelli</dd></div><div><dt>Adresse</dt><dd>{F['addr']}</dd></div><div><dt>Catégories</dt><dd>{ph()}</dd></div><div><dt>Site web</dt><dd>{ph('aucun site officiel identifié')}</dd></div></dl></div></div></section>
<section class="sec" style="padding-top:0"><div class="w duo"><figure data-rv>{M.img('rondpoint', 'Rond-point en Tunisie (photo d’illustration)', sizes='(max-width: 960px) 92vw, 600px')}<figcaption>Illustration · ne montre pas l'école</figcaption></figure>
<figure data-rv style="--d:.12s">{M.img('tableau', 'Volant et tableau de bord (photo d’illustration)', sizes='(max-width: 960px) 92vw, 600px')}<figcaption>Illustration</figcaption></figure></div></section>
<section class="sec" id="horaires" style="padding-top:0"><div class="w info"><div class="card" data-rv><h3>Horaires</h3>{lux.hours(F)}</div><div class="card" data-rv style="--d:.1s"><h3>Contact</h3>{lux.contacts(F, 'WhatsApp · renseignements', msg)}</div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w rdv"><div data-rv><p class="kick">Inscription</p><h2>Se renseigner.</h2><p style="margin-top:1.4rem;opacity:.8">Indiquez le permis qui vous intéresse : le message s'ouvre dans WhatsApp.</p></div>
<div class="card" data-rv style="--d:.1s">{lux.form(F, 'Bonjour, je souhaite des informations pour le permis.', spec, 'Envoyer la demande', NOTE)}</div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Hammamet.</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F, 'Écrire', '#rdv', 'wa')}'''
    return lux.page(F, 'Auto-école Anis Abdelli · Hammamet (démo)', 'Auto-école Anis Abdelli, rue Chedly Mrad, Hammamet : contact, horaires et demande d’inscription.', FONTS, CSS, body, '#070C1F', lux.fav('#070C1F', '#3CF2FF', 'AA', 'Arial', 'rect'))
