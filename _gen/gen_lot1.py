# Lot 1 (Cap Bon, 20 prospects): restaurant / event-hall / invitation-studio builders.
# Same design system as gen_guest.py / gen_para.py (site.css, site.js, ribbon, badge, WhatsApp float, WhatsApp-prefill form).
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
from urllib.parse import quote
BASE = 'https://islemyakoubi.github.io/synaris-demos/'
def qr_svg(slug):
    """Inline SVG QR code pointing to the demo menu (segno, installed by the Action; local fallback: qr_lot1.json)."""
    try:
        import segno, io
        b = io.BytesIO()
        segno.make(f'{BASE}{slug}/#menu', error='m').save(b, kind='svg', xmldecl=False, svgns=True, scale=4, border=2, dark='#111', omitsize=True, svgclass='qr')
        return b.getvalue().decode().replace('<svg ', '<svg role="img" aria-label="QR code du menu" ', 1)
    except ImportError:
        return json.load(open(os.path.join(GEN, 'qr_lot1.json')))[slug]
CONSULTED = '30/09/2026'

def walink(wa, msg): return f'https://wa.me/{wa}?text=' + quote(msg)
def stars(score):
    pct = max(0, min(100, float(score) / 5 * 100))
    return f'<span class="stars" aria-label="{score} sur 5">★★★★★<i style="width:{pct:.0f}%">★★★★★</i></span>'
def ph(t='à confirmer'): return f'<span class="ph">{t}</span>'

def head(S, extra_css=''):
    th = S['theme']; fam, furl = FONTS[S['font']]
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(S['title'])}</title>
<meta name="description" content="{esc(S['desc'])}">
<meta name="robots" content="noindex,nofollow">
<meta name="theme-color" content="{th['accent']}">
<meta property="og:title" content="{esc(S['title'])}"><meta property="og:description" content="{esc(S['desc'])}"><meta property="og:image" content="img/hero.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{furl}" rel="stylesheet">
<link rel="stylesheet" href="site.css">
<style>:root{{--accent:{th['accent']};--accent-2:{th['accent2']};--accent-soft:{th['soft']};--bg:{th['bg']};--bg-alt:{th['bgalt']};--ink-strong:{th['ink']};--font-head:'{fam}',Georgia,serif;--font-body:'Inter',system-ui,sans-serif}}{extra_css}</style>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='{th['accent'].replace('#','%23')}'/%3E%3Ctext x='32' y='43' font-size='30' text-anchor='middle' fill='white' font-family='Georgia'%3E{S['mark']}%3C/text%3E%3C/svg%3E">
</head>
<body>
<div class="demo-ribbon"><b>Démo</b> — maquette non officielle réalisée par Synaris Labs à partir d'informations publiques, à valider par l'établissement.</div>
'''

def header(S, nav, cta_href, cta_label):
    links = ''.join(f'<li><a href="#{a}">{l}</a></li>' for a, l in nav)
    mlinks = ''.join(f'<a href="#{a}">{l}</a>' for a, l in nav)
    return f'''<header class="site-header">
 <div class="container nav">
  <a class="brand" href="#top"><span class="brand-mark">{S['mark']}</span><span>{esc(S['name'])}<small>{S['tagline']}</small></span></a>
  <ul class="nav-links">{links}</ul>
  <div class="nav-tools">
   <a class="btn btn-primary header-cta" href="{cta_href}">{cta_label}</a>
   <button class="menu-btn" type="button" aria-label="Menu" aria-expanded="false"><span></span></button>
  </div>
 </div>
 <nav class="mobile-menu container">{mlinks}</nav>
</header>
<main id="top">
'''

def ratings_section(S, sid='avis', eyebrow='Avis clients', h2='Ce que disent les clients en ligne'):
    cards = ''
    for r in S['ratings']:
        cards += f'''<div class="rating reveal"><div class="score">{r['score']}<small> / 5</small></div>{stars(r['score'])}<p><b>{r['count']}</b> avis · {r['label']}</p><a href="{esc(r['url'])}" target="_blank" rel="noopener">Source : {esc(r['src'])} →</a><p>Relevé le {r.get('date', CONSULTED)}</p></div>'''
    cards += f'''<div class="rating reveal" style="background:var(--accent-soft)"><h3 style="margin:0;font-size:1.1rem">Collecte d'avis Google</h3><p style="color:var(--ink)">{S.get('collect_txt', "Un QR « Laissez un avis » sur l'addition et un message WhatsApp de remerciement après la visite : plus d'avis récents, moins de mauvaises surprises.")}</p><span class="ph">module Synaris, démo</span></div>'''
    return f'''<section class="section" id="{sid}">
 <div class="container">
  <div class="center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lead">Notes publiques uniquement, avec leur source. Aucun avis n'a été inventé ni copié pour cette démo.</p></div>
  <div class="ratings">{cards}</div>
 </div>
</section>
'''

