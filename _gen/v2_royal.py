# Royal Palace (Béni Khalled) — v2 bespoke design: dark luxury event hall.
# Black / ivory / gold, full-bleed cinematic hero, numbered event list, gold-line packages, masonry gallery,
# generic testimonial placeholders, date-request form (WhatsApp). Fonts: Cormorant Garamond + Jost + Amiri (Arabic).
from gen_v2 import esc, walink, RIBBON, CONSULTED, page, WA_SVG
SLUG = 'royal-palace-beni-khalled'
WA, WA_DISP, TEL = '21622316000', '+216 22 316 000', '+21622316000'
ADDR, MAPQ = 'Béni Khalled, gouvernorat de Nabeul', '36.6539114,10.5920255'
FONTS = 'https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Cormorant+Garamond:ital,wght@0,300;0,500;1,300;1,500&family=Jost:wght@300;400;500&display=swap'
PH = '<span class="ph">à confirmer</span>'

CSS = r'''
:root{--noir:#0D0C0A;--noir2:#16140F;--noir3:#1F1C15;--ivory:#F6F0E4;--ivory2:#ECE3D1;--gold:#C9A45C;--gold-l:#E8D3A0;--ink:#1B1811;--muted:#8E8574;
--f-d:'Cormorant Garamond',Georgia,serif;--f-t:'Jost',system-ui,sans-serif;--f-ar:'Amiri',serif}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--noir);color:var(--ivory);font:300 1.02rem/1.7 var(--f-t);-webkit-font-smoothing:antialiased}
img{max-width:100%;height:auto;display:block}a{color:inherit}h1,h2,h3{font-family:var(--f-d);font-weight:300;line-height:1.05;margin:0 0 .8rem}
.wrap{width:min(1240px,100% - 2.5rem);margin-inline:auto}.ar{font-family:var(--f-ar);direction:rtl}
.caps{font:400 .72rem/1.4 var(--f-t);letter-spacing:.32em;text-transform:uppercase;color:var(--gold)}
.ph{display:inline-block;font:400 .7rem/1.2 var(--f-t);letter-spacing:.04em;color:var(--gold-l);border:1px dashed rgba(201,164,92,.6);border-radius:2px;padding:.12rem .4rem;vertical-align:middle;white-space:nowrap}
.ph.long{white-space:normal}.light .ph{color:#8A6A2C;border-color:#C9A45C}
.skip{position:absolute;left:-999px}.skip:focus{left:1rem;top:1rem;z-index:99;background:#fff;color:#000;padding:.5rem 1rem}
.ribbon{background:rgba(0,0,0,.85);color:#bdb3a0;font-size:.72rem;text-align:center;padding:.38rem 1rem;border-bottom:1px solid rgba(201,164,92,.3)}.ribbon b{color:var(--gold)}
/* header */
.hd{position:fixed;top:0;left:0;right:0;z-index:50;transition:background .3s,border-color .3s;border-bottom:1px solid transparent}
.hd.scrolled{background:rgba(13,12,10,.92);backdrop-filter:blur(10px);border-color:rgba(201,164,92,.25)}
.hd .wrap{display:flex;align-items:center;justify-content:space-between;height:78px;gap:1rem}
.logo{display:flex;align-items:center;gap:.8rem;text-decoration:none}
.logo .mono{width:42px;height:42px;border:1px solid var(--gold);transform:rotate(45deg);display:grid;place-items:center}
.logo .mono span{transform:rotate(-45deg);font:500 1.05rem/1 var(--f-d);color:var(--gold);letter-spacing:.04em}
.logo b{font:400 .95rem/1 var(--f-t);letter-spacing:.34em;text-transform:uppercase;display:block}.logo small{font-size:.66rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.nav{display:none}.nav a{text-decoration:none;font-size:.8rem;letter-spacing:.2em;text-transform:uppercase;color:#d9d0bf}.nav a:hover{color:var(--gold)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.6rem;padding:1rem 1.7rem;font:400 .78rem/1 var(--f-t);letter-spacing:.24em;text-transform:uppercase;text-decoration:none;border:1px solid var(--gold);cursor:pointer;transition:background .2s,color .2s}
.btn svg{width:18px;height:18px}.btn-gold{background:var(--gold);color:var(--noir)}.btn-gold:hover{background:var(--gold-l)}
.btn-ghost{background:transparent;color:var(--ivory)}.btn-ghost:hover{background:rgba(201,164,92,.15)}
.hd .btn{display:none}
.burger{width:46px;height:46px;border:1px solid rgba(201,164,92,.5);background:transparent;display:grid;place-items:center;cursor:pointer}
.burger i,.burger i:before,.burger i:after{display:block;width:20px;height:1px;background:var(--gold);position:relative;content:''}.burger i:before{position:absolute;top:-6px}.burger i:after{position:absolute;top:6px}
.nav.open{display:flex;position:fixed;inset:0;top:0;z-index:-1;flex-direction:column;justify-content:center;align-items:center;gap:1.6rem;background:rgba(13,12,10,.97)}
.nav.open a{font:300 1.9rem/1 var(--f-d);letter-spacing:.04em;text-transform:none}
/* hero */
.hero{position:relative;min-height:100svh;display:grid;place-items:center;text-align:center;overflow:hidden;isolation:isolate}
.hero>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;transform:scale(1.04)}
.hero:after{content:'';position:absolute;inset:0;z-index:-1;background:radial-gradient(ellipse at center,rgba(13,12,10,.2) 0,rgba(13,12,10,.62) 72%),linear-gradient(180deg,rgba(13,12,10,.55),rgba(13,12,10,.05) 40%,rgba(13,12,10,.92))}
.hero .in{padding:9rem 1.25rem 7rem;max-width:980px}
.hero .ar{font-size:1.9rem;color:var(--gold);margin:1.2rem 0 .2rem}
.hero h1{font-size:clamp(3.4rem,13vw,8.5rem);letter-spacing:.02em;margin:0;line-height:.95}
.hero h1 i{font-style:italic;color:var(--gold-l)}
.hero .sub{font:300 italic clamp(1.25rem,3vw,1.8rem)/1.35 var(--f-d);color:#e7dfcf;margin:1.2rem auto 2.2rem;max-width:40rem}
.rule{display:flex;align-items:center;gap:1rem;justify-content:center;color:var(--gold)}.rule:before,.rule:after{content:'';width:60px;height:1px;background:currentColor}
.hero .acts{display:flex;flex-wrap:wrap;gap:.8rem;justify-content:center}
.hfacts{position:absolute;left:0;right:0;bottom:0;border-top:1px solid rgba(201,164,92,.25);background:rgba(13,12,10,.55);backdrop-filter:blur(6px)}
.hfacts .wrap{display:grid;grid-template-columns:repeat(3,1fr);text-align:center}
.hfacts div{padding:.8rem .3rem;font-size:.68rem;line-height:1.35;letter-spacing:.04em;color:#cfc6b4}.hfacts div+div{border-left:1px solid rgba(201,164,92,.2)}
.hfacts b{display:block;font:400 1.1rem/1.1 var(--f-d);letter-spacing:0;color:var(--ivory);margin-bottom:.2rem}
/* ivory intro */
.light{background:var(--ivory);color:var(--ink)}.light .caps{color:#9A7A3A}
.sec{padding:6rem 0}
.intro{text-align:center;max-width:58rem;margin:0 auto}
.intro p.big{font:300 clamp(1.6rem,3.6vw,2.6rem)/1.3 var(--f-d);margin:1.4rem 0}
.intro p.big em{color:#9A7A3A}
.orn{width:180px;height:22px;margin:0 auto;display:block}
.duo{display:grid;gap:2.5rem;margin-top:4rem;align-items:center}
.duo .ph-img{position:relative}.duo .ph-img img{width:100%;aspect-ratio:4/5;object-fit:cover}
.duo .ph-img:before{content:'';position:absolute;inset:18px -18px -18px 18px;border:1px solid var(--gold);z-index:0}.duo .ph-img img{position:relative}
.specs{list-style:none;padding:0;margin:1.5rem 0 0;border-top:1px solid #d9cdb4}
.specs li{display:flex;justify-content:space-between;gap:1rem;padding:.9rem 0;border-bottom:1px solid #d9cdb4;font-size:.95rem}
.specs li span:first-child{letter-spacing:.14em;text-transform:uppercase;font-size:.74rem;color:#6d6453;padding-top:.2rem}
/* events */
.events h2,.pk h2,.gal h2,.tst h2,.req h2{font-size:clamp(2.4rem,6vw,4.2rem)}
.evlist{list-style:none;padding:0;margin:3rem 0 0;border-top:1px solid rgba(201,164,92,.3)}
.evlist li{display:grid;grid-template-columns:3.2rem 1fr;gap:.2rem 1rem;padding:1.5rem 0;border-bottom:1px solid rgba(201,164,92,.3);transition:padding .3s,background .3s}
.evlist li:hover{background:linear-gradient(90deg,rgba(201,164,92,.08),transparent);padding-left:.8rem}
.evlist .n{font:300 1rem/2.6 var(--f-d);color:var(--gold)}.evlist h3{font-size:clamp(1.8rem,4vw,2.6rem);margin:0}
.evlist h3 .ar{font-size:.6em;color:var(--gold);margin-left:.8rem}.evlist p{grid-column:2;margin:0;color:#a79e8b;max-width:36rem}
/* packages */
.pkgs{display:grid;gap:1.4rem;margin-top:3rem}
.pkg{border:1px solid #cdb98f;padding:2.4rem 1.8rem;position:relative;background:#fbf7ef;display:flex;flex-direction:column}
.pkg.hl{background:var(--noir2);color:var(--ivory);border-color:var(--gold)}.pkg.hl .caps{color:var(--gold)}
.pkg.hl:before{content:'Clé en main';position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:var(--gold);color:var(--noir);font-size:.66rem;letter-spacing:.24em;text-transform:uppercase;padding:.35rem .9rem}
.pkg h3{font-size:2.1rem;margin:.6rem 0 .4rem}.pkg p{color:#6d6453;margin:0 0 1.2rem}.pkg.hl p{color:#b6ad9a}
.pkg ul{list-style:none;padding:0;margin:0 0 1.8rem;flex:1}.pkg li{padding:.6rem 0 .6rem 1.4rem;border-top:1px solid rgba(201,164,92,.35);position:relative;font-size:.95rem}
.pkg li:before{content:'';position:absolute;left:0;top:1.15rem;width:7px;height:7px;border:1px solid var(--gold);transform:rotate(45deg)}
.pkg .price{font:300 1.6rem/1 var(--f-d);margin-bottom:1.2rem}.pkg .price small{font:400 .7rem/1 var(--f-t);letter-spacing:.2em;text-transform:uppercase;color:var(--muted);display:block;margin-bottom:.4rem}
/* capacity */
.cap{position:relative;overflow:hidden;isolation:isolate}
.cap>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;opacity:.35}
.cap:after{content:'';position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(13,12,10,.95),rgba(13,12,10,.7))}
.cfg{display:grid;gap:1px;background:rgba(201,164,92,.3);margin-top:2.5rem;border:1px solid rgba(201,164,92,.3)}
.cfg div{background:rgba(13,12,10,.85);padding:2rem 1.6rem}.cfg svg{width:54px;height:54px;color:var(--gold);margin-bottom:1rem}
.cfg h3{font-size:1.7rem;margin:0 0 .3rem}.cfg p{margin:0;color:#a79e8b;font-size:.95rem}
/* gallery masonry */
.masonry{columns:2;column-gap:.8rem;margin-top:3rem}
.masonry a{display:block;margin:0 0 .8rem;break-inside:avoid;position:relative;overflow:hidden}
.masonry img{width:100%;height:auto;transition:transform .6s}.masonry a:hover img{transform:scale(1.04)}
.masonry span{position:absolute;left:0;right:0;bottom:0;padding:1.6rem .9rem .7rem;font:400 italic 1.05rem/1.2 var(--f-d);background:linear-gradient(transparent,rgba(0,0,0,.75));color:#f1e9da}
.lb{position:fixed;inset:0;z-index:90;background:rgba(0,0,0,.92);display:none;place-items:center;padding:1.5rem}.lb.open{display:grid}
.lb img{max-height:88vh;width:auto}.lb button{position:absolute;top:1rem;right:1rem;width:48px;height:48px;background:none;border:1px solid var(--gold);color:var(--gold);font-size:1.6rem;cursor:pointer}
/* testimonials */
.quotes{display:grid;gap:1.2rem;margin-top:3rem}
.q{border:1px solid #d9cdb4;padding:2.2rem 1.8rem;background:#fbf7ef;position:relative}
.q:before{content:'“';font:300 5rem/1 var(--f-d);color:var(--gold);position:absolute;top:.4rem;left:1.2rem}
.q p{font:300 italic 1.35rem/1.45 var(--f-d);margin:1.6rem 0 1.2rem;color:#5b5343}.q .who{font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.score{display:grid;gap:.4rem;justify-items:center;text-align:center;border:1px solid var(--gold);padding:2.2rem 1.6rem;background:var(--noir2);color:var(--ivory)}
.score b{font:300 4rem/1 var(--f-d);color:var(--gold-l)}.score a{color:var(--gold)}
.stars{color:var(--gold);letter-spacing:.2em}
/* request form */
.req .grid{display:grid;gap:3rem}
.form{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem 1rem}.form .full{grid-column:1/-1}
.form label{display:grid;gap:.45rem;font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold)}
.form input,.form select,.form textarea{font:300 1rem/1.4 var(--f-t);letter-spacing:0;text-transform:none;color:var(--ivory);background:transparent;border:0;border-bottom:1px solid rgba(201,164,92,.5);padding:.7rem 0;min-height:46px;border-radius:0;width:100%}
.form select option{background:var(--noir2)}.form input::-webkit-calendar-picker-indicator{filter:invert(.8) sepia(1)}
.form textarea{min-height:80px;resize:vertical}.form input:focus,.form select:focus,.form textarea:focus{outline:none;border-bottom-color:var(--gold-l);box-shadow:0 1px 0 var(--gold-l)}
.form .btn{width:100%;padding:1.2rem}.fine{font-size:.8rem;color:var(--muted);text-transform:none;letter-spacing:0}
.steps{counter-reset:s;list-style:none;padding:0;margin:2rem 0}.steps li{counter-increment:s;display:grid;grid-template-columns:2.6rem 1fr;padding:.9rem 0;border-top:1px solid rgba(201,164,92,.25)}
.steps li:before{content:'0' counter(s);font:300 1.2rem/1.4 var(--f-d);color:var(--gold)}
/* access */
.acc{display:grid;gap:2rem}.map{min-height:360px;border:1px solid rgba(201,164,92,.35)}.map iframe{width:100%;height:100%;min-height:360px;border:0;display:block;filter:grayscale(1) invert(.92) contrast(.9) sepia(.25)}
.clist{list-style:none;padding:0;margin:1.5rem 0}.clist li{padding:.9rem 0;border-bottom:1px solid rgba(201,164,92,.2);display:grid;gap:.1rem}.clist small{font-size:.66rem;letter-spacing:.24em;text-transform:uppercase;color:var(--gold)}
.clist a{text-decoration:none}.clist a:hover{color:var(--gold)}
.ft{border-top:1px solid rgba(201,164,92,.25);padding:3rem 0 7rem;font-size:.85rem;color:#8f8676;text-align:center}
.ft .logo{justify-content:center;margin-bottom:1.2rem}.ft details{margin:1.2rem auto;max-width:56rem;text-align:left;font-size:.78rem}.ft summary{cursor:pointer;text-align:center}.ft a{color:#cdbb92}
.badge{display:inline-flex;align-items:center;gap:.4rem;text-decoration:none;border:1px solid rgba(201,164,92,.4);padding:.3rem .8rem;margin-top:.6rem}.badge i{width:7px;height:7px;background:var(--gold);transform:rotate(45deg)}
.float{position:fixed;right:1rem;bottom:1rem;z-index:40;display:inline-flex;align-items:center;gap:.5rem;background:var(--gold);color:var(--noir);text-decoration:none;padding:.9rem 1.2rem;font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;box-shadow:0 10px 30px rgba(0,0,0,.5)}
.float svg{width:20px;height:20px}.float span{display:none}.hero .caps{letter-spacing:.2em}
@media (min-width:760px){
 .float span{display:inline}.hero .caps{letter-spacing:.32em}.hfacts div{padding:1rem .4rem;font-size:.75rem;letter-spacing:.1em}.hfacts b{font-size:1.35rem}
 .masonry{columns:3}.duo{grid-template-columns:.9fr 1.1fr;gap:5rem}.pkgs{grid-template-columns:repeat(3,1fr);align-items:stretch}.pkg.hl{transform:translateY(-14px)}
 .cfg{grid-template-columns:repeat(3,1fr)}.quotes{grid-template-columns:repeat(3,1fr)}.tst .top{display:grid;grid-template-columns:1.6fr 1fr;gap:2rem;align-items:end}
 .req .grid{grid-template-columns:.9fr 1.1fr;gap:5rem}.acc{grid-template-columns:1.2fr .8fr}.evlist li{grid-template-columns:5rem 1fr 1fr;align-items:center}.evlist p{grid-column:3}
}
@media (min-width:1020px){.nav{display:flex;gap:2rem}.nav.open{position:static;background:none;flex-direction:row}.burger{display:none}.hd .btn{display:inline-flex;padding:.85rem 1.3rem}}
'''

