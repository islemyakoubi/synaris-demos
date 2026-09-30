# Dar Mrad (Nabeul) — v2 bespoke design: warm traditional Tunisian house.
# Terracotta / cream / Nabeul-pottery blue, zellige SVG pattern, arched hero, paper "carte", enamel-plaque hours.
# Fonts: Young Serif (display) + Work Sans (text) + Aref Ruqaa (Arabic accents).
from gen_v2 import esc, walink, RIBBON, CONSULTED, page, WA_SVG, PHONE_SVG, PIN_SVG
SLUG = 'dar-mrad-nabeul'
WA, WA_DISP, TEL = '21620859220', '+216 20 859 220', '+21620859220'
ADDR, MAPQ = 'Av. Mongi Slim, 8000 Nabeul', '36.452895,10.743317'
FONTS = 'https://fonts.googleapis.com/css2?family=Aref+Ruqaa:wght@400;700&family=Work+Sans:wght@400;500;600&family=Young+Serif&display=swap'
PH = '<span class="ph">à confirmer</span>'

ZELLIGE = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80' viewBox='0 0 80 80'%3E"
  "%3Crect width='80' height='80' fill='%23F6EBDD'/%3E"
  "%3Cg fill='%231D4E6B'%3E%3Crect x='22' y='22' width='36' height='36'/%3E%3Crect x='22' y='22' width='36' height='36' transform='rotate(45 40 40)'/%3E%3C/g%3E"
  "%3Cg fill='%23E0A43A'%3E%3Crect x='31' y='31' width='18' height='18'/%3E%3Crect x='31' y='31' width='18' height='18' transform='rotate(45 40 40)'/%3E%3C/g%3E"
  "%3Ccircle cx='40' cy='40' r='4' fill='%23F6EBDD'/%3E"
  "%3Cg fill='%23B4532A'%3E%3Crect x='-8' y='-8' width='16' height='16' transform='rotate(45 0 0)'/%3E%3Crect x='72' y='-8' width='16' height='16' transform='rotate(45 80 0)'/%3E"
  "%3Crect x='-8' y='72' width='16' height='16' transform='rotate(45 0 80)'/%3E%3Crect x='72' y='72' width='16' height='16' transform='rotate(45 80 80)'/%3E%3C/g%3E%3C/svg%3E")

