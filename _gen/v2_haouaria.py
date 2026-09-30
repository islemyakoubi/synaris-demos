# Haouaria Beach (El Haouaria) — v2 bespoke design: bright Mediterranean seaside.
# White / turquoise / sand + coral, split photo hero with wave, dish ticker, "fish of the day" board,
# swipeable menu cards, bento sunset gallery, turquoise reservation band. Fonts: Bricolage Grotesque + DM Sans + Tajawal (Arabic).
from gen_v2 import esc, walink, RIBBON, CONSULTED, page, WA_SVG, PHONE_SVG, PIN_SVG
SLUG = 'haouaria-beach'
WA, WA_DISP, TEL = '21654006083', '+216 54 006 083', '+21654006083'
ADDR, MAPQ = 'Plage d’El Haouaria, 8045 El Haouaria', 'Haouaria Beach, El Haouaria'
FONTS = 'https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=Tajawal:wght@500;800&display=swap'
PH = '<span class="ph">à confirmer</span>'

CSS = r'''
:root{--sea:#0B9FB0;--sea-d:#067585;--deep:#063E4D;--sky:#E6F7F8;--sand:#F8F1E6;--sand2:#EFE3CF;--coral:#FF7A59;--coral-d:#E85F3E;--ink:#0B2530;--muted:#557079;--white:#fff;
--f-d:'Bricolage Grotesque',system-ui,sans-serif;--f-t:'DM Sans',system-ui,sans-serif;--f-ar:'Tajawal',sans-serif}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--white);color:var(--ink);font:400 1rem/1.6 var(--f-t);-webkit-font-smoothing:antialiased}
img{max-width:100%;height:auto;display:block}a{color:inherit}h1,h2,h3{font-family:var(--f-d);font-weight:800;line-height:1.02;letter-spacing:-.025em;margin:0 0 .7rem}
.wrap{width:min(1200px,100% - 2.5rem);margin-inline:auto}.ar{font-family:var(--f-ar);font-weight:800;direction:rtl}
.ph{display:inline-block;font:500 .72rem/1.2 var(--f-t);color:var(--sea-d);background:var(--sky);border:1px dashed #7CCBD3;border-radius:6px;padding:.12rem .4rem;vertical-align:middle;white-space:nowrap}
.ph.long{white-space:normal}.skip{position:absolute;left:-999px}.skip:focus{left:1rem;top:1rem;z-index:99;background:#fff;padding:.5rem 1rem}
.ribbon{background:var(--sky);color:var(--deep);font-size:.74rem;text-align:center;padding:.4rem 1rem}.ribbon b{color:var(--coral-d)}
.hd{position:sticky;top:0;z-index:40;background:rgba(255,255,255,.9);backdrop-filter:blur(10px);transition:box-shadow .2s}.hd.scrolled{box-shadow:0 6px 24px -12px rgba(6,62,77,.3)}
.hd .wrap{display:flex;align-items:center;justify-content:space-between;height:70px;gap:1rem}
.logo{display:flex;align-items:center;gap:.55rem;text-decoration:none;font:800 1.3rem/1 var(--f-d);letter-spacing:-.03em}
.logo svg{width:38px;height:38px}.logo span small{display:block;font:500 .68rem/1.2 var(--f-t);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.nav{display:none}.nav a{text-decoration:none;font-weight:500;padding:.5rem .9rem;border-radius:999px}.nav a:hover{background:var(--sky);color:var(--sea-d)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.55rem;border-radius:14px;padding:.95rem 1.35rem;font:700 1rem/1 var(--f-t);text-decoration:none;border:0;cursor:pointer;transition:transform .15s,box-shadow .15s}
.btn:hover{transform:translateY(-2px)}.btn svg{width:20px;height:20px}
.btn-coral{background:var(--coral);color:#fff;box-shadow:0 10px 22px -10px rgba(232,95,62,.8)}.btn-sea{background:var(--sea);color:#fff}.btn-white{background:#fff;color:var(--deep)}
.btn-soft{background:var(--sky);color:var(--sea-d)}
.hd .btn{display:none}
.burger{width:46px;height:46px;border-radius:14px;border:0;background:var(--sky);display:grid;place-items:center;cursor:pointer}
.burger i,.burger i:before,.burger i:after{display:block;width:18px;height:2px;background:var(--deep);border-radius:2px;position:relative;content:''}.burger i:before{position:absolute;top:-6px}.burger i:after{position:absolute;top:6px}
.nav.open{display:flex;position:absolute;top:70px;left:.8rem;right:.8rem;flex-direction:column;background:#fff;border-radius:18px;padding:.8rem;box-shadow:0 20px 40px -15px rgba(6,62,77,.35)}
/* hero split */
.hero{background:var(--sand);position:relative;overflow:hidden}
.hero .grid{display:grid}
.hero .txt{padding:2.4rem 1.25rem 2.6rem;position:relative;z-index:2}
.pill{display:inline-flex;align-items:center;gap:.5rem;background:#fff;border-radius:999px;padding:.4rem .9rem .4rem .45rem;font-size:.85rem;font-weight:500;box-shadow:0 4px 14px -6px rgba(6,62,77,.25)}
.pill i{width:24px;height:24px;border-radius:50%;background:var(--coral);display:grid;place-items:center;color:#fff;font-style:normal;font-size:.8rem}
.hero h1{font-size:clamp(2.7rem,9vw,5.4rem);margin:1.2rem 0 1rem}.hero h1 span{color:var(--sea)}
.hero h1 .u{position:relative;white-space:nowrap}.hero h1 .u svg{position:absolute;left:0;right:0;bottom:-.12em;width:100%;height:.3em}
.hero .lead{font-size:1.12rem;color:var(--muted);max-width:32rem}
.acts{display:flex;flex-wrap:wrap;gap:.7rem;margin:1.7rem 0 1.4rem}
.chips{display:flex;flex-wrap:wrap;gap:.5rem}.chips span{background:#fff;border-radius:10px;padding:.45rem .75rem;font-size:.86rem;font-weight:500}.chips b{color:var(--coral-d)}
.hero .pic{position:relative;min-height:380px}
.hero .pic>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.floatcard{position:absolute;left:1rem;bottom:2.4rem;background:#fff;border-radius:18px;padding:.6rem .9rem .6rem .6rem;display:flex;gap:.7rem;align-items:center;box-shadow:0 20px 40px -18px rgba(6,62,77,.5);max-width:270px}
.floatcard img{width:62px;height:62px;border-radius:12px;object-fit:cover}.floatcard b{display:block;font:700 1rem/1.2 var(--f-d)}.floatcard small{color:var(--muted);font-size:.8rem;line-height:1.3;display:block}
.wave{display:block;width:100%;height:60px;margin-top:-1px}
/* ticker */
.ticker{background:var(--coral);color:#fff;overflow:hidden;white-space:nowrap;padding:.95rem 0;font:700 1.25rem/1 var(--f-d)}
.ticker div{display:inline-flex;gap:2rem;animation:tick 30s linear infinite;padding-left:2rem}.ticker span:nth-child(even){opacity:.7}
@keyframes tick{to{transform:translateX(-50%)}}@media (prefers-reduced-motion:reduce){.ticker div{animation:none}}
/* sections */
.sec{padding:5rem 0}.tag{display:inline-block;font:700 .78rem/1 var(--f-t);letter-spacing:.14em;text-transform:uppercase;color:var(--sea-d);background:var(--sky);border-radius:999px;padding:.5rem .85rem}
.sec h2{font-size:clamp(2.1rem,5.5vw,3.6rem);margin-top:.9rem}.sub{color:var(--muted);max-width:38rem;font-size:1.05rem}
/* fish of the day */
.fish{display:grid;gap:1.5rem;align-items:stretch}
.fish .ph-wrap{position:relative;border-radius:28px;overflow:hidden;min-height:320px}.fish .ph-wrap img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.fish .ph-wrap .ar{position:absolute;top:1rem;right:1rem;background:rgba(255,255,255,.92);color:var(--deep);font-size:1.5rem;border-radius:14px;padding:.35rem .8rem}
.board{background:var(--deep);color:#EAF7F8;border-radius:28px;padding:1.8rem 1.4rem;position:relative;overflow:hidden}
.board:after{content:'';position:absolute;right:-60px;top:-60px;width:180px;height:180px;border-radius:50%;background:radial-gradient(circle,rgba(11,159,176,.5),transparent 70%)}
.board .date{display:flex;justify-content:space-between;align-items:center;font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:#8FD3DA;border-bottom:1px dashed rgba(255,255,255,.25);padding-bottom:.9rem}
.board h3{font-size:2rem;margin:1rem 0 .4rem}.board ul{list-style:none;padding:0;margin:1rem 0 1.4rem}
.board li{display:grid;grid-template-columns:auto 1fr auto;gap:.8rem;align-items:center;padding:.8rem 0;border-bottom:1px solid rgba(255,255,255,.12)}
.board li i{width:38px;height:38px;border-radius:12px;background:rgba(255,255,255,.1);display:grid;place-items:center;font-style:normal}
.board li b{font:700 1.1rem/1.2 var(--f-d)}.board li small{display:block;color:#9CC6CC;font-size:.82rem}.board li em{font-style:normal;font-size:.85rem;color:#FFD2C4}
.board .ph{background:rgba(255,255,255,.1);color:#BFEFF3;border-color:rgba(255,255,255,.35)}
.board .note{font-size:.8rem;color:#8FB7BD;margin-top:.9rem}
/* menu scroller */
.mhead{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:end;gap:1rem}
.scroller{display:grid;grid-auto-flow:column;grid-auto-columns:78%;gap:1rem;overflow-x:auto;scroll-snap-type:x mandatory;padding:1.8rem 1.25rem 1.2rem;margin:0 -1.25rem;scrollbar-width:thin}
.dish{scroll-snap-align:start;background:#fff;border-radius:24px;overflow:hidden;border:1px solid #E3EEF0;display:flex;flex-direction:column;box-shadow:0 18px 36px -26px rgba(6,62,77,.45)}
.dish .im{aspect-ratio:4/3;overflow:hidden;background:var(--sky)}.dish .im img{width:100%;height:100%;object-fit:cover;transition:transform .5s}.dish:hover .im img{transform:scale(1.05)}
.dish .bd{padding:1.1rem 1.2rem 1.3rem;display:flex;flex-direction:column;gap:.35rem;flex:1}
.dish h3{font-size:1.35rem;margin:0}.dish p{margin:0;color:var(--muted);font-size:.92rem;flex:1}
.dish .row{display:flex;justify-content:space-between;align-items:center;margin-top:.6rem;font-size:.85rem}.dish .row b{font-family:var(--f-d)}
.lbl{font-size:.7rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--coral-d);background:#FFEDE7;border-radius:6px;padding:.2rem .45rem}
.shell{display:grid;place-items:center;height:100%;background:linear-gradient(135deg,#0B9FB0,#063E4D)}.shell svg{width:44%;color:#fff;opacity:.9}
/* bento */
.bento{display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:160px;gap:.8rem;margin-top:2.2rem}
.bento a{position:relative;border-radius:22px;overflow:hidden;display:block}.bento img{width:100%;height:100%;object-fit:cover;transition:transform .6s}.bento a:hover img{transform:scale(1.05)}
.bento a span{position:absolute;left:.7rem;bottom:.7rem;background:rgba(255,255,255,.92);border-radius:999px;padding:.3rem .7rem;font-size:.78rem;font-weight:700;color:var(--deep)}
.bento .b1{grid-column:1/-1;grid-row:span 2}.bento .b4{grid-column:1/-1}
.lb{position:fixed;inset:0;z-index:90;background:rgba(6,30,38,.94);display:none;place-items:center;padding:1.5rem}.lb.open{display:grid}
.lb img{max-height:88vh;width:auto;border-radius:14px}.lb button{position:absolute;top:1rem;right:1rem;width:48px;height:48px;border-radius:50%;border:0;background:#fff;font-size:1.6rem;cursor:pointer}
/* reservation band */
.resa{background:var(--sea);color:#fff;position:relative}
.resa .wave-top{position:absolute;top:-59px;left:0;width:100%;height:60px}
.resa .in{display:grid;gap:2rem;align-items:center}
.resa h2{color:#fff}.resa .sub{color:#D7F3F5}.resa .ar{font-size:1.6rem;color:#FFE1D6}
.form{background:#fff;color:var(--ink);border-radius:26px;padding:1.3rem;display:grid;grid-template-columns:1fr 1fr;gap:.8rem;box-shadow:0 30px 60px -30px rgba(3,40,50,.7)}
.form .full{grid-column:1/-1}.form label{display:grid;gap:.3rem;font-size:.8rem;font-weight:700;color:var(--muted)}
.form input,.form select,.form textarea{font:inherit;font-weight:400;color:var(--ink);border:0;background:var(--sky);border-radius:12px;padding:.8rem .9rem;min-height:48px;width:100%}
.form input:focus,.form select:focus,.form textarea:focus{outline:3px solid #7CCBD3}.form textarea{min-height:80px;resize:vertical}
.form .btn{width:100%;padding:1.05rem}.fine{font-size:.78rem;color:var(--muted)}
/* infos */
.infos{display:grid;gap:1rem}
.card{background:var(--sand);border-radius:24px;padding:1.5rem}.card .ic{width:46px;height:46px;border-radius:14px;background:#fff;display:grid;place-items:center;color:var(--sea-d);margin-bottom:.9rem}.card .ic svg{width:22px;height:22px}
.card h3{font-size:1.3rem;margin:0 0 .3rem}.card p{margin:0;color:var(--muted)}.card a{font-weight:700;color:var(--sea-d)}
.card.rt{background:var(--deep);color:#fff}.card.rt p{color:#A9CDD2}.card.rt .big{font:800 3rem/1 var(--f-d);color:#fff}.card.rt a{color:#8FE3EC}
.mapw{margin-top:1rem;border-radius:28px;overflow:hidden;height:360px;background:var(--sky)}.mapw iframe{width:100%;height:100%;border:0;display:block}
.caveat{font-size:.82rem;color:var(--muted);margin-top:.6rem}
.ft{background:var(--deep);color:#A9CDD2;padding:3rem 0 6.5rem;font-size:.9rem}.ft a{color:#CFF3F6}
.ft .top{display:grid;gap:1.5rem}.ft .logo{color:#fff}.ft details{margin-top:1.5rem;font-size:.8rem}.ft summary{cursor:pointer}
.badge{display:inline-flex;align-items:center;gap:.4rem;text-decoration:none;border:1px solid rgba(255,255,255,.25);border-radius:999px;padding:.3rem .8rem;margin-top:.6rem}.badge i{width:8px;height:8px;border-radius:50%;background:var(--coral)}
.fab{position:fixed;left:1rem;right:1rem;bottom:1rem;z-index:45;display:flex;gap:.6rem}
.fab a{flex:1;border-radius:16px;box-shadow:0 14px 30px -12px rgba(6,62,77,.6)}
@media (min-width:760px){
 .hero .grid{grid-template-columns:1fr 1fr;min-height:620px}.hero .txt{padding:4.5rem 3rem 4rem max(1.25rem,calc((100vw - 1200px)/2));display:flex;flex-direction:column;justify-content:center}
 .hero .pic{border-bottom-left-radius:160px;overflow:hidden}.floatcard{left:-2rem;bottom:4rem}
 .fish{grid-template-columns:1.1fr .9fr}.board{padding:2.4rem 2.2rem}
 .scroller{grid-auto-flow:row;grid-template-columns:repeat(3,1fr);overflow:visible;margin:0;padding:2rem 0 0}
 .bento{grid-template-columns:repeat(4,1fr);grid-auto-rows:210px}.bento .b1{grid-column:span 2;grid-row:span 2}.bento .b4{grid-column:span 2}
 .resa .in{grid-template-columns:.9fr 1.1fr;gap:4rem}.form{padding:1.8rem}
 .infos{grid-template-columns:repeat(4,1fr)}.ft .top{grid-template-columns:1.5fr 1fr 1fr}
 .fab{display:none}.ft{padding-bottom:3rem}
}
@media (min-width:1000px){.nav{display:flex;gap:.2rem}.nav.open{position:static;box-shadow:none;flex-direction:row;padding:0}.burger{display:none}.hd .btn{display:inline-flex;padding:.8rem 1.15rem}.scroller{grid-template-columns:repeat(3,1fr)}}
'''

