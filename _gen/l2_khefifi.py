# Dr Souha Khefifi, interniste gériatre (Grombalia) : conception « accessibilité d'abord » pour patients âgés et aidants. Très grand texte, boutons A−/A+, gros boutons d'appel, contraste AAA, oliveraie du Cap Bon.
# Atkinson Hyperlegible + Literata ; crème / sarcelle profonde / or.
import gen_lot2 as K
FONTS = 'family=Atkinson+Hyperlegible:wght@400;700&family=Literata:opsz,wght@7..72,500;7..72,700'
CSS = '''
:root{--cr:#FFFBF2;--tl:#134E4A;--gd:#B8860B;--ink:#10201f;--mut:#3f504e;--line:#d9d2bf}
html{font-size:19px}body{background:var(--cr);color:var(--ink);font:400 1rem/1.7 'Atkinson Hyperlegible',system-ui,sans-serif}h1,h2,h3{font-family:Literata,serif;font-weight:700;line-height:1.1;margin:0 0 .6rem}
.w{width:min(1080px,100% - 2rem);margin-inline:auto}.ph{font:700 .72rem/1 'Atkinson Hyperlegible';color:#fff;background:var(--tl);border-radius:4px;padding:.25rem .5rem;white-space:nowrap}
.rb{background:var(--ink);color:#e0e0d8;font-size:.72rem;text-align:center;padding:.4rem 1rem}.rb b{color:#fff}
.tools{background:#fff;border-bottom:2px solid var(--line)}.tools .w{display:flex;justify-content:space-between;align-items:center;gap:1rem;padding:.6rem 0;flex-wrap:wrap}.tools b{font-family:Literata;font-size:1.1rem}
.fs{display:flex;gap:.4rem;align-items:center;font-size:.85rem}.fs button{font:700 1rem 'Atkinson Hyperlegible';min-width:52px;min-height:48px;border:2px solid var(--tl);background:#fff;color:var(--tl);border-radius:10px;cursor:pointer}.fs button:focus-visible{outline:4px solid var(--gd)}
.hero{display:grid;gap:2rem;padding:2.5rem 0}.hero h1{font-size:clamp(2.3rem,6vw,3.6rem);color:var(--tl)}.hero .sp{font-size:1.25rem;font-weight:700;margin:0 0 1rem}.hero p{font-size:1.1rem}
.pic{border-radius:18px;overflow:hidden;border:3px solid var(--tl)}.pic img{width:100%;aspect-ratio:4/3;object-fit:cover}.pic figcaption{background:var(--tl);color:#fff;font-size:.8rem;padding:.4rem .8rem}.pic figure{margin:0}
.call{display:grid;gap:.8rem;margin:1.4rem 0}.call a{display:flex;gap:.9rem;align-items:center;justify-content:center;min-height:72px;border-radius:16px;font-size:1.25rem;font-weight:700;text-decoration:none;background:var(--tl);color:#fff}
.call a.wa{background:#fff;color:var(--tl);border:3px solid var(--tl)}.call svg{width:30px;height:30px}.call small{display:block;font-size:.8rem;font-weight:400}
.sec{padding:3rem 0;border-top:3px solid var(--line)}.sec h2{font-size:clamp(1.9rem,4.5vw,2.6rem);color:var(--tl)}
.steps{list-style:none;padding:0;margin:0;display:grid;gap:1rem;counter-reset:s}.steps li{counter-increment:s;background:#fff;border:2px solid var(--line);border-radius:16px;padding:1.1rem 1.1rem 1.1rem 4.2rem;position:relative;font-size:1.05rem}
.steps li:before{content:counter(s);position:absolute;left:1rem;top:1rem;width:2.4rem;height:2.4rem;border-radius:50%;background:var(--gd);color:#fff;font:700 1.2rem Literata;display:grid;place-items:center}
.tb{width:100%;border-collapse:collapse;font-size:1.1rem}.tb td{padding:.8rem .4rem;border-bottom:2px solid var(--line)}.tb td+td{text-align:right}.tb .today{background:#fff4d6}.tb .today td{font-weight:700}
.id{display:grid;gap:.6rem}.id div{background:#fff;border-left:6px solid var(--tl);padding:.8rem 1rem;border-radius:0 12px 12px 0}.id small{display:block;font-size:.8rem;color:var(--mut)}.id span{font-size:1.1rem;font-weight:700}
.form{display:grid;grid-template-columns:1fr;gap:.9rem}.form label{display:grid;gap:.35rem;font-weight:700;font-size:1rem}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;font-size:1.05rem;border:2px solid var(--tl);border-radius:12px;padding:.8rem;min-height:56px;width:100%;background:#fff}
.form button{display:flex;gap:.6rem;justify-content:center;align-items:center;background:var(--tl);color:#fff;border:0;border-radius:14px;padding:1.1rem;font:700 1.15rem 'Atkinson Hyperlegible';cursor:pointer;min-height:64px}.form button svg{width:26px}
.fnote{font-size:.85rem;color:var(--mut);margin:0}.map{height:380px;border-radius:16px;overflow:hidden;border:3px solid var(--tl)}.note{font-size:.9rem;color:var(--mut)}
.duo{display:grid;gap:2rem}.sm{border-radius:14px;overflow:hidden;max-width:420px}.sm img{width:100%;aspect-ratio:4/3;object-fit:cover}.ft{padding:2rem 0 3rem;font-size:.85rem;color:var(--mut)}
@media(min-width:880px){.hero{grid-template-columns:1.1fr .9fr;align-items:center}.duo{grid-template-columns:1fr 1fr;align-items:start}.form{grid-template-columns:1fr 1fr}.form button,.fnote{grid-column:1/-1}}
'''
def build(F, M):
    hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else "à confirmer"}</td></tr>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour Docteur, je souhaite prendre rendez-vous en consultation.')
    t2 = [t.strip() for t in F['tel2'].split('·')]
    others = ' · '.join(f'<a href="{K.telhref(t)}">{t}</a>' for t in t2)
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<div class="tools"><div class="w"><b>Dr Souha Khefifi</b><div class="fs" role="group" aria-label="Taille du texte">Taille du texte<button type="button" data-fs="-2" aria-label="Réduire le texte">A−</button><button type="button" data-fs="2" aria-label="Agrandir le texte">A+</button></div></div></div>
<main id="main" class="w"><section class="hero"><div><h1>Dr Souha Khefifi</h1><p class="sp">Médecine interne et gériatrie, à Grombalia</p><p>Consultations sur rendez-vous. Pour les patients comme pour les proches qui les accompagnent : tout est écrit en grand ici.</p>
<div class="call"><a href="{K.telhref(F['tel'])}">{K.I['phone']}<span>Appeler le cabinet<small>{F['tel']}</small></span></a><a class="wa" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}<span>Écrire sur WhatsApp<small>Demande de rendez-vous</small></span></a></div></div>
<figure class="pic">{M.img('hero', 'Oliveraie du Cap Bon (photo d’illustration)', sizes='(max-width: 880px) 100vw, 480px', lazy=False)}<figcaption>Oliveraie du Cap Bon · photo d'illustration</figcaption></figure></section>
<section class="sec"><div class="duo"><div><h2>Le cabinet</h2><div class="id"><div><small>Médecin</small><span>Dr Souha Khefifi</span></div><div><small>Spécialité</small><span>{F['sector']}</span></div><div><small>Adresse</small><span>{F['addr']}</span></div>
<div><small>Téléphones</small><span><a href="{K.telhref(F['tel'])}">{F['tel']}</a> · {others}</span></div><div><small>N° d'Ordre · Langues · CNAM</small><span>{K.ph()} · {K.ph()} · {K.ph()}</span></div></div></div>
<div><h2>Horaires</h2><table class="tb">{hrs}</table><p class="note">{K.HOURS_NOTE}</p><div class="sm">{M.img('tension', 'Tensiomètre (photo d’illustration)', sizes='(max-width: 880px) 100vw, 420px')}</div></div></div></section>
<section class="sec"><h2>Préparer la consultation</h2><ol class="steps"><li>Prenez rendez-vous par téléphone ou par WhatsApp.</li><li>Apportez la carte CNAM ou d'assurance et une pièce d'identité.</li><li>Apportez la liste ou les boîtes des médicaments pris actuellement, et les analyses ou comptes rendus récents.</li><li>Un proche peut vous accompagner.</li></ol><p class="note">En cas d'urgence vitale, appelez le 190 (SAMU).</p></section>
<section class="sec" id="rdv"><div class="duo"><div><h2>Demander un rendez-vous</h2><p>Remplissez les cases, puis appuyez sur le bouton : WhatsApp s'ouvre avec votre message déjà écrit. Le cabinet vous répond pour fixer l'heure.</p><div class="sm">{M.img('stetho', 'Stéthoscope (photo d’illustration)', sizes='(max-width: 880px) 100vw, 420px')}</div></div>
{K.form(F, 'Bonjour, je souhaite un rendez-vous chez le Dr Souha Khefifi :', K.MED_FORM, 'Envoyer sur WhatsApp')}</div></section>
<section class="sec" id="acces"><h2>Venir au cabinet</h2><p>{F['addr']}</p><div class="map">{K.mapframe(F)}</div><div class="call" style="max-width:480px"><a href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}<span>Ouvrir l'itinéraire</span></a></div></section></main>
<footer class="ft w">{M.credits()}{K.footer_legal(F)}</footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='12' fill='#134E4A'/><text x='32' y='44' font-size='30' text-anchor='middle' fill='#FFFBF2' font-family='Georgia' font-weight='700'>SK</text></svg>"
    return K.page(F, 'Dr Souha Khefifi — Médecin interniste et gériatre à Grombalia (démo)', 'Cabinet du Dr Souha Khefifi, médecine interne et gériatrie à Grombalia : informations, horaires, accès et demande de rendez-vous.', FONTS, CSS, body, '#134E4A', fav)
