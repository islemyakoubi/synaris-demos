# Cabinet Meissem Gouddi, kinésithérapie (Nabeul) : « mouvement ». Sable chaud, terre cuite, prune. Titre géant Syne, visuel à masque organique qui respire,
# marquee cinétique en lettres détourées, domaines en rangées extensibles, cartes horaires/contacts, formulaire WhatsApp. Syne + DM Sans. Informatif uniquement.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Syne:wght@500;600;700;800&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,700'
CSS = '''
:root{--bg:#F3E9DC;--fg:#2B1830;--acc:#C4552D;--onacc:#fff;--line:rgba(43,24,48,.14);--hbg:rgba(243,233,220,.88);--disp:Syne,system-ui,sans-serif;--sans:'DM Sans',system-ui,sans-serif;--r:14px;--mapbg:#E8D9C5;--plum:#4A2350;--rbg:#2B1830}
h1,h2,h3{font-weight:700;letter-spacing:-.03em}.brand .mono{width:44px;height:44px;border-radius:14px;display:grid;place-items:center;background:var(--acc);color:#fff;font:800 1rem var(--disp)}
.hero{padding:9rem 0 3rem;display:grid;grid-template-columns:1.25fr .75fr;gap:3rem;align-items:end}
.hero h1{font-size:clamp(3.4rem,9vw,9.6rem);line-height:.86;text-transform:uppercase;font-weight:800}.hero h1 span{display:block}.hero h1 .o{color:transparent;-webkit-text-stroke:2px var(--fg)}
.hero h1 .c{color:var(--acc)}.lede{max-width:34rem;font-size:1.1rem;margin:2rem 0 2.2rem;opacity:.85}.acts{display:flex;gap:1rem;flex-wrap:wrap}
.blob{aspect-ratio:3/4;overflow:hidden;border-radius:58% 42% 46% 54%/48% 56% 44% 52%;animation:morph 14s ease-in-out infinite;box-shadow:0 40px 80px rgba(74,35,80,.25)}
.blob img{width:100%;height:100%;object-fit:cover;filter:saturate(.9)}@keyframes morph{50%{border-radius:42% 58% 60% 40%/58% 40% 60% 42%}}
.hmeta{display:flex;gap:2.4rem;flex-wrap:wrap;margin-top:2.6rem;font-size:.9rem}.hmeta b{display:block;font:700 .62rem/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--acc);margin-bottom:.4rem}
.mq{background:var(--plum);color:#F3E9DC;padding:1.6rem 0;font:800 clamp(2.4rem,5vw,4.6rem)/1 var(--disp);text-transform:uppercase;--mqs:36s}.mq span:nth-child(even){color:transparent;-webkit-text-stroke:1.5px #F3E9DC}
.sec{padding:8rem 0}.sec h2{font-size:clamp(2.4rem,5vw,4.8rem);line-height:.98}
.rows{margin-top:4rem;border-top:2px solid var(--fg)}.row{display:grid;grid-template-columns:5rem 1fr 1.2fr auto;gap:2rem;align-items:center;padding:2.2rem 0;border-bottom:1px solid var(--line);transition:padding .5s var(--ease),background .5s}
.row:hover{padding-left:1.4rem;background:rgba(196,85,45,.07)}.row .n{font:800 1rem var(--disp);color:var(--acc)}.row h3{font-size:clamp(1.6rem,3vw,2.6rem)}.row p{margin:0;opacity:.75}.row .ph{justify-self:start}
.split{display:grid;grid-template-columns:1fr 1fr;gap:1.4rem}.tile{border-radius:28px;overflow:hidden;position:relative;min-height:520px}.tile img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.6s var(--ease)}.tile:hover img{transform:scale(1.05)}
.tile figcaption{position:absolute;left:1.2rem;bottom:1.2rem;background:#F3E9DC;border-radius:99px;padding:.45rem .9rem;font-size:.74rem}
.plum{background:var(--plum);color:#F3E9DC;border-radius:28px;padding:3rem;display:flex;flex-direction:column;justify-content:space-between;--line:rgba(243,233,220,.18);--acc:#F29A6B}
.plum h3{font-size:2.4rem;margin-bottom:1rem}.plum .big{font:800 clamp(2.6rem,5vw,4.4rem)/1 var(--disp);color:#F29A6B}
.grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.4rem}.box{background:#FBF5EC;border-radius:28px;padding:2.4rem;border:1px solid var(--line)}.box h3{font-size:1.8rem;margin-bottom:1.2rem}
.dl{margin:0}.dl div{padding:.9rem 0;border-bottom:1px solid var(--line)}.dl dt{font:700 .62rem/1.6 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.6}.dl dd{margin:0;font-weight:500}
.rdv{display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem}.rdv .box{background:var(--fg);color:#F3E9DC;--line:rgba(243,233,220,.2);--fln:rgba(243,233,220,.3);--fbg:rgba(255,255,255,.05)}.rdv .box select option{color:#2B1830}
.mapw{border-radius:28px}
@media(max-width:960px){.hero{grid-template-columns:1fr}.blob{max-width:420px;aspect-ratio:1}.split,.grid3,.rdv{grid-template-columns:1fr}.row{grid-template-columns:3rem 1fr;gap:.6rem 1rem}.row p,.row .ph{grid-column:2}.row svg{display:none}.tile{min-height:380px}}
@media(max-width:760px){.sec{padding:5.5rem 0}.hero h1 .o{-webkit-text-stroke:1.4px var(--fg)}.box,.plum{padding:1.8rem}}
'''
def build(F, M):
    msg = 'Bonjour, je souhaite prendre rendez-vous au cabinet de kinésithérapie.'
    brand = '<span class="mono">MG</span><span><b>Meissem Gouddi</b><small>Kinésithérapie · Nabeul</small></span>'
    links = [('Domaines', '#domaines'), ('Le cabinet', '#cabinet'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    rows = [('run', 'Kinésithérapie', 'Rééducation par le mouvement et les techniques de kinésithérapie.', 'fiche Google'),
            ('spine', 'Rééducation périnéale', 'Mentionnée sur la fiche publique du cabinet.', 'à confirmer'),
            ('pulse', 'TTNS', 'Technique citée sur le profil professionnel en ligne de la praticienne.', 'à confirmer')]
    rh = ''.join(f'<div class="row" data-rv style="--d:{i*.1:.1f}s"><span class="n">0{i+1}</span><h3>{t}</h3><p>{p}</p>{ph(s)}</div>' for i, (k, t, p, s) in enumerate(rows))
    mq = ''.join(f'<span>{w}</span>' for w in ['Kinésithérapie', 'Nabeul', 'Rééducation', 'Mouvement'] * 2)
    body = f'''{lux.header(brand, links)}<main id="main">
<section class="w hero" id="top"><div><p class="kick rise">Cabinet de kinésithérapie · Nabeul</p><h1 class="rise d1"><span>Kiné</span><span class="o">sithé</span><span class="c">rapie.</span></h1>
<p class="lede rise d2">Le cabinet de Meissem Gouddi, kinésithérapeute, se trouve au 3e étage de l'immeuble Turki, avenue Habib Thameur, près de la Faculté des langues. Séances sur rendez-vous.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Prendre rendez-vous {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div>
<div class="hmeta rise d4"><div><b>Horaire relevé</b>Mercredi, {F['wed']}</div><div><b>Adresse</b>123 av. Habib Thameur</div></div></div>
<div class="blob rise d2">{M.img('hero', 'Plage de Nabeul (photo d’illustration)', sizes='(max-width: 960px) 90vw, 440px', lazy=False)}</div></section>
<div class="mq" aria-hidden="true"><div>{mq}{mq}</div></div>
<section class="sec" id="domaines"><div class="w"><p class="kick" data-rv>Domaines</p><h2 data-rv>Ce que le cabinet<br>propose, d'après ses fiches.</h2><div class="rows">{rh}</div>
<p class="note" data-rv>Liste indicative reprise des informations publiques, à confirmer par la praticienne avant publication.</p></div></section>
<section class="sec" id="cabinet" style="padding-top:0"><div class="w split"><figure class="tile" data-rv>{M.img('salle', 'Appareils de rééducation dans une salle de kinésithérapie (photo d’illustration)', sizes='(max-width: 960px) 92vw, 600px')}<figcaption>Illustration · ne montre pas le cabinet</figcaption></figure>
<div class="plum" data-rv style="--d:.12s"><div><p class="kick">Le cabinet</p><h3>Immeuble Turki, 3e étage.</h3><p>123 avenue Habib Thameur, Nabeul, près de la Faculté des langues.</p></div><div><span class="big">3e</span><p style="margin:.4rem 0 0">étage · accès et ascenseur {ph()}</p></div></div></div></section>
<section class="sec" id="horaires" style="padding-top:0"><div class="w grid3"><div class="box" data-rv><h3>Horaires</h3>{lux.hours(F)}</div>
<div class="box" data-rv style="--d:.1s"><h3>Contact</h3>{lux.contacts(F, wa_msg=msg)}</div>
<div class="box" data-rv style="--d:.2s"><h3>Fiche</h3><dl class="dl"><div><dt>Praticienne</dt><dd>Meissem Gouddi</dd></div><div><dt>Profession</dt><dd>Kinésithérapeute</dd></div><div><dt>Diplômes</dt><dd>{ph()}</dd></div><div><dt>Conventions</dt><dd>{ph()}</dd></div></dl></div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w rdv"><div data-rv><p class="kick">Rendez-vous</p><h2>Réserver une séance.</h2><p style="margin-top:1.4rem;opacity:.8">Le message s'ouvre dans WhatsApp ; le cabinet confirme le créneau.</p></div>
<div class="box" data-rv style="--d:.1s">{lux.form(F, 'Bonjour, je souhaite un rendez-vous au cabinet de kinésithérapie.', lux.MED_FORM)}</div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><figure class="tile" data-rv style="min-height:300px;margin:0 0 3rem">{M.img('mer', 'Front de mer de Nabeul (photo d’illustration)', sizes='100vw')}<figcaption>Nabeul · illustration</figcaption></figure>
<p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Avenue Habib Thameur.</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F)}'''
    return lux.page(F, 'Cabinet Meissem Gouddi · Kinésithérapie à Nabeul (démo)', 'Cabinet de kinésithérapie de Meissem Gouddi, avenue Habib Thameur, Nabeul : coordonnées, horaires et demande de rendez-vous.', FONTS, CSS, body, '#F3E9DC', lux.fav('#C4552D', '#fff', 'MG', 'Arial', 'rect'))
