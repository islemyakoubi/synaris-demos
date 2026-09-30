# La Cabane Café Resto (Nabeul) : « goûter ». Chocolat, fraise, crème. Hero gourmand : crêpe en médaillon organique, pastilles-stickers qui tournent,
# titre Fraunces à axes variables, séparateurs ondulés, carte extraite de la carte en ligne (sans prix), réservation WhatsApp. Fraunces + Outfit.
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..900,100;1,9..144,300..900,100&family=Outfit:wght@300;400;500;600;700'
CSS = '''
:root{--bg:#FFF4E6;--fg:#3B2218;--acc:#E8435A;--onacc:#fff;--line:rgba(59,34,24,.14);--hbg:rgba(255,244,230,.9);--disp:Fraunces,Georgia,serif;--sans:Outfit,system-ui,sans-serif;--r:999px;--choc:#3B2218;--mapbg:#F6E4CF;--rbg:#3B2218}
h1,h2,h3{font-variation-settings:'SOFT' 100,'opsz' 144;font-weight:700;letter-spacing:-.03em}em{font-style:italic;font-weight:400;color:var(--acc)}
.brand .mono{width:46px;height:46px;border-radius:50%;background:var(--acc);display:grid;place-items:center;color:#fff}.brand .mono svg{width:26px;height:26px}
.hero{display:grid;grid-template-columns:1.1fr .9fr;gap:3rem;align-items:center;min-height:100svh;padding:8.5rem 0 4rem}
.hero h1{font-size:clamp(3.6rem,9vw,9.4rem);line-height:.88}.hero h1 span{display:block}.lede{font-size:1.12rem;max-width:32rem;margin:1.8rem 0 2.2rem;opacity:.85}.acts{display:flex;gap:1rem;flex-wrap:wrap}
.plate{position:relative;justify-self:center;width:min(560px,100%)}.plate .m{aspect-ratio:1;border-radius:46% 54% 50% 50%/52% 46% 54% 48%;overflow:hidden;animation:wob 12s ease-in-out infinite;box-shadow:0 40px 80px rgba(59,34,24,.25)}.plate img{width:100%;height:100%;object-fit:cover}
@keyframes wob{50%{border-radius:54% 46% 44% 56%/46% 56% 44% 54%}}
.stk{position:absolute;display:grid;place-items:center;border-radius:50%;font:700 .9rem/1.1 var(--sans);text-align:center;text-transform:uppercase;letter-spacing:.06em}
.stk.a{width:130px;height:130px;background:var(--choc);color:#FFF4E6;right:-10px;top:-10px;animation:spin 18s linear infinite}.stk.b{width:110px;height:110px;background:#FFD166;color:var(--choc);left:-20px;bottom:30px;transform:rotate(-12deg)}
.stk.a svg{position:absolute;inset:0;width:100%;height:100%}@keyframes spin{to{transform:rotate(360deg)}}
.wave{display:block;width:100%;height:60px}.wave path{fill:var(--choc)}
.choc{background:var(--choc);color:#FFF4E6;--line:rgba(255,244,230,.16)}.choc em{color:#FF8FA0}.choc .kick{color:#FFD166}
.sec{padding:7rem 0}.sec h2{font-size:clamp(2.6rem,5.6vw,5.4rem);line-height:.95}
.menu2{display:grid;grid-template-columns:1fr 1fr;gap:4rem;margin-top:3.6rem}.menu2 h3{font-size:2rem;margin-bottom:1rem;display:flex;align-items:center;gap:.8rem}.menu2 h3 svg{width:40px;height:40px;color:#FFD166}
.menu2 ul{list-style:none;margin:0;padding:0}.menu2 li{display:flex;align-items:baseline;gap:.8rem;padding:1rem 0;border-bottom:1px dashed var(--line);font-size:1.15rem}.menu2 li:after{content:'';flex:1;order:1;border-bottom:1px dotted rgba(255,244,230,.25)}.menu2 li .ph{order:2;color:#FFD166}
.pics{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem;margin-top:4rem}.pics figure{margin:0;border-radius:32px;overflow:hidden;position:relative;aspect-ratio:4/5;transform:rotate(-2deg);transition:transform .6s var(--ease)}.pics figure:nth-child(2){transform:rotate(2deg) translateY(2rem)}.pics figure:hover{transform:rotate(0) scale(1.02)}
.pics img{width:100%;height:100%;object-fit:cover}.pics figcaption{position:absolute;left:1rem;bottom:1rem;background:#FFF4E6;color:var(--choc);border-radius:99px;padding:.35rem .8rem;font-size:.72rem}
.two{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem}.card{background:#fff;border-radius:32px;padding:2.6rem;box-shadow:0 20px 50px rgba(59,34,24,.07)}.card h3{font-size:1.9rem;margin-bottom:1rem}
.rdv{display:grid;grid-template-columns:.9fr 1.1fr;gap:4rem;align-items:start}.rdv .card{background:#FFE1E5}
.beach{position:relative;height:60vh;min-height:360px;overflow:hidden;isolation:isolate;display:grid;place-items:center;color:#fff;text-align:center}.beach:after{content:'';position:absolute;inset:0;z-index:-1;background:rgba(59,34,24,.35)}.beach h2{font-size:clamp(2.6rem,7vw,6.4rem)}.beach em{color:#FFD166}
.mapw{border-radius:32px}
@media(max-width:960px){.hero,.menu2,.two,.rdv{grid-template-columns:1fr}.plate{width:min(440px,92%)}.pics{grid-template-columns:1fr 1fr}.pics figure:nth-child(3){display:none}}
@media(max-width:760px){.sec{padding:5rem 0}.card{padding:1.6rem}.stk.a{width:100px;height:100px;right:-6px;font-size:.72rem}.stk.b{width:86px;height:86px;left:-6px;font-size:.72rem}.pics figure:nth-child(2){transform:rotate(2deg)}}
'''
NOTE = "Démo : aucune donnée n'est enregistrée. Le bouton ouvre WhatsApp avec votre demande ; La Cabane confirme la réservation."
def build(F, M):
    msg = 'Bonjour, je souhaite réserver une table à La Cabane.'
    brand = f'<span class="mono">{IC["crepe"]}</span><span><b>La Cabane</b><small>Café · Resto · Nabeul</small></span>'
    links = [('La carte', '#carte'), ('En images', '#images'), ('Infos', '#infos'), ('Réserver', '#rdv')]
    sucre = ['Crêpe chocolat amande', 'Crêpe chocolat banane', 'Petit-déjeuner']
    bois = ['Jus de fraise', 'Smoothie banane', 'Thé aux pignons']
    li = lambda L: ''.join(f'<li>{x}{ph("prix à confirmer")}</li>' for x in L)
    ring = '<svg viewBox="0 0 100 100" aria-hidden="true"><defs><path id="c" d="M50 50m-36 0a36 36 0 1 1 72 0a36 36 0 1 1-72 0"/></defs><text font-size="10.5" font-family="Outfit" font-weight="700" letter-spacing="2.4" fill="#FFF4E6"><textPath href="#c">CRÊPES · JUS · SMOOTHIES · CAFÉ · </textPath></text></svg>'
    spec = [('text', 'Nom et prénom'), ('tel', 'Téléphone'), ('date', 'Date'), ('select', 'Heure', ['Matin', 'Midi', 'Après-midi', 'Soir']), ('select', 'Personnes', ['1', '2', '3', '4', '5', '6', 'Plus de 6']), ('textarea', 'Message (facultatif)')]
    body = f'''{lux.header(brand, links, ('Réserver', '#rdv'))}<main id="main">
<section class="w hero" id="top"><div><p class="kick rise">Café-restaurant · Nabeul</p><h1 class="rise d1"><span>La</span><span><em>Cabane</em></span></h1>
<p class="lede rise d2">Crêpes, jus, smoothies, pâtes et petit-déjeuner : un café-restaurant à Nabeul. Réservation par téléphone ou WhatsApp.</p>
<div class="acts rise d3"><a class="btn p" href="#rdv">Réserver une table {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div></div>
<div class="plate rise d2"><div class="m">{M.img('hero', 'Crêpe au chocolat et à la noix de coco (photo d’illustration)', sizes='(max-width: 960px) 90vw, 560px', lazy=False)}</div><span class="stk a">{ring}</span><span class="stk b">Photo<br>d'illus&shy;tration</span></div></section>
<svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 60V30C120 0 240 0 360 30s240 30 360 0 240-30 360 0 240 30 360 0v30z"/></svg>
<section class="sec choc" id="carte"><div class="w"><p class="kick" data-rv>La carte</p><h2 data-rv>Quelques <em>douceurs</em> de la carte.</h2>
<div class="menu2"><div data-rv><h3>{IC['crepe']}Crêpes & petit-déj'</h3><ul>{li(sucre)}</ul></div><div data-rv style="--d:.12s"><h3>{IC['cup']}À boire</h3><ul>{li(bois)}</ul></div></div>
<p class="note" data-rv style="margin-top:2rem">Extraits de la carte publiée en ligne (lacarte.menu), à confirmer par l'établissement ; les pâtes figurent aussi à la carte. Prix et disponibilités à confirmer.</p>
<div class="pics" id="images"><figure data-rv>{M.img('fraise', 'Crêpe aux fraises, banane et chocolat (photo d’illustration)', sizes='(max-width: 960px) 46vw, 380px')}<figcaption>Illustration</figcaption></figure>
<figure data-rv style="--d:.1s">{M.img('kiwi', 'Smoothie au kiwi (photo d’illustration)', sizes='(max-width: 960px) 46vw, 380px')}<figcaption>Illustration</figcaption></figure>
<figure data-rv style="--d:.2s">{M.img('jus', 'Jus de fruits (photo d’illustration)', sizes='380px')}<figcaption>Illustration</figcaption></figure></div></div></section>
<svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true" style="transform:scaleY(-1)"><path d="M0 60V30C120 0 240 0 360 30s240 30 360 0 240-30 360 0 240 30 360 0v30z"/></svg>
<section class="sec" id="infos"><div class="w two"><div class="card" data-rv><h3>Horaires</h3>{lux.hours(F)}</div><div class="card" data-rv style="--d:.1s"><h3>Contact</h3>{lux.contacts(F, 'WhatsApp · réservation', msg, [('Facebook', f'<a href="{F["fb"]}" target="_blank" rel="noopener">facebook.com/cafe.laCABANE</a>')])}</div></div></section>
<figure class="beach" style="margin:0"><div class="pxw">{M.img('plage', 'Parasols sur la plage de Nabeul (photo d’illustration)', cls='px', sizes='100vw', extra=' data-px=".15"')}</div><h2 data-rv>Nabeul, <em>côté plage</em></h2></figure>
<section class="sec" id="rdv"><div class="w rdv"><div data-rv><p class="kick">Réserver</p><h2>Une table à <em>La Cabane</em>.</h2><p style="margin-top:1.4rem;opacity:.8">Choisissez la date, le moment et le nombre de personnes : la demande s'ouvre dans WhatsApp.</p></div>
<div class="card" data-rv style="--d:.1s">{lux.form(F, 'Bonjour, je souhaite réserver une table à La Cabane.', spec, 'Envoyer la réservation', NOTE)}</div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">À <em>Nabeul</em>.</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:underline">Rechercher sur Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, '<span><b>La Cabane</b><small>Café · Resto · Nabeul</small></span>', links)}{lux.dock(F, 'Réserver', '#rdv', 'wa')}'''
    return lux.page(F, 'La Cabane Café Resto · Nabeul (démo)', 'La Cabane, café-restaurant à Nabeul : crêpes, jus, smoothies, contact et réservation.', FONTS, CSS, body, '#FFF4E6', lux.fav('#E8435A', '#fff', 'C', 'Georgia'))
