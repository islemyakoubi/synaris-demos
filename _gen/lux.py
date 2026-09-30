# Moteur commun des sites premium (lots 3+) : en-tête + ruban démo, révélations au défilement, parallaxe, horaires, contacts, formulaire WhatsApp,
# carte, pied de page, barre mobile. Chaque site fournit sa propre direction artistique (polices, palette, mise en page) dans son gabarit l<N>_*.py.
import gen_lot2 as K
esc, ph, I, telhref = K.esc, K.ph, K.I, K.telhref
def _i(p, sw='1.3'): return f'<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
IC = dict(
 ear=_i('<path d="M15 20a10 10 0 0 1 20 0c0 6-5 8-6 12s-2 8-7 8-6-4-6-6"/><path d="M20 21a4.5 4.5 0 0 1 9 0c0 3-3 3.5-3 6"/>'),
 nose=_i('<path d="M24 8c-1 8-7 16-7 22a5 5 0 0 0 5 5h4a5 5 0 0 0 5-5"/><path d="M19 35c-2 1-4 1-5-1M29 35c2 1 4 1 5-1"/>'),
 throat=_i('<path d="M18 6v10c0 6-4 9-4 16v10M30 6v10c0 6 4 9 4 16v10"/><path d="M20 26h8M21 31h6"/>'),
 wave=_i('<path d="M4 24h6l3-8 4 16 4-22 4 28 4-20 3 10 3-4h9"/>'),
 heart=_i('<path d="M24 40S8 30 8 18a8 8 0 0 1 16-2 8 8 0 0 1 16 2c0 12-16 22-16 22z"/><path d="M12 24h7l2-4 3 8 2-4h9"/>'),
 pulse=_i('<path d="M4 26h10l3-7 5 14 5-20 4 13h13"/>'),
 steth=_i('<path d="M12 6v12a8 8 0 0 0 16 0V6"/><path d="M20 26v4a9 9 0 0 0 18 0v-4"/><circle cx="38" cy="22" r="4"/>'),
 eye=_i('<path d="M4 24s7-12 20-12 20 12 20 12-7 12-20 12S4 24 4 24z"/><circle cx="24" cy="24" r="6"/><circle cx="24" cy="24" r="2"/>'),
 lens=_i('<circle cx="15" cy="26" r="8"/><circle cx="33" cy="26" r="8"/><path d="M23 25c1-1 1-1 2 0M7 24l-3-6M41 24l3-6"/>'),
 prism=_i('<path d="M24 8 40 38H8z"/><path d="M4 22l14 4M26 24l18-8M27 27l17 2M27 30l17 10"/>'),
 tooth=_i('<path d="M15 8c-5 0-8 4-8 9 0 4 2 7 3 10 1 4 1 8 2 12 1 3 2 4 4 4 3 0 3-8 5-12 1-2 2-2 3 0 2 4 2 12 5 12 2 0 3-1 4-4 1-4 1-8 2-12 1-3 3-6 3-10 0-5-3-9-8-9-4 0-6 2-9 2s-5-2-9-2z"/>'),
 flask=_i('<path d="M19 6h10M21 6v12L10 38a3 3 0 0 0 3 4h22a3 3 0 0 0 3-4L27 18V6"/><path d="M14 30h20"/>'),
 tube=_i('<path d="M17 6h14M20 6v30a4 4 0 0 0 8 0V6"/><path d="M20 22h8"/>'),
 micro=_i('<path d="M20 8l6 3-5 10-6-3zM18 21l-2 4M24 18c7 2 10 8 8 15M10 42h28M16 36h18"/>'),
 drop=_i('<path d="M24 6s-12 13-12 22a12 12 0 0 0 24 0C36 19 24 6 24 6z"/>'),
 car=_i('<path d="M6 32v-7l5-10h26l5 10v7z"/><path d="M6 25h36"/><circle cx="14" cy="33" r="3.5"/><circle cx="34" cy="33" r="3.5"/>'),
 wheel=_i('<circle cx="24" cy="24" r="17"/><circle cx="24" cy="24" r="4"/><path d="M7.5 21c6 1 10 1 12.6 1.8M40.5 21c-6 1-10 1-12.6 1.8M24 28v13"/>'),
 road=_i('<path d="M18 6 10 42M30 6l8 36M24 8v5M24 19v6M24 31v7"/>'),
 moto=_i('<circle cx="11" cy="32" r="6"/><circle cx="37" cy="32" r="6"/><path d="M11 32l8-10h9l9 10M22 22l-3-6h-5M28 22l4-6h5"/>'),
 sign=_i('<path d="M24 5 43 24 24 43 5 24z"/><path d="M24 16v10M24 31v1"/>'),
 cone=_i('<path d="M20 8h8l8 30H12z"/><path d="M8 38h32M17 20h14M15 29h18"/>'),
 book=_i('<path d="M8 10c6-2 11-1 16 3 5-4 10-5 16-3v28c-6-2-11-1-16 3-5-4-10-5-16-3z"/><path d="M24 13v28"/>'),
 cap=_i('<path d="M4 19 24 10l20 9-20 9z"/><path d="M12 23v9c4 4 20 4 24 0v-9M44 19v10"/>'),
 pen=_i('<path d="M32 6l10 10-22 22H10V28z"/><path d="M28 10l10 10"/>'),
 scale=_i('<path d="M24 6v34M14 42h20M8 12h32"/><path d="M8 12 3 24a5 5 0 0 0 10 0zM40 12l-5 12a5 5 0 0 0 10 0z"/>'),
 doc=_i('<path d="M12 6h17l9 9v27H12z"/><path d="M29 6v9h9M18 24h14M18 30h14M18 36h8"/>'),
 knee=_i('<path d="M20 4v14c0 3 2 5 5 5h1c3 0 5 2 5 5v16"/><path d="M15 4v14c0 6 4 10 10 10M36 44V29"/>'),
 spine=_i('<rect x="19" y="5" width="10" height="6" rx="2"/><rect x="18" y="14" width="12" height="6" rx="2"/><rect x="17" y="23" width="14" height="6" rx="2"/><rect x="18" y="32" width="12" height="6" rx="2"/><path d="M24 38v5"/>'),
 hand=_i('<path d="M16 26V12a3 3 0 0 1 6 0v10M22 20V9a3 3 0 0 1 6 0v12M28 20v-8a3 3 0 0 1 6 0v14c0 9-5 16-13 16-6 0-9-4-12-9l-4-7a3 3 0 0 1 5-3l4 5"/>'),
 band=_i('<path d="M8 30c6-10 26-10 32 0M8 30c6 8 26 8 32 0"/><circle cx="8" cy="30" r="3"/><circle cx="40" cy="30" r="3"/>'),
 run=_i('<circle cx="30" cy="8" r="3.5"/><path d="M18 20l7-5 6 4 4 7M25 15l-3 11 7 6v10M22 26l-6 8H9M35 26h5"/>'),
 flower=_i('<circle cx="24" cy="20" r="4"/><path d="M24 16c-3-8 3-10 3-10s6 2 3 10M28 19c8-2 10 4 10 4s-2 6-10 3M20 19c-8-2-10 4-10 4s2 6 10 3M22 24c-4 7 1 10 1 10M26 24c4 7-1 10-1 10M24 34v10"/>'),
 baby=_i('<circle cx="24" cy="16" r="8"/><path d="M12 42c0-8 5-14 12-14s12 6 12 14"/><path d="M21 16h.1M27 16h.1M21 20c2 1.5 4 1.5 6 0"/>'),
 echo=_i('<path d="M10 40 24 8l14 32"/><path d="M15 30c6 3 12 3 18 0M18 22c4 2 8 2 12 0"/>'),
 house=_i('<path d="M6 22 24 8l18 14"/><path d="M11 18v22h26V18M20 40V28h8v12"/>'),
 pool=_i('<path d="M4 34c4 0 4 3 8 3s4-3 8-3 4 3 8 3 4-3 8-3 4 3 8 3M4 40c4 0 4 3 8 3s4-3 8-3 4 3 8 3 4-3 8-3 4 3 8 3"/><path d="M14 30V10a4 4 0 0 1 8 0M30 30V10a4 4 0 0 1 8 0M14 16h16M14 23h16"/>'),
 fire=_i('<path d="M24 42c-8 0-13-5-13-12 0-9 9-12 8-22 7 4 12 10 12 17 2-2 3-4 3-7 4 4 6 8 6 12 0 7-7 12-16 12z"/><path d="M8 44h32"/>'),
 bed=_i('<path d="M4 36V12M44 36V26a6 6 0 0 0-6-6H20v10M4 30h40M4 36h40"/><circle cx="12" cy="24" r="4"/>'),
 leaf=_i('<path d="M40 8C18 8 8 18 8 32c0 4 1 6 2 8 2-12 10-20 20-24-8 6-14 14-16 24 18 2 26-12 26-32z"/>'),
 cup=_i('<path d="M8 18h26v10a12 12 0 0 1-12 12h-2A12 12 0 0 1 8 28z"/><path d="M34 22h3a5 5 0 0 1 0 10h-4M16 6c-2 3 2 5 0 8M24 6c-2 3 2 5 0 8"/>'),
 crepe=_i('<path d="M6 30c8 10 28 10 36 0L24 10z"/><path d="M14 26c4 2 6-2 10 0s6-2 10 0"/>'),
 glass=_i('<path d="M14 6h20l-3 34a3 3 0 0 1-3 2h-8a3 3 0 0 1-3-2z"/><path d="M15 16h18M30 6l6-4"/>'),
 sun=_i('<circle cx="24" cy="24" r="8"/><path d="M24 4v5M24 39v5M4 24h5M39 24h5M10 10l3.5 3.5M34.5 34.5 38 38M10 38l3.5-3.5M34.5 13.5 38 10"/>'),
 moon=_i('<path d="M36 30A15 15 0 0 1 18 12a15 15 0 1 0 18 18z"/>'),
 clock=_i('<circle cx="24" cy="24" r="18"/><path d="M24 13v11l8 5"/>'),
 cal=_i('<rect x="6" y="10" width="36" height="32" rx="3"/><path d="M6 20h36M16 6v8M32 6v8"/>'),
 pin=_i('<path d="M38 20c0 11-14 24-14 24S10 31 10 20a14 14 0 0 1 28 0z"/><circle cx="24" cy="20" r="5"/>'),
 chat=_i('<path d="M42 30a4 4 0 0 1-4 4H16l-8 8V10a4 4 0 0 1 4-4h26a4 4 0 0 1 4 4z"/>'),
 shield=_i('<path d="M24 44s16-8 16-20V10L24 4 8 10v14c0 12 16 20 16 20z"/><path d="m17 24 5 5 9-10"/>'),
 spark=_i('<path d="M24 4l4 16 16 4-16 4-4 16-4-16-16-4 16-4z"/>'),
 arrow='<svg class="arw" viewBox="0 0 26 10" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M0 5h24M20 1l4 4-4 4"/></svg>',
)
CSS = '''
:root{--ease:cubic-bezier(.2,.7,.2,1);--r:0px}
html{background:var(--bg);overflow-x:clip}body{overflow-x:clip;background:var(--bg);color:var(--fg);font:400 1rem/1.72 var(--sans);-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{text-decoration:none}h1,h2,h3,h4{font-family:var(--disp);margin:0;line-height:1.04;font-weight:400}p{margin:0 0 1rem}
::selection{background:var(--acc);color:var(--bg)}
.w{width:min(1200px,100% - 3rem);margin-inline:auto}
.ph{display:inline-block;font:600 .64rem/1 var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--acc);border:1px solid currentColor;padding:.34rem .6rem;border-radius:99px;white-space:nowrap;vertical-align:middle;opacity:.9}
.kick{display:inline-flex;align-items:center;gap:.8rem;font:600 .72rem/1 var(--sans);letter-spacing:.24em;text-transform:uppercase;color:var(--acc);margin:0 0 1.4rem}.kick:before{content:'';width:34px;height:1px;background:currentColor}
.hdr{position:fixed;inset:0 0 auto;z-index:50;isolation:isolate;transition:color .4s}
.hdr:before{content:'';position:absolute;inset:0;z-index:-1;background:var(--hbg);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);opacity:0;transition:opacity .45s var(--ease);box-shadow:0 1px 0 var(--line)}.hdr.scrolled:before{opacity:1}
.rb{background:var(--rbg,rgba(0,0,0,.6));color:var(--rfg,#e8e4dc);font:400 .7rem/1.4 var(--sans);text-align:center;padding:.36rem 1rem}.rb b{font-weight:700;color:var(--rfg2,#fff)}
.nav{display:flex;align-items:center;justify-content:space-between;gap:1.5rem;height:76px;transition:height .45s var(--ease)}.hdr.scrolled .nav{height:64px}
.brand{display:flex;align-items:center;gap:.8rem;color:inherit;min-width:0}.brand b{display:block;font:500 1.12rem/1.1 var(--disp)}.brand small{display:block;font:500 .6rem/1.5 var(--sans);letter-spacing:.24em;text-transform:uppercase;opacity:.7}
.menu{display:flex;align-items:center;gap:2rem}.menu a{color:inherit;font:500 .8rem/1 var(--sans);letter-spacing:.06em;position:relative;padding:.35rem 0}
.menu a:not(.cta):after{content:'';position:absolute;left:0;right:100%;bottom:0;height:1px;background:currentColor;transition:right .35s var(--ease)}.menu a:not(.cta):hover:after{right:0}
.menu a.cta{padding:.8rem 1.25rem;background:var(--acc);color:var(--onacc);border-radius:var(--r)}
.burger{display:none;width:46px;height:46px;border:1px solid currentColor;background:transparent;color:inherit;border-radius:50%;cursor:pointer;position:relative;flex:none}
.burger span,.burger:before,.burger:after{content:'';position:absolute;left:14px;right:14px;height:1.5px;background:currentColor;transition:transform .3s,opacity .3s}.burger:before{top:17px}.burger span{top:22px}.burger:after{top:27px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.7rem;font:600 .8rem/1 var(--sans);letter-spacing:.08em;padding:1.1rem 1.6rem;border-radius:var(--r);transition:transform .3s var(--ease),background .3s,color .3s,gap .3s;border:1px solid transparent}
.btn svg{width:17px;height:17px;flex:none}.btn .arw{width:24px;height:10px}.btn:hover{gap:1rem}
.btn.p{background:var(--acc);color:var(--onacc)}.btn.o{border-color:currentColor;color:inherit}
.rv-on [data-rv]{opacity:0;transform:translateY(34px);transition:opacity 1s var(--ease),transform 1s var(--ease),clip-path 1.2s var(--ease);transition-delay:var(--d,0s)}
.rv-on [data-rv=l]{transform:translateX(-44px)}.rv-on [data-rv=r]{transform:translateX(44px)}.rv-on [data-rv=s]{transform:scale(.93)}.rv-on [data-rv=c]{transform:none;opacity:1}.rv-on [data-rv=c]:after{content:'';position:absolute;inset:0;z-index:3;background:var(--bg);transform-origin:50% 100%;transition:transform 1.3s var(--ease) var(--d,0s)}.rv-on [data-rv=c].rvd:after{transform:scaleY(0)}
.rv-on [data-rv].rvd{opacity:1;transform:none}
.rise{animation:rise 1.2s var(--ease) both}.rise.d1{animation-delay:.12s}.rise.d2{animation-delay:.24s}.rise.d3{animation-delay:.36s}.rise.d4{animation-delay:.5s}
@keyframes rise{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:none}}
.pxw{position:absolute;inset:0;overflow:hidden;z-index:-2}.px{position:absolute;left:0;top:-14%;width:100%;height:128%;object-fit:cover;will-change:transform}
.mq{overflow:hidden;white-space:nowrap;user-select:none}.mq>div{display:inline-flex;animation:mq var(--mqs,42s) linear infinite}.mq span{padding-right:3rem}@keyframes mq{to{transform:translateX(-50%)}}
.tb{width:100%;border-collapse:collapse;font-size:.93rem}.tb td{padding:.62rem 0;border-bottom:1px solid var(--line)}.tb td+td{text-align:right}.tb .today td{color:var(--acc);font-weight:700}
.tb .today td:first-child:after{content:' · aujourd’hui';font-weight:400;opacity:.7}.note{font-size:.78rem;opacity:.72;margin:.8rem 0 0}
.ci{list-style:none;margin:0;padding:0}.ci li{display:flex;gap:1rem;align-items:center;padding:1rem 0;border-bottom:1px solid var(--line)}.ci svg{width:22px;height:22px;flex:none;color:var(--acc)}
.ci small{display:block;font:600 .62rem/1.4 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.65}.ci a,.ci span.v{font-size:1.08rem;color:inherit;font-weight:500}
.form{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem 1.4rem}.form .full{grid-column:1/-1}.form label{display:grid;gap:.4rem}
.form label span{font:600 .64rem/1 var(--sans);letter-spacing:.18em;text-transform:uppercase;opacity:.75}
.form input,.form select,.form textarea{font:400 1rem var(--sans);color:inherit;background:var(--fbg,transparent);border:1px solid var(--fln,var(--line));border-radius:var(--r);padding:.8rem .9rem;min-height:48px;width:100%;-webkit-appearance:none;appearance:none;transition:border-color .3s,box-shadow .3s}
.form select{background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' fill='none' stroke='%23888' stroke-width='1.4'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right .9rem center;background-size:12px}
.form input:focus,.form select:focus,.form textarea:focus{outline:0;border-color:var(--acc);box-shadow:0 0 0 3px color-mix(in srgb,var(--acc) 22%,transparent)}
.form button{grid-column:1/-1;display:flex;gap:.7rem;justify-content:center;align-items:center;background:var(--acc);color:var(--onacc);border:0;border-radius:var(--r);padding:1.15rem;font:700 .82rem/1 var(--sans);letter-spacing:.1em;text-transform:uppercase;cursor:pointer;transition:filter .3s}
.form button:hover{filter:brightness(1.08)}.form button svg{width:18px;height:18px}.fnote{grid-column:1/-1;font-size:.76rem;opacity:.72;margin:0;line-height:1.6}
.mapw{position:relative;min-height:380px;overflow:hidden;background:var(--mapbg,#e9e6df)}.mapfb{position:absolute;inset:0;display:grid;place-content:center;justify-items:center;gap:.8rem;font:600 .66rem/1 var(--sans);letter-spacing:.24em;text-transform:uppercase;opacity:.7}
.mapfb svg{width:34px;height:34px;color:var(--acc)}.map{position:absolute;inset:0;width:100%;height:100%}
.ft{padding:4rem 0 6.5rem;font-size:.82rem}.ft .top{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1.6rem;padding-bottom:2rem;margin-bottom:1.6rem;border-bottom:1px solid var(--line)}
.ft nav{display:flex;gap:1.6rem;flex-wrap:wrap}.ft nav a{color:inherit;opacity:.8}.ft nav a:hover{opacity:1}.ft .credits{margin-bottom:1rem}.ft .credits a,.ft .legal a{text-decoration:underline;text-underline-offset:3px}.ft .legal{margin:0;opacity:.75;line-height:1.7}
.deo{font-size:.92rem;line-height:1.75}
.dock{display:none}
@media(max-width:1020px){.menu a:not(.cta){display:none}.burger{display:block}
.menu.open{display:flex;position:fixed;inset:0;z-index:60;background:var(--bg);color:var(--fg);flex-direction:column;justify-content:center;align-items:flex-start;gap:1.4rem;padding:0 2rem}
.menu.open a,.menu.open a:not(.cta){display:block;font:400 2.3rem/1.1 var(--disp);letter-spacing:0}.menu.open a.cta{background:none;color:var(--acc);padding:0}
.burger[aria-expanded=true]{position:fixed;right:1.2rem;top:3.4rem;z-index:61;color:var(--fg)}.burger[aria-expanded=true]:before{transform:translateY(5px) rotate(45deg)}.burger[aria-expanded=true]:after{transform:translateY(-5px) rotate(-45deg)}.burger[aria-expanded=true] span{opacity:0}}
@media(max-width:760px){.w{width:min(1200px,100% - 2.4rem)}.menu:not(.open){display:none}.nav{height:64px}.brand b{font-size:1rem}
.form{grid-template-columns:1fr}.mapw{min-height:320px}
.dock{display:grid;grid-template-columns:1fr 1fr;position:fixed;left:0;right:0;bottom:0;z-index:40;background:var(--dbg,var(--bg));border-top:1px solid var(--line);box-shadow:0 -8px 30px rgba(0,0,0,.08)}
.dock a{display:flex;gap:.55rem;align-items:center;justify-content:center;min-height:58px;font:700 .74rem/1 var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--fg)}.dock a+a{background:var(--acc);color:var(--onacc)}.dock svg{width:18px;height:18px}}
'''
JS = r'''<script>(function(){var d=document,R=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var els=d.querySelectorAll('[data-rv]');if('IntersectionObserver' in window&&!R){d.documentElement.classList.add('rv-on');
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('rvd');io.unobserve(e.target)}})},{rootMargin:'0px 0px -6% 0px',threshold:.05});
els.forEach(function(e){io.observe(e)})}
var px=[].slice.call(d.querySelectorAll('[data-px]'));if(!R&&px.length){var tk=0,vh=innerHeight;
function u(){px.forEach(function(el){var r=el.parentElement.getBoundingClientRect();if(r.bottom<-50||r.top>vh+50)return;var k=parseFloat(el.getAttribute('data-px'));
el.style.transform='translate3d(0,'+((r.top+r.height/2-vh/2)*-k).toFixed(1)+'px,0)'});tk=0}
addEventListener('scroll',function(){if(!tk){tk=1;requestAnimationFrame(u)}},{passive:true});addEventListener('resize',function(){vh=innerHeight;u()});u()}
})();</script>'''
def ribbon(): return f'<div class="rb">{K.RIBBON}</div>'
def header(brand, links, cta=('Rendez-vous', '#rdv'), cls=''):
    a = ''.join(f'<a href="{h}">{t}</a>' for t, h in links)
    return (f'<a class="skip" href="#main">Aller au contenu</a><header class="hdr {cls}" data-header>{ribbon()}<div class="w nav"><a class="brand" href="#top">{brand}</a>'
            f'<nav class="menu" data-nav aria-label="Navigation">{a}<a class="cta" href="{cta[1]}">{cta[0]}</a></nav>'
            f'<button class="burger" type="button" data-menu aria-expanded="false" aria-label="Menu"><span></span></button></div></header>')
