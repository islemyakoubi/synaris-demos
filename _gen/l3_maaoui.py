# Maître Imen Maaoui, avocate (Grombalia) : « bilingue ». Parchemin, bordeaux, or. Hero typographique bilingue (Bodoni Moda / Noto Naskh Arabic) séparé
# par un filet or animé, statue de la Justice en colonne, principes en chiffres romains, domaines indicatifs (à confirmer), olivier en parallaxe, rendez-vous sans consultation.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400&family=Work+Sans:wght@300;400;500;600&family=Noto+Naskh+Arabic:wght@400;500;600'
CSS = '''
:root{--bg:#F3EBDD;--fg:#2A1214;--acc:#6E1E22;--onacc:#F3EBDD;--line:rgba(42,18,20,.15);--hbg:rgba(243,235,221,.9);--disp:'Bodoni Moda',Didot,serif;--sans:'Work Sans',system-ui,sans-serif;--r:0;--gold:#B08D57;--mapbg:#E7DCC8;--rbg:#2A1214}
em{font-style:italic;color:var(--acc)}.ar{font-family:'Noto Naskh Arabic',serif;direction:rtl}.brand .mono{width:44px;height:44px;border:1px solid var(--acc);display:grid;place-items:center;font:italic 400 1.05rem var(--disp);color:var(--acc)}
.hero{min-height:100svh;display:grid;grid-template-columns:1fr auto 1fr .55fr;gap:3rem;align-items:center;padding:9rem 0 4rem}
.hero h1{font-size:clamp(3rem,6.6vw,6.8rem);line-height:.95;font-weight:400;letter-spacing:-.02em}.hero h1 span{display:block}
.rule{width:1px;height:62vh;background:linear-gradient(transparent,var(--gold),transparent);transform-origin:top;animation:grow 1.6s var(--ease) .3s both}@keyframes grow{from{transform:scaleY(0)}}
.arh{font-size:clamp(2.4rem,4.8vw,4.8rem);line-height:1.35;color:var(--acc);font-weight:500;text-align:right}.arh small{display:block;font-size:.4em;color:var(--fg);opacity:.75;margin-top:1rem}
.lede{font-size:1.05rem;max-width:30rem;margin:1.8rem 0 2.2rem;opacity:.82}.acts{display:flex;gap:1rem;flex-wrap:wrap}
.spine{align-self:stretch;position:relative;overflow:hidden;min-height:420px}.spine img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:71% 50%;filter:sepia(.28) saturate(.8)}.spine:after{content:'';position:absolute;inset:0;box-shadow:inset 0 0 0 1px var(--gold)}
.ox{background:var(--acc);color:var(--bg);--line:rgba(243,235,221,.2)}.ox .kick{color:#E3C58F}.ox em{color:#E3C58F}
.sec{padding:8rem 0}.sec h2{font-size:clamp(2.4rem,4.8vw,4.6rem);line-height:1.02}
.prin{display:grid;grid-template-columns:repeat(3,1fr);margin-top:4rem}.prin div{padding:0 2.4rem;border-left:1px solid var(--line)}.prin div:first-child{padding-left:0;border:0}
.prin b{display:block;font:400 4rem/1 var(--disp);color:#E3C58F;margin-bottom:1.2rem;font-style:italic}.prin h3{font-size:1.8rem;margin-bottom:.6rem}.prin p{opacity:.8;margin:0}
.doms{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--fg);margin-top:4rem}.doms article{padding:2.4rem 2rem 2.4rem 0;border-bottom:1px solid var(--line);transition:padding .5s var(--ease)}.doms article:hover{padding-left:1rem}
.doms h3{font-size:1.6rem;margin-bottom:.4rem;display:flex;gap:.8rem;align-items:baseline}.doms h3 i{font:italic 400 1rem var(--disp);color:var(--gold)}.doms p{margin:0 0 .8rem;opacity:.72;font-size:.94rem}
.olive{position:relative;height:74vh;min-height:440px;overflow:hidden;isolation:isolate;display:flex;align-items:flex-end;color:#fff}.olive:after{content:'';position:absolute;inset:0;z-index:-1;background:linear-gradient(0deg,rgba(42,18,20,.8),transparent 60%)}
.olive .w{padding-bottom:3rem}.olive h2{font-size:clamp(2.4rem,5.6vw,5.4rem)}.olive h2 em{color:#E3C58F}.olive small{opacity:.75}
.info{display:grid;grid-template-columns:1fr 1fr;gap:0;border:1px solid var(--fg)}.info>div{padding:2.8rem}.info>div+div{border-left:1px solid var(--fg)}.info h3{font-size:2rem;margin-bottom:1.2rem}
.rdv{display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem}.rdv .f{background:#FBF7EF;border:1px solid var(--gold);padding:2.6rem}
.mapw{border:1px solid var(--fg)}
@media(max-width:1100px){.hero{grid-template-columns:1fr auto 1fr}.spine{grid-column:1/-1;min-height:0;height:340px}.spine img{object-position:60% 72%}}
@media(max-width:960px){.hero{grid-template-columns:1fr;gap:2rem;padding-top:8rem}.rule{width:120px;height:1px;background:var(--gold)}.arh{text-align:right}.prin,.doms,.info,.rdv{grid-template-columns:1fr}.prin div{padding:2rem 0;border-left:0;border-top:1px solid var(--line)}.info>div+div{border-left:0;border-top:1px solid var(--fg)}}
@media(max-width:760px){.sec{padding:5.5rem 0}.info>div,.rdv .f{padding:1.6rem}}
'''
DOM = [('Droit civil et de la famille', 'Contrats, successions, questions familiales.'), ('Droit immobilier', 'Ventes, baux et litiges fonciers.'), ('Droit des affaires', 'Sociétés et contrats commerciaux.'),
       ('Droit du travail', 'Relations entre employeurs et salariés.'), ('Droit pénal', 'Assistance aux différentes étapes de la procédure.'), ('Contentieux', 'Représentation devant les juridictions.')]