ORN = '<svg class="orn" viewBox="0 0 180 22" aria-hidden="true"><path d="M0 11h66M114 11h66" stroke="#C9A45C" stroke-width=".8"/><path d="M90 2l9 9-9 9-9-9z" fill="none" stroke="#C9A45C"/><path d="M90 7l4 4-4 4-4-4z" fill="#C9A45C"/><circle cx="72" cy="11" r="1.6" fill="#C9A45C"/><circle cx="108" cy="11" r="1.6" fill="#C9A45C"/></svg>'
I_TABLE = '<svg viewBox="0 0 54 54" fill="none" stroke="currentColor" stroke-width="1" aria-hidden="true"><circle cx="16" cy="16" r="7"/><circle cx="38" cy="16" r="7"/><circle cx="16" cy="38" r="7"/><circle cx="38" cy="38" r="7"/><g fill="currentColor" stroke="none"><circle cx="16" cy="6" r="1.4"/><circle cx="26" cy="16" r="1.4"/><circle cx="6" cy="16" r="1.4"/><circle cx="38" cy="6" r="1.4"/><circle cx="48" cy="16" r="1.4"/><circle cx="16" cy="48" r="1.4"/><circle cx="6" cy="38" r="1.4"/><circle cx="38" cy="48" r="1.4"/><circle cx="48" cy="38" r="1.4"/></g></svg>'
I_STAGE = '<svg viewBox="0 0 54 54" fill="none" stroke="currentColor" stroke-width="1" aria-hidden="true"><path d="M6 20h42v8H6zM10 28v18M44 28v18"/><path d="M20 20v-6a7 7 0 0 1 14 0v6"/><path d="M4 8c8 4 16 4 23 0 7 4 15 4 23 0"/></svg>'
I_GLASS = '<svg viewBox="0 0 54 54" fill="none" stroke="currentColor" stroke-width="1" aria-hidden="true"><circle cx="27" cy="27" r="20"/><circle cx="27" cy="27" r="12" stroke-dasharray="2 3"/><circle cx="27" cy="27" r="3"/><path d="M27 3v6M27 45v6M3 27h6M45 27h6"/></svg>'

