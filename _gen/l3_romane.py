# Cabinet d'orthoptie Amina Romane (Nabeul) : « vision binoculaire ». Refonte complète (v2) : papier ivoire, encre bleu-noir, sarcelle profonde, filets laiton.
# Hero scindé (texte sur encre / macro d'un œil en plein cadre), emblème de deux anneaux qui fusionnent, explication claire de l'orthoptie (générale, non inventée),
# section « deux yeux, une seule image », bande photo en parallaxe, préparer son rendez-vous, fiche, horaires, formulaire, accès. Source Serif 4 + Schibsted Grotesk.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;0,8..60,500;1,8..60,300;1,8..60,400&family=Schibsted+Grotesk:wght@400;500;600;700'
RINGS = '<svg class="rings" viewBox="0 0 120 64" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><circle class="r1" cx="38" cy="32" r="26"/><circle class="r2" cx="82" cy="32" r="26"/></svg>'
CSS = '''
:root{--bg:#F4EFE7;--fg:#15202A;--acc:#1F5D5F;--onacc:#fff;--line:rgba(21,32,42,.14);--hbg:rgba(244,239,231,.92);--disp:'Source Serif 4',Georgia,serif;--sans:'Schibsted Grotesk',system-ui,sans-serif;--r:2px;
--ink:#111B24;--aqua:#A9D5CF;--brass:#B8966A;--paper2:#ECE5D9;--mapbg:#E6DED1;--rbg:#0B1218}
h1,h2,h3{font-weight:300;letter-spacing:-.018em}em{font-style:italic;color:var(--acc)}
.brand .mono{width:46px;height:46px;border-radius:50%;border:1px solid currentColor;display:grid;place-items:center;flex:none}.brand .mono .rings{width:30px;height:16px}
.hdr{color:#EEF1EE}.hdr.scrolled{color:var(--fg)}
.rings .r1,.rings .r2{transition:transform 1.8s var(--ease)}
.hero{position:relative;min-height:100svh;display:grid;grid-template-columns:1.06fr .94fr;background:var(--ink);color:#EEF1EE;isolation:isolate;overflow:hidden}
.hero .tx{padding:10.5rem clamp(1.5rem,4.5vw,4.5rem) 0 max(1.5rem,calc((100vw - 1200px)/2));display:flex;flex-direction:column;justify-content:center;min-width:0}
.hero .tx>*{max-width:620px}
.hero .kick{color:var(--aqua)}
.hero h1{font-size:clamp(3.3rem,6.2vw,6.4rem);line-height:.96}.hero h1 em{display:block;color:var(--aqua);font-weight:300}
.lede{font-size:1.08rem;line-height:1.75;opacity:.8;max-width:31rem;margin:1.8rem 0 2.4rem}
.acts{display:flex;gap:1rem;flex-wrap:wrap}.hero .btn.p{background:var(--aqua);color:var(--ink)}.hero .btn.o{color:#EEF1EE;border-color:rgba(238,241,238,.38)}.hero .btn.o:hover{background:rgba(238,241,238,.08)}
.rail{display:grid;grid-template-columns:auto auto auto;justify-content:start;gap:2.8rem;margin-top:4.2rem;padding:1.5rem 0 2.6rem;border-top:1px solid rgba(238,241,238,.16)}
.rail small{display:block;font:600 .6rem/1 var(--sans);letter-spacing:.24em;text-transform:uppercase;opacity:.55;margin-bottom:.65rem}.rail p{margin:0;font:400 1.08rem/1.35 var(--disp)}.rail a{color:inherit}
.hero figure{position:relative;margin:0;overflow:hidden;min-height:100%}.hero figure img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:34% 50%;animation:kb 18s var(--ease) both}
@keyframes kb{from{transform:scale(1.12)}to{transform:scale(1)}}
.hero figure:after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,var(--ink) 0%,rgba(17,27,36,.35) 22%,rgba(17,27,36,0) 45%),linear-gradient(0deg,rgba(17,27,36,.55),transparent 35%)}
.hero figcaption{position:absolute;right:1.6rem;bottom:1.4rem;z-index:2;font-size:.7rem;letter-spacing:.06em;opacity:.7}
.fuse{position:absolute;left:2.4rem;bottom:2rem;z-index:2;color:var(--brass);display:flex;align-items:center;gap:1rem;font:600 .6rem/1.4 var(--sans);letter-spacing:.24em;text-transform:uppercase;color:#E9DCC6}
.fuse .rings{width:84px;height:45px;color:var(--brass)}.fuse .r1{animation:c1 2.6s var(--ease) .8s both}.fuse .r2{animation:c2 2.6s var(--ease) .8s both}
@keyframes c1{from{transform:translateX(-14px)}to{transform:translateX(9px)}}@keyframes c2{from{transform:translateX(14px)}to{transform:translateX(-9px)}}
.sec{padding:8.5rem 0}.sec h2{font-size:clamp(2.5rem,4.8vw,4.6rem);line-height:1.02}
.intro{display:grid;grid-template-columns:.95fr 1.05fr;gap:5rem;align-items:end;padding-bottom:4rem;border-bottom:1px solid var(--line)}
.big{font:300 clamp(1.22rem,1.75vw,1.5rem)/1.6 var(--disp);margin:0}.big+.big{margin-top:1.1rem}
.dom{display:grid;grid-template-columns:.92fr 1.08fr;gap:5rem;margin-top:4.5rem;align-items:start}
.dom figure{position:sticky;top:120px;margin:0}.dom .pic{aspect-ratio:1546/1135;overflow:hidden;box-shadow:0 30px 70px rgba(21,32,42,.12)}
.dom .pic img{width:100%;height:100%;object-fit:cover;transition:transform 1.6s var(--ease)}.dom .pic:hover img{transform:scale(1.03)}
.dom figcaption,.cap{font-size:.76rem;opacity:.65;margin-top:.9rem;line-height:1.5}
.doms{list-style:none;margin:0;padding:0;border-top:1px solid var(--fg)}.doms li{display:grid;grid-template-columns:4.2rem 1fr;gap:.4rem;padding:2rem 0;border-bottom:1px solid var(--line)}
.doms b{font:italic 300 1.5rem/1.2 var(--disp);color:var(--brass);display:flex;flex-direction:column;gap:.7rem}.doms b svg{width:30px;height:30px;color:var(--acc)}.doms h3{font-size:1.75rem;font-weight:400;margin-bottom:.55rem}.doms p{margin:0;opacity:.78}
.gen{display:flex;gap:1rem;align-items:flex-start;margin-top:2rem;padding:1.3rem 1.4rem;background:var(--paper2);font-size:.9rem;line-height:1.6}.gen svg{width:22px;height:22px;flex:none;color:var(--acc);margin-top:.1rem}.gen p{margin:0}
.bino{background:var(--ink);color:#EEF1EE;--line:rgba(238,241,238,.15)}.bino .kick{color:var(--aqua)}.bino em{color:var(--aqua)}
.bgrid{display:grid;grid-template-columns:1fr 1fr;gap:6rem;align-items:center}
.frame{position:relative;margin:0 18px 0 0}
.frame .in{position:relative;aspect-ratio:4/3;overflow:hidden;box-shadow:18px 18px 0 -1px var(--ink),18px 18px 0 0 rgba(184,150,106,.75)}.frame .in img{transition:transform 1.6s var(--ease)}.frame:hover .in img{transform:scale(1.03)}.frame img{width:100%;height:100%;object-fit:cover}
.bino .cap{opacity:.6;margin-top:2.6rem}
.bino p.l{font-size:1.06rem;opacity:.82;margin-top:1.4rem}
.trio{display:grid;grid-template-columns:repeat(3,1fr);margin-top:2.6rem;border-top:1px solid var(--line)}.trio div{padding:1.5rem 1.2rem 0 0}.trio div+div{padding-left:1.2rem;border-left:1px solid var(--line)}
.trio h3{font-size:1.45rem;font-weight:400;color:var(--aqua);margin-bottom:.4rem}.trio p{margin:0;font-size:.9rem;opacity:.75;line-height:1.55}
.band{position:relative;height:72vh;min-height:420px;overflow:hidden;isolation:isolate;display:flex;align-items:flex-end;color:#fff}
.band .px{object-position:50% 40%}.band:after{content:'';position:absolute;inset:0;z-index:-1;background:linear-gradient(0deg,rgba(17,27,36,.92) 8%,rgba(17,27,36,.55) 42%,rgba(17,27,36,.12) 75%)}
.band .w{padding-bottom:3rem;display:flex;justify-content:space-between;align-items:flex-end;gap:2rem;flex-wrap:wrap}.band h2{font-size:clamp(2.2rem,4.6vw,4.4rem);max-width:14em}.band em{color:var(--aqua)}.band small{opacity:.8;font-size:.72rem;white-space:nowrap}
.venir{display:grid;grid-template-columns:.85fr 1.15fr;gap:6rem;align-items:center}
.venir figure{margin:0}.venir .in{aspect-ratio:4/5;overflow:hidden}.venir img{width:100%;height:100%;object-fit:cover;object-position:50% 30%;filter:saturate(.78) contrast(1.03) sepia(.08)}
.steps{list-style:none;margin:2.6rem 0 0;padding:0;counter-reset:s}.steps li{display:grid;grid-template-columns:3.6rem 1fr;padding:1.7rem 0;border-top:1px solid var(--line)}.steps li:last-child{border-bottom:1px solid var(--line)}
.steps li:before{counter-increment:s;content:'0' counter(s);font:italic 300 1.35rem/1.3 var(--disp);color:var(--brass)}.steps h3{font-size:1.5rem;font-weight:400;margin-bottom:.4rem}.steps p{margin:0;opacity:.8}.steps a{color:var(--acc);text-decoration:underline;text-underline-offset:3px}
section[id]{scroll-margin-top:64px}.cab{background:var(--paper2)}#rdv{padding:6.5rem 0}.cgrid{display:grid;grid-template-columns:1.1fr .9fr;gap:1.4rem;margin-top:3.4rem}
.card{background:var(--bg);padding:2.8rem;border:1px solid var(--line);display:flex;flex-direction:column}.card .cta2{margin-top:auto;padding-top:2rem;display:flex;gap:.8rem;flex-wrap:wrap}.card .cta2 .btn{padding:1rem 1.3rem}.card .sr{margin:1.6rem 0 0;padding:1.4rem 1.5rem;background:var(--paper2);font:400 1.15rem/1.5 var(--disp)}.card h3{font-size:1.9rem;font-weight:400;margin-bottom:1.4rem}
.dl{margin:0}.dl div{display:grid;grid-template-columns:11rem 1fr;gap:1rem;padding:1rem 0;border-bottom:1px solid var(--line)}.dl dt{font:600 .62rem/1.8 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.6}.dl dd{margin:0;font:400 1.1rem/1.45 var(--disp)}
.rdv{background:var(--ink);color:#EEF1EE;display:grid;grid-template-columns:.8fr 1.2fr;gap:4.5rem;padding:4.6rem;--line:rgba(238,241,238,.14);--fln:rgba(238,241,238,.26);--fbg:rgba(255,255,255,.04);--acc:#A9D5CF;--onacc:#111B24}.rdv h2{color:#EEF1EE}.rdv em{color:var(--aqua)}.rdv select option{color:#15202A}
.rdv .kick{color:var(--aqua)}.rdv p.l{opacity:.8;margin-top:1.4rem}.rdv .fuse2{margin-top:2.6rem;color:var(--brass)}.rdv .fuse2 .rings{width:110px;height:59px}
.mapw{margin-top:2.4rem;border:1px solid var(--line)}
.ft{background:var(--ink);color:#DDE3E1;--line:rgba(238,241,238,.14)}.ft .brand .mono{border-color:rgba(238,241,238,.5)}
@media(max-width:1100px){.hero{grid-template-columns:1fr 1fr}.hero h1{font-size:clamp(3rem,6.4vw,5rem)}.rail{grid-template-columns:1fr 1fr;gap:1.6rem}.rail div:last-child{grid-column:1/-1}}
@media(max-width:960px){.hero{grid-template-columns:1fr;min-height:auto}.hero figure{order:-1;height:62svh;min-height:400px}.hero figure:after{background:linear-gradient(0deg,var(--ink) 4%,rgba(17,27,36,.2) 45%,rgba(17,27,36,.55))}
.hero figure img{object-position:42% 45%}.hero .tx{padding:0 1.5rem;margin-top:-5.5rem;position:relative;z-index:1}.hero figcaption{top:auto;bottom:6.6rem;right:1.2rem}.fuse{display:none}
.intro,.dom,.bgrid,.venir,.cgrid,.rdv{grid-template-columns:1fr;gap:3rem}.dom figure{position:relative;top:0}.dom .pic{aspect-ratio:4/3}.venir .in{aspect-ratio:4/3}.frame{margin-right:18px}.rdv{padding:2.6rem 1.5rem}}
@media(max-width:760px){.sec{padding:5.5rem 0}.hero .tx{padding:0 1.2rem}.hero figure{height:56svh;min-height:360px}.rail{grid-template-columns:1fr;gap:1.1rem;margin-top:2.8rem}.rail div:last-child{grid-column:auto}
.trio{grid-template-columns:1fr}.trio div,.trio div+div{padding:1.2rem 0;border-left:0;border-bottom:1px solid var(--line)}.card{padding:1.6rem}.dl div{grid-template-columns:1fr;gap:.15rem}.doms li{grid-template-columns:3rem 1fr}.band{height:60vh}}
'''
def build(F, M):
    # Crédits : les fichiers Wellcome n'ont pas de champ auteur sur Commons ; titres longs abrégés proprement.
    M.cr = [(n, dict(x, artist=x['artist'] or ('Science Museum, London (Wellcome Images)' if 'Wellcome' in x['title'] else ''),
                     title=x['title'] if len(x['title']) <= 80 else x['title'][:48].rstrip(' ,') + '… Wellcome ' + x['title'].rsplit('Wellcome ', 1)[-1])) for n, x in M.cr]
    msg = 'Bonjour, je souhaite prendre rendez-vous au cabinet d’orthoptie.'
    brand = f'<span class="mono">{RINGS}</span><span><b>Amina Romane</b><small>Orthoptiste · Nabeul</small></span>'
    links = [('L’orthoptie', '#orthoptie'), ('Vision binoculaire', '#binoculaire'), ('Le cabinet', '#cabinet'), ('Accès', '#acces')]
    doms = [('Le bilan orthoptique', 'Une évaluation de la vision binoculaire, de l’équilibre entre les deux yeux et de leurs mouvements. Il est le plus souvent réalisé à la demande d’un médecin.'),
            ('La rééducation orthoptique', 'Des séances d’exercices visuels qui visent à améliorer la coordination des deux yeux, par exemple en cas de fatigue visuelle ou de difficulté à fixer de près.'),
            ('Strabisme et amblyopie', 'Le suivi, en lien avec l’ophtalmologiste, d’un enfant ou d’un adulte présentant un strabisme ou une amblyopie (« œil paresseux »).'),
            ('La basse vision', 'L’accompagnement des personnes malvoyantes, pour mieux utiliser leurs capacités visuelles dans les gestes du quotidien.')]
    # Pictos fins (vision) : bilan = œil, rééducation = convergence des deux yeux, strabisme/amblyopie = cache, basse vision = loupe.
    ICO = ['<circle cx="12" cy="12" r="3.2"/><circle cx="12" cy="12" r=".6" fill="currentColor"/><path d="M2 12s3.7-6.4 10-6.4S22 12 22 12s-3.7 6.4-10 6.4S2 12 2 12z"/>',
           '<circle cx="6.8" cy="9" r="3.4"/><circle cx="17.2" cy="9" r="3.4"/><path d="M6.8 15.2 12 19.6l5.2-4.4"/>',
           '<path d="M2.5 7.2c6.2-2.6 12.8-2.6 19 0"/><circle cx="7" cy="12.4" r="3.4"/><circle cx="17" cy="12.4" r="3.9" fill="currentColor" fill-opacity=".22"/>',
           '<circle cx="10" cy="10" r="6.6"/><path d="m15 15 5.6 5.6M6.4 10s1.5-2.3 3.6-2.3 3.6 2.3 3.6 2.3-1.5 2.3-3.6 2.3S6.4 10 6.4 10z"/>']
    svg = lambda k: f'<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">{ICO[k]}</svg>'
    dh = ''.join(f'<li data-rv style="--d:{i*.08:.2f}s"><b>0{i+1}{svg(i)}</b><div><h3>{t}</h3><p>{p}</p></div></li>' for i, (t, p) in enumerate(doms))
    trio = [('Fusion', 'L’assemblage, par le cerveau, des images des deux yeux en une seule.'), ('Convergence', 'Le rapprochement des deux yeux pour regarder de près, en lecture par exemple.'), ('Relief', 'La perception de la profondeur, rendue possible par la vision des deux yeux.')]
    th = ''.join(f'<div data-rv style="--d:{i*.1:.1f}s"><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(trio))
    wa = K.walink(F['wa'], msg)
    body = f'''{lux.header(brand, links)}<main id="main">
<section class="hero" id="top"><div class="tx"><p class="kick rise">Cabinet d'orthoptie · Nabeul</p><h1 class="rise d1">Amina Romane<em>orthoptiste</em></h1>
<p class="lede rise d2">Cabinet au 1er étage de l'immeuble Essalama, avenue Habib Thameur, à Nabeul. Bilans et séances sur rendez-vous, par téléphone ou WhatsApp.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Demander un rendez-vous {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div>
<div class="rail rise d4"><div><small>Téléphone</small><p><a href="{K.telhref(F['tel'])}">{F['tel']}</a></p></div><div><small>Horaire relevé</small><p>Mercredi, {F['wed']}</p></div><div><small>Cabinet</small><p>Immeuble Essalama, app. 208</p></div></div></div>
<figure>{M.img('hero', 'Gros plan sur un œil (photo d’illustration)', sizes='(max-width: 960px) 100vw, 48vw', lazy=False)}<div class="fuse" aria-hidden="true">{RINGS}<span>Deux yeux,<br>une seule image</span></div><figcaption>Photo d'illustration</figcaption></figure></section>
<section class="sec" id="orthoptie"><div class="w"><div class="intro"><div><p class="kick" data-rv>L'orthoptie</p><h2 data-rv>Qu'est-ce que <em>l'orthoptie</em> ?</h2></div>
<div data-rv style="--d:.1s"><p class="big">L'orthoptiste est un professionnel de santé paramédical. Il intervient dans le dépistage, l'évaluation et la rééducation des troubles de la vision : l'équilibre entre les deux yeux, leurs mouvements et la fatigue visuelle.</p>
<p class="big">Il travaille le plus souvent sur prescription médicale, en lien avec le médecin ophtalmologiste.</p></div></div>
<div class="dom"><figure data-rv><div class="pic">{M.img('syno', 'Synoptophore, instrument d’orthoptie (photo d’illustration)', sizes='(max-width: 960px) 92vw, 520px')}</div><figcaption>Synoptophore, un instrument classique d'orthoptie qui présente une image différente à chaque œil. Photo d'illustration (Wellcome Collection).</figcaption></figure>
<div><p class="kick" data-rv>Les grands domaines de la profession</p><ol class="doms">{dh}</ol>
<div class="gen" data-rv>{IC['doc']}<p>Présentation générale de l'orthoptie, à titre informatif. Les bilans et prises en charge proposés au cabinet sont {ph()}</p></div></div></div></div></section>
<section class="sec bino" id="binoculaire"><div class="w bgrid"><figure class="frame" data-rv><div class="in">{M.img('stereo', 'Stéréoscope ancien (photo d’illustration)', sizes='(max-width: 960px) 92vw, 560px')}</div><figcaption class="cap">Stéréoscope ancien : deux images, une seule vision en relief. Photo d'illustration.</figcaption></figure>
<div><p class="kick" data-rv>Vision binoculaire</p><h2 data-rv>Deux yeux, <em>une seule image</em>.</h2>
<p class="l" data-rv>Chaque œil voit une image légèrement différente. Le cerveau les assemble en une image unique et en relief : c'est la vision binoculaire.</p>
<p class="l" data-rv>Quand cet équilibre est perturbé, il peut se traduire par exemple par une fatigue visuelle, une vision double ou un strabisme. Le diagnostic relève du médecin.</p>
<div class="trio">{th}</div></div></div></section>
<figure class="band" style="margin:0"><div class="pxw">{M.img('verres', 'Boîte ancienne de verres d’essai et monture d’essai (photo d’illustration)', cls='px', sizes='100vw', extra=' data-px=".14"')}</div><div class="w" data-rv><h2>Sur rendez-vous, avenue <em>Habib Thameur</em>.</h2><small>Photo d'illustration · ne montre pas le cabinet</small></div></figure>
<section class="sec" id="venir"><div class="w venir"><figure data-rv><div class="in">{M.img('patch', 'Enfant portant un cache sur un œil (photo d’illustration)', sizes='(max-width: 960px) 92vw, 460px')}</div><figcaption class="cap">Photo d'illustration · ne montre pas le cabinet ni ses patients.</figcaption></figure>
<div><p class="kick" data-rv>Votre rendez-vous</p><h2 data-rv>Préparer votre <em>venue</em>.</h2><ol class="steps">
<li data-rv><div><h3>Prendre rendez-vous</h3><p>Par téléphone au <a href="{K.telhref(F['tel'])}">{F['tel']}</a>, ou par <a href="{wa}" target="_blank" rel="noopener">WhatsApp</a>.</p></div></li>
<li data-rv style="--d:.08s"><div><h3>Documents à apporter</h3><p>Ordonnance et documents utiles : liste {ph()}</p></div></li>
<li data-rv style="--d:.16s"><div><h3>Se rendre au cabinet</h3><p>Immeuble Essalama, 1er étage, appartement 208, avenue Habib Thameur, près de Carrefour Market.</p></div></li></ol></div></div></section>
<section class="sec cab" id="cabinet"><div class="w"><p class="kick" data-rv>Le cabinet</p><h2 data-rv>Informations <em>pratiques</em></h2><div class="cgrid">
<div class="card" data-rv><h3>Fiche du cabinet</h3><dl class="dl"><div><dt>Praticienne</dt><dd>Amina Romane</dd></div><div><dt>Profession</dt><dd>Orthoptiste</dd></div><div><dt>Diplôme</dt><dd>{ph()}</dd></div><div><dt>Langues</dt><dd>{ph()}</dd></div></dl>
<div style="margin-top:1.2rem">{lux.contacts(F, wa_msg=msg)}</div></div>
<div class="card" data-rv style="--d:.1s"><h3>Horaires</h3>{lux.hours(F)}<p class="sr">Séances et bilans sur rendez-vous.</p><div class="cta2"><a class="btn p" href="{K.telhref(F['tel'])}">{K.I['phone']}Appeler</a><a class="btn o" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a></div></div></div></div></section>
<section class="sec" id="rdv"><div class="w"><div class="rdv"><div data-rv><p class="kick">Rendez-vous</p><h2>Demander un <em>rendez-vous</em></h2><p class="l">Indiquez le jour et le moment souhaités : le message s'ouvre dans WhatsApp, et le cabinet vous confirme le créneau.</p><div class="fuse2" aria-hidden="true">{RINGS}</div></div>
<div data-rv style="--d:.1s">{lux.form(F, 'Bonjour, je souhaite un rendez-vous au cabinet d’orthoptie.', lux.MED_FORM)}</div></div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:5rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv>Immeuble <em>Essalama</em>, Nabeul</h2><p data-rv style="margin-top:1.2rem;opacity:.8">{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline;text-underline-offset:3px">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F)}'''
    return lux.page(F, 'Cabinet d’orthoptie Amina Romane · Nabeul (démo)', 'Cabinet d’orthoptie d’Amina Romane, immeuble Essalama, avenue Habib Thameur, Nabeul : l’orthoptie expliquée, coordonnées, horaires et demande de rendez-vous.', FONTS, CSS, body, '#111B24', lux.fav('#111B24', '#A9D5CF', 'AR'))
