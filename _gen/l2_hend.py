# Dr Hend Ben Mustapha, médecin dentiste (Soliman) : interface « application » à onglets (Cabinet / Horaires / Rendez-vous / Accès) dans un grand panneau.
# Sora + Nunito Sans ; lavande / violet / nuit. Pastilles d'actions rapides, tout sur un écran.
import gen_lot2 as K
FONTS = 'family=Sora:wght@400;600;700&family=Nunito+Sans:wght@400;600;700'
CSS = '''
:root{--lav:#EFEBFF;--vio:#5B3FD1;--night:#1E1646;--mut:#6b6690;--line:#e3ddfb}
body{background:var(--lav);color:var(--night);font:400 1rem/1.6 'Nunito Sans',system-ui,sans-serif;background-image:radial-gradient(circle at 85% 10%,#d9d0ff 0,transparent 35%),radial-gradient(circle at 5% 90%,#e3dcff 0,transparent 30%)}
h1,h2,h3{font-family:Sora,sans-serif;line-height:1.05;margin:0 0 .6rem;letter-spacing:-.02em}.w{width:min(1180px,100% - 2rem);margin-inline:auto}
.ph{font:700 .7rem/1 'Nunito Sans';color:var(--vio);background:#e6e0ff;border-radius:99px;padding:.22rem .55rem;white-space:nowrap}
.rb{background:var(--night);color:#c9c2ee;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:#fff}
.app{display:grid;gap:1.6rem;padding:2rem 0 3rem;align-items:start}.intro h1{font-size:clamp(2.4rem,5.5vw,4rem)}.intro h1 span{color:var(--vio)}
.intro .k{display:inline-flex;gap:.5rem;align-items:center;background:#fff;border-radius:99px;padding:.35rem .8rem;font-weight:700;font-size:.82rem;margin-bottom:1rem}.intro .k svg{width:18px;color:var(--vio)}
.intro p{color:var(--mut);font-size:1.08rem}.quick{display:grid;grid-template-columns:repeat(3,1fr);gap:.6rem;margin:1.4rem 0}
.quick a{background:#fff;border-radius:18px;padding:.9rem .6rem;text-align:center;text-decoration:none;font-weight:700;font-size:.85rem;box-shadow:0 10px 24px -18px rgba(30,22,70,.5)}
.quick svg{width:24px;height:24px;color:var(--vio);display:block;margin:0 auto .35rem}.shot{border-radius:26px;overflow:hidden;aspect-ratio:16/10}.shot img{width:100%;height:100%;object-fit:cover}
.panel{background:#fff;border-radius:30px;box-shadow:0 40px 80px -40px rgba(30,22,70,.45);overflow:hidden}
.tabs{display:grid;grid-template-columns:repeat(4,1fr);background:var(--night);padding:.45rem;gap:.3rem}
.tabs button{font:600 .82rem Sora;border:0;background:transparent;color:#c9c2ee;border-radius:18px;padding:.8rem .3rem;cursor:pointer}.tabs button[aria-selected=true]{background:#fff;color:var(--night)}
.pn{padding:1.6rem}.pn h2{font-size:1.7rem}.li{list-style:none;padding:0;margin:0}.li li{display:flex;justify-content:space-between;gap:1rem;padding:.8rem 0;border-bottom:1px solid var(--line)}.li li span:first-child{color:var(--mut)}
.days{display:grid;grid-template-columns:repeat(7,1fr);gap:.35rem;margin:1rem 0}.days div{background:var(--lav);border-radius:14px;padding:.6rem .2rem;text-align:center;font:600 .74rem Sora}.days div.today{background:var(--vio);color:#fff}
.days small{display:block;font:400 .62rem 'Nunito Sans';margin-top:.2rem;opacity:.8}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.7rem}.form label{display:grid;gap:.25rem;font-weight:700;font-size:.8rem}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;border:0;background:var(--lav);border-radius:14px;padding:.75rem;min-height:46px;width:100%}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--vio);color:#fff;border:0;border-radius:16px;padding:1rem;font:600 1rem Sora;cursor:pointer}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.76rem;color:var(--mut);margin:0}.map{height:300px;border-radius:20px;overflow:hidden}.note{font-size:.78rem;color:var(--mut)}
.bt{display:inline-flex;gap:.5rem;align-items:center;background:var(--night);color:#fff;text-decoration:none;font-weight:700;padding:.8rem 1.1rem;border-radius:14px;margin-top:.8rem}.bt svg{width:18px}
.ft{padding:1rem 0 3rem;font-size:.8rem;color:var(--mut)}
@media(min-width:940px){.app{grid-template-columns:.9fr 1.1fr;padding:4rem 0;gap:3.5rem}.pn{padding:2.2rem;min-height:520px}}
'''
def build(F, M):
    ab = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim']
    days = ''.join(f'<div data-d="{n}">{ab[n - 1]}<small>{v if k else "à conf."}</small></div>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet.')
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<main id="main" class="w app"><section class="intro"><span class="k">{K.I['tooth']}Cabinet dentaire · Soliman</span><h1>Dr Hend <span>Ben Mustapha</span></h1><p>Médecin dentiste à Soliman. Toutes les informations du cabinet, et la demande de rendez-vous, sur un seul écran.</p>
<div class="quick"><a href="{K.telhref(F['tel'])}">{K.I['phone']}Appeler</a><a href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a><a href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire</a></div>
<div class="shot">{M.img('hero', 'Fauteuil dentaire (photo d’illustration, ne montre pas le cabinet)', sizes='(max-width: 940px) 100vw, 45vw', lazy=False)}</div></section>
<section class="panel" data-tabs><div class="tabs" role="tablist"><button type="button" role="tab" data-tab="c" aria-selected="true">Cabinet</button><button type="button" role="tab" data-tab="h" aria-selected="false">Horaires</button><button type="button" role="tab" data-tab="r" aria-selected="false">Rendez-vous</button><button type="button" role="tab" data-tab="a" aria-selected="false">Accès</button></div>
<div class="pn" data-panel="c"><h2>Le cabinet</h2><ul class="li"><li><span>Praticienne</span><span>Dr Hend Ben Mustapha</span></li><li><span>Qualification</span><span>{F['sector']}</span></li><li><span>Ville</span><span>Soliman</span></li><li><span>Adresse</span><span>{K.ph()}</span></li>
<li><span>Téléphone</span><span><a href="{K.telhref(F['tel'])}">{F['tel']}</a></span></li><li><span>N° d'Ordre</span><span>{K.ph()}</span></li><li><span>Langues</span><span>{K.ph()}</span></li><li><span>CNAM / assurances</span><span>{K.ph()}</span></li></ul></div>
<div class="pn" data-panel="h" hidden><h2>Horaires</h2><div class="days">{days}</div><p class="note">Horaires de consultation à confirmer avec le cabinet (la fiche Google indique « ouvert 24h/24 », à vérifier).</p><p>Pour une urgence dentaire, appelez d'abord le cabinet au <b>{F['tel']}</b>.</p></div>
<div class="pn" data-panel="r" hidden><h2>Demander un rendez-vous</h2>{K.form(F, 'Bonjour, je souhaite prendre rendez-vous au cabinet du Dr Hend Ben Mustapha :', K.MED_FORM, 'Envoyer sur WhatsApp')}</div>
<div class="pn" data-panel="a" hidden><h2>Accès</h2><p>{F['addr']}</p><div class="map">{K.mapframe(F)}</div><a class="bt" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Ouvrir dans Google Maps</a></div></section></main>
<footer class="ft w">{M.credits()}{K.footer_legal(F)}</footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='18' fill='#5B3FD1'/><text x='32' y='42' font-size='24' text-anchor='middle' fill='#fff' font-family='Arial' font-weight='700'>HB</text></svg>"
    return K.page(F, 'Dr Hend Ben Mustapha — Médecin dentiste à Soliman (démo)', 'Cabinet dentaire du Dr Hend Ben Mustapha à Soliman : informations, horaires, accès et demande de rendez-vous par WhatsApp.', FONTS, CSS, body, '#5B3FD1', fav)