CSS = r'''
:root{--terra:#B4532A;--terra-d:#8A3A1A;--cream:#F6EBDD;--paper:#FCF6EC;--blue:#1D4E6B;--blue-d:#143A50;--saffron:#E0A43A;--olive:#5E6B2E;--ink:#2B1A12;--muted:#6F5A4B;
--f-d:'Young Serif',Georgia,serif;--f-t:'Work Sans',system-ui,sans-serif;--f-ar:'Aref Ruqaa','Amiri',serif;--z:url("ZELLIGE")}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font:400 1rem/1.65 var(--f-t);-webkit-font-smoothing:antialiased}
img{max-width:100%;height:auto;display:block}a{color:inherit}h1,h2,h3{font-family:var(--f-d);font-weight:400;line-height:1.12;margin:0 0 .6rem;letter-spacing:-.01em}
.ar{font-family:var(--f-ar);font-weight:700;direction:rtl}
.wrap{width:min(1180px,100% - 2.5rem);margin-inline:auto}
.ph{display:inline-block;font:500 .72rem/1.2 var(--f-t);color:var(--terra-d);background:#F3DCC8;border:1px dashed #D19A78;border-radius:4px;padding:.12rem .4rem;vertical-align:middle;white-space:nowrap}
.ph.long{white-space:normal}.skip{position:absolute;left:-999px}.skip:focus{left:1rem;top:1rem;z-index:99;background:#fff;padding:.5rem 1rem}
.ribbon{background:var(--ink);color:#EBD9C6;font-size:.74rem;text-align:center;padding:.4rem 1rem}.ribbon b{color:var(--saffron)}
/* header */
.hd{position:sticky;top:0;z-index:40;background:rgba(252,246,236,.94);backdrop-filter:blur(8px);border-bottom:1px solid #EAD8C4}
.hd .wrap{display:flex;align-items:center;justify-content:space-between;gap:1rem;height:68px}
.brand{display:flex;align-items:center;gap:.65rem;text-decoration:none}
.brand .arch{width:40px;height:48px;border-radius:20px 20px 4px 4px;background:var(--terra);display:grid;place-items:center;color:#fff;font:700 1.35rem/1 var(--f-ar);box-shadow:inset 0 0 0 3px var(--terra),inset 0 0 0 4px #F3C9A6}
.brand b{font:400 1.35rem/1 var(--f-d);display:block}.brand small{font-size:.72rem;color:var(--muted);letter-spacing:.08em;text-transform:uppercase}
.nav{display:none}.nav a{text-decoration:none;font-weight:500;padding:.4rem .2rem;border-bottom:2px solid transparent}.nav a:hover{border-color:var(--saffron)}
.burger{width:44px;height:44px;border:1px solid #E1CBB4;border-radius:12px;background:#fff;display:grid;place-items:center;cursor:pointer}
.burger i,.burger i:before,.burger i:after{display:block;width:18px;height:2px;background:var(--ink);border-radius:2px;position:relative;content:''}
.burger i:before{position:absolute;top:-6px}.burger i:after{position:absolute;top:6px}
.nav.open{display:flex;position:absolute;top:68px;left:0;right:0;flex-direction:column;background:var(--paper);padding:1rem 1.25rem 1.5rem;border-bottom:1px solid #EAD8C4;gap:.4rem}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.55rem;border-radius:999px;padding:.85rem 1.35rem;font:600 .98rem/1 var(--f-t);text-decoration:none;border:2px solid transparent;cursor:pointer;transition:transform .15s,background .15s}
.btn:hover{transform:translateY(-1px)}.btn svg{width:20px;height:20px}
.btn-terra{background:var(--terra);color:#fff}.btn-terra:hover{background:var(--terra-d)}
.btn-line{border-color:var(--ink);color:var(--ink);background:transparent}.btn-wa{background:#1F8F4E;color:#fff}
.hd .btn{display:none}
/* hero */
.hero{position:relative;padding:2.2rem 0 3.5rem;overflow:hidden}
.hero .wrap{display:grid;gap:2.2rem}
.hello{font-size:1.9rem;color:var(--terra);margin:0 0 .2rem;text-align:left}
.kicker{font:600 .78rem/1 var(--f-t);letter-spacing:.16em;text-transform:uppercase;color:var(--blue)}
.hero h1{font-size:clamp(2.3rem,7vw,4.3rem);margin:.7rem 0 1rem}.hero h1 em{font-style:normal;color:var(--terra)}
.hero .lead{font-size:1.1rem;color:var(--muted);max-width:34rem}
.cta{display:flex;flex-wrap:wrap;gap:.7rem;margin:1.6rem 0}
.facts{display:flex;flex-wrap:wrap;gap:.5rem 1.4rem;font-size:.9rem;color:var(--muted);padding-top:1.2rem;border-top:1px dashed #D9BFA5}
.facts b{color:var(--ink)}.facts .st{color:var(--saffron)}
.frame{position:relative;max-width:470px;margin-inline:auto;width:100%}
.frame:before{content:'';position:absolute;inset:-14px -14px 22px 22px;background:var(--z) 0 0/48px;border-radius:260px 260px 18px 18px;opacity:.9}
.frame .pic{position:relative;border-radius:240px 240px 14px 14px;overflow:hidden;aspect-ratio:4/5;box-shadow:0 30px 60px -30px rgba(90,40,15,.55);border:6px solid var(--paper)}
.frame .pic img{width:100%;height:100%;object-fit:cover}
.stamp{position:absolute;right:-6px;bottom:-26px;width:124px;height:124px;background:var(--saffron);border-radius:50%;display:grid;place-items:center;box-shadow:0 10px 25px -10px rgba(0,0,0,.4)}
.stamp svg{position:absolute;inset:0;animation:spin 28s linear infinite}.stamp span{font:700 2.1rem/1 var(--f-ar);color:var(--ink)}
@keyframes spin{to{transform:rotate(360deg)}}@media (prefers-reduced-motion:reduce){.stamp svg{animation:none}}
.band{height:34px;background:var(--z) 0 0/34px;border-block:4px solid var(--terra)}
/* sections */
.sec{padding:4.5rem 0}.eyebrow{display:inline-flex;align-items:center;gap:.6rem;font:600 .76rem/1 var(--f-t);letter-spacing:.18em;text-transform:uppercase;color:var(--terra)}
.eyebrow:before{content:'';width:26px;height:2px;background:currentColor}
.sec h2{font-size:clamp(1.9rem,4.6vw,3rem);margin-top:.7rem}
/* story */
.story{display:grid;gap:2.2rem;align-items:center}
.story .pics{display:grid;grid-template-columns:1.2fr 1fr;gap:.9rem;align-items:end}
.story .pics img{border-radius:140px 140px 10px 10px;aspect-ratio:3/4;object-fit:cover;width:100%}
.story .pics img:last-child{border-radius:10px;aspect-ratio:1;margin-bottom:2.2rem}
.story p{color:#4d3a2e}.story .drop:first-letter{font:400 3.6rem/.8 var(--f-d);float:left;margin:.35rem .5rem 0 0;color:var(--terra)}
.note{background:#fff;border:1px solid #EAD8C4;border-left:4px solid var(--saffron);border-radius:10px;padding:1rem 1.1rem;font-size:.92rem;color:var(--muted);margin-top:1.3rem}
.tags{display:flex;flex-wrap:wrap;gap:.45rem;margin-top:1.2rem}.tags span{border:1px solid #D9BFA5;border-radius:999px;padding:.3rem .8rem;font-size:.85rem;background:#fff}
/* carte */
.carte-sec{background:var(--terra);background-image:radial-gradient(circle at 20% 0,rgba(255,255,255,.12),transparent 55%);color:#fff;position:relative}
.carte-sec .head{text-align:center;max-width:40rem;margin:0 auto 2.4rem}.carte-sec .eyebrow{color:#FFE2BF}.carte-sec .head p{color:#FBE3CF}
.carte-grid{display:grid;gap:2rem;align-items:start}
.carte{background:var(--paper);color:var(--ink);border-radius:6px;padding:10px;box-shadow:0 30px 60px -25px rgba(0,0,0,.5)}
.carte .in{border:2px solid var(--terra);outline:1px solid var(--terra);outline-offset:-7px;border-radius:3px;padding:2rem 1.3rem 1.6rem}
.carte h3{text-align:center;font-size:1.9rem;margin:0}.carte .sub{text-align:center;color:var(--terra);font-size:1.5rem;margin:-.1rem 0 .3rem}
.carte .orn{display:block;margin:0 auto 1.2rem;width:120px;height:14px}
.carte h4{font:600 .78rem/1 var(--f-t);letter-spacing:.18em;text-transform:uppercase;color:var(--blue);margin:1.6rem 0 .6rem;display:flex;align-items:center;gap:.6rem}
.carte h4:after{content:'';flex:1;height:1px;background:#DCC5AE}
.item{display:grid;grid-template-columns:1fr auto;gap:.1rem .8rem;padding:.55rem 0;border-bottom:1px dotted #D8C0A8}
.item .n{font:400 1.12rem/1.3 var(--f-d)}.item .n .ar{font-size:1.05rem;color:var(--terra);margin-left:.5rem}
.item .p{font-weight:600;color:var(--muted);white-space:nowrap}.item .d{grid-column:1/-1;font-size:.88rem;color:var(--muted)}
.item .t{font-size:.7rem;letter-spacing:.06em;text-transform:uppercase;color:var(--olive);border:1px solid #C7CFA4;border-radius:4px;padding:.05rem .3rem;margin-inline-start:.4rem;vertical-align:2px;font-family:var(--f-t)}
.carte .foot{text-align:center;font-size:.8rem;color:var(--muted);margin-top:1.3rem}
.polas{display:grid;grid-template-columns:1fr 1fr;gap:1rem;padding:.5rem}
.pola{background:#fff;padding:.6rem .6rem 0;border-radius:3px;box-shadow:0 18px 30px -18px rgba(0,0,0,.6);color:var(--ink);margin:0}
.pola img{aspect-ratio:1;object-fit:cover;width:100%}.pola figcaption{font:400 1rem/1 var(--f-d);text-align:center;padding:.7rem 0 .8rem}
.pola:nth-child(1){transform:rotate(-2.5deg)}.pola:nth-child(2){transform:rotate(2deg) translateY(1.2rem)}.pola:nth-child(3){transform:rotate(1.5deg)}.pola:nth-child(4){transform:rotate(-2deg) translateY(1.2rem)}
/* tea strip */
.tea{display:grid;background:var(--blue);color:#EAF1F5}
.tea img{width:100%;height:100%;object-fit:cover;min-height:260px}
.tea .txt{padding:3rem 1.4rem;background:var(--blue) var(--z) right -40px top -40px/0;position:relative}
.tea .txt h2{font-size:clamp(1.8rem,4vw,2.6rem)}.tea .txt .ar{font-size:2.2rem;color:var(--saffron);display:block;margin-bottom:.4rem}
.tea .txt p{color:#C9DAE4;max-width:30rem}
.tea .zcol{display:none}
/* booking */
.book{display:grid;gap:2rem;align-items:start}
.panel{background:#fff;border:1px solid #EAD8C4;border-radius:22px;padding:1.3rem;box-shadow:0 25px 50px -35px rgba(90,40,15,.45)}
.tabs{display:grid;grid-template-columns:1fr 1fr;background:var(--cream);border-radius:14px;padding:5px;margin-bottom:1.2rem}
.tabs button{border:0;background:transparent;border-radius:10px;padding:.75rem .5rem;font:600 .95rem/1 var(--f-t);color:var(--muted);cursor:pointer}
.tabs button[aria-selected=true]{background:#fff;color:var(--terra);box-shadow:0 2px 8px rgba(0,0,0,.08)}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.9rem}.form .full{grid-column:1/-1}
.form label{display:grid;gap:.35rem;font-size:.85rem;font-weight:600;color:var(--muted)}
.form input,.form select,.form textarea{font:inherit;font-weight:400;color:var(--ink);border:1.5px solid #E1CBB4;border-radius:12px;padding:.75rem .85rem;background:var(--paper);width:100%;min-height:48px}
.form textarea{min-height:90px;resize:vertical}.form input:focus,.form select:focus,.form textarea:focus{outline:3px solid #F3C9A6;border-color:var(--terra)}
.form .btn{width:100%;padding:1rem}.small{font-size:.8rem;color:var(--muted)}
.call{display:grid;gap:.9rem}.call a.big{font:400 1.8rem/1.1 var(--f-d);text-decoration:none;color:var(--terra)}
.steps{list-style:none;padding:0;margin:1.2rem 0;display:grid;gap:.8rem;counter-reset:s}
.steps li{display:grid;grid-template-columns:38px 1fr;gap:.8rem;align-items:start;counter-increment:s}
.steps li:before{content:counter(s);width:38px;height:38px;border-radius:50%;background:var(--cream);color:var(--terra);display:grid;place-items:center;font:400 1.1rem/1 var(--f-d);border:1px solid #E1CBB4}
/* rating */
.rate{display:grid;gap:2rem;align-items:center;justify-items:center;text-align:center}
.plate{width:230px;height:230px;border-radius:50%;background:radial-gradient(circle,#fff 0 52%,var(--blue) 52% 54%,#fff 54% 60%,var(--saffron) 60% 62%,#fff 62% 70%,var(--terra) 70% 71%,#fff 71%);box-shadow:0 20px 40px -20px rgba(0,0,0,.35),inset 0 0 0 8px var(--cream);display:grid;place-items:center}
.plate div{font:400 3.2rem/1 var(--f-d)}.plate small{display:block;font:500 .8rem/1.3 var(--f-t);color:var(--muted)}
.rate p{max-width:36rem;color:var(--muted)}
/* visit */
.visit{background:var(--cream);background-image:linear-gradient(rgba(246,235,221,.93),rgba(246,235,221,.93)),var(--z);background-size:auto,60px}
.visit .grid{display:grid;gap:2rem}
.plaque{background:var(--blue);color:#fff;border-radius:16px;padding:1.6rem 1.4rem;border:4px solid #fff;outline:2px solid var(--blue);box-shadow:0 20px 40px -25px rgba(0,0,0,.5)}
.plaque h3{font-size:1.5rem;display:flex;justify-content:space-between;align-items:baseline;gap:1rem}.plaque h3 .ar{font-size:1.4rem;color:var(--saffron)}
.plaque table{width:100%;border-collapse:collapse;margin:.6rem 0 1rem}.plaque td{padding:.65rem 0;border-bottom:1px solid rgba(255,255,255,.2)}.plaque td:last-child{text-align:right;font-weight:600}
.plaque .ph{background:rgba(255,255,255,.14);color:#FFE2BF;border-color:rgba(255,255,255,.4)}
.plaque svg{width:18px;height:18px;vertical-align:-3px;margin-right:.35rem}.plaque ul{list-style:none;padding:0;margin:0;display:grid;gap:.55rem;font-size:.95rem}.plaque a{color:#fff}
.mapbox{border-radius:200px 200px 16px 16px;overflow:hidden;border:6px solid #fff;box-shadow:0 20px 40px -25px rgba(0,0,0,.5);min-height:340px;background:#e8e0d4}
.mapbox iframe{width:100%;height:100%;min-height:340px;border:0;display:block}
/* footer */
.ft{background:var(--ink);color:#D8C6B5;padding:3rem 0 6.5rem;font-size:.9rem}
.ft .sig{font:700 2.4rem/1 var(--f-ar);color:var(--saffron)}.ft a{color:#F3D9BF}.ft .cols{display:grid;gap:1.5rem;margin:1.5rem 0}
.ft details{margin-top:1rem;font-size:.8rem;opacity:.85}.ft summary{cursor:pointer}.ft li{margin:.25rem 0}
.badge{display:inline-flex;align-items:center;gap:.4rem;text-decoration:none;border:1px solid #5a4536;border-radius:999px;padding:.3rem .7rem;margin-top:.6rem}
.badge i{width:8px;height:8px;border-radius:50%;background:var(--saffron)}
.dock{position:fixed;left:0;right:0;bottom:0;z-index:50;display:grid;grid-template-columns:repeat(3,1fr);background:var(--paper);border-top:1px solid #E1CBB4;padding:.45rem .5rem calc(.45rem + env(safe-area-inset-bottom));gap:.4rem}
.dock a{display:grid;justify-items:center;gap:.15rem;font-size:.74rem;font-weight:600;text-decoration:none;padding:.35rem;border-radius:12px}
.dock a svg{width:22px;height:22px}.dock a.wa{background:#1F8F4E;color:#fff}
@media (min-width:760px){
 .hero .wrap{grid-template-columns:1.05fr .95fr;align-items:center}.hero{padding:3.5rem 0 5rem}
 .story{grid-template-columns:1fr 1fr;gap:3.5rem}
 .carte-grid{grid-template-columns:1.25fr 1fr;gap:3rem}
 .tea{grid-template-columns:1fr 1fr}.tea .txt{padding:4rem 3rem;display:flex;flex-direction:column;justify-content:center}
 .book{grid-template-columns:.85fr 1.15fr;gap:3rem}.panel{padding:2rem}
 .rate{grid-template-columns:auto 1fr;text-align:left;justify-items:start}
 .visit .grid{grid-template-columns:.9fr 1.1fr;align-items:start}
 .ft .cols{grid-template-columns:1.4fr 1fr 1fr}
}
@media (min-width:980px){
 .nav{display:flex;gap:1.6rem}.nav.open{position:static;flex-direction:row;padding:0;border:0;background:none}
 .burger{display:none}.hd .btn{display:inline-flex;padding:.7rem 1.1rem}
 .dock{display:none}.ft{padding-bottom:3rem}
}
'''.replace('ZELLIGE', ZELLIGE)