def gallery_section(S, sid='gallery', eyebrow='Galerie', h2=None, lead=None):
    gal = ''.join(f'<button type="button" data-full="img/{g}.jpg" aria-label="Agrandir"><img src="img/{g}.jpg" alt="{esc(a)}" loading="lazy" width="600" height="600"></button>' for g, a in (S['gallery'][:5] if 5 < len(S['gallery']) < 9 else S['gallery']))
    return f'''<section class="section alt" id="{sid}">
 <div class="container">
  <div class="center"><span class="eyebrow">{eyebrow}</span><h2>{h2 or S['gal_h2']}</h2><p class="lead">{lead or S['gal_lead']} <span class="ph">photos d'ambiance sous licence libre — à remplacer par vos photos</span></p></div>
  <div class="gallery">{gal}</div>
 </div>
</section>
'''

def location_section(S, sid='location'):
    wa = S['wa']
    hours = ''.join(f'<tr><td>{d}</td><td>{h}</td></tr>' for d, h in S['hours'])
    tel_li = ''.join(f'<li><span class="ico">{ico("phone")}</span><div><small>Téléphone</small><a href="tel:{t.replace(" ","")}">{t}</a></div></li>' for t in S['tels'])
    wa_note = f' {ph(S["wa_note"])}' if S.get('wa_note') else ''
    social = ''.join(f'<li><span class="ico">{ico("fb")}</span><div><small>{n}</small><a href="https://{u}" target="_blank" rel="noopener">{esc(u.split('/', 1)[1] if n != 'Instagram' else '@' + u.rstrip('/').split('/')[-1])}</a></div></li>' for n, u in S.get('social', []))
    mail = (f'<li><span class="ico">{ico("mail")}</span><div><small>Email</small><a href="mailto:{S["email"]}">{S["email"]}</a></div></li>' if S.get('email')
            else f'<li><span class="ico">{ico("mail")}</span><div><small>Email</small><span class="ph">adresse email à ajouter</span></div></li>')
    note = f'<p class="caveat">{S["map_note"]}</p>' if S.get('map_note') else ''
    return f'''<section class="section alt" id="{sid}">
 <div class="container grid-2">
  <div class="reveal"><div class="map-wrap"><iframe title="Carte {esc(S['name'])}" src="https://maps.google.com/maps?q={quote(S['map_q'])}&z={S.get('map_z',16)}&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>{note}</div>
  <div class="reveal" id="contact">
   <span class="eyebrow">Accès & horaires</span><h2>{S['loc_h2']}</h2><p class="lead">{S['loc_p']}</p>
   <table class="hours">{hours}</table>
   <ul class="contact-list">
    <li><span class="ico">{ico('pin')}</span><div><small>Adresse</small><span>{S['address']}</span></div></li>
    {tel_li}
    <li><span class="ico">{ico('wa')}</span><div><small>WhatsApp</small><a href="https://wa.me/{wa}" target="_blank" rel="noopener">{S['wa_disp']}</a>{wa_note}</div></li>
    {mail}{social}
   </ul>
   <a class="btn btn-primary" href="https://www.google.com/maps/search/?api=1&query={quote(S['map_q'])}" target="_blank" rel="noopener">{ico('map')}Itinéraire Google Maps</a>
  </div>
 </div>
</section>
'''