def build(M):
    S = dict(title='Royal Palace — Salle des fêtes à Béni Khalled, mariages & événements (démo)',
             desc='Royal Palace, salle des fêtes à Béni Khalled (Cap Bon) : mariages, fiançailles, henna, fêtes de famille. Formules, capacité, demande de date et visite sur WhatsApp.',
             favicon="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%230D0C0A'/%3E%3Cpath d='M32 8l24 24-24 24L8 32z' fill='none' stroke='%23C9A45C' stroke-width='2'/%3E%3Ctext x='32' y='40' font-size='20' text-anchor='middle' fill='%23C9A45C' font-family='Georgia'%3ERP%3C/text%3E%3C/svg%3E")
    wa_msg = walink(WA, 'Bonjour Royal Palace, je souhaite connaître vos disponibilités et tarifs.')
    maps = 'https://www.google.com/maps/search/?api=1&query=' + MAPQ
    events = [('Mariage', 'عرس', 'La soirée des mariés, de l’arrivée du cortège au dernier morceau.'),
              ('Fiançailles · Outya', 'خطوبة', 'Pour réunir les deux familles autour d’un premier grand moment.'),
              ('Henna', 'حنة', 'La soirée du henné, entre traditions, keswa et musique.'),
              ('Circoncision · Tahour', 'طهور', 'Une fête de famille pour célébrer les petits.'),
              ('Anniversaire', 'عيد ميلاد', 'Anniversaires, réussites, retrouvailles.'),
              ('Autre événement', 'مناسبة', 'Toute célébration familiale : parlons-en lors de la visite.')]
    evl = ''.join(f'<li><span class="n">{i+1:02d}</span><h3>{n}<span class="ar" lang="ar">{a}</span></h3><p>{d}</p></li>' for i, (n, a, d) in enumerate(events))
    pk = [('Essentielle', 'Location de la salle', 'La salle seule, pour votre traiteur et votre décorateur.', ['Salle et mobilier', 'Climatisation / sonorisation ' + PH, 'Horaires ' + PH], False),
          ('Clé en main', 'Mariage complet', 'Salle, décoration et service réunis.', ['Salle et décoration « kosha »', 'Service en salle', 'Traiteur partenaire ' + PH], True),
          ('Petits comités', 'Fiançailles & henna', 'Pour les fêtes plus intimes.', ['Salle en configuration réduite', 'Décoration', 'Jours de semaine ' + PH], False)]
    pkh = ''.join(f'''<article class="pkg{' hl' if hl else ''}"><span class="caps">{e}</span><h3>{n}</h3><p>{d}</p><ul>{''.join(f'<li>{x}</li>' for x in items)}</ul>
<div class="price"><small>Tarif</small>Sur devis {PH}</div><a class="btn {'btn-gold' if hl else 'btn-ghost'}" href="#date" style="{'' if hl else 'color:var(--ink)'}">Demander un devis</a></article>''' for e, n, d, items, hl in pk)
    gal = [('lustre', 'Lustre en cristal'), ('table', 'Centre de table fleuri'), ('banquet', 'Salle de réception dressée'), ('broderie', 'Broderie tunisienne traditionnelle'),
           ('bougies', 'Bougies et fleurs'), ('henne', 'Henné de la mariée'), ('salon', 'Salon de réception'), ('coupole', 'Lustre sous verrière')]
    galh = ''.join(f'<a href="media/{n}.webp" data-full="media/{n}.webp">{M.img(n, a + " (photo d’ambiance)", sizes="(max-width: 760px) 50vw, 33vw")}<span>{a}</span></a>' for n, a in gal)
    q = ''.join(f'<figure class="q"><p>Espace réservé au témoignage d’une famille, publié avec son accord après l’événement.</p><figcaption class="who">Prénom · {t} · date</figcaption></figure>' for t in ('Mariage', 'Fiançailles', 'Henna'))
    body = f'''<a class="skip" href="#main">Aller au contenu</a>
<header class="hd" data-header><div class="ribbon">{RIBBON}</div><div class="wrap">
 <a class="logo" href="#top" aria-label="Royal Palace, accueil"><span class="mono"><span>RP</span></span><span><b>Royal Palace</b><small>Salle des fêtes · Béni Khalled</small></span></a>
 <nav class="nav" data-nav aria-label="Navigation"><a href="#salle">La salle</a><a href="#evenements">Événements</a><a href="#formules">Formules</a><a href="#galerie">Galerie</a><a href="#acces">Accès</a></nav>
 <a class="btn btn-ghost" href="#date">Vérifier une date</a>
 <button class="burger" type="button" data-menu aria-label="Ouvrir le menu" aria-expanded="false"><i></i></button>
</div></header>
<main id="main">
<section class="hero" id="top">
 {M.img('hero', 'Grande salle de réception avec lustres (photo d’ambiance, ne représente pas la salle)', sizes='100vw', lazy=False)}
 <div class="in">
  <p class="caps">Salle des fêtes · Béni Khalled · Cap Bon</p>
  <p class="ar" lang="ar">قاعة الأفراح</p>
  <h1>Royal <i>Palace</i></h1>
  <p class="sub">Mariages, fiançailles, henna et fêtes de famille&nbsp;: le cadre de vos plus grands jours, au cœur du Cap Bon.</p>
  <div class="acts"><a class="btn btn-gold" href="#date">Demander une date</a><a class="btn btn-ghost" href="{wa_msg}" target="_blank" rel="noopener">{WA_SVG}WhatsApp</a></div>
 </div>
 <div class="hfacts"><div class="wrap"><div><b>3,9 / 5</b>76 avis · plurielle.tn</div><div><b>Sur rendez-vous</b>visites de la salle</div><div><b>Béni Khalled</b>≈ 45 min de Tunis</div></div></div>
</section>

<section class="sec light" id="salle"><div class="wrap">
 <div class="intro"><p class="caps">La salle</p>{ORN}<p class="big">Le Royal Palace accueille les <em>mariages</em> et les <em>fêtes de famille</em> de Béni Khalled et de tout le Cap Bon — pour que vous n’ayez qu’à profiter.</p></div>
 <div class="duo">
  <div class="ph-img">{M.img('table', 'Table de réception décorée de fleurs blanches (photo d’ambiance)', sizes='(max-width: 760px) 90vw, 45vw')}</div>
  <div><h2 style="font-size:clamp(2rem,4.5vw,3.2rem)">Une salle pour les grands jours</h2>
   <p>Capacité, équipements et tarifs seront renseignés avec vous&nbsp;: ils apparaîtront ici clairement, pour que les familles aient toutes les réponses avant la visite.</p>
   <ul class="specs"><li><span>Capacité</span><span>{PH}</span></li><li><span>Climatisation</span><span>{PH}</span></li><li><span>Parking</span><span>{PH}</span></li><li><span>Cuisine traiteur</span><span>{PH}</span></li><li><span>Loge des mariés</span><span>{PH}</span></li></ul></div>
 </div>
</div></section>

<section class="sec events" id="evenements"><div class="wrap">
 <p class="caps">Vos célébrations</p><h2>Chaque fête a <i>son</i> rituel</h2>
 <ol class="evlist">{evl}</ol>
</div></section>

<section class="sec light pk" id="formules"><div class="wrap">
 <div style="text-align:center"><p class="caps">Formules</p><h2>Des formules claires,<br>un devis rapide</h2><p style="max-width:38rem;margin:0 auto;color:#6d6453">Trois formules d’exemple pour aider les familles à choisir. Contenu exact et tarifs {PH}.</p></div>
 <div class="pkgs">{pkh}</div>
</div></section>

<section class="sec cap" aria-labelledby="cap-h">
 {M.img('coupole', '', sizes='100vw', extra=' aria-hidden="true"')}
 <div class="wrap"><p class="caps">Capacité & configurations</p><h2 id="cap-h" style="font-size:clamp(2.2rem,5vw,3.6rem)">Une salle, plusieurs mises en scène</h2>
 <div class="cfg">
  <div>{I_TABLE}<h3>Dîner assis</h3><p>Tables rondes dressées · invités {PH}</p></div>
  <div>{I_STAGE}<h3>Kosha & scène</h3><p>Estrade des mariés, piste de danse · dimensions {PH}</p></div>
  <div>{I_GLASS}<h3>Réception</h3><p>Fiançailles, henna, réception debout · invités {PH}</p></div>
 </div></div>
</section>

<section class="sec gal" id="galerie"><div class="wrap">
 <p class="caps">Inspirations</p><h2>L’art de recevoir</h2><p style="color:#a79e8b;max-width:40rem">Décors, lumières et traditions de mariage. <span class="ph long">photos d’ambiance sous licence libre — à remplacer par vos photos</span></p>
 <div class="masonry">{galh}</div>
</div></section>

<section class="sec light tst" id="avis"><div class="wrap">
 <div class="top"><div><p class="caps">Témoignages</p><h2>Ils ont fêté ici</h2><p style="color:#6d6453;max-width:36rem">Exemple de mise en page&nbsp;: <b>aucun avis réel n’est affiché</b>. Dans la version finale, les familles laissent un mot après leur événement (avec leur accord).</p></div>
 <div class="score"><span class="caps">Note publique</span><b>3,9</b><span class="stars" aria-label="3,9 sur 5">★★★★☆</span><span>76 avis · <a href="https://plurielle.tn/pro/nabeul/salle-des-fetes-royal-palace/" target="_blank" rel="noopener">plurielle.tn</a></span><small style="color:var(--muted)">Relevé le {CONSULTED}</small></div></div>
 <div class="quotes">{q}</div>
</div></section>

<section class="sec req" id="date"><div class="wrap grid">
 <div><p class="caps">Demande de date</p><h2>Votre date est-elle libre&nbsp;?</h2>
  <p style="color:#b6ad9a">Indiquez la date, le type de fête et le nombre d’invités&nbsp;: la demande arrive directement sur le WhatsApp de la salle, qui vous propose une visite.</p>
  <ol class="steps"><li><span><b>Votre événement</b> — date, type, invités.</span></li><li><span><b>Envoi WhatsApp</b> — message pré-rempli, sans appel.</span></li><li><span><b>Visite & devis</b> — la salle vous rappelle.</span></li></ol>
  <p class="fine">Visite de la salle sur rendez-vous. Acompte et conditions de réservation {PH}. Par e-mail&nbsp;: <span class="ph">adresse à ajouter</span></p>
 </div>
 <form class="form" data-wa="{WA}" data-intro="Bonjour Royal Palace, je souhaite vérifier une date / demander un devis :" novalidate>
  <label>Date souhaitée<input type="date" name="date" data-label="Date" required></label>
  <label>Type d’événement<select name="type" data-label="Événement">{''.join(f'<option>{n}</option>' for n, _, _ in events)}</select></label>
  <label>Invités<select name="invites" data-label="Invités"><option>Moins de 100</option><option>100 – 200</option><option>200 – 300</option><option>300 – 400</option><option>Plus de 400</option><option>Je ne sais pas encore</option></select></label>
  <label>Formule<select name="formule" data-label="Formule"><option>Je souhaite être conseillé(e)</option>{''.join(f'<option>{n}</option>' for _, n, _, _, _ in pk)}</select></label>
  <label class="full">Nom<input name="nom" data-label="Nom" autocomplete="name" required></label>
  <label class="full">Téléphone / WhatsApp<input name="tel" data-label="Téléphone" type="tel" inputmode="tel" autocomplete="tel" required></label>
  <label class="full">Message (optionnel)<textarea name="message" data-label="Message" placeholder="Visite souhaitée le samedi matin, traiteur, décoration…"></textarea></label>
  <div class="full"><button class="btn btn-gold" type="submit">{WA_SVG}<span>Envoyer ma demande</span></button></div>
  <p class="full fine">Démo&nbsp;: aucune donnée n’est enregistrée. Le formulaire ouvre WhatsApp avec votre demande ; rien n’est envoyé sans votre validation.</p>
 </form>
</div></section>

<section class="sec" id="acces" style="padding-top:2rem"><div class="wrap acc">
 <div class="map"><iframe title="Carte : Royal Palace, Béni Khalled" src="https://maps.google.com/maps?q={MAPQ}&z=16&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
 <div><p class="caps">Accès</p><h2 style="font-size:clamp(2.2rem,5vw,3.4rem)">À Béni Khalled</h2><p style="color:#b6ad9a">Au cœur du Cap Bon, à environ 45 min de Tunis et 25 min de Nabeul.</p>
  <ul class="clist"><li><small>Adresse</small><span>{ADDR}</span></li><li><small>Téléphone</small><a href="tel:{TEL}">{WA_DISP}</a></li><li><small>WhatsApp</small><a href="https://wa.me/{WA}" target="_blank" rel="noopener">{WA_DISP}</a></li>
   <li><small>Réseaux</small><span><a href="https://www.facebook.com/Royal-Palace-793421110739436" target="_blank" rel="noopener">Facebook</a> · <a href="https://www.instagram.com/salle_des_fetes_royal_palace" target="_blank" rel="noopener">@salle_des_fetes_royal_palace</a></span></li><li><small>Visites</small><span>Sur rendez-vous {PH}</span></li></ul>
  <a class="btn btn-ghost" href="{maps}" target="_blank" rel="noopener">Itinéraire</a></div>
</div></section>
</main>
<footer class="ft"><div class="wrap">
 <a class="logo" href="#top"><span class="mono"><span>RP</span></span><span><b>Royal Palace</b><small>Salle des fêtes · Béni Khalled</small></span></a>
 <p>Site de démonstration non officiel réalisé à partir d’informations publiques. Contenus, formules et tarifs indicatifs, à valider par l’établissement.</p>
 <details><summary>Crédits photos (licences libres, Wikimedia Commons)</summary><ul>{M.credits_html()}<li>Ornements et pictogrammes : dessins SVG originaux Synaris Labs.</li></ul></details>
 <p>© <span id="year">2026</span> Royal Palace · <a class="badge" href="https://github.com/islemyakoubi" target="_blank" rel="noopener"><i></i>Démo réalisée par Synaris Labs · Menzel Temime</a></p>
</div></footer>
<a class="float" href="{wa_msg}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_SVG}<span>Disponibilités</span></a>
<div class="lb" role="dialog" aria-modal="true" aria-label="Photo agrandie"><button type="button" aria-label="Fermer">×</button><img alt=""></div>'''
    return page(S, M, FONTS, CSS, body, '#0D0C0A')
