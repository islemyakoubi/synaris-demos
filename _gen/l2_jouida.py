# Maître Aymen Jouida, avocat (Hammamet) : v3 « boutique internationale ». Anthracite presque noir, champagne doré, ivoire.
# Hero plein écran cinématographique (arcades de Dar Sébastien, parallaxe douce), grandes lignes typographiques, cartes de domaines à icônes fines,
# approche en 4 étapes, formulaire ivoire sur fond sombre, carte en mode nuit. Cormorant Garamond + Manrope. Informatif uniquement (Ordre des avocats).
import os, io
import gen_lot2 as K
SLUG = 'avocat-aymen-jouida-hammamet'
FONTS = 'family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=Manrope:wght@300;400;500;600;700'
CSS = '''
:root{--ink:#0B0B0D;--coal:#121215;--coal2:#18181C;--gold:#C9A96A;--gold2:#E6D3A6;--ivory:#F3EDE2;--ivory2:#E9E1D2;--mut:#A7A197;--mut2:#6E6960;--line:rgba(201,169,106,.24);--line2:rgba(243,237,226,.10);
--serif:'Cormorant Garamond',Georgia,serif;--sans:Manrope,system-ui,sans-serif;--ease:cubic-bezier(.2,.7,.2,1)}
html{background:var(--ink)}body{background:var(--ink);color:var(--ivory);font:300 1rem/1.75 var(--sans);-webkit-font-smoothing:antialiased;letter-spacing:.005em}
::selection{background:var(--gold);color:var(--ink)}a{text-decoration:none}
h1,h2,h3{font-family:var(--serif);font-weight:300;line-height:1.02;margin:0;letter-spacing:-.01em}em{font-style:italic;color:var(--gold2);font-weight:300}
.w{width:min(1240px,100% - 3rem);margin-inline:auto}
.ph{display:inline-block;font:500 .66rem/1 var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--gold);border:1px solid var(--line);padding:.32rem .6rem;border-radius:99px;white-space:nowrap;vertical-align:middle}
.lbl{display:flex;align-items:center;gap:.9rem;font:500 .7rem/1 var(--sans);letter-spacing:.32em;text-transform:uppercase;color:var(--gold);margin:0 0 1.6rem}.lbl:before{content:'';width:42px;height:1px;background:var(--gold)}
/* en-tête fixe */
.hdr{position:fixed;inset:0 0 auto;z-index:50;isolation:isolate;transition:border-color .5s;border-bottom:1px solid transparent}
.hdr:before{content:'';position:absolute;inset:0;z-index:-1;background:rgba(11,11,13,.82);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);opacity:0;transition:opacity .5s var(--ease)}.hdr.scrolled:before{opacity:1}.hdr.scrolled{border-color:var(--line2)}
.rb{background:rgba(0,0,0,.55);color:#b9b3a8;font:400 .7rem/1.4 var(--sans);text-align:center;padding:.38rem 1rem;letter-spacing:.02em}.rb b{color:var(--gold2);font-weight:600}
.nav{display:flex;align-items:center;justify-content:space-between;height:78px;transition:height .5s var(--ease)}.hdr.scrolled .nav{height:64px}
.brand{display:flex;align-items:center;gap:.9rem;color:var(--ivory)}.mono{display:grid;place-items:center;width:44px;height:44px;border:1px solid var(--gold);border-radius:50%;font:italic 400 1.15rem/1 var(--serif);color:var(--gold2);letter-spacing:.02em}
.brand b{display:block;font:400 1.28rem/1.05 var(--serif);letter-spacing:.02em}.brand small{display:block;font:500 .6rem/1.6 var(--sans);letter-spacing:.3em;text-transform:uppercase;color:var(--mut)}
.menu{display:flex;align-items:center;gap:2.2rem}.menu a{font:500 .74rem/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:#d8d2c6;position:relative;padding:.4rem 0}
.menu a:after{content:'';position:absolute;left:0;right:100%;bottom:0;height:1px;background:var(--gold);transition:right .4s var(--ease)}.menu a:hover:after{right:0}
.menu a.cta{border:1px solid var(--gold);color:var(--gold2);padding:.8rem 1.2rem}.menu a.cta:after{display:none}.menu a.cta:hover{background:var(--gold);color:var(--ink)}
.burger{display:none;width:46px;height:46px;border:1px solid var(--line);background:transparent;border-radius:50%;cursor:pointer;position:relative}.burger span,.burger:before,.burger:after{content:'';position:absolute;left:14px;right:14px;height:1px;background:var(--ivory);transition:transform .3s}
.burger:before{top:18px}.burger span{top:22.5px}.burger:after{top:27px}
/* hero */
.hero{position:relative;min-height:100vh;min-height:100svh;display:flex;flex-direction:column;justify-content:flex-end;overflow:hidden;isolation:isolate}
.pxw{position:absolute;inset:0;overflow:hidden;z-index:-2}.px{position:absolute;left:0;top:-20%;width:100%;height:140%;object-fit:cover;will-change:transform}
.hero .px{object-position:50% 40%;filter:saturate(.75) contrast(1.05) brightness(.9)}
.shade{position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(11,11,13,.94) 0%,rgba(11,11,13,.78) 34%,rgba(11,11,13,.25) 70%,rgba(11,11,13,.45) 100%),linear-gradient(0deg,rgba(11,11,13,1) 0%,rgba(11,11,13,0) 38%),linear-gradient(180deg,rgba(11,11,13,.7) 0%,rgba(11,11,13,0) 22%)}
.hin{padding:11rem 0 3.2rem}.eyebrow{display:flex;align-items:center;gap:1rem;font:500 .74rem/1 var(--sans);letter-spacing:.36em;text-transform:uppercase;color:var(--gold);margin:0 0 2rem}.eyebrow:before{content:'';width:64px;height:1px;background:var(--gold)}
.hero h1{font-size:clamp(3.6rem,9.2vw,9.4rem);line-height:.9;font-weight:300;letter-spacing:-.025em}.hero h1 span{display:block}.hero h1 em{font-weight:300}
.lede{max-width:34rem;font-size:1.08rem;color:#d4cec3;margin:2rem 0 0}
.acts{display:flex;flex-wrap:wrap;gap:1rem;margin-top:2.6rem}
.btn{display:inline-flex;align-items:center;gap:.8rem;font:600 .76rem/1 var(--sans);letter-spacing:.18em;text-transform:uppercase;padding:1.15rem 1.6rem;border:1px solid var(--gold);transition:background .35s var(--ease),color .35s,gap .35s}
.btn svg{width:17px;height:17px;flex:none}.btn.g{background:var(--gold);color:var(--ink)}.btn.g:hover{background:var(--gold2);gap:1.1rem}.btn.o{color:var(--ivory);border-color:rgba(243,237,226,.35)}.btn.o:hover{border-color:var(--gold);color:var(--gold2)}
.arrow{width:26px!important;height:10px!important}
.hbar{display:grid;grid-template-columns:repeat(3,1fr) auto;border-top:1px solid var(--line2);margin-bottom:0}.hbar>div{padding:1.5rem 1.5rem 1.8rem 0;border-right:1px solid var(--line2);margin-right:1.5rem}.hbar>div:nth-child(3){border-right:0}
.hbar small{display:block;font:500 .62rem/1 var(--sans);letter-spacing:.3em;text-transform:uppercase;color:var(--mut);margin-bottom:.7rem}.hbar p{margin:0;font:400 1.3rem/1.2 var(--serif);color:var(--ivory)}.hbar p a:hover{color:var(--gold2)}
.cue{display:flex;align-items:center;gap:.8rem;font:500 .62rem/1 var(--sans);letter-spacing:.3em;text-transform:uppercase;color:var(--mut);align-self:center}.cue i{display:block;width:1px;height:46px;background:linear-gradient(var(--gold),transparent);animation:cue 2.4s var(--ease) infinite}
@keyframes cue{0%{transform:scaleY(0);transform-origin:top}50%{transform:scaleY(1);transform-origin:top}51%{transform-origin:bottom}100%{transform:scaleY(0);transform-origin:bottom}}
.hero .rise{animation:rise 1.4s var(--ease) both}.hero .rise:nth-child(2){animation-delay:.12s}.hero .rise:nth-child(3){animation-delay:.24s}.hero .rise:nth-child(4){animation-delay:.36s}
@keyframes rise{from{opacity:0;transform:translateY(34px)}to{opacity:1;transform:none}}
/* révélations */
.rv-on [data-rv]{opacity:0;transform:translateY(34px);transition:opacity 1.1s var(--ease),transform 1.1s var(--ease);transition-delay:var(--d,0s)}.rv-on [data-rv].in{opacity:1;transform:none}
/* principes (ivoire) */
.ivory{background:var(--ivory);color:#1b1a18}.ivory .lbl{color:#8a6d35}.ivory .lbl:before{background:#8a6d35}.ivory em{color:#8a6d35}
.state{padding:9rem 0 8rem}.state h2{font-size:clamp(2.4rem,5.2vw,5rem);line-height:1.04;max-width:21ch}
.prin{display:grid;grid-template-columns:repeat(3,1fr);gap:0;margin-top:5rem;border-top:1px solid rgba(27,26,24,.16)}.prin div{padding:2rem 2rem 0 0;border-right:1px solid rgba(27,26,24,.12);margin-right:2rem}.prin div:last-child{border-right:0;margin-right:0}
.prin b{display:block;font:500 .7rem/1 var(--sans);letter-spacing:.26em;text-transform:uppercase;color:#8a6d35;margin-bottom:1rem}.prin h3{font-size:1.9rem;font-weight:400;margin-bottom:.6rem}.prin p{margin:0;color:#4d4a44;font-size:.95rem}
/* sections sombres */
.sec{padding:8.5rem 0}.sec#approche{padding-bottom:6.5rem}.coal{background:var(--coal)}.sec h2{font-size:clamp(2.6rem,5vw,4.6rem)}
.cab{display:grid;grid-template-columns:5fr 6fr;gap:6rem;align-items:center}
.frame{position:relative;margin:0}.fx{position:relative}.fx:before{content:'';position:absolute;inset:1.4rem -1.4rem -1.4rem 1.4rem;border:1px solid var(--gold);z-index:0;pointer-events:none}
.frame .in{position:relative;overflow:hidden;z-index:1;aspect-ratio:4/5}.frame img{width:100%;height:100%;object-fit:cover;transition:transform 1.6s var(--ease);filter:saturate(.7) contrast(1.05)}.frame:hover img{transform:scale(1.04)}
.frame figcaption{position:relative;z-index:1;font:400 .7rem/1.4 var(--sans);letter-spacing:.08em;color:var(--mut);margin-top:2.4rem}
.cab p.intro{font-size:1.1rem;color:#d4cec3;max-width:36rem;margin:2rem 0 2.6rem}
.dl{margin:0;border-top:1px solid var(--line2)}.dl div{display:grid;grid-template-columns:13rem 1fr;gap:1.5rem;padding:1.05rem 0;border-bottom:1px solid var(--line2);align-items:baseline}
.dl dt{font:500 .66rem/1.5 var(--sans);letter-spacing:.24em;text-transform:uppercase;color:var(--mut)}.dl dd{margin:0;font:400 1.22rem/1.35 var(--serif);color:var(--ivory)}.dl dd a:hover{color:var(--gold2)}
/* domaines */
.dhead{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:end;margin-bottom:4.5rem}.dhead>p{margin:0;color:var(--mut);max-width:30rem;justify-self:end}
.cards{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line2);border-left:1px solid var(--line2)}
.card{position:relative;padding:2.8rem 2.4rem 2.6rem;border-right:1px solid var(--line2);border-bottom:1px solid var(--line2);transition:background .5s var(--ease)}
.card:before{content:'';position:absolute;left:0;top:-1px;height:1px;width:0;background:var(--gold);transition:width .7s var(--ease)}.card:hover{background:var(--coal2)}.card:hover:before{width:100%}
.card .n{position:absolute;right:2rem;top:2.2rem;font:italic 300 1.1rem/1 var(--serif);color:var(--mut2)}
.card svg{width:44px;height:44px;color:var(--gold);margin-bottom:2rem}.card h3{font-size:1.85rem;font-weight:400;margin-bottom:.8rem}.card p{margin:0 0 1.4rem;color:var(--mut);font-size:.95rem}
/* bande parallaxe */
.band{position:relative;height:78vh;min-height:520px;overflow:hidden;display:grid;place-items:center;text-align:center;isolation:isolate}
.band .px{filter:saturate(.6) brightness(.72)}.band .shade{background:radial-gradient(ellipse at center,rgba(11,11,13,.35),rgba(11,11,13,.85)),linear-gradient(180deg,var(--ink),transparent 18%,transparent 82%,var(--coal))}
.band h2{font-size:clamp(3rem,8vw,7.6rem);line-height:.95}.band p{font:500 .74rem/1 var(--sans);letter-spacing:.34em;text-transform:uppercase;color:var(--gold2);margin:2rem 0 0}
.band figcaption{position:absolute;right:1.5rem;bottom:1.2rem;font-size:.66rem;color:rgba(243,237,226,.55);letter-spacing:.06em}
/* approche */
.appr{display:grid;grid-template-columns:5fr 7fr;gap:6rem;align-items:start}.stick{position:sticky;top:7rem}
.stick .in{aspect-ratio:3/4}.stick p.s{margin:2.2rem 0 0;color:var(--mut);max-width:26rem}
.steps{list-style:none;margin:3.5rem 0 0;padding:0;counter-reset:s}.steps li{counter-increment:s;display:grid;grid-template-columns:7rem 1fr;gap:1.5rem;padding:2.4rem 0;border-top:1px solid var(--line2)}.steps li:last-child{border-bottom:1px solid var(--line2)}
.steps li:before{content:'0' counter(s);font:300 4.2rem/.9 var(--serif);color:transparent;-webkit-text-stroke:1px var(--gold)}
.steps h3{font-size:1.9rem;font-weight:400;margin-bottom:.6rem}.steps p{margin:0;color:var(--mut)}
/* rendez-vous */
.rdv{display:grid;grid-template-columns:5fr 6fr;gap:5rem;align-items:start}
.ci{list-style:none;padding:0;margin:2.6rem 0 0}.ci li{display:flex;gap:1.1rem;align-items:center;padding:1.1rem 0;border-bottom:1px solid var(--line2)}.ci li:first-child{border-top:1px solid var(--line2)}
.ci svg{width:20px;height:20px;color:var(--gold);flex:none}.ci small{display:block;font:500 .6rem/1.4 var(--sans);letter-spacing:.26em;text-transform:uppercase;color:var(--mut)}.ci a,.ci span.v{font:400 1.25rem/1.3 var(--serif);color:var(--ivory)}.ci a:hover{color:var(--gold2)}
.hrs{margin-top:2.8rem}.hrs h3{font:500 .66rem/1 var(--sans);letter-spacing:.3em;text-transform:uppercase;color:var(--gold);margin-bottom:1rem}
.tb{width:100%;border-collapse:collapse;font-size:.92rem}.tb td{padding:.62rem 0;border-bottom:1px solid var(--line2);color:#cfc9be}.tb td+td{text-align:right}.tb .today td{color:var(--gold2);font-weight:600}.tb .today td:first-child:after{content:' · aujourd’hui';font-weight:400;color:var(--mut)}
.note{font-size:.78rem;color:var(--mut);margin:.9rem 0 0}
.fcard{background:var(--ivory);color:#1b1a18;padding:3.2rem;position:relative}.fcard:before{content:'';position:absolute;inset:.7rem;border:1px solid rgba(138,109,53,.35);pointer-events:none}
.fcard h3{font-size:2.3rem;font-weight:400;margin-bottom:.4rem}.fcard>p{color:#5a564f;margin:0 0 2rem;font-size:.95rem}
.form{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem 1.8rem;position:relative}.form .full{grid-column:1/-1}
.form label{display:grid;gap:.45rem}.form label span{font:600 .62rem/1 var(--sans);letter-spacing:.24em;text-transform:uppercase;color:#6d5626}
.form input,.form select,.form textarea{font:400 1.02rem var(--sans);color:#1b1a18;background:transparent;border:0;border-bottom:1px solid rgba(27,26,24,.3);border-radius:0;padding:.55rem 0 .7rem;min-height:46px;width:100%;transition:border-color .3s;-webkit-appearance:none;appearance:none}
.form select{background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' fill='none' stroke='%238a6d35' stroke-width='1.2'/%3E%3C/svg%3E") no-repeat right .2rem center/12px}
.form input:focus,.form select:focus,.form textarea:focus{outline:0;border-bottom-color:#8a6d35;border-bottom-width:2px}
.form button{grid-column:1/-1;display:flex;gap:.8rem;justify-content:center;align-items:center;background:var(--ink);color:var(--gold2);border:0;padding:1.25rem;font:600 .78rem/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;cursor:pointer;margin-top:.6rem;transition:background .35s}
.form button:hover{background:#26231e}.form button svg{width:18px;height:18px}.fnote{grid-column:1/-1;font-size:.76rem;color:#6a655c;margin:0;line-height:1.6}
/* accès */
.acc{display:grid;grid-template-columns:7fr 5fr;min-height:560px;border-top:1px solid var(--line2);border-bottom:1px solid var(--line2)}
.acc .mapw{position:relative;background:#141417 linear-gradient(rgba(201,169,106,.07) 1px,transparent 1px) 0 0/48px 48px,#141417 linear-gradient(90deg,rgba(201,169,106,.07) 1px,transparent 1px) 0 0/48px 48px}.mapfb{position:absolute;inset:0;display:grid;place-content:center;justify-items:center;gap:.9rem;color:var(--mut);font:500 .64rem/1 var(--sans);letter-spacing:.3em;text-transform:uppercase}.mapfb i{display:grid;place-items:center;width:96px;height:96px;border:1px solid var(--line);border-radius:50%;box-shadow:0 0 0 22px rgba(201,169,106,.03),0 0 0 44px rgba(201,169,106,.02)}.mapfb svg{width:30px;height:30px;color:var(--gold)}.map{position:absolute;inset:0;width:100%;height:100%;filter:grayscale(1) invert(.92) contrast(.88) brightness(.95) sepia(.18)}
.acc .side{position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:flex-start;padding:4.2rem 3.2rem;isolation:isolate}.acc .side img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;filter:saturate(.9) brightness(1.2)}
.acc .side:after{content:'';position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(11,11,13,.92) 0%,rgba(11,11,13,.7) 45%,rgba(11,11,13,.05) 100%)}
.acc h2{font-size:clamp(2.4rem,4vw,3.6rem);margin-bottom:1.2rem}.acc address{font:400 1.3rem/1.4 var(--serif);font-style:normal;color:var(--ivory);margin-bottom:2rem}.acc .acts{margin-top:0}.acc small.cr{position:absolute;bottom:1rem;right:1.2rem;text-shadow:0 1px 6px #000;font-size:.64rem;color:rgba(243,237,226,.6)}
/* déontologie */
.deo{padding:7rem 0;text-align:center}.deo .mono{margin:0 auto 2rem;width:64px;height:64px;font-size:1.6rem}.deo h2{font-size:clamp(2rem,3.4vw,2.8rem);margin-bottom:1.4rem}
.deo p{max-width:46rem;margin:0 auto .9rem;color:var(--mut);font-size:.94rem}.deo .rule{width:1px;height:70px;background:linear-gradient(transparent,var(--gold));margin:0 auto 2.2rem}
/* pied */
.ft{background:#070708;border-top:1px solid var(--line2);padding:4.5rem 0 7rem;font-size:.8rem;color:var(--mut2)}.ft .top{display:flex;justify-content:space-between;align-items:center;gap:2rem;flex-wrap:wrap;padding-bottom:2.5rem;border-bottom:1px solid var(--line2);margin-bottom:2rem}
.ft nav{display:flex;gap:1.8rem;flex-wrap:wrap}.ft nav a{font:500 .68rem/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--mut)}.ft nav a:hover{color:var(--gold2)}
.ft .credits{margin-bottom:1rem}.ft .credits summary{color:var(--mut)}.ft .credits a,.ft .legal a{color:var(--mut);text-decoration:underline;text-underline-offset:3px}.ft .legal{margin:0;line-height:1.7}
/* barre mobile */
.dock{display:none}
@media(max-width:1080px){.menu a:not(.cta){display:none}.burger{display:block;margin-left:1rem}.nav .menu{margin-left:auto}.menu.open{display:flex;position:fixed;inset:0;z-index:60;background:var(--ink);flex-direction:column;justify-content:center;align-items:flex-start;gap:1.6rem;padding:0 2rem}.menu.open a,.menu.open a:not(.cta){display:block;font:300 2.4rem/1.1 var(--serif);letter-spacing:0;text-transform:none;color:var(--ivory)}.menu.open a.cta{border:0;padding:0;color:var(--gold2)}.burger[aria-expanded=true]{position:fixed;right:1.2rem;top:3.2rem;z-index:61}.burger[aria-expanded=true]:before{transform:translateY(4.5px) rotate(45deg)}.burger[aria-expanded=true]:after{transform:translateY(-4.5px) rotate(-45deg)}.burger[aria-expanded=true] span{opacity:0}.cab,.appr,.rdv{gap:3.5rem}.cards{grid-template-columns:1fr 1fr}.dl div{grid-template-columns:10rem 1fr}}
@media(max-width:860px){
.w{width:min(1240px,100% - 2.4rem)}.menu:not(.open){display:none}
.nav{height:66px}.brand b{font-size:1.12rem}.mono{width:40px;height:40px}
.hin{padding:9rem 0 2.2rem}.hero h1{font-size:clamp(3.4rem,15vw,5.6rem)}.eyebrow{letter-spacing:.28em;font-size:.66rem;margin-bottom:1.5rem}.eyebrow:before{width:36px}.lede{font-size:1rem;margin-top:1.5rem}
.acts{gap:.7rem;margin-top:2rem}.acts .btn{flex:1 1 100%;justify-content:center}
.hbar{grid-template-columns:1fr 1fr}.hbar>div{padding:1.1rem .8rem 1.2rem 0;margin-right:.8rem}.hbar>div:nth-child(2){border-right:0;margin-right:0}.hbar>div:nth-child(3){grid-column:1/-1;border-top:1px solid var(--line2)}.hbar p{font-size:1.1rem}.cue{display:none}
.shade{background:linear-gradient(0deg,rgba(11,11,13,1) 12%,rgba(11,11,13,.72) 55%,rgba(11,11,13,.5) 100%)}
.sec{padding:5.5rem 0}.state{padding:5.5rem 0}.prin{grid-template-columns:1fr;margin-top:3rem}.prin div{border-right:0;margin-right:0;padding:1.6rem 0;border-bottom:1px solid rgba(27,26,24,.12)}
.cab,.appr,.rdv{grid-template-columns:1fr}.frame{margin-right:1.4rem}.stick{position:static}.stick .in{aspect-ratio:16/10}
.dhead{grid-template-columns:1fr;gap:1.4rem;margin-bottom:2.5rem}.dhead>p{justify-self:start}.cards{grid-template-columns:1fr}.card{padding:2.2rem 1.6rem}
.dl div{grid-template-columns:1fr;gap:.3rem}.steps li{grid-template-columns:4.6rem 1fr;gap:1rem;padding:1.8rem 0}.steps li:before{font-size:3rem}
.band{height:62vh;min-height:420px}.band>div[data-rv]{padding:0 1.4rem}.band h2{font-size:clamp(2.4rem,11vw,3.4rem)}.band p{letter-spacing:.26em}.appr .stick{order:2}.fcard{padding:2.2rem 1.5rem}.form{grid-template-columns:1fr}
.acc{grid-template-columns:1fr}.acc .mapw{height:360px}.acc .side{padding:2.4rem 1.4rem;min-height:420px}
.dock{display:grid;grid-template-columns:1fr 1fr;position:fixed;left:0;right:0;bottom:0;z-index:40;background:rgba(11,11,13,.94);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-top:1px solid var(--line)}
.dock a{display:flex;gap:.6rem;align-items:center;justify-content:center;min-height:58px;font:600 .72rem/1 var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--ivory)}.dock a+a{background:var(--gold);color:var(--ink)}.dock svg{width:18px;height:18px}
.ft{padding-bottom:6rem}}
'''
ICO = dict(
 civil='<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 22 24 9l16 13"/><path d="M12 19v20h24V19"/><circle cx="20" cy="27" r="3"/><circle cx="29" cy="28" r="2.2"/><path d="M15 39c0-4 2.4-6.6 5-6.6s5 2.6 5 6.6M26 39c0-3 1.4-5 3-5s3 2 3 5"/></svg>',
 aff='<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="7" y="15" width="34" height="24" rx="1.5"/><path d="M18 15v-4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v4M7 25h34M22 25v3h4v-3"/></svg>',
 immo='<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 40h36M10 40V18l14-9 14 9v22"/><path d="M19 40V28h10v12M16 21h3M29 21h3"/><path d="M24 14.5v2"/></svg>',
 trav='<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="8" width="30" height="34" rx="1.5"/><path d="M19 8v4h10V8"/><circle cx="24" cy="22" r="4"/><path d="M16 34c1.2-4 4.2-6 8-6s6.8 2 8 6"/></svg>',
 penal='<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M24 7v34M16 41h16M10 13h28M24 10.5a2 2 0 1 0 0-4"/><path d="M10 13 5 25a5.5 5.5 0 0 0 10 0L10 13zM38 13l-5 12a5.5 5.5 0 0 0 10 0L38 13z"/></svg>',
 cont='<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 18 24 9l16 9H8z"/><path d="M11 18v17M19 18v17M29 18v17M37 18v17M6 35h36M5 40h38"/></svg>',
 arrow='<svg class="arrow" viewBox="0 0 26 10" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><path d="M0 5h24M20 1l4 4-4 4"/></svg>',
)
DOM = [('civil', 'Droit civil et de la famille', 'Contrats, successions, régimes matrimoniaux et questions patrimoniales.'),
       ('aff', 'Droit des affaires', 'Sociétés, contrats commerciaux et relations entre associés.'),
       ('immo', 'Droit immobilier', 'Ventes, baux, copropriété et litiges fonciers.'),
       ('trav', 'Droit du travail', 'Relations entre employeurs et salariés, contrats et différends.'),
       ('penal', 'Droit pénal', 'Assistance et défense aux différentes étapes de la procédure.'),
       ('cont', 'Contentieux et exécution', 'Représentation devant les juridictions et procédures d’exécution.')]
