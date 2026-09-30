# Laboratoire Majdoubi (Hammamet) : « verre ». Bleu-violet froid, verre dépoli. Hero : tubes à essai plein cadre, cartes en verre flottantes,
# bulles montantes animées, grille d'informations pratiques (à confirmer), mosaïque, formulaire d'information (aucun résultat transmis). Red Hat Display + Red Hat Text.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Red+Hat+Display:wght@400;500;600;700;800;900&family=Red+Hat+Text:wght@300;400;500;600'
CSS = '''
:root{--bg:#F3F5FF;--fg:#141A3A;--acc:#4338CA;--onacc:#fff;--line:rgba(20,26,58,.12);--hbg:rgba(243,245,255,.82);--disp:'Red Hat Display',system-ui,sans-serif;--sans:'Red Hat Text',system-ui,sans-serif;--r:16px;--mapbg:#E4E8FB;--rbg:#141A3A}
h1,h2,h3{font-weight:800;letter-spacing:-.035em}.brand .mono{width:44px;height:44px;border-radius:14px;background:linear-gradient(135deg,#6D5DF6,#22D3EE);display:grid;place-items:center;color:#fff}.brand .mono svg{width:24px;height:24px}
.hdr{color:#fff}.hdr.scrolled{color:var(--fg)}
.hero{position:relative;min-height:100svh;display:flex;align-items:flex-end;overflow:hidden;isolation:isolate;color:#fff}
.hero:after{content:'';position:absolute;inset:0;z-index:-1;background:linear-gradient(0deg,rgba(20,26,58,.95) 0%,rgba(67,56,202,.45) 50%,rgba(20,26,58,.5) 100%)}
.bub{position:absolute;inset:0;z-index:-1;pointer-events:none;overflow:hidden}.bub i{position:absolute;bottom:-40px;border-radius:50%;border:1px solid rgba(255,255,255,.5);background:rgba(255,255,255,.08);animation:up linear infinite}
@keyframes up{to{transform:translateY(-110vh)}}
.hin{padding:10rem 0 3rem;display:grid;grid-template-columns:1.2fr .8fr;gap:3rem;align-items:end}.hero h1{font-size:clamp(3.4rem,8.6vw,8.6rem);line-height:.88}.hero h1 span{display:block;background:linear-gradient(90deg,#A5B4FC,#67E8F9);-webkit-background-clip:text;background-clip:text;color:transparent}
.lede{max-width:33rem;font-size:1.08rem;margin:1.6rem 0 2.2rem;opacity:.9}.acts{display:flex;gap:1rem;flex-wrap:wrap}.hero .btn.p{background:#fff;color:var(--acc)}.hero .btn.o{color:#fff}
.glass{display:grid;gap:.8rem}.glass div{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.28);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-radius:20px;padding:1.2rem 1.4rem;animation:bob 6s ease-in-out infinite}.glass div:nth-child(2){animation-delay:1s;margin-left:2rem}.glass div:nth-child(3){animation-delay:2s}
@keyframes bob{50%{transform:translateY(-8px)}}.glass small{display:block;font:700 .62rem/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.75;margin-bottom:.4rem}.glass p{margin:0;font:700 1.15rem/1.2 var(--disp)}
.sec{padding:8rem 0}.sec h2{font-size:clamp(2.4rem,5vw,4.8rem);line-height:.96}.sec h2 span{color:var(--acc)}
.prac{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin-top:4rem}.prac article{background:rgba(255,255,255,.7);border:1px solid #fff;box-shadow:0 20px 50px rgba(67,56,202,.08);backdrop-filter:blur(10px);border-radius:24px;padding:2rem 1.6rem;transition:transform .6s var(--ease)}
.prac article:hover{transform:translateY(-6px)}.prac svg{width:56px;height:56px;color:var(--acc);margin-bottom:2rem}.prac h3{font-size:1.35rem;margin-bottom:.5rem}.prac p{opacity:.72;margin:0 0 1rem;font-size:.94rem}
.mos{display:grid;grid-template-columns:1.2fr .8fr 1fr;gap:1rem;height:520px}.mos figure{margin:0;position:relative;overflow:hidden;border-radius:24px}.mos img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.6s var(--ease)}.mos figure:hover img{transform:scale(1.05)}
.mos figcaption{position:absolute;left:1rem;bottom:1rem;background:rgba(255,255,255,.85);backdrop-filter:blur(6px);border-radius:99px;padding:.35rem .8rem;font-size:.72rem}
.two{display:grid;grid-template-columns:1fr 1fr;gap:1rem}.card{background:#fff;border-radius:24px;padding:2.6rem;box-shadow:0 20px 50px rgba(67,56,202,.06)}.card h3{font-size:1.7rem;margin-bottom:1.2rem}
.dl{margin:0}.dl div{display:grid;grid-template-columns:10rem 1fr;gap:1rem;padding:.9rem 0;border-bottom:1px solid var(--line)}.dl dt{font:700 .62rem/1.7 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.55}.dl dd{margin:0}
.rdv{display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem;background:linear-gradient(135deg,#1E1B4B,#4338CA);color:#fff;border-radius:32px;padding:4.5rem;--line:rgba(255,255,255,.2);--fln:rgba(255,255,255,.3);--fbg:rgba(255,255,255,.08);--acc:#fff;--onacc:#4338CA}.rdv select option{color:#141A3A}
.mapw{border-radius:24px}
@media(max-width:1020px){.prac{grid-template-columns:1fr 1fr}}
@media(max-width:960px){.hin,.two,.rdv{grid-template-columns:1fr}.glass div:nth-child(2){margin-left:0}.mos{grid-template-columns:1fr 1fr;height:auto}.mos figure{min-height:260px}.mos figure:first-child{grid-column:span 2}.rdv{padding:2.4rem 1.4rem}}
@media(max-width:760px){.sec{padding:5.5rem 0}.prac{grid-template-columns:1fr}.card{padding:1.6rem}.dl div{grid-template-columns:1fr;gap:.1rem}}
'''
NOTE = "Démo : aucune donnée n'est enregistrée. Le bouton ouvre WhatsApp avec votre message. Aucun résultat d'analyse n'est communiqué par WhatsApp. En cas d'urgence, appelez le 190 (SAMU)."
def build(F, M):
    msg = 'Bonjour, je souhaite un renseignement auprès du laboratoire.'
    brand = f'<span class="mono">{IC["flask"]}</span><span><b>Laboratoire Majdoubi</b><small>Analyses médicales · Hammamet</small></span>'
    links = [('Le laboratoire', '#labo'), ('Pratique', '#pratique'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    pr = [('clock', 'Horaires de prélèvement', 'Jours et heures d’ouverture au public.'), ('doc', 'Ordonnance', 'Documents à présenter à l’accueil.'), ('cal', 'Délais', 'Délais habituels de remise des résultats.'), ('shield', 'Remise des résultats', 'Modalités de remise, en toute confidentialité.')]
    prh = ''.join(f'<article data-rv style="--d:{i*.1:.1f}s">{IC[k]}<h3>{t}</h3><p>{p}</p>{ph()}</article>' for i, (k, t, p) in enumerate(pr))
    import random; random.seed(7)
    bub = ''.join(f'<i style="left:{random.randint(2,96)}%;width:{(s:=random.randint(8,34))}px;height:{s}px;animation-duration:{random.randint(12,26)}s;animation-delay:-{random.randint(0,20)}s"></i>' for _ in range(16))
    spec = [('text', 'Nom et prénom'), ('tel', 'Téléphone'), ('date', 'Jour de passage envisagé'), ('textarea', 'Votre question (facultatif)')]
    body = f'''{lux.header(brand, links, ('Contact', '#rdv'))}<main id="main">
<section class="hero" id="top"><div class="pxw">{M.img('hero', 'Tubes à essai dans un laboratoire (photo d’illustration)', cls='px', sizes='100vw', lazy=False, extra=' data-px=".14"')}</div><div class="bub" aria-hidden="true">{bub}</div>
<div class="w hin"><div><p class="kick rise" style="color:#A5B4FC">Laboratoire d'analyses médicales · Hammamet</p><h1 class="rise d1">Laboratoire<span>Majdoubi</span></h1>
<p class="lede rise d2">93 avenue du Koweït, en face de la Tour bleue, à Hammamet. Renseignements par téléphone ou via WhatsApp.</p>
<div class="acts rise d3"><a class="btn p" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a><a class="btn o" href="#rdv">Poser une question {IC['arrow']}</a></div></div>
<div class="glass rise d2"><div><small>Mercredi</small><p>{F['wed']}</p></div><div><small>Adresse</small><p>93 av. du Koweït</p></div><div><small>Repère</small><p>En face de la Tour bleue</p></div></div></div></section>
<section class="sec" id="labo"><div class="w two"><div data-rv><p class="kick">Le laboratoire</p><h2>Analyses médicales, <span>à Hammamet</span>.</h2><p style="font-size:1.12rem;margin-top:1.6rem;max-width:34rem;opacity:.85">Le Laboratoire Majdoubi est un laboratoire d'analyses médicales situé avenue du Koweït. Les informations pratiques ci-dessous restent à compléter par le laboratoire.</p></div>
<div class="card" data-rv style="--d:.1s"><h3>Fiche</h3><dl class="dl"><div><dt>Établissement</dt><dd>Laboratoire Majdoubi</dd></div><div><dt>Activité</dt><dd>Analyses médicales</dd></div><div><dt>Biologiste responsable</dt><dd>{ph()}</dd></div><div><dt>Adresse</dt><dd>{F['addr']}</dd></div></dl></div></div></section>
<section class="sec" id="pratique" style="padding-top:0"><div class="w"><p class="kick" data-rv>Pratique</p><h2 data-rv>Avant de <span>venir</span>.</h2><div class="prac">{prh}</div>
<p class="note" data-rv style="margin-top:2rem">Rubriques à compléter avec les informations fournies par le laboratoire. Aucun conseil de santé n'est donné par ce site.</p></div></section>
<section class="sec" style="padding-top:0"><div class="w mos"><figure data-rv>{M.img('verre', 'Verrerie de laboratoire (photo d’illustration)', sizes='(max-width: 960px) 92vw, 520px')}<figcaption>Illustration · ne montre pas le laboratoire</figcaption></figure>
<figure data-rv style="--d:.1s">{M.img('micro', 'Microscope de laboratoire (photo d’illustration)', sizes='(max-width: 960px) 46vw, 340px')}<figcaption>Illustration</figcaption></figure>
<figure data-rv style="--d:.2s">{M.img('tubes', 'Tubes de prélèvement (photo d’illustration)', sizes='(max-width: 960px) 46vw, 420px')}<figcaption>Illustration</figcaption></figure></div></section>
<section class="sec" id="horaires" style="padding-top:0"><div class="w two"><div class="card" data-rv><h3>Horaires</h3>{lux.hours(F)}</div><div class="card" data-rv style="--d:.1s"><h3>Contact</h3>{lux.contacts(F, 'WhatsApp · renseignements', msg)}</div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w"><div class="rdv"><div data-rv><p class="kick" style="color:#A5B4FC">Contact</p><h2 style="color:#fff">Poser une question.</h2><p style="margin-top:1.4rem;opacity:.85">Le message s'ouvre dans WhatsApp. Aucun résultat d'analyse n'est transmis par ce canal.</p></div>
<div data-rv style="--d:.1s">{lux.form(F, 'Bonjour, je souhaite un renseignement auprès du laboratoire.', spec, 'Envoyer la question', NOTE)}</div></div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Avenue du <span>Koweït</span>.</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F, 'Écrire', '#rdv', 'wa')}'''
    return lux.page(F, 'Laboratoire Majdoubi · Analyses médicales à Hammamet (démo)', 'Laboratoire d’analyses médicales Majdoubi, 93 avenue du Koweït, Hammamet : coordonnées, horaires et renseignements.', FONTS, CSS, body, '#141A3A', lux.fav('#4338CA', '#fff', 'LM', 'Arial', 'rect'))