def footer(S, float_msg, float_label='Réponse sur WhatsApp', site_extra=None):
    wa = S['wa']
    site = {'slug': S['slug'], 'wa': wa, 'formIntro': {'fr': S['form_intro']}}
    if site_extra: site.update(site_extra)
    return f'''</main>
<footer class="site-footer">
 <div class="container">
  <div class="foot-grid">
   <div><h3>{esc(S['name'])}</h3><p>{S['tagline']}</p><p style="font-size:.8rem;opacity:.75">Site de démonstration non officiel, réalisé à partir d'informations publiques. Contenus, cartes et tarifs indicatifs, à valider par l'établissement.</p></div>
   <div><h3>Contact</h3><p>{'<br>'.join(f'<a href="tel:{t.replace(" ","")}">{t}</a>' for t in S['tels'])}<br><a href="https://wa.me/{wa}" target="_blank" rel="noopener">WhatsApp {S['wa_disp']}</a></p></div>
   <div><h3>Horaires</h3><p>{S['hours_short']}</p></div>
  </div>
  <details><summary>Crédits photos (licences libres, Wikimedia Commons)</summary><ul>{'<li>Illustrations et icônes : créations originales Synaris Labs (SVG).</li>' if S.get('svg_credit') else ''}{credits_html(S['slug'])}</ul></details>
  <p>© <span id="year">2026</span> {esc(S['name'])} · <a class="synaris-badge" href="https://github.com/islemyakoubi" target="_blank" rel="noopener"><i></i>Démo réalisée par Synaris Labs · Menzel Temime</a></p>
 </div>
</footer>
<a class="wa-float" href="{walink(wa, float_msg)}" target="_blank" rel="noopener" aria-label="WhatsApp">{ico('wa')}<span>{float_label}</span></a>
<div class="lightbox" role="dialog" aria-modal="true"><button type="button" aria-label="Fermer">×</button><img alt=""></div>
<script>window.SITE={json.dumps(site, ensure_ascii=False)};</script>
<script src="site.js" defer></script>
</body>
</html>'''

def write(S, h):
    os.makedirs(os.path.join(ROOT, S['slug']), exist_ok=True)
    open(os.path.join(ROOT, S['slug'], 'index.html'), 'w').write(h); copy_assets(S['slug']); print('built', S['slug'], len(h))

def hero(S, actions, facts):
    fx = ''.join(f'<div class="fact"><b>{b}</b><span>{s}</span></div>' for b, s in facts)
    return f'''<section class="hero">
 <img class="hero-bg" src="img/hero.jpg" alt="{esc(S['hero_alt'])}" fetchpriority="high">
 <div class="container">
  <span class="eyebrow">{S['eyebrow']}</span>
  <h1>{S['h1']}</h1>
  <p class="lead">{S['lead']}</p>
  <div class="hero-actions">{actions}</div>
  <div class="facts">{fx}</div>
 </div>
</section>
'''

def about(S):
    ps = ''.join(f'<p>{p}</p>' for p in S['about_p'][1:])
    chips = ''.join(f'<span>{c}</span>' for c in S.get('chips', []))
    return f'''<section class="section" id="about">
 <div class="container grid-2">
  <div class="reveal"><span class="eyebrow">{S.get('about_eyebrow','La maison')}</span><h2>{S['about_h2']}</h2><p class="lead">{S['about_p'][0]}</p>{ps}<div class="spaces">{chips}</div></div>
  <div class="about-img reveal"><img src="img/{S['about_img']}.jpg" alt="{esc(S['about_alt'])}" loading="lazy" width="800" height="1000"></div>
 </div>
</section>
'''

def features(S, eyebrow='Services', h2='Pensé pour vos clients'):
    fx = ''.join(f'<div class="feature reveal"><div class="ico">{ico(i)}</div><h3>{t}</h3><p>{d}</p></div>' for i, t, d in S['features'])
    return f'''<section class="section">
 <div class="container">
  <div class="center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2></div>
  <div class="features">{fx}</div>
 </div>
</section>
'''