ORN = '<svg class="orn" viewBox="0 0 120 14" aria-hidden="true"><path d="M0 7h44M76 7h44" stroke="#B4532A" stroke-width="1.5"/><path d="M60 1l6 6-6 6-6-6z" fill="#E0A43A"/><circle cx="48" cy="7" r="2" fill="#1D4E6B"/><circle cx="72" cy="7" r="2" fill="#1D4E6B"/></svg>'

def item(n, ar, d, tag):
    t = f'<span class="t">{tag}</span>' if tag else ''
    return f'<div class="item"><div class="n">{n}<span class="ar" lang="ar">{ar}</span>{t}</div><div class="p">— DT</div><div class="d">{d}</div></div>'

def build(M):
    S = dict(title='Dar Mrad — Cuisine tunisienne de maison à Nabeul (démo)',
             desc='Dar Mrad, restaurant de cuisine tunisienne à Nabeul (Av. Mongi Slim) : kamounia, poulet grillé, soupe crème de tomates, thé à la menthe. Carte, réservation WhatsApp, horaires, accès.',
             favicon="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cpath d='M8 60V28a24 24 0 0 1 48 0v32z' fill='%23B4532A'/%3E%3Ctext x='32' y='47' font-size='26' text-anchor='middle' fill='white' font-family='Georgia'%3EM%3C/text%3E%3C/svg%3E")
    wa_resa = walink(WA, 'Bonjour Dar Mrad, je souhaite réserver une table.')
    maps = 'https://www.google.com/maps/search/?api=1&query=' + MAPQ
    stamp = ('<svg viewBox="0 0 124 124" aria-hidden="true"><defs><path id="c" d="M62 62m-46 0a46 46 0 1 1 92 0a46 46 0 1 1-92 0"/></defs>'
             '<text font-family="Work Sans,sans-serif" font-size="10.5" font-weight="600" letter-spacing="2.6" fill="#2B1A12"><textPath href="#c">CUISINE TUNISIENNE · NABEUL · </textPath></text></svg>')
    carte = ''.join([
        '<h4>Plats mijotés & grillades</h4>',
        item('Kamounia', 'كمونية', 'Ragoût parfumé au cumin, spécialité citée sur la carte en ligne.', 'cité en ligne'),
        item('Poulet grillé', 'دجاج مشوي', 'Servi avec les accompagnements du jour.', 'cité en ligne'),
        item('Paella', 'بايلا', 'Citée sur la fiche publique du restaurant.', 'cité en ligne'),
        '<h4>Pour commencer</h4>',
        item('Soupe crème de tomates', 'شوربة طماطم', 'Velouté de tomates, servi chaud.', 'cité en ligne'),
        item('Salade mechouia', 'سلطة مشوية', 'Poivrons et tomates grillés, huile d’olive.', 'exemple'),
        item('Brik', 'بريك', 'Feuille croustillante, œuf et thon.', 'exemple'),
        '<h4>Pour finir</h4>',
        item('Thé vert à la menthe', 'تاي بالنعناع', 'Le thé de la maison, servi bien chaud.', 'cité en ligne'),
        f'<div class="item"><div class="n">Plat du jour<span class="ar" lang="ar">طبق اليوم</span></div><div class="p">— DT</div><div class="d">Annoncé chaque matin sur WhatsApp {PH}</div></div>'])
    body = f'''<a class="skip" href="#main">Aller au contenu</a>
<div class="ribbon">{RIBBON}</div>
<header class="hd"><div class="wrap">
 <a class="brand" href="#top" aria-label="Dar Mrad, accueil"><span class="arch" lang="ar">م</span><span><b>Dar Mrad</b><small>Cuisine tunisienne · Nabeul</small></span></a>
 <nav class="nav" data-nav aria-label="Navigation"><a href="#maison">La maison</a><a href="#carte">La carte</a><a href="#reserver">Réserver</a><a href="#horaires">Horaires & accès</a></nav>
 <a class="btn btn-terra" href="#reserver">Réserver une table</a>
 <button class="burger" type="button" data-menu aria-label="Ouvrir le menu" aria-expanded="false"><i></i></button>
</div></header>
<main id="main">
<section class="hero" id="top"><div class="wrap">
 <div>
  <p class="hello ar" lang="ar">أهلا وسهلا</p>
  <span class="kicker">Ahlan wa sahlan · Restaurant à Nabeul</span>
  <h1>La cuisine tunisienne <em>de maison</em>, au cœur de Nabeul</h1>
  <p class="lead">Kamounia, poulet grillé, soupe à la tomate et thé à la menthe&nbsp;: des plats simples et généreux, servis comme en famille, avenue Mongi Slim.</p>
  <div class="cta"><a class="btn btn-terra" href="{wa_resa}" target="_blank" rel="noopener">{WA_SVG}Réserver sur WhatsApp</a><a class="btn btn-line" href="#carte">Voir la carte</a></div>
  <div class="facts"><span><b class="st">★</b> <b>4,0/5</b> · 337 avis (lacarte.menu)</span><span><b>Midi</b> · lun.–sam. 12h–17h {PH}</span><span><b>Av. Mongi Slim</b> · Nabeul</span></div>
 </div>
 <div class="frame"><div class="pic">{M.img('hero', 'Couscous tunisien servi sur une table en céramique (photo d’ambiance)', sizes='(max-width: 760px) 92vw, 470px', lazy=False)}</div>
  <div class="stamp">{stamp}<span lang="ar">دار</span></div></div>
</div></section>
<div class="band" role="presentation"></div>

<section class="sec" id="maison"><div class="wrap story">
 <div class="pics">{M.img('poterie', 'Poteries de Nabeul (photo d’ambiance)', sizes='(max-width: 760px) 50vw, 300px')}{M.img('assiettes', 'Assiettes en céramique peinte (photo d’ambiance)', sizes='(max-width: 760px) 45vw, 260px')}</div>
 <div>
  <span class="eyebrow">La maison · <span class="ar" lang="ar">الدار</span></span>
  <h2>Une table familiale, sans chichi</h2>
  <p class="drop">Dar Mrad sert une cuisine tunisienne de tous les jours, comme à la maison&nbsp;: plats mijotés, grillades et soupes, dans la ville de la poterie et de la fleur d’oranger.</p>
  <p>Les clients citent en ligne la kamounia, le poulet grillé, la soupe crème de tomates, la paella et le thé vert à la menthe. Plats du jour et formules {PH}.</p>
  <div class="note"><b>L’histoire de la famille</b> — cet espace racontera, avec vos mots et vos photos, qui cuisine chez Dar Mrad et d’où viennent les recettes. <span class="ph long">texte à écrire avec vous</span></div>
  <div class="tags"><span>Cuisine tunisienne</span><span>Plats mijotés</span><span>Grillades</span><span>Thé à la menthe</span></div>
 </div>
</div></section>

<section class="sec carte-sec" id="carte"><div class="wrap">
 <div class="head"><span class="eyebrow">La carte · <span class="ar" lang="ar">القائمة</span></span><h2>Les classiques de la maison</h2><p>Plats relevés sur les fiches publiques du restaurant. La carte complète, les prix et les plats du jour seront ajoutés avec vous.</p></div>
 <div class="carte-grid">
  <div class="carte"><div class="in"><h3>Dar Mrad</h3><p class="sub ar" lang="ar">دار مراد</p>{ORN}{carte}
   <p class="foot">Prix {PH} · photos d’ambiance non contractuelles</p></div></div>
  <div class="polas">
   <figure class="pola">{M.img('kamounia', 'Kamounia, ragoût au cumin (photo d’ambiance)', sizes='(max-width: 760px) 45vw, 240px')}<figcaption>Kamounia</figcaption></figure>
   <figure class="pola">{M.img('mechouia', 'Salade mechouia (photo d’ambiance)', sizes='(max-width: 760px) 45vw, 240px')}<figcaption>Mechouia</figcaption></figure>
   <figure class="pola">{M.img('brik', 'Briks tunisiennes (photo d’ambiance)', sizes='(max-width: 760px) 45vw, 240px')}<figcaption>Brik</figcaption></figure>
   <figure class="pola">{M.img('the', 'Thé à la menthe (photo d’ambiance)', sizes='(max-width: 760px) 45vw, 240px')}<figcaption>Thé à la menthe</figcaption></figure>
  </div>
 </div>
</div></section>

<section class="tea" aria-labelledby="tea-h">
 {M.img('zellige', 'Mur de carreaux de céramique tunisiens (photo d’ambiance)', sizes='(max-width: 760px) 100vw, 50vw')}
 <div class="txt"><span class="ar" lang="ar">بالهناء والشفاء</span><h2 id="tea-h">Bel hna wa chfa&nbsp;!</h2><p>« Bon appétit » à la tunisienne. À Nabeul, la céramique et les carreaux peints font partie du décor de tous les jours&nbsp;: la maison les met à l’honneur, du plat à la table.</p>
 <p><a class="btn btn-terra" href="#reserver">Réserver une table</a></p></div>
</section>

<section class="sec" id="reserver"><div class="wrap book">
 <div class="call">
  <span class="eyebrow">Réserver ou commander</span>
  <h2>Une table pour midi&nbsp;? Un plat à emporter&nbsp;?</h2>
  <p>Envoyez votre demande en une minute&nbsp;: elle arrive toute prête sur le WhatsApp du restaurant, qui confirme dès qu’il est disponible.</p>
  <ol class="steps"><li><span><b>Choisissez</b> — date, heure, nombre de personnes ou plats.</span></li><li><span><b>Envoyez sur WhatsApp</b> — le message est pré-rempli.</span></li><li><span><b>Dar Mrad confirme</b> — par WhatsApp ou téléphone.</span></li></ol>
  <p class="small">Vous préférez appeler&nbsp;?</p><a class="big" href="tel:{TEL}">{WA_DISP}</a>
 </div>
 <div class="panel" data-tabs>
  <div class="tabs" role="tablist" aria-label="Type de demande">
   <button type="button" role="tab" aria-selected="true" data-mode="resa" data-cta="Envoyer la réservation" data-intro="Bonjour Dar Mrad, je souhaite réserver une table :">Réserver une table</button>
   <button type="button" role="tab" aria-selected="false" data-mode="emp" data-cta="Envoyer la commande" data-intro="Bonjour Dar Mrad, je souhaite commander à emporter :">À emporter</button>
  </div>
  <form class="form" data-wa="{WA}" data-intro="Bonjour Dar Mrad, je souhaite réserver une table :" novalidate>
   <label>Date<input type="date" name="date" data-label="Date" required></label>
   <label>Heure<select name="heure" data-label="Heure"><option>12:00</option><option>12:30</option><option>13:00</option><option>13:30</option><option>14:00</option><option>14:30</option><option>15:00</option></select></label>
   <div class="full" data-only="resa"><label>Personnes<select name="personnes" data-label="Personnes"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7 – 10</option><option>Plus de 10 (famille / groupe)</option></select></label></div>
   <div class="full" data-only="emp" hidden><label>Votre commande<textarea name="commande" data-label="Commande" placeholder="Ex. : 2 kamounia, 1 poulet grillé, 2 soupes…" disabled></textarea></label></div>
   <label class="full">Nom<input name="nom" data-label="Nom" autocomplete="name" required></label>
   <label class="full">Téléphone / WhatsApp<input name="tel" data-label="Téléphone" type="tel" inputmode="tel" autocomplete="tel" required></label>
   <div class="full"><button class="btn btn-wa" type="submit">{WA_SVG}<span>Envoyer la réservation</span></button></div>
   <p class="full small">Démo&nbsp;: aucune donnée n’est enregistrée. Le formulaire ouvre WhatsApp avec votre message ; rien n’est envoyé sans votre validation. Vente à emporter {PH}.</p>
  </form>
 </div>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap rate">
 <div class="plate"><div>4,0<small>sur 5 · 337 avis</small></div></div>
 <div><span class="eyebrow">Ils en parlent</span><h2>Une adresse appréciée à Nabeul</h2>
  <p>Note moyenne publique relevée sur <a href="https://lacarte.menu/restaurants/tunisia/dar-mrad" target="_blank" rel="noopener">lacarte.menu</a> le {CONSULTED}. Aucun avis n’a été inventé ni recopié pour cette démo&nbsp;; dans la version finale, un QR «&nbsp;Laissez un avis&nbsp;» sur l’addition aide à collecter des avis Google récents.</p></div>
</div></section>

<section class="sec visit" id="horaires"><div class="wrap grid">
 <div class="plaque">
  <h3>Horaires <span class="ar" lang="ar">أوقات العمل</span></h3>
  <table><tr><td>Lundi – Samedi</td><td>12:00 – 17:00 {PH}</td></tr><tr><td>Dimanche</td><td>{PH}</td></tr></table>
  <ul>
   <li>{PIN_SVG} {ADDR}</li>
   <li>{PHONE_SVG} <a href="tel:{TEL}">{WA_DISP}</a> · <a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp</a></li>
   <li>Facebook&nbsp;: <a href="https://www.facebook.com/nabeul1973" target="_blank" rel="noopener">facebook.com/nabeul1973</a></li>
  </ul>
  <p style="margin:1.2rem 0 0"><a class="btn btn-terra" href="{maps}" target="_blank" rel="noopener">{PIN_SVG}Itinéraire</a></p>
 </div>
 <div><span class="eyebrow">En plein centre</span><h2>À deux pas du souk de Nabeul</h2><p style="color:var(--muted)">Avenue Mongi Slim, à quelques minutes à pied du souk et de la médina.</p>
  <div class="mapbox"><iframe title="Carte : Dar Mrad, Av. Mongi Slim, Nabeul" src="https://maps.google.com/maps?q={MAPQ}&z=17&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div>
</div></section>
</main>
<footer class="ft"><div class="wrap">
 <div class="sig" lang="ar">دار مراد</div>
 <div class="cols">
  <div><b>Dar Mrad</b> — cuisine tunisienne, {ADDR}.<br>Site de démonstration non officiel réalisé à partir d’informations publiques&nbsp;: contenus, carte et prix à valider par l’établissement.</div>
  <div><b>Contact</b><br><a href="tel:{TEL}">{WA_DISP}</a><br><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp</a></div>
  <div><b>Horaires</b><br>Lun.–sam. 12h–17h {PH}</div>
 </div>
 <details><summary>Crédits photos (licences libres, Wikimedia Commons)</summary><ul>{M.credits_html()}<li>Motifs zellige et ornements : dessins SVG originaux Synaris Labs.</li></ul></details>
 <p>© <span id="year">2026</span> Dar Mrad · <a class="badge" href="https://github.com/islemyakoubi" target="_blank" rel="noopener"><i></i>Démo réalisée par Synaris Labs · Menzel Temime</a></p>
</div></footer>
<nav class="dock" aria-label="Actions rapides"><a href="tel:{TEL}">{PHONE_SVG}Appeler</a><a class="wa" href="{wa_resa}" target="_blank" rel="noopener">{WA_SVG}Réserver</a><a href="{maps}" target="_blank" rel="noopener">{PIN_SVG}Itinéraire</a></nav>'''
    return page(S, M, FONTS, CSS, body, '#B4532A')
