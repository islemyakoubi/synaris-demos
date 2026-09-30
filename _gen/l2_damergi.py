# Dr Yasmine Damergi, médecin dentiste (Nabeul) : céramique de Nabeul. Frise de carreaux en CSS, frise chronologique verticale du parcours, horaires en carreaux.
# DM Serif Display + DM Sans ; vert émaillé / safran / crème / cobalt.
import gen_lot2 as K
FONTS = 'family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700'
CSS = '''
:root{--glaze:#2F6F5E;--saf:#E0A526;--cream:#FFF8EE;--cob:#23408E;--ink:#1f2b27;--mut:#62706b}
body{background:var(--cream);color:var(--ink);font:400 1rem/1.65 'DM Sans',system-ui,sans-serif}h1,h2,h3{font-family:'DM Serif Display',serif;font-weight:400;line-height:1.05;margin:0 0 .6rem}
.w{width:min(1140px,100% - 2.4rem);margin-inline:auto}.ph{font:500 .72rem/1 'DM Sans';color:var(--glaze);background:#e3efe9;border-radius:4px;padding:.18rem .45rem;white-space:nowrap}
.rb{background:var(--glaze);color:#d9ebe4;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:#fff}
.tiles{height:34px;background:conic-gradient(from 45deg,var(--cob) 0 25%,var(--cream) 0 50%,var(--saf) 0 75%,var(--cream) 0) 0 0/34px 34px}
.tiles.g{background:conic-gradient(from 45deg,var(--glaze) 0 25%,var(--cream) 0 50%,var(--saf) 0 75%,var(--cream) 0) 0 0/28px 28px;height:28px}
.hd .w{display:flex;justify-content:space-between;align-items:center;height:72px}.lg{text-decoration:none;font:1.35rem 'DM Serif Display';color:var(--glaze)}.nav{display:none;gap:1.5rem;font-weight:500}.nav a{text-decoration:none}
.bt{display:inline-flex;gap:.5rem;align-items:center;background:var(--glaze);color:#fff;text-decoration:none;font-weight:700;padding:.85rem 1.25rem;border-radius:10px}.bt svg{width:18px}.bt.s{background:var(--saf);color:var(--ink)}
.hero{display:grid;gap:2.4rem;padding:3rem 0 4rem;align-items:center}.hero h1{font-size:clamp(2.8rem,7vw,5rem)}.hero h1 i{color:var(--cob)}.hero p{color:var(--mut);font-size:1.1rem;max-width:32rem}
.frame{position:relative;padding:14px;background:conic-gradient(from 45deg,var(--cob) 0 25%,#fff 0 50%,var(--saf) 0 75%,#fff 0) 0 0/28px 28px;border-radius:24px}
.frame img{width:100%;aspect-ratio:1;object-fit:cover;border-radius:14px}.frame span{position:absolute;right:28px;bottom:28px;background:#fff;border-radius:8px;padding:.3rem .6rem;font-size:.75rem}
.acts{display:flex;gap:.7rem;flex-wrap:wrap;margin-top:1.4rem}.sec{padding:4.5rem 0}.ey{font-weight:700;font-size:.76rem;letter-spacing:.2em;text-transform:uppercase;color:var(--saf)}h2{font-size:clamp(2.2rem,5vw,3.4rem);color:var(--glaze)}
.tl{list-style:none;padding:0;margin:2rem 0 0;position:relative}.tl:before{content:'';position:absolute;left:11px;top:6px;bottom:6px;width:2px;background:repeating-linear-gradient(var(--glaze) 0 8px,transparent 8px 14px)}
.tl li{position:relative;padding:0 0 2rem 3rem}.tl li:before{content:'';position:absolute;left:0;top:4px;width:24px;height:24px;border-radius:6px;transform:rotate(45deg);background:var(--saf);border:4px solid var(--cream);box-shadow:0 0 0 2px var(--glaze)}
.tl b{display:block;font:1.5rem 'DM Serif Display';color:var(--cob)}.two{display:grid;gap:2.5rem}
.cal{display:grid;grid-template-columns:repeat(2,1fr);gap:.6rem}.cal div{background:#fff;border:2px solid #e6dcc8;border-radius:12px;padding:.9rem;text-align:center}
.cal div.today{border-color:var(--saf);background:#fff6df}.cal b{display:block;font:1.15rem 'DM Serif Display';color:var(--glaze)}.cal span{font-size:.85rem}
.info{background:#fff;border-radius:18px;padding:1.4rem;border:2px solid #e6dcc8}.info p{margin:.3rem 0}.info small{color:var(--mut);display:block;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;margin-top:.8rem}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.8rem;background:#fff;border-radius:18px;padding:1.5rem;border:2px solid #e6dcc8}.form label{display:grid;gap:.3rem;font-weight:700;font-size:.84rem}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;border:1.5px solid #e0d6c2;border-radius:10px;padding:.75rem;min-height:48px;width:100%;background:var(--cream)}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--glaze);color:#fff;border:0;border-radius:10px;padding:1rem;font:700 1rem 'DM Sans';cursor:pointer}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.78rem;color:var(--mut);margin:0}.map{height:360px;border-radius:18px;overflow:hidden;border:2px solid #e6dcc8}.note{font-size:.8rem;color:var(--mut)}
.jar{border-radius:18px;overflow:hidden;max-width:360px}.jar img{width:100%;aspect-ratio:3/4;object-fit:cover}
.ft{padding:2rem 0 3rem;font-size:.82rem;color:var(--mut)}
@media(min-width:840px){.nav{display:flex}.hero{grid-template-columns:1.1fr .9fr}.two{grid-template-columns:1fr 1fr;align-items:start}.cal{grid-template-columns:repeat(4,1fr)}}
'''
def build(F, M):
    cal = ''.join(f'<div data-d="{n}"><b>{d}</b><span>{v if k else K.ph()}</span></div>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet.')
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div><div class="tiles" aria-hidden="true"></div>
<header class="hd"><div class="w"><a class="lg" href="#top">Dr Yasmine Damergi</a><nav class="nav" aria-label="Navigation"><a href="#parcours">Parcours</a><a href="#horaires">Horaires</a><a href="#rdv">Rendez-vous</a></nav><a class="bt s" href="#rdv">Rendez-vous</a></div></header>
<main id="main"><section class="w hero" id="top"><div><p class="ey">Cabinet dentaire · Nabeul</p><h1>Dr Yasmine <i>Damergi</i></h1><p>Médecin dentiste à Nabeul, la ville de la céramique. Cabinet ouvert en janvier 2024, consultations sur rendez-vous.</p>
<div class="acts"><a class="bt" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a><a class="bt s" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div></div>
<div class="frame">{M.img('hero', 'Décor de carreaux de céramique tunisienne (photo d’illustration)', sizes='(max-width: 840px) 90vw, 45vw', lazy=False)}<span>Céramique tunisienne · illustration</span></div></section>
<div class="tiles g" aria-hidden="true"></div>
<section class="sec" id="parcours"><div class="w two"><div><p class="ey">Parcours</p><h2>Repères</h2><ul class="tl"><li><b>Décembre 2023</b>Diplôme de médecin dentiste.</li><li><b>Janvier 2024</b>Ouverture du cabinet à Nabeul.</li><li><b>Aujourd'hui</b>Consultations sur rendez-vous, par téléphone ou WhatsApp.</li></ul></div>
<div class="info"><h3 style="color:var(--glaze);font-size:1.6rem">Le cabinet</h3><small>Qualification</small><p>{F['sector']}</p><small>Adresse</small><p>{F['addr']}</p><small>Contact</small><p><a href="{K.telhref(F['tel'])}">{F['tel']}</a> · <a href="mailto:{F['email']}">{F['email']}</a></p>
<small>N° d'Ordre · Langues · CNAM</small><p>{K.ph()} · {K.ph()} · {K.ph()}</p></div></div></section>
<section class="sec" id="horaires" style="padding-top:0"><div class="w"><p class="ey">Horaires</p><h2>La semaine au cabinet</h2><div class="cal">{cal}</div><p class="note">{K.HOURS_NOTE}</p></div></section>
<section class="sec" id="rdv" style="background:#f4ecdc"><div class="w two"><div><p class="ey">Rendez-vous</p><h2>Écrire au cabinet</h2><p>Remplissez le formulaire : il ouvre WhatsApp avec votre demande pour le {F['tel']}. Le cabinet vous confirme l'heure.</p>
<div class="jar">{M.img('soin', 'Brosse à dents et dentifrice (photo d’illustration)', sizes='(max-width: 840px) 90vw, 360px')}</div></div>{K.form(F, 'Bonjour, je souhaite prendre rendez-vous au cabinet du Dr Yasmine Damergi :', K.MED_FORM, 'Envoyer sur WhatsApp')}</div></section>
<section class="sec"><div class="w two"><div class="map">{K.mapframe(F)}</div><div><p class="ey">Accès</p><h2>À Nabeul</h2><p>{F['addr']}</p><a class="bt" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire</a>
<div class="jar" style="margin-top:1.5rem;max-width:240px">{M.img('jarre', 'La jarre de Nabeul, sur le rond-point (photo d’illustration)', sizes='240px')}</div></div></div></section></main>
<div class="tiles" aria-hidden="true"></div><footer class="ft w">{M.credits()}{K.footer_legal(F)}</footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' fill='#2F6F5E'/><path d='M32 8 56 32 32 56 8 32z' fill='#E0A526'/><path d='M32 20 44 32 32 44 20 32z' fill='#23408E'/></svg>"
    return K.page(F, 'Dr Yasmine Damergi — Médecin dentiste à Nabeul (démo)', 'Cabinet dentaire du Dr Yasmine Damergi à Nabeul : parcours, horaires, accès et demande de rendez-vous par WhatsApp.', FONTS, CSS, body, '#2F6F5E', fav)