# ---------------------------------------------------------------- RESTAURANT / CAFÉ
def build_resto(S):
    wa = S['wa']; name = S['name']
    order = S.get('mode') == 'order'
    nav = [('about', 'La maison'), ('menu', 'La carte'), ('booking', 'Commander' if order else 'Réserver'), ('avis', 'Avis'), ('gallery', 'Galerie'), ('location', 'Accès')]
    cta = 'Commander' if order else 'Réserver une table'
    r0 = S['ratings'][0]
    acts = (f'<a class="btn btn-light" href="#booking">{ico("calendar")}<span>{cta}</span></a>'
            f'<a class="btn btn-wa" href="{walink(wa, S["wa_msg"])}" target="_blank" rel="noopener">{ico("wa")}<span>WhatsApp</span></a>')
    facts = [(f'<span class="star">★</span> {r0["score"]}/5', f'{r0["count"]} avis · {r0["src"]}')] + S['facts']
    dishes = ''.join(f'''<article class="card dish reveal"><div class="card-img"><img src="img/{d['img']}.jpg" alt="{esc(d['alt'])}" loading="lazy" width="800" height="600"></div><div class="card-body"><h3>{d['name']}</h3><p>{d['desc']}</p><div class="price"><span class="muted" style="font-size:.85rem">{d.get('tag','Prix')}</span><span><b>— DT</b> {ph()}</span></div></div></article>''' for d in S['dishes'])
    cats = ''.join(f'<span>{c}</span>' for c in S['menu_cats'])
    qr = qr_svg(S['slug'])
    menu = f'''<section class="section alt" id="menu">
 <div class="container">
  <div class="center"><span class="eyebrow">La carte</span><h2>{S['menu_h2']}</h2><p class="lead">{S['menu_lead']}</p></div>
  <div class="cards {S.get('dish_cols','c4')}">{dishes}</div>
  <div class="chips">{cats}</div>
  <p class="form-note center" style="margin-top:1rem">{S.get('menu_note','Plats relevés sur les cartes et avis publics en ligne. Noms, compositions et prix à confirmer avec vous ; photos d’ambiance non contractuelles.')}</p>
  <div class="qr-teaser reveal">
   <div><span class="eyebrow">Menu QR</span><h3>Votre carte sur chaque table, toujours à jour</h3>
    <ul class="checks"><li>Prix modifiables en 1 minute depuis votre téléphone, sans réimprimer.</li><li>Carte en français, anglais et arabe, avec photos de vos vrais plats.</li><li>{'Commande et suivi sur WhatsApp, livraison ou à emporter.' if order else 'Bouton « Réserver » et « Commander à emporter » via WhatsApp.'}</li><li>Plats du jour et poisson du marché mis en avant.</li></ul></div>
   <div class="qr-card">{qr}<b>Scannez : carte de démo</b><small>Le QR ouvre cette page. Dans la version finale : votre menu complet.</small></div>
  </div>
 </div>
</section>
'''
    # booking / order form
    slots = S.get('slots', ['12:00', '12:30', '13:00', '13:30', '14:00', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30'])
    if order:
        form = f'''<form class="form reveal" id="req-form" novalidate>
   <label class="full"><span>Votre commande</span><textarea name="commande" required placeholder="{esc(S.get('order_ph','Ex. : plateau 24 pièces, 2 soupes miso…'))}"></textarea></label>
   <label><span>Mode</span><select name="mode"><option>Livraison</option><option>À emporter</option><option>Sur place (réservation)</option></select></label>
   <label><span>Heure souhaitée</span><select name="heure"><option>Dès que possible</option>{''.join(f'<option>{s}</option>' for s in slots)}</select></label>
   <label class="full"><span>Adresse (si livraison)</span><input name="adresse" autocomplete="street-address"></label>
   <label><span>Nom</span><input name="nom" autocomplete="name" required></label>
   <label><span>Téléphone</span><input name="telephone" type="tel" inputmode="tel" autocomplete="tel" required></label>
   <div class="form-actions full"><button class="btn btn-wa" type="submit">{ico('wa')}Envoyer sur WhatsApp</button></div>
   <p class="form-note full">Démo : aucune donnée n'est enregistrée sur ce site. Le formulaire ouvre WhatsApp avec votre message pré-rempli ; rien n'est envoyé sans votre validation.</p>
  </form>'''
        steps = '<li><span><b>Composez votre commande</b>plateaux, pièces, boissons.</span></li><li><span><b>Envoyez sur WhatsApp</b>le message part tout prêt, sans appel.</span></li><li><span><b>Confirmation</b>prix, délai et frais de livraison confirmés par le restaurant.</span></li>'
        bt, bl = 'Commandez en 1 minute', 'Livraison, à emporter ou sur place : votre commande arrive directement sur le WhatsApp du restaurant.'
    else:
        form = f'''<form class="form reveal" id="req-form" novalidate>
   <label><span>Date</span><input type="date" name="date" required></label>
   <label><span>Heure</span><select name="heure">{''.join(f'<option>{s}</option>' for s in slots)}</select></label>
   <label><span>Personnes</span><select name="personnes">{''.join(f'<option>{i}</option>' for i in range(1, 13))}<option>Plus de 12 (groupe)</option></select></label>
   <label><span>Occasion</span><select name="occasion"><option>{S.get('occ0','Repas')}</option><option>Anniversaire</option><option>Repas d'affaires</option><option>Groupe / famille</option></select></label>
   <label class="full"><span>Nom</span><input name="nom" autocomplete="name" required></label>
   <label class="full"><span>Téléphone / WhatsApp</span><input name="telephone" type="tel" inputmode="tel" autocomplete="tel" required></label>
   <label class="full"><span>Message (optionnel)</span><textarea name="message" placeholder="{esc(S.get('msg_ph','Terrasse, chaise bébé, allergie…'))}"></textarea></label>
   <div class="form-actions full"><button class="btn btn-wa" type="submit">{ico('wa')}Envoyer sur WhatsApp</button></div>
   <p class="form-note full">Démo : aucune donnée n'est enregistrée sur ce site. Le formulaire ouvre WhatsApp avec la demande pré-remplie ; la table est confirmée par le restaurant.</p>
  </form>'''
        steps = '<li><span><b>Choisissez date, heure et nombre</b>en quelques secondes.</span></li><li><span><b>Envoyez sur WhatsApp</b>le message part tout prêt, même la nuit.</span></li><li><span><b>Le restaurant confirme</b>et rappelle si besoin.</span></li>'
        bt, bl = S.get('book_title', 'Réservez votre table sans appeler'), S.get('book_lead', 'Aujourd’hui, on vous joint uniquement par téléphone. Ici, vos clients envoient leur demande en 1 minute, et vous confirmez quand vous êtes disponible.')
    booking = f'''<section class="section" id="booking">
 <div class="container booking">
  <div class="reveal"><span class="eyebrow">{'Commande' if order else 'Réservation'}</span><h2>{bt}</h2><p class="lead">{bl}</p>
   <ol class="steps">{steps}</ol>
   <div class="notice">{S['book_note']}</div>
  </div>
  {form}
 </div>
</section>
'''
    h = (head(S) + header(S, nav, '#booking', cta) + hero(S, acts, facts) + about(S) + menu + features(S) + booking
         + ratings_section(S) + gallery_section(S) + location_section(S) + footer(S, S['wa_msg']))
    write(S, h)

# ---------------------------------------------------------------- EVENT HALL
def build_event(S):
    wa = S['wa']
    nav = [('about', 'La salle'), ('formules', 'Formules'), ('dispo', 'Disponibilités'), ('gallery', 'Galerie'), ('visite', 'Visite & devis'), ('location', 'Accès')]
    acts = (f'<a class="btn btn-light" href="#visite">{ico("calendar")}<span>Demander une visite</span></a>'
            f'<a class="btn btn-wa" href="{walink(wa, S["wa_msg"])}" target="_blank" rel="noopener">{ico("wa")}<span>WhatsApp</span></a>')
    r0 = S['ratings'][0]
    facts = [(f'<span class="star">★</span> {r0["score"]}/5', f'{r0["count"]} avis · {r0["src"]}')] + S['facts']
    pk = ''.join(f'''<article class="pkg reveal{' hl' if p.get('hl') else ''}"><span class="eyebrow" style="margin:0">{p['eyebrow']}</span><h3>{p['name']}</h3><p class="muted" style="margin:0">{p['desc']}</p><ul>{''.join(f'<li>{x}</li>' for x in p['items'])}</ul><p style="margin:.4rem 0 0"><b>Tarif</b> {ph('sur devis · à confirmer')}</p><a class="btn {'btn-primary' if p.get('hl') else 'btn-light'}" style="border-color:rgba(0,0,0,.1)" href="{walink(wa, f"Bonjour {S['name']}, je souhaite le tarif de la formule « {p['name']} ». Date : … / Invités : …")}" target="_blank" rel="noopener">{ico('wa')}Demander le tarif</a></article>''' for p in S['pkgs'])
    formules = f'''<section class="section alt" id="formules">
 <div class="container">
  <div class="center"><span class="eyebrow">Formules</span><h2>{S['pkg_h2']}</h2><p class="lead">{S['pkg_lead']}</p></div>
  <div class="pkgs">{pk}</div>
  <p class="form-note center" style="margin-top:1.2rem">Formules d'exemple pour la démo : contenu, capacité et tarifs à définir avec la salle.</p>
 </div>
</section>
'''
    # demo availability calendar (static, clearly labelled)
    days = ['L', 'M', 'M', 'J', 'V', 'S', 'D']
    busy = {10, 11, 17, 18, 24, 31}; opt = {3, 25}; free = {4, 5, 12, 19, 26}
    cells = ''.join(f'<b>{d}</b>' for d in days) + '<span class="empty"></span>' * 3  # Oct 2026 starts Thursday
    for d in range(1, 32):
        c = 'busy' if d in busy else 'opt' if d in opt else 'free' if d in free else ''
        cells += f'<span class="{c}">{d}</span>'
    dispo = f'''<section class="section" id="dispo">
 <div class="container grid-2">
  <div class="reveal"><span class="eyebrow">Disponibilités</span><h2>Vos dates libres, visibles en un coup d'œil</h2><p class="lead">Fini les dizaines d'appels « la salle est libre le samedi 17 ? ». Le calendrier se met à jour depuis votre téléphone ; les familles demandent une visite ou une option en un clic.</p>
   <ul class="checks"><li>Option provisoire de 48 h sur une date, confirmée par acompte.</li><li>Rappel automatique WhatsApp avant la visite et avant l'événement.</li><li>Galerie par type d'événement : mariage, fiançailles, henna, anniversaire.</li></ul></div>
  <div class="cal reveal"><div class="cal-head"><span>Octobre 2026</span><span class="ph">calendrier de démo</span></div><div class="cal-grid">{cells}</div>
   <div class="cal-legend"><span><i style="background:#dcfce7"></i>Libre</span><span><i style="background:#fff4cc"></i>Option</span><span><i style="background:#fde2e2"></i>Réservé</span></div>
   <p class="caveat">Dates fictives pour illustrer le module : aucune information réelle sur l'occupation de la salle.</p></div>
 </div>
</section>
'''
    form = f'''<section class="section" id="visite">
 <div class="container booking">
  <div class="reveal"><span class="eyebrow">Visite & devis</span><h2>Demandez une visite ou un devis</h2><p class="lead">Indiquez la date, le type d'événement et le nombre d'invités : la demande arrive directement sur WhatsApp, avec toutes les informations.</p>
   <ol class="steps"><li><span><b>Votre événement</b>date, type, nombre d'invités.</span></li><li><span><b>Envoi WhatsApp</b>message pré-rempli, sans appel.</span></li><li><span><b>Visite & devis</b>la salle vous propose un créneau de visite.</span></li></ol>
   <div class="notice">{S['book_note']}</div></div>
  <form class="form reveal" id="req-form" novalidate>
   <label><span>Date de l'événement</span><input type="date" name="date" required></label>
   <label><span>Type d'événement</span><select name="type">{''.join(f'<option>{t}</option>' for t in S['event_types'])}</select></label>
   <label><span>Nombre d'invités</span><select name="invites"><option>Moins de 100</option><option>100 – 200</option><option>200 – 300</option><option>300 – 400</option><option>Plus de 400</option><option>Je ne sais pas encore</option></select></label>
   <label><span>Formule</span><select name="formule"><option>Je souhaite être conseillé(e)</option>{''.join(f'<option>{p["name"]}</option>' for p in S['pkgs'])}</select></label>
   <label class="full"><span>Nom</span><input name="nom" autocomplete="name" required></label>
   <label class="full"><span>Téléphone / WhatsApp</span><input name="telephone" type="tel" inputmode="tel" autocomplete="tel" required></label>
   <label class="full"><span>Message (optionnel)</span><textarea name="message" placeholder="Visite souhaitée le samedi matin, traiteur, décoration…"></textarea></label>
   <div class="form-actions full"><button class="btn btn-wa" type="submit">{ico('wa')}Envoyer sur WhatsApp</button></div>
   <p class="form-note full">Démo : aucune donnée n'est enregistrée sur ce site. Le formulaire ouvre WhatsApp avec la demande pré-remplie.</p>
  </form>
 </div>
</section>
'''
    h = (head(S) + header(S, nav, '#visite', 'Demander une visite') + hero(S, acts, facts) + about(S) + formules + dispo
         + gallery_section(S) + form + ratings_section(S, eyebrow='Avis', h2='Leur note en ligne') + location_section(S) + footer(S, S['wa_msg']))
    write(S, h)

# ---------------------------------------------------------------- INVITATION STUDIO (faire-part)
def inv_svg(a, b, c):
    return f'''<svg class="inv-art" viewBox="0 0 520 440" role="img" aria-label="Illustration originale : faire-part et enveloppe">
<defs><filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="12" stdDeviation="12" flood-opacity=".18"/></filter>
<linearGradient id="kr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d8b48a"/><stop offset="1" stop-color="#c49a6c"/></linearGradient></defs>
<circle cx="420" cy="80" r="60" fill="{b}" opacity=".18"/><circle cx="90" cy="380" r="46" fill="{a}" opacity=".15"/>
<g filter="url(#sh)" transform="rotate(-8 190 250)"><rect x="70" y="120" width="240" height="190" rx="8" fill="url(#kr)"/><path d="M70 128l120 90 120-90" fill="none" stroke="#a97f52" stroke-width="3"/><circle cx="190" cy="218" r="20" fill="{a}"/><text x="190" y="225" text-anchor="middle" font-family="Georgia" font-size="18" fill="#fff">&amp;</text></g>
<g filter="url(#sh)" transform="rotate(6 350 220)"><rect x="250" y="70" width="200" height="280" rx="10" fill="#fffdf8" stroke="{c}" stroke-width="2"/>
<rect x="264" y="84" width="172" height="252" rx="6" fill="none" stroke="{a}" stroke-width="1.5" stroke-dasharray="4 4"/>
<path d="M300 118c20-18 80-18 100 0" stroke="{b}" stroke-width="2" fill="none"/><circle cx="350" cy="112" r="5" fill="{b}"/>
<text x="350" y="175" text-anchor="middle" font-family="Georgia" font-style="italic" font-size="26" fill="{a}">Yasmine</text>
<text x="350" y="203" text-anchor="middle" font-family="Georgia" font-size="16" fill="#8a7a66">&amp;</text>
<text x="350" y="232" text-anchor="middle" font-family="Georgia" font-style="italic" font-size="26" fill="{a}">Karim</text>
<rect x="305" y="255" width="90" height="2" fill="{c}"/><text x="350" y="282" text-anchor="middle" font-family="Inter,Arial" font-size="11" letter-spacing="2" fill="#8a7a66">SAMEDI · HAMMAMET</text>
<path d="M290 312c15-10 30-10 45 0M365 312c15-10 30-10 45 0" stroke="{b}" stroke-width="2" fill="none"/></g>
<g fill="{b}" opacity=".7"><path d="M60 110c10-20 30-20 34 0-14 8-24 8-34 0z"/><path d="M470 360c10-20 30-20 34 0-14 8-24 8-34 0z"/></g>
</svg>'''

def build_invit(S):
    wa = S['wa']; th = S['theme']
    nav = [('collections', 'Collections'), ('sur-mesure', 'Sur mesure'), ('devis', 'Devis'), ('avis', 'Avis'), ('gallery', 'Inspirations'), ('location', 'Accès')]
    r0 = S['ratings'][0]
    herohtml = f'''<section class="hero-split">
 <div class="container">
  <div>
   <span class="eyebrow">{S['eyebrow']}</span>
   <h1>{S['h1']}</h1>
   <p class="lead">{S['lead']}</p>
   <div class="hero-actions"><a class="btn btn-primary" href="#devis">{ico('calendar')}Demander un devis</a><a class="btn btn-wa" href="{walink(wa, S['wa_msg'])}" target="_blank" rel="noopener">{ico('wa')}WhatsApp</a></div>
   <div class="badges"><span><i class="open-dot"></i>{S['open_badge']}</span><span>★ {r0['score']}/5 · {r0['count']} avis</span><span>{ico('store')}Atelier à Hammamet</span></div>
  </div>
  {inv_svg(th['accent'], th['accent2'], th['soft'])}
 </div>
</section>
'''
    cards = ''.join(f'''<article class="card reveal"><div class="card-img"><img src="img/{c['img']}.jpg" alt="{esc(c['alt'])}" loading="lazy" width="800" height="600"></div><div class="card-body"><h3>{c['name']}</h3><p>{c['desc']}</p><div class="price"><span class="muted" style="font-size:.85rem">Prix unitaire</span><span><b>— DT</b> {ph()}</span></div></div></article>''' for c in S['collections'])
    coll = f'''<section class="section alt" id="collections">
 <div class="container">
  <div class="center"><span class="eyebrow">Collections</span><h2>{S['coll_h2']}</h2><p class="lead">{S['coll_lead']}</p></div>
  <div class="cards c3">{cards}</div>
  <p class="form-note center" style="margin-top:1.2rem">Catégories d'exemple et photos d'ambiance : vos vrais modèles, prix par quantité et délais seront ajoutés avec vous.</p>
 </div>
</section>
'''
    fx = ''.join(f'<div class="feature reveal"><div class="ico">{ico(i)}</div><h3>{t}</h3><p>{d}</p></div>' for i, t, d in S['features'])
    surmesure = f'''<section class="section" id="sur-mesure">
 <div class="container">
  <div class="center"><span class="eyebrow">Sur mesure</span><h2>Du premier croquis au carton livré</h2><p class="lead">Un parcours clair, avec validation du bon à tirer sur WhatsApp : moins d'allers-retours, zéro faute sur les prénoms.</p></div>
  <div class="features">{fx}</div>
 </div>
</section>
'''
    form = f'''<section class="section alt" id="devis">
 <div class="container booking">
  <div class="reveal"><span class="eyebrow">Devis</span><h2>Votre devis en 1 minute</h2><p class="lead">Type de carte, quantité, date : la demande arrive directement sur WhatsApp. Vous pouvez joindre ensuite une photo du modèle qui vous plaît.</p>
   <ol class="steps"><li><span><b>Décrivez votre projet</b>type, quantité, langue(s) du texte.</span></li><li><span><b>Envoi WhatsApp</b>message pré-rempli, sans appel.</span></li><li><span><b>Proposition & BAT</b>prix, maquette et délai confirmés par l'atelier.</span></li></ol>
   <div class="notice">{S['book_note']}</div></div>
  <form class="form reveal" id="req-form" novalidate>
   <label><span>Type de carte</span><select name="type"><option>Faire-part de mariage</option><option>Fiançailles / Outya</option><option>Henna</option><option>Naissance / baptême</option><option>Anniversaire</option><option>Menus, marque-places, étiquettes</option></select></label>
   <label><span>Quantité</span><select name="quantite"><option>Moins de 100</option><option>100 – 200</option><option>200 – 400</option><option>Plus de 400</option></select></label>
   <label><span>Date de l'événement</span><input type="date" name="date" required></label>
   <label><span>Langue(s) du texte</span><select name="langue"><option>Français</option><option>Arabe</option><option>Français + arabe</option><option>Autre</option></select></label>
   <label class="full"><span>Nom</span><input name="nom" autocomplete="name" required></label>
   <label class="full"><span>Téléphone / WhatsApp</span><input name="telephone" type="tel" inputmode="tel" autocomplete="tel" required></label>
   <label class="full"><span>Votre idée (optionnel)</span><textarea name="message" placeholder="Style kraft et fleurs séchées, couleurs, enveloppe, sceau de cire…"></textarea></label>
   <div class="form-actions full"><button class="btn btn-wa" type="submit">{ico('wa')}Envoyer sur WhatsApp</button></div>
   <p class="form-note full">Démo : aucune donnée n'est enregistrée sur ce site. Le formulaire ouvre WhatsApp avec la demande pré-remplie.</p>
  </form>
 </div>
</section>
'''
    S['svg_credit'] = True
    h = (head(S) + header(S, nav, '#devis', 'Demander un devis') + herohtml + about(S) + coll + surmesure + form
         + ratings_section(S, eyebrow='Avis', h2='Une note parfaite en ligne') + gallery_section(S) + location_section(S)
         + footer(S, S['wa_msg']))
    write(S, h)