def hours(F): return '<table class="tb">' + ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else "à confirmer"}</td></tr>' for n, d, v, k in K.hours(F)) + '</table>' + f'<p class="note">{K.HOURS_NOTE if (F.get("wed") or F.get("thu")) else "Horaires non affichés sur la fiche Google le " + K.CONSULTED + " : à confirmer avec l’établissement."}</p>'
def hours_short(F): return K.hours_short(F)
def contacts(F, wa_label='WhatsApp · demande de rendez-vous', wa_msg='Bonjour, je souhaite prendre rendez-vous.', extra=()):
    li = [f'<li>{I["phone"]}<div><small>Téléphone</small><a href="{telhref(F["tel"])}">{F["tel"]}</a></div></li>']
    for lab, t in F.get('tels', []): li.append(f'<li>{I["phone"]}<div><small>{esc(lab)}</small><a href="{telhref(t)}">{t}</a></div></li>')
    li.append(f'<li>{I["wa"]}<div><small>{wa_label}</small><a href="{K.walink(F["wa"], wa_msg)}" target="_blank" rel="noopener">{F["tel"]}</a></div></li>')
    if F.get('email'): li.append(f'<li>{I["mail"]}<div><small>E-mail</small><a href="mailto:{F["email"]}">{F["email"]}</a></div></li>')
    li.append(f'<li>{I["pin"]}<div><small>Adresse</small><span class="v">{F["addr"]}</span></div></li>')
    for lab, v in extra: li.append(f'<li>{I["globe"]}<div><small>{esc(lab)}</small><span class="v">{v}</span></div></li>')
    return '<ul class="ci">' + ''.join(li) + '</ul>'