def build(F, M):
    msg = 'Bonjour Maître, je souhaite prendre rendez-vous à votre cabinet.'
    brand = '<span class="mono">IM</span><span><b>Maître Imen Maaoui</b><small>Avocate · Grombalia</small></span>'
    links = [('Principes', '#principes'), ('Domaines', '#domaines'), ('Cabinet', '#cabinet'), ('Accès', '#acces')]
    dh = ''.join(f'<article data-rv style="--d:{i%3*.1:.1f}s"><h3><i>{"I II III IV V VI".split()[i]}</i>{t}</h3><p>{p}</p>{ph()}</article>' for i, (t, p) in enumerate(DOM))
    spec = [('text', 'Nom et prénom'), ('tel', 'Téléphone'), ('date', 'Jour souhaité'), ('select', 'Moment', ['Matin', 'Après-midi', 'Peu importe']), ('select', 'Être recontacté par', ['Appel téléphonique', 'WhatsApp'])]
    note = "Démo : aucune donnée n'est enregistrée. Ce formulaire sert uniquement à demander un rendez-vous : n'y décrivez pas votre affaire. Aucune consultation n'est donnée par message."
    body = f'''{lux.header(brand, links)}<main id="main">
<section class="w hero" id="top"><div><p class="kick rise">Avocate · Grombalia</p><h1 class="rise d1"><span>Maître</span><span>Imen <em>Maaoui</em></span></h1>
<p class="lede rise d2">Cabinet d'avocate avenue de la Paix, à Grombalia. Les clients sont reçus sur rendez-vous, dans le respect du secret professionnel.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Demander un rendez-vous {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div></div>
<span class="rule" aria-hidden="true"></span><p class="arh ar rise d2" lang="ar">{F['ar']}<br>محامية<small>قرمبالية · شارع السلام</small></p>
<figure class="spine rise d3" style="margin:0">{M.img('hero', 'Statue dorée de la Justice tenant la balance (photo d’illustration)', sizes='(max-width: 1100px) 100vw, 300px', lazy=False)}</figure></section>
<section class="sec ox" id="principes"><div class="w"><p class="kick" data-rv>Principes</p><h2 data-rv>Écoute, <em>confidentialité</em>, indépendance.</h2>
<div class="prin"><div data-rv><b>I</b><h3>Secret professionnel</h3><p>Ce qui est confié à l'avocate reste couvert par le secret professionnel.</p></div><div data-rv style="--d:.1s"><b>II</b><h3>Indépendance</h3><p>Un exercice indépendant, dans le cadre de la déontologie de l'Ordre.</p></div>
<div data-rv style="--d:.2s"><b>III</b><h3>Sur rendez-vous</h3><p>Chaque dossier s'examine au cabinet, lors d'un entretien fixé à l'avance.</p></div></div></div></section>
<section class="sec" id="domaines"><div class="w"><p class="kick" data-rv>Domaines</p><h2 data-rv>Domaines <em>d'intervention</em></h2><p data-rv style="max-width:36rem;margin-top:1.2rem;opacity:.75">Liste indicative, à confirmer par le cabinet avant publication : seuls les domaines effectivement traités par Maître Maaoui seront conservés.</p><div class="doms">{dh}</div></div></section>
<figure class="olive" style="margin:0"><div class="pxw">{M.img('olivier', 'Olivier dans la campagne tunisienne (photo d’illustration)', cls='px', sizes='100vw', extra=' data-px=".15"')}</div><div class="w" data-rv><h2>Grombalia, <em>Cap Bon</em>.</h2><small>Photo d'illustration · ne montre pas le cabinet</small></div></figure>
<section class="sec" id="cabinet"><div class="w"><div class="info" data-rv><div><h3>Le cabinet</h3><dl class="dl" style="margin:0">{''.join(f'<div style="display:grid;grid-template-columns:10rem 1fr;gap:1rem;padding:.9rem 0;border-bottom:1px solid var(--line)"><dt style="font:600 .62rem/1.7 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.6">{a}</dt><dd style="margin:0">{b}</dd></div>' for a, b in [('Avocate', 'Maître Imen Maaoui'), ('Barreau', ph()), ('Langues', ph()), ('Adresse', F['addr'])])}</dl>
<div style="margin-top:1rem">{lux.contacts(F, 'WhatsApp · demande de rendez-vous', msg)}</div></div><div><h3>Horaires</h3>{lux.hours(F)}<figure style="margin:2rem 0 0;max-width:260px">{M.img('balance', 'Balance de la justice (illustration)', sizes='260px', extra=' style="mix-blend-mode:multiply"')}</figure></div></div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w rdv"><div data-rv><p class="kick">Rendez-vous</p><h2>Demander un <em>rendez-vous</em></h2><p style="margin-top:1.4rem;opacity:.8">Le formulaire prépare un message WhatsApp pour fixer un entretien au cabinet. Aucune consultation n'est donnée par message.</p>
<figure style="margin:2rem 0 0;max-width:380px" data-rv>{M.img('codes', 'Arcades du Palais de justice de Tunis (photo d’illustration)', sizes='380px')}</figure></div>
<div class="f" data-rv style="--d:.1s">{lux.form(F, 'Bonjour Maître, je souhaite prendre rendez-vous à votre cabinet.', spec, 'Envoyer la demande', note)}</div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Avenue de la Paix, <em>Grombalia</em></h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F)}'''
    return lux.page(F, 'Maître Imen Maaoui · Avocate à Grombalia (démo)', 'Cabinet de Maître Imen Maaoui, avocate, avenue de la Paix, Grombalia : coordonnées, horaires et demande de rendez-vous.', FONTS, CSS, body, '#F3EBDD', lux.fav('#6E1E22', '#F3EBDD', 'IM'))