SUN_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
LOGO_SVG = '<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="20" fill="#E6F7F8"/><circle cx="20" cy="17" r="7" fill="#FF7A59"/><path d="M4 24c4 0 4-2.5 8-2.5s4 2.5 8 2.5 4-2.5 8-2.5 4 2.5 8 2.5v4c-4 0-4-2.5-8-2.5s-4 2.5-8 2.5-4-2.5-8-2.5-4 2.5-8 2.5z" fill="#0B9FB0"/><path d="M8 31c3 0 3-2 6-2s3 2 6 2 3-2 6-2 3 2 6 2" stroke="#067585" stroke-width="2" fill="none"/></svg>'
SHELL_SVG = '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" aria-hidden="true"><path d="M32 8C18 8 8 20 8 34c0 8 4 14 10 18h28c6-4 10-10 10-18C56 20 46 8 32 8z"/><path d="M32 8v44M20 12c-2 10-2 26 2 40M44 12c2 10 2 26-2 40M11 24c6 4 12 26 11 28M53 24c-6 4-12 26-11 28"/></svg>'

def build(M):
    S = dict(title='Haouaria Beach — Restaurant de plage, poisson & fruits de mer à El Haouaria (démo)',
             desc='Haouaria Beach, restaurant sur la plage d’El Haouaria (Cap Bon) : paella, gratin de fruits de mer, seiches grillées, marmite de moules, loup grillé, thé aux pignons. Arrivage du jour et réservation WhatsApp.',
             favicon="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E%3Ccircle cx='20' cy='20' r='20' fill='%23E6F7F8'/%3E%3Ccircle cx='20' cy='17' r='7' fill='%23FF7A59'/%3E%3Cpath d='M4 24c4 0 4-2.5 8-2.5s4 2.5 8 2.5 4-2.5 8-2.5 4 2.5 8 2.5v8H4z' fill='%230B9FB0'/%3E%3C/svg%3E")
    wa_resa = walink(WA, 'Bonjour Haouaria Beach, je souhaite réserver une table.')
    wa_fish = walink(WA, 'Bonjour Haouaria Beach, quel est l’arrivage de poisson aujourd’hui ?')
    maps = 'https://www.google.com/maps/search/?api=1&query=' + MAPQ.replace(' ', '+')
    ticker_items = ['Paella pour deux', 'Gratin de fruits de mer', 'Seiches grillées', 'Marmite de moules', 'Loup grillé', 'Thé aux pignons', 'Les pieds dans le sable']
    tk = ''.join(f'<span>{t}</span><span aria-hidden="true">✺</span>' for t in ticker_items)
    dishes = [('paella', 'Paella (2 pers.)', 'Le plat à partager, face à la mer.', 'Carte en ligne'),
              ('gratin', 'Gratin de fruits de mer', 'Gratiné au four, servi bien chaud.', 'Carte en ligne'),
              ('seiches', 'Seiches grillées', 'Selon arrivage.', 'Carte en ligne'),
              (None, 'Marmite de moules', 'Citée dans les avis clients.', 'Avis clients'),
              ('loup', 'Loup grillé', 'Au kilo, selon la pêche du jour.', 'Carte en ligne'),
              ('the', 'Thé aux pignons', 'Pour finir, le classique tunisien.', 'Carte en ligne')]
    dh = ''
    for img, n, d, lbl in dishes:
        im = M.img(img, f'{n} (photo d’ambiance)', sizes='(max-width: 760px) 78vw, 380px') if img else f'<div class="shell">{SHELL_SVG}</div>'
        dh += f'<article class="dish"><div class="im">{im}</div><div class="bd"><h3>{n}</h3><p>{d}</p><div class="row"><span class="lbl">{lbl}</span><b>— DT {PH}</b></div></div></article>'
    bento = [('zembra', 'Coucher de soleil sur Zembra', 'b1'), ('epave', 'Eaux turquoise', ''), ('plage', 'La plage', ''), ('cote', 'Les côtes d’El Haouaria', 'b4'), ('falaises', 'Falaises et grottes', 'b4'), ('crevettes', 'Crevettes du marché', 'b4')]
    bh = ''.join(f'<a class="{c}" href="media/{n}.webp" data-full="media/{n}.webp">{M.img(n, a + " (photo d’ambiance)", sizes="(max-width: 760px) 100vw, 50vw" if c else "(max-width: 760px) 50vw, 25vw")}<span>{a}</span></a>' for n, a, c in bento)
    body = f'''<a class="skip" href="#main">Aller au contenu</a>
<div class="ribbon">{RIBBON}</div>
<header class="hd" data-header><div class="wrap">
 <a class="logo" href="#top" aria-label="Haouaria Beach, accueil">{LOGO_SVG}<span>haouaria beach<small>Restaurant de plage · El Haouaria</small></span></a>
 <nav class="nav" data-nav aria-label="Navigation"><a href="#arrivage">Arrivage</a><a href="#carte">La carte</a><a href="#terrasse">Terrasse</a><a href="#infos">Infos</a></nav>
 <a class="btn btn-coral" href="#reserver">Réserver</a>
 <button class="burger" type="button" data-menu aria-label="Ouvrir le menu" aria-expanded="false"><i></i></button>
</div></header>
<main id="main">
<section class="hero" id="top"><div class="grid">
 <div class="txt">
  <span class="pill"><i>★</i>3,7/5 · 273 avis sur lacarte.menu</span>
  <h1>Les pieds dans le sable, <span>la mer</span> dans <span class="u">l’assiette<svg viewBox="0 0 200 20" preserveAspectRatio="none" aria-hidden="true"><path d="M2 14C40 4 80 4 100 10s70 8 98-4" stroke="#FF7A59" stroke-width="5" fill="none" stroke-linecap="round"/></svg></span></h1>
  <p class="lead">Paella pour deux, gratin de fruits de mer, seiches grillées et thé aux pignons, sur la plage d’El Haouaria, à la pointe du Cap Bon.</p>
  <div class="acts"><a class="btn btn-coral" href="#reserver">Réserver une table</a><a class="btn btn-soft" href="{wa_fish}" target="_blank" rel="noopener">{WA_SVG}Arrivage du jour</a></div>
  <div class="chips"><span><b>●</b> Sur la plage</span><span>$$ · budget moyen</span><span>Horaires {PH}</span></div>
 </div>
 <div class="pic">{M.img('hero', 'Côte et plage d’El Haouaria, eau turquoise (photo d’ambiance)', sizes='(max-width: 760px) 100vw, 50vw', lazy=False)}
  <div class="floatcard">{M.img('zembra', 'Coucher de soleil sur l’île de Zembra', sizes='62px')}<div><b>Face à Zembra</b><small>Couchers de soleil sur l’île, vus depuis El Haouaria.</small></div></div></div>
</div>
<svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 30c120 20 240 20 360 0s240-20 360 0 240 20 360 0 240-20 360 0v30H0z" fill="#FF7A59"/></svg>
</section>
<div class="ticker" aria-label="Spécialités"><div>{tk}{tk}</div></div>

<section class="sec" id="arrivage"><div class="wrap">
 <span class="tag">Poisson du jour</span>
 <h2>Ce matin, la mer a donné… <span class="ar" lang="ar" style="color:var(--sea)">حوت اليوم</span></h2>
 <p class="sub">Chaque jour, le restaurant affiche ici son arrivage&nbsp;: vos clients savent ce qu’il y a avant même de venir.</p>
 <div class="fish" style="margin-top:2rem">
  <div class="ph-wrap">{M.img('arrivage', 'Poissons frais sur la glace (photo d’ambiance)', sizes='(max-width: 760px) 100vw, 55vw')}</div>
  <div class="board">
   <div class="date"><span>Arrivage · exemple d’affichage</span><span>{SUN_SVG.replace('<svg ', '<svg width="18" height="18" ')}</span></div>
   <h3>Selon la pêche</h3>
   <ul>
    <li><i>🐟</i><div><b>Loup</b><small>grillé, au kilo</small></div><em>prix {PH}</em></li>
    <li><i>🦑</i><div><b>Seiches</b><small>grillées</small></div><em>prix {PH}</em></li>
    <li><i>🐚</i><div><b>Moules</b><small>en marmite</small></div><em>prix {PH}</em></li>
    <li><i>🌊</i><div><b>Autres poissons</b><small>selon l’arrivage du jour</small></div><em>{PH}</em></li>
   </ul>
   <a class="btn btn-coral" href="{wa_fish}" target="_blank" rel="noopener">{WA_SVG}Demander l’arrivage</a>
   <p class="note">Module de démo&nbsp;: la liste réelle et les prix au kilo seraient mis à jour chaque matin par le restaurant, en une minute depuis son téléphone.</p>
  </div>
 </div>
</div></section>

<section class="sec" id="carte" style="background:var(--sand)"><div class="wrap">
 <div class="mhead"><div><span class="tag">La carte</span><h2>Les plats de la mer</h2><p class="sub">Plats relevés sur la fiche publique et les avis. Prix {PH}.</p></div></div>
 <div class="scroller">{dh}</div>
</div></section>

<section class="sec" id="terrasse"><div class="wrap">
 <span class="tag">Terrasse & coucher de soleil</span><h2>El Haouaria, côté mer</h2>
 <p class="sub">Plages, criques turquoise et soleil couchant sur l’île de Zembra. <span class="ph long">photos d’ambiance sous licence libre — à remplacer par vos photos</span></p>
 <div class="bento">{bh}</div>
</div></section>

<section class="sec resa" id="reserver">
 <svg class="wave-top" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 30c120-20 240-20 360 0s240 20 360 0 240-20 360 0 240 20 360 0v30H0z" fill="#0B9FB0"/></svg>
 <div class="wrap in">
  <div><span class="ar" lang="ar">مرحبا بيكم</span><h2>Une table face à la mer&nbsp;?</h2><p class="sub">Choisissez le jour, l’heure et le nombre de personnes&nbsp;: la demande part toute prête sur le WhatsApp du restaurant, qui vous confirme la table.</p>
   <p><a class="btn btn-white" href="tel:{TEL}">{PHONE_SVG}{WA_DISP}</a></p></div>
  <form class="form" data-wa="{WA}" data-intro="Bonjour Haouaria Beach, je souhaite réserver une table :" novalidate>
   <label>Date<input type="date" name="date" data-label="Date" required></label>
   <label>Heure<select name="heure" data-label="Heure"><option>12:00</option><option>12:30</option><option>13:00</option><option>13:30</option><option>14:00</option><option>19:00</option><option>19:30</option><option>20:00</option><option>20:30</option><option>21:00</option></select></label>
   <label>Personnes<select name="personnes" data-label="Personnes"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7 – 10</option><option>Plus de 10</option></select></label>
   <label>Envie de…<select name="envie" data-label="Préférence"><option>Au plus près de la mer</option><option>À l’ombre</option><option>Pour le coucher du soleil</option><option>Peu importe</option></select></label>
   <label class="full">Nom<input name="nom" data-label="Nom" autocomplete="name" required></label>
   <label class="full">Téléphone / WhatsApp<input name="tel" data-label="Téléphone" type="tel" inputmode="tel" autocomplete="tel" required></label>
   <div class="full"><button class="btn btn-coral" type="submit">{WA_SVG}<span>Envoyer sur WhatsApp</span></button></div>
   <p class="full fine">Démo&nbsp;: aucune donnée n’est enregistrée. Le formulaire ouvre WhatsApp avec votre demande ; la table est confirmée par le restaurant. Horaires et saison {PH}.</p>
  </form>
 </div>
</section>

<section class="sec" id="infos"><div class="wrap">
 <span class="tag">Infos pratiques</span><h2>Sur la plage d’El Haouaria</h2>
 <div class="infos" style="margin-top:2rem">
  <div class="card"><div class="ic">{PIN_SVG}</div><h3>Où</h3><p>{ADDR}.<br>À la pointe du Cap Bon, à environ 1h30 de Tunis.</p></div>
  <div class="card"><div class="ic">{SUN_SVG}</div><h3>Quand</h3><p>Tous les jours · horaires et saison {PH}</p></div>
  <div class="card"><div class="ic">{PHONE_SVG}</div><h3>Contact</h3><p><a href="tel:{TEL}">{WA_DISP}</a><br><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp</a></p></div>
  <div class="card rt"><span class="big">3,7</span><p>sur 5 · 273 avis · note moyenne relevée sur <a href="https://lacarte.menu/restaurants/el-haouaria/haouaria-beach" target="_blank" rel="noopener">lacarte.menu</a> le {CONSULTED}. Aucun avis inventé.</p></div>
 </div>
 <div class="mapw"><iframe title="Carte : Haouaria Beach, El Haouaria" src="https://maps.google.com/maps?q={MAPQ.replace(' ', '+')}&z=15&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
 <p class="caveat">Position approximative (plage d’El Haouaria)&nbsp;: emplacement exact à confirmer avec l’établissement. <a href="{maps}" target="_blank" rel="noopener">Ouvrir dans Google Maps →</a></p>
</div></section>
</main>
<footer class="ft"><div class="wrap">
 <div class="top">
  <div><a class="logo" href="#top">{LOGO_SVG}<span>haouaria beach</span></a><p>Site de démonstration non officiel réalisé à partir d’informations publiques. Carte, horaires et prix à valider par l’établissement.</p></div>
  <div><b style="color:#fff">Contact</b><br><a href="tel:{TEL}">{WA_DISP}</a><br><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp</a></div>
  <div><b style="color:#fff">Adresse</b><br>{ADDR}</div>
 </div>
 <details><summary>Crédits photos (licences libres, Wikimedia Commons)</summary><ul>{M.credits_html()}<li>Logo, vagues et pictogrammes : dessins SVG originaux Synaris Labs.</li></ul></details>
 <p>© <span id="year">2026</span> Haouaria Beach · <a class="badge" href="https://github.com/islemyakoubi" target="_blank" rel="noopener"><i></i>Démo réalisée par Synaris Labs · Menzel Temime</a></p>
</div></footer>
<div class="fab"><a class="btn btn-white" href="tel:{TEL}">{PHONE_SVG}Appeler</a><a class="btn btn-coral" href="{wa_resa}" target="_blank" rel="noopener">{WA_SVG}Réserver</a></div>
<div class="lb" role="dialog" aria-modal="true" aria-label="Photo agrandie"><button type="button" aria-label="Fermer">×</button><img alt=""></div>'''
    return page(S, M, FONTS, CSS, body, '#0B9FB0')