STEPS = [('Prise de contact', 'Par téléphone ou WhatsApp, uniquement pour fixer un rendez-vous. Aucun conseil n’est donné par message.'),
         ('Rendez-vous au cabinet', 'Vous exposez votre situation de vive voix, avec les documents utiles. Les échanges sont couverts par le secret professionnel.'),
         ('Cadre de l’intervention', 'L’avocat vous présente la démarche envisageable ainsi que les modalités d’honoraires, convenues avec vous.'),
         ('Suivi du dossier', 'Les échanges se poursuivent au cabinet ou par les moyens convenus ensemble, à chaque étape.')]
JS2 = r'''<script>(function(){var d=document,R=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var els=d.querySelectorAll('[data-rv]');if('IntersectionObserver' in window&&!R){d.documentElement.classList.add('rv-on');
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -6% 0px',threshold:.06});
els.forEach(function(e){io.observe(e)})}
var px=[].slice.call(d.querySelectorAll('[data-px]'));if(!R&&px.length){var tk=0,vh=innerHeight;
function u(){px.forEach(function(el){var r=el.parentElement.getBoundingClientRect();if(r.bottom<-50||r.top>vh+50)return;var k=parseFloat(el.getAttribute('data-px'));
el.style.transform='translate3d(0,'+((r.top+r.height/2-vh/2)*-k).toFixed(1)+'px,0)'});tk=0}
addEventListener('scroll',function(){if(!tk){tk=1;requestAnimationFrame(u)}},{passive:true});addEventListener('resize',function(){vh=innerHeight;u()});u()}
})();</script>'''
def hero_xl(M):
    """Variante 1920 px du hero (source Commons), pour un plein écran net."""
    from PIL import Image
    p = os.path.join(K.ROOT, SLUG, 'media', 'hero-1920.webp')
    if not os.path.exists(p):
        url = dict(M.cr)['hero']['url'].replace('/1280px-', '/1920px-')
        im = Image.open(io.BytesIO(K.get(url))).convert('RGB'); im.thumbnail((1920, 1920)); im.save(p, 'WEBP', quality=70, method=6)
    with Image.open(p) as im: return im.size
