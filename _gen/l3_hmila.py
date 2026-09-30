# Dr Asma Hmila, gynécologue-obstétricienne (Nabeul) : « maternité ». Rose poudré, aubergine, or. Hero scindé : titre DM Serif très grand à gauche,
# grand médaillon cerclé d'or (grossesse, mains en cœur) à droite ; pieds de nouveau-né ; actes publiés en deux colonnes ; bandeau échographie en parallaxe ; fiche, horaires, rendez-vous. DM Serif Display + Figtree.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=DM+Serif+Display:ital@0;1&family=Figtree:wght@300;400;500;600;700'
CSS = '''
:root{--bg:#FBF3F1;--fg:#3A1631;--acc:#8E2F63;--onacc:#fff;--line:rgba(58,22,49,.13);--hbg:rgba(251,243,241,.88);--disp:'DM Serif Display',Georgia,serif;--sans:Figtree,system-ui,sans-serif;--r:999px;--gold:#B8894A;--mapbg:#F1E2DE;--rbg:#3A1631}
em{font-style:italic;color:var(--acc)}.brand .mono{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;border:1px solid var(--gold);color:var(--gold);font:italic 400 1.1rem var(--disp)}
.hero{position:relative;min-height:100svh;display:flex;align-items:center;overflow:hidden;isolation:isolate;background:radial-gradient(60% 70% at 78% 45%,#F4DCDF 0,rgba(244,220,223,0) 70%),#FBF3F1}
.hin{padding:9rem 0 5rem;display:grid;grid-template-columns:1.05fr .95fr;gap:4rem;align-items:center}.hero h1{font-size:clamp(3.4rem,7vw,7.4rem);line-height:.92;letter-spacing:-.015em}.hero h1 span{display:block}
.hcirc{position:relative;margin:0;justify-self:center;width:min(40vw,560px)}.hcirc .i{border-radius:50%;overflow:hidden;aspect-ratio:1;box-shadow:0 40px 90px rgba(58,22,49,.18)}.hcirc img{width:100%;height:100%;object-fit:cover;object-position:50% 55%}
.hcirc:before{content:'';position:absolute;inset:-22px;border:1px solid var(--gold);border-radius:50%}.hcirc:after{content:'';position:absolute;width:14px;height:14px;border-radius:50%;background:var(--gold);top:50%;left:-29px;transform:translateY(-50%)}.hcirc figcaption{text-align:center;font-size:.72rem;opacity:.6;margin-top:1.8rem}
.lede{max-width:31rem;font-size:1.1rem;margin:2rem 0 2.4rem;opacity:.85}.acts{display:flex;gap:1rem;flex-wrap:wrap}
.pill{display:inline-flex;gap:.6rem;align-items:center;margin-top:2.6rem;background:rgba(255,255,255,.7);backdrop-filter:blur(8px);border:1px solid var(--line);border-radius:99px;padding:.6rem 1.1rem .6rem .6rem;font-size:.86rem}
.pill i{width:30px;height:30px;border-radius:50%;background:var(--acc);display:grid;place-items:center;color:#fff}.pill svg{width:14px;height:14px}
.sec{padding:8rem 0}.sec h2{font-size:clamp(2.4rem,4.8vw,4.6rem)}
.intro{display:grid;grid-template-columns:1fr 1fr;gap:6rem;align-items:center}.intro p.big{font-size:1.3rem;line-height:1.6;margin-top:1.8rem}
.circ{position:relative;margin:0;justify-self:center;width:min(460px,100%)}.circ .i{border-radius:40px;overflow:hidden;aspect-ratio:4/5}.circ img{width:100%;height:100%;object-fit:cover}
.circ:before{content:'';position:absolute;inset:-16px;border:1px solid var(--gold);border-radius:52px}.circ figcaption{text-align:center;font-size:.74rem;opacity:.6;margin-top:1.6rem}
.plum{background:var(--fg);color:#FBF3F1;--line:rgba(251,243,241,.15)}.plum em{color:#E7B7CF}.plum .kick{color:var(--gold)}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:1.6rem;margin-top:4rem}.col{border:1px solid var(--line);border-radius:32px;padding:2.8rem;background:rgba(255,255,255,.03)}
.col h3{font-size:2rem;margin-bottom:1.4rem;display:flex;gap:1rem;align-items:center}.col h3 svg{width:40px;height:40px;color:var(--gold)}
.col ul{list-style:none;margin:0;padding:0}.col li{padding:1rem 0;border-top:1px solid var(--line);font-size:1.12rem;display:flex;justify-content:space-between;gap:1rem;align-items:center}
.col li:before{content:'';width:7px;height:7px;border-radius:50%;background:var(--gold);flex:none;margin-right:.4rem}.col li span{flex:1}
.band{position:relative;height:70vh;min-height:420px;overflow:hidden;isolation:isolate;display:grid;place-items:center;text-align:center;color:#fff}
.band:after{content:'';position:absolute;inset:0;background:rgba(58,22,49,.35);z-index:-1}.band h2{font-size:clamp(2.4rem,6vw,5.4rem)}.band figcaption{position:absolute;bottom:1rem;right:1.4rem;font-size:.72rem;opacity:.8}
.info{display:grid;grid-template-columns:1.1fr .9fr;gap:1.6rem}.card{background:#fff;border-radius:32px;padding:2.6rem;box-shadow:0 24px 60px rgba(58,22,49,.07)}.card h3{font-size:1.9rem;margin-bottom:1.2rem}
.dl{margin:0}.dl div{display:grid;grid-template-columns:10rem 1fr;gap:1rem;padding:.95rem 0;border-bottom:1px solid var(--line)}.dl dt{font:600 .62rem/1.7 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.6}.dl dd{margin:0}
.rdv{display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem;align-items:start}.rdv .card{background:#F4E4E3}
.mapw{border-radius:32px}
@media(max-width:960px){.intro,.cols,.info,.rdv{grid-template-columns:1fr;gap:2.4rem}.hin{grid-template-columns:1fr;gap:3rem;padding:7.5rem 0 4rem}.hcirc{order:-1;width:min(76vw,380px)}.hcirc:after{display:none}}
@media(max-width:760px){.sec{padding:5.5rem 0}.col,.card{padding:1.8rem}.dl div{grid-template-columns:1fr;gap:.1rem}.band{height:52vh}}
'''
def build(F, M):
    msg = 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet.'
    brand = '<span class="mono">AH</span><span><b>Dr Asma Hmila</b><small>Gynécologie-obstétrique · Nabeul</small></span>'
    links = [('Le cabinet', '#cabinet'), ('Actes', '#actes'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    g1 = ['Suivi de grossesse', 'Accouchement', 'Échographie 3D/4D']; g2 = ['Aide médicale à la procréation', 'Cœlioscopie', 'Hystéroscopie', 'Chirurgie des seins']
    li = lambda L: ''.join(f'<li><span>{x}</span></li>' for x in L)
    w, h = M.dims['hero']
    body = f'''{lux.header(brand, links)}<main id="main">
<section class="hero" id="top">
<div class="w hin"><div><p class="kick rise">Gynécologie-obstétrique · Nabeul</p><h1 class="rise d1"><span>Dr Asma</span><span><em>Hmila</em></span></h1>
<p class="lede rise d2">Cabinet de gynécologie et d'obstétrique, immeuble Jawhara, 101 avenue Habib Thameur à Nabeul. Consultations sur rendez-vous.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Prendre rendez-vous {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div>
<div class="pill rise d4"><i>{K.I['clock']}</i>Mercredi {F['wed']} · autres jours à confirmer</div></div>
<figure class="hcirc rise d2"><div class="i">{M.img('hero', 'Mains formant un cœur sur un ventre de femme enceinte (photo d’illustration)', sizes='(max-width: 960px) 76vw, 560px', lazy=False)}</div><figcaption>Grossesse · photo d'illustration</figcaption></figure></div></section>
<section class="sec" id="cabinet"><div class="w intro"><div><p class="kick" data-rv>Le cabinet</p><h2 data-rv>Au 3e étage de <em>l'immeuble Jawhara</em>.</h2>
<p class="big" data-rv>Le Dr Asma Hmila, gynécologue-obstétricienne, reçoit au bureau 3.3 de l'immeuble Jawhara, avenue Habib Thameur. Le cabinet est joignable par téléphone, sur son numéro fixe et via WhatsApp.</p>
<p class="note" data-rv>Parcours et qualifications {ph()}</p></div>
<figure class="circ" data-rv="s">{'<div class="i">'+M.img('pieds', 'Pieds de nouveau-né dans la main d’un parent (photo d’illustration)', sizes='(max-width: 960px) 90vw, 460px')+'</div>'}<figcaption>Illustration · ne montre pas le cabinet</figcaption></figure></div></section>
<section class="sec plum" id="actes"><div class="w"><p class="kick" data-rv>Actes</p><h2 data-rv>Actes indiqués sur la <em>fiche du cabinet</em>.</h2>
<div class="cols"><div class="col" data-rv><h3>{IC['baby']}Obstétrique</h3><ul>{li(g1)}</ul></div><div class="col" data-rv style="--d:.12s"><h3>{IC['flower']}Gynécologie</h3><ul>{li(g2)}</ul></div></div>
<p class="note" data-rv style="margin-top:2rem">Liste reprise de la fiche publique du cabinet, présentée à titre informatif et à confirmer par le médecin avant publication.</p></div></section>
<figure class="band" style="margin:0"><div class="pxw">{M.img('echo', 'Image d’échographie 3D d’un fœtus (photo d’illustration)', cls='px', sizes='100vw', extra=' data-px=".16"')}</div><h2 data-rv>Du suivi de grossesse <em style="color:#F6D8E5">à l'échographie</em></h2><figcaption>Échographie · image d'illustration, ne montre pas le cabinet</figcaption></figure>
<section class="sec" id="horaires"><div class="w info"><div class="card" data-rv><h3>Fiche du cabinet</h3><dl class="dl"><div><dt>Médecin</dt><dd>Dr Asma Hmila</dd></div><div><dt>Spécialité</dt><dd>Gynécologie-obstétrique</dd></div><div><dt>Adresse</dt><dd>{F['addr']}</dd></div></dl>
<div style="margin-top:1rem">{lux.contacts(F, wa_msg=msg)}</div></div><div class="card" data-rv style="--d:.12s"><h3>Horaires</h3>{lux.hours(F)}</div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w rdv"><div data-rv><p class="kick">Rendez-vous</p><h2>Demander un <em>rendez-vous</em></h2><p style="margin-top:1.4rem;opacity:.8">Le message s'ouvre dans WhatsApp ; le cabinet confirme le créneau.</p></div>
<div class="card" data-rv style="--d:.1s">{lux.form(F, 'Bonjour Docteur, je souhaite un rendez-vous au cabinet.', lux.MED_FORM)}</div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Immeuble Jawhara, <em>Nabeul</em></h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F)}'''
    return lux.page(F, 'Dr Asma Hmila · Gynécologue-obstétricienne à Nabeul (démo)', 'Cabinet de gynécologie-obstétrique du Dr Asma Hmila, immeuble Jawhara, Nabeul : coordonnées, horaires et demande de rendez-vous.', FONTS, CSS, body, '#FBF3F1', lux.fav('#3A1631', '#E7B7CF', 'AH'))
