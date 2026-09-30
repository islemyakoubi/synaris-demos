# Dr Ghada Bassoumi, médecin dentiste (Hammamet) : rail de navigation vertical fixe à gauche (desktop), contenu en colonnes éditoriales, hero photo médina avec grand titre en Spectral italique.
# Lexend + Spectral ; sauge / anthracite / blanc cassé.
import gen_lot2 as K
FONTS = 'family=Lexend:wght@300;400;600&family=Spectral:ital,wght@0,400;1,300;1,400'
CSS = '''
:root{--sage:#8FA98F;--sd:#4d6b52;--char:#2B2D2F;--off:#F5F4EF;--mut:#6c706c;--line:#dcdcd2}
body{background:var(--off);color:var(--char);font:300 1rem/1.7 Lexend,system-ui,sans-serif}h1,h2,h3{font-family:Spectral,serif;font-weight:400;line-height:1.05;margin:0 0 .6rem}
.ph{font:400 .7rem/1 Lexend;color:var(--sd);background:#e4ebe2;border-radius:3px;padding:.2rem .45rem;white-space:nowrap}
.rb{background:var(--char);color:#c9ccc6;font-size:.74rem;text-align:center;padding:.4rem 1rem;position:relative;z-index:5}.rb b{color:#fff}
.rail{background:var(--char);color:#fff;display:flex;justify-content:space-between;align-items:center;padding:.8rem 1.2rem;position:sticky;top:0;z-index:4}
.rail .lg{font:italic 400 1.25rem Spectral;text-decoration:none}.rail nav{display:none}.rail .bt{padding:.6rem .9rem}
.bt{display:inline-flex;gap:.5rem;align-items:center;background:var(--sage);color:var(--char);text-decoration:none;font-weight:600;padding:.8rem 1.15rem;border-radius:4px}.bt svg{width:18px}.bt.d{background:var(--char);color:#fff}
.main{min-width:0}.hero{position:relative;min-height:78vh;display:grid;align-items:end}.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero:after{content:'';position:absolute;inset:0;background:linear-gradient(0deg,rgba(43,45,47,.85),rgba(43,45,47,.1) 60%)}.hero .in{position:relative;z-index:1;color:#fff;padding:2rem 1.4rem 3rem;max-width:900px}
.hero .k{font-size:.78rem;letter-spacing:.24em;text-transform:uppercase;color:#cfe0cf}.hero h1{font-size:clamp(3rem,8vw,6.5rem);font-style:italic;font-weight:300}.hero p{max-width:30rem;color:#e3e6e0}
.acts{display:flex;gap:.6rem;flex-wrap:wrap;margin-top:1.2rem}.pad{padding:4rem 1.4rem;max-width:1080px}.sec{border-bottom:1px solid var(--line)}
.num{font:italic 300 4rem/1 Spectral;color:var(--sage)}.cols{display:grid;gap:2rem}.sec h2{font-size:clamp(2.2rem,5vw,3.4rem)}
.kv{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--line)}.kv div{padding:.9rem 0;border-bottom:1px solid var(--line)}.kv div:nth-child(odd){padding-right:1rem}.kv small{display:block;font-size:.72rem;color:var(--mut);letter-spacing:.12em;text-transform:uppercase}
.tb{width:100%;border-collapse:collapse}.tb td{padding:.7rem 0;border-bottom:1px solid var(--line)}.tb td:first-child{font:italic 1.15rem Spectral}.tb td+td{text-align:right}.tb .today td{color:var(--sd);font-weight:600}
.side{border-radius:4px;overflow:hidden}.side img{width:100%;aspect-ratio:3/4;object-fit:cover}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}.form label{display:grid;gap:.3rem;font-weight:400;font-size:.84rem}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;border:0;border-bottom:1.5px solid var(--char);border-radius:0;padding:.7rem 0;min-height:46px;width:100%;background:transparent}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--char);color:#fff;border:0;border-radius:4px;padding:1rem;font:600 1rem Lexend;cursor:pointer;margin-top:.6rem}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.76rem;color:var(--mut);margin:0}.map{height:380px;border-radius:4px;overflow:hidden}.note{font-size:.8rem;color:var(--mut)}.ft{padding:2rem 1.4rem 3rem;font-size:.82rem;color:var(--mut);max-width:1080px}
@media(min-width:1000px){.wrap{display:grid;grid-template-columns:230px 1fr}.rail{position:sticky;top:0;height:100vh;flex-direction:column;align-items:flex-start;justify-content:space-between;padding:2rem 1.6rem}
.rail nav{display:grid;gap:1rem;font-size:.9rem}.rail nav a{text-decoration:none;color:#c9ccc6;display:flex;gap:.7rem;align-items:baseline}.rail nav a span{font:italic 1rem Spectral;color:var(--sage)}.rail nav a:hover{color:#fff}
.rail .lg{font-size:1.6rem;line-height:1.1}.hero .in{padding:3rem 3.5rem 4rem}.pad{padding:5.5rem 3.5rem}.cols{grid-template-columns:120px 1fr 1fr}.ft{padding:2rem 3.5rem 3rem}}
'''
def build(F, M):
    hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else K.ph()}</td></tr>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet.')
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div><div class="wrap">
<aside class="rail"><a class="lg" href="#top">Dr Ghada<br>Bassoumi</a><nav aria-label="Navigation"><a href="#cabinet"><span>01</span>Le cabinet</a><a href="#horaires"><span>02</span>Horaires</a><a href="#rdv"><span>03</span>Rendez-vous</a><a href="#acces"><span>04</span>Accès</a></nav><a class="bt" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></aside>
<div class="main"><main id="main"><section class="hero" id="top">{M.img('hero', 'Ruelle de la médina de Hammamet (photo d’illustration)', sizes='(max-width: 1000px) 100vw, 80vw', lazy=False)}<div class="in"><p class="k">Cabinet dentaire · Hammamet</p><h1>Dr Ghada Bassoumi</h1><p>Médecin dentiste à Hammamet. Consultations sur rendez-vous.</p>
<div class="acts"><a class="bt" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}Rendez-vous WhatsApp</a></div></div></section>
<section class="sec" id="cabinet"><div class="pad cols"><p class="num">01</p><div><h2>Le cabinet</h2><p>Informations d'identification du cabinet. Les éléments marqués « à confirmer » seront complétés par le cabinet.</p></div>
<div class="kv"><div><small>Praticienne</small>Dr Ghada Bassoumi</div><div><small>Qualification</small>{F['sector']}</div><div><small>Adresse</small>{F['addr']}</div><div><small>Téléphone</small><a href="{K.telhref(F['tel'])}">{F['tel']}</a></div><div><small>N° d'Ordre</small>{K.ph()}</div><div><small>Langues</small>{K.ph()}</div><div><small>CNAM</small>{K.ph()}</div><div><small>Accès PMR</small>{K.ph()}</div></div></div></section>
<section class="sec" id="horaires"><div class="pad cols"><p class="num">02</p><div><h2>Horaires</h2><p class="note">{K.HOURS_NOTE}</p><div class="side">{M.img('sonde', 'Sonde dentaire (photo d’illustration)', sizes='(max-width: 1000px) 100vw, 30vw')}</div></div><table class="tb">{hrs}</table></div></section>
<section class="sec" id="rdv"><div class="pad cols"><p class="num">03</p><div><h2>Rendez-vous</h2><p>Remplissez ces quelques champs : WhatsApp s'ouvre avec votre demande. Vous pouvez aussi appeler le {F['tel']}. Pensez à votre carte CNAM et à vos radios récentes.</p></div>
{K.form(F, 'Bonjour, je souhaite prendre rendez-vous au cabinet du Dr Ghada Bassoumi :', K.MED_FORM, 'Envoyer sur WhatsApp')}</div></section>
<section class="sec" id="acces"><div class="pad cols"><p class="num">04</p><div><h2>Accès</h2><p>{F['addr']}</p><a class="bt d" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire</a></div><div class="map">{K.mapframe(F)}</div></div></section></main>
<footer class="ft">{M.credits()}{K.footer_legal(F)}</footer></div></div>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' fill='#2B2D2F'/><text x='32' y='44' font-size='32' text-anchor='middle' fill='#8FA98F' font-family='Georgia' font-style='italic'>GB</text></svg>"
    return K.page(F, 'Dr Ghada Bassoumi — Médecin dentiste à Hammamet (démo)', 'Cabinet dentaire du Dr Ghada Bassoumi à Hammamet : informations, horaires, accès et demande de rendez-vous par WhatsApp.', FONTS, CSS, body, '#2B2D2F', fav)