def build(F, M):
    xw, xh = hero_xl(M); w, h = M.dims['hero']
    tel1, tel2 = F['tel'], F['tel2']
    wa = K.walink(F['wa'], 'Bonjour Maître, je souhaite prendre rendez-vous à votre cabinet.')
    hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else "à confirmer"}</td></tr>' for n, d, v, k in K.hours(F))
    cards = ''.join(f'<article class="card" data-rv style="--d:{i % 3 * .1:.1f}s"><span class="n">{"I II III IV V VI".split()[i]}</span>{ICO[k]}<h3>{t}</h3><p>{p}</p>{K.ph()}</article>' for i, (k, t, p) in enumerate(DOM))
    steps = ''.join(f'<li data-rv><div><h3>{t}</h3><p>{p}</p></div></li>' for t, p in STEPS)
    hero = (f'<img class="px" data-px=".22" src="media/hero-640.webp" srcset="media/hero-640.webp 640w, media/hero.webp {w}w, media/hero-1920.webp {xw}w" sizes="100vw" '
            f'width="{xw}" height="{xh}" alt="Arcades de Dar Sébastien à Hammamet (photo d’illustration, ne montre pas le cabinet)" fetchpriority="high">')
    spec = [('text', 'Nom et prénom'), ('tel', 'Téléphone'), ('date', 'Jour souhaité'), ('select', 'Moment', ['Matin', 'Après-midi', 'Peu importe']),
            ('select', 'Être recontacté par', ['Appel téléphonique', 'WhatsApp'])]
    note = ("Démo : aucune donnée n'est enregistrée. Ce formulaire sert uniquement à demander un rendez-vous : n'y décrivez pas votre affaire. "
            "Aucune consultation n'est donnée par message.")
    body = f'''<a class="skip" href="#main">Aller au contenu</a>
<header class="hdr" data-header><div class="rb">{K.RIBBON}</div><div class="w nav"><a class="brand" href="#top" aria-label="Maître Aymen Jouida, accueil"><span class="mono">AJ</span><span><b>Aymen Jouida</b><small>Avocat · Hammamet</small></span></a>
<nav class="menu" data-nav aria-label="Navigation"><a href="#cabinet">Le cabinet</a><a href="#domaines">Domaines</a><a href="#approche">Approche</a><a href="#acces">Accès</a><a class="cta" href="#rdv">Rendez-vous</a></nav>
<button class="burger" type="button" data-menu aria-expanded="false" aria-label="Menu"><span></span></button></div></header>
<main id="main"><section class="hero" id="top"><div class="pxw">{hero}</div><div class="shade"></div>
<div class="w hin"><p class="eyebrow rise">Avocat · Hammamet · Cap Bon</p><h1 class="rise"><span>Maître</span><span>Aymen <em>Jouida</em></span></h1>
<p class="lede rise">Bureau d'avocat à Hammamet. Les clients sont reçus sur rendez-vous, dans le respect du secret professionnel et des règles de la profession.</p>
<div class="acts rise"><a class="btn g" href="#rdv">Demander un rendez-vous {ICO['arrow']}</a><a class="btn o" href="{K.telhref(tel1)}">{K.I['phone']}{tel1}</a></div></div>
<div class="w hbar"><div><small>Téléphone</small><p><a href="{K.telhref(tel1)}">{tel1}</a></p></div><div><small>Horaire relevé</small><p>Mercredi, {F['wed']}</p></div><div><small>Bureau</small><p>Hammamet {K.ph('adresse à confirmer')}</p></div><span class="cue"><i></i>Défiler</span></div></section>
<section class="ivory state"><div class="w"><p class="lbl" data-rv>Principes</p><h2 data-rv>Écoute, <em>confidentialité</em> et indépendance : les règles qui encadrent le métier d'avocat.</h2>
<div class="prin"><div data-rv><b>I</b><h3>Secret professionnel</h3><p>Ce qui est confié à l'avocat reste couvert par le secret professionnel.</p></div>
<div data-rv style="--d:.1s"><b>II</b><h3>Indépendance</h3><p>L'avocat exerce en toute indépendance, dans le cadre de la déontologie de l'Ordre.</p></div>
<div data-rv style="--d:.2s"><b>III</b><h3>Sur rendez-vous</h3><p>Chaque dossier s'examine au cabinet, lors d'un entretien fixé à l'avance.</p></div></div></div></section>
<section class="sec coal" id="cabinet"><div class="w cab"><figure class="frame" data-rv><div class="fx"><div class="in">{M.img('porte', 'Porte sculptée de Dar Sébastien, Hammamet (photo d’illustration)', sizes='(max-width: 860px) 92vw, 520px')}</div></div><figcaption>Hammamet · photo d'illustration, ne montre pas le cabinet</figcaption></figure>
<div><p class="lbl" data-rv>01 · Le cabinet</p><h2 data-rv>Un bureau d'avocat, <em>à Hammamet</em>.</h2><p class="intro" data-rv>Maître Aymen Jouida reçoit sur rendez-vous à son bureau de Hammamet. Les informations ci-dessous proviennent de sources publiques et restent à compléter par le cabinet.</p>
<dl class="dl" data-rv><div><dt>Avocat</dt><dd>Maître Aymen Jouida</dd></div><div><dt>Barreau · inscription</dt><dd>{K.ph()}</dd></div><div><dt>Parcours · diplômes</dt><dd>{K.ph()}</dd></div>
<div><dt>Langues de travail</dt><dd>{K.ph()}</dd></div><div><dt>Adresse</dt><dd>{F['addr']}</dd></div><div><dt>Téléphones</dt><dd><a href="{K.telhref(tel1)}">{tel1}</a> · <a href="{K.telhref(tel2)}">{tel2}</a></dd></div></dl></div></div></section>
<section class="sec" id="domaines"><div class="w"><div class="dhead"><div><p class="lbl" data-rv>02 · Domaines</p><h2 data-rv>Domaines <em>d'intervention</em></h2></div><p data-rv>Liste indicative, à confirmer par le cabinet avant toute publication : seuls les domaines effectivement traités par Maître Jouida seront conservés.</p></div>
<div class="cards">{cards}</div></div></section>
<figure class="band" style="margin:0"><div class="pxw">{M.img('arcade', 'Patio à arcades de Dar Sébastien, Hammamet (photo d’illustration)', cls='px', sizes='100vw', extra=' data-px=".16"')}</div><div class="shade"></div>
<div data-rv><h2>Hammamet, <em>Cap Bon</em>.</h2><p>Reçu sur rendez-vous</p></div><figcaption>Dar Sébastien, Hammamet · photo d'illustration</figcaption></figure>
<section class="sec coal" id="approche"><div class="w appr"><div class="stick"><figure class="frame" data-rv><div class="fx"><div class="in">{M.img('justice', 'Statuette de la Justice tenant une balance (photo d’illustration)', sizes='(max-width: 860px) 92vw, 480px')}</div></div></figure>
<p class="s" data-rv>Un premier rendez-vous se prépare simplement : pièce d'identité et documents en lien avec votre situation.</p></div>
<div><p class="lbl" data-rv>03 · Approche</p><h2 data-rv>Le déroulement d'un <em>premier rendez-vous</em></h2><ol class="steps">{steps}</ol></div></div></section>
<section class="sec" id="rdv"><div class="w rdv"><div><p class="lbl" data-rv>04 · Rendez-vous</p><h2 data-rv>Prendre <em>rendez-vous</em></h2>
<ul class="ci" data-rv><li>{K.I['phone']}<div><small>Téléphone</small><a href="{K.telhref(tel1)}">{tel1}</a></div></li><li>{K.I['phone']}<div><small>Second numéro</small><a href="{K.telhref(tel2)}">{tel2}</a></div></li>
<li>{K.I['wa']}<div><small>WhatsApp · demande de rendez-vous</small><a href="{wa}" target="_blank" rel="noopener">{tel1}</a></div></li></ul>
<div class="hrs" data-rv><h3>Horaires du bureau</h3><table class="tb">{hrs}</table><p class="note">{K.HOURS_NOTE}</p></div></div>
<div class="fcard" data-rv><h3>Demande de rendez-vous</h3><p>Le bouton ouvre WhatsApp avec votre demande ; le cabinet vous recontacte pour fixer l'heure.</p>
{K.form(F, 'Bonjour Maître, je souhaite prendre rendez-vous à votre cabinet :', spec, 'Envoyer la demande', note=note)}</div></div></section>
<section class="acc" id="acces"><div class="mapw"><div class="mapfb" aria-hidden="true"><i>{K.I['pin']}</i>Hammamet · carte Google</div>{K.mapframe(F)}</div><div class="side">{M.img('nuit', 'La médina de Hammamet la nuit (photo d’illustration)', sizes='(max-width: 860px) 100vw, 42vw')}<small class="cr">Médina de Hammamet · photo d'illustration</small>
<p class="lbl" data-rv>05 · Accès</p><h2 data-rv>Venir <em>au cabinet</em></h2><address data-rv>{F['addr']}</address>
<div class="acts" data-rv><a class="btn g" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire</a><a class="btn o" href="{K.telhref(tel1)}">{K.I['phone']}Appeler</a></div></div></section>
<section class="deo coal"><div class="w"><div class="rule"></div><span class="mono">AJ</span><h2 data-rv>Déontologie <em>et mentions</em></h2>
<p data-rv>{K.compliance(F)}</p><p data-rv>Ce site ne comporte ni témoignage, ni référence de clients, ni résultat, ni tarif. Informations publiques relevées le {K.CONSULTED} ; éléments marqués « à confirmer » à valider par le cabinet.</p></div></section></main>
<footer class="ft"><div class="w"><div class="top"><a class="brand" href="#top"><span class="mono">AJ</span><span><b>Aymen Jouida</b><small>Avocat · Hammamet</small></span></a>
<nav aria-label="Pied de page"><a href="#cabinet">Le cabinet</a><a href="#domaines">Domaines</a><a href="#approche">Approche</a><a href="#rdv">Rendez-vous</a><a href="#acces">Accès</a></nav></div>
{M.credits()}<p class="legal">Site de démonstration non officiel réalisé à partir d'informations publiques ; contenus à valider par l'établissement. © <span data-year>2026</span> {F['name']} · Démo réalisée par <a href="https://github.com/islemyakoubi" target="_blank" rel="noopener">Synaris Labs</a>, Menzel Temime.</p></div></footer>
<nav class="dock" aria-label="Contact rapide"><a href="{K.telhref(tel1)}">{K.I['phone']}Appeler</a><a href="#rdv">{K.I['cal']}Rendez-vous</a></nav>
{JS2}'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' fill='#0B0B0D'/><circle cx='32' cy='32' r='25' fill='none' stroke='#C9A96A' stroke-width='1.5'/><text x='32' y='40' font-size='22' text-anchor='middle' fill='#E6D3A6' font-family='Georgia' font-style='italic'>AJ</text></svg>"
    return K.page(F, 'Maître Aymen Jouida — Avocat à Hammamet (démo)', 'Cabinet de Maître Aymen Jouida, avocat à Hammamet : le cabinet, domaines d’intervention à confirmer, déroulement d’un rendez-vous, horaires, accès et demande de rendez-vous.', FONTS, CSS, body, '#0B0B0D', fav)