def form(F, intro, spec, btn='Envoyer la demande', note=None): return K.form(F, intro, spec, btn, note=note)
MED_FORM, FORM_NOTE = K.MED_FORM, K.FORM_NOTE
def mapblock(F, cls=''):
    return f'<div class="mapw {cls}"><div class="mapfb" aria-hidden="true">{IC["pin"]}{esc(F["city"])} · carte Google</div>{K.mapframe(F)}</div>'
def compliance(F):
    k = F['kind']
    if k == 'para': return ("Site d'information du cabinet : identité, coordonnées, horaires et accès uniquement, dans le respect des règles déontologiques de la profession. "
                            "Aucun avis de patient, aucun témoignage, aucune publicité, aucun tarif. Aucun conseil de santé n'est donné par ce site ni par WhatsApp.")
    if k == 'lab': return ("Site d'information du laboratoire : coordonnées, horaires et accès uniquement. Aucun avis, aucun témoignage, aucune publicité, aucun tarif. "
                           "Aucun résultat d'analyse n'est transmis par ce site ni par WhatsApp.")
    return K.compliance(F)
def footer(F, M, brand, links, extra=''):
    a = ''.join(f'<a href="{h}">{t}</a>' for t, h in links)
    c = compliance(F)
    return (f'<footer class="ft"><div class="w"><div class="top"><a class="brand" href="#top">{brand}</a><nav aria-label="Pied de page">{a}</nav></div>{M.credits(extra)}'
            f'<p class="legal">{c + " " if c else ""}Site de démonstration non officiel réalisé à partir d\'informations publiques ; contenus à valider par l\'établissement. '
            f'© <span data-year>2026</span> {esc(F["name"])} · Démo réalisée par <a href="https://github.com/islemyakoubi" target="_blank" rel="noopener">Synaris Labs</a>, Menzel Temime.</p></div></footer>')
def dock(F, label='Rendez-vous', href='#rdv', icon='cal'):
    return f'<nav class="dock" aria-label="Contact rapide"><a href="{telhref(F["tel"])}">{I["phone"]}Appeler</a><a href="{href}">{I[icon]}{label}</a></nav>'
def page(F, title, desc, fonts, css, body, theme, fav):
    return K.page(F, title, desc, fonts, CSS + css, body + JS, theme, fav)
def fav(bg, fg, txt, font='Georgia', shape='circle'):
    s = f"<circle cx='32' cy='32' r='30' fill='{bg}'/>" if shape == 'circle' else f"<rect width='64' height='64' rx='14' fill='{bg}'/>"
    return f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'>{s}<text x='32' y='41' font-size='24' text-anchor='middle' fill='{fg}' font-family='{font}'>{txt}</text></svg>"
