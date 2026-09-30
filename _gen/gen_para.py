import json, sys
import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
from urllib.parse import quote
CI = {
 'face':'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="16" cy="16" r="12"/><path d="M11 19c1.5 2 3 3 5 3s3.5-1 5-3M12 13h.01M20 13h.01"/><path d="M24 6l2-2M26 10h2"/></svg>',
 'sun':'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="16" cy="16" r="6"/><path d="M16 3v3M16 26v3M3 16h3M26 16h3M6.8 6.8l2.1 2.1M23.1 23.1l2.1 2.1M6.8 25.2l2.1-2.1M23.1 8.9l2.1-2.1"/></svg>',
 'soap':'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><rect x="9" y="12" width="14" height="16" rx="4"/><path d="M13 12V8h6v4M16 8V4h5"/><circle cx="24" cy="6" r="1.5"/><circle cx="27" cy="11" r="1"/></svg>',
 'baby':'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M12 10h8v16a4 4 0 0 1-8 0z"/><path d="M13 10V7a3 3 0 0 1 6 0v3M12 16h4M12 20h4"/></svg>',
 'hair':'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 12h20v5H6zM9 17v9M13 17v9M17 17v9M21 17v9"/><path d="M10 12c0-4 3-7 6-7s6 3 6 7"/></svg>',
 'pill':'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="11" width="24" height="10" rx="5" transform="rotate(-35 16 16)"/><path d="M12.5 10.5l7 11" /></svg>',
 'leaf':'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 26C6 14 14 6 27 5c-1 13-9 21-21 21z"/><path d="M6 26l11-11"/></svg>',
 'chair':'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="13" cy="5" r="2"/><path d="M13 9v9h8l3 7"/><path d="M13 13h7"/><path d="M10 14a8 8 0 1 0 11 9"/></svg>',
 'bp':'<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="5" y="6" width="16" height="20" rx="3"/><path d="M9 20l3-5 3 3 3-6"/><path d="M21 14h4a3 3 0 0 1 0 6h-1"/></svg>',
}
def hero_svg(a,b,c):
    return f'''<svg class="hero-art" viewBox="0 0 520 440" role="img" aria-label="Illustration originale : produits de soin">
<defs><linearGradient id="g1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>
<linearGradient id="g2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="{c}"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-opacity=".18"/></filter></defs>
<path d="M88 70C160 10 330 0 420 70s110 220 30 300-280 90-370 20S16 130 88 70z" fill="url(#g1)" opacity=".18"/>
<circle cx="420" cy="90" r="46" fill="{b}" opacity=".25"/><circle cx="92" cy="360" r="30" fill="{a}" opacity=".25"/>
<g filter="url(#sh)">
 <rect x="120" y="150" width="96" height="220" rx="26" fill="url(#g2)" stroke="{a}" stroke-width="3"/>
 <rect x="146" y="112" width="44" height="40" rx="8" fill="{a}"/><rect x="160" y="88" width="16" height="26" rx="4" fill="{a}"/><path d="M176 94h34" stroke="{a}" stroke-width="10" stroke-linecap="round"/>
 <rect x="138" y="230" width="60" height="60" rx="12" fill="#fff" stroke="{b}" stroke-width="2"/><path d="M168 244v32M152 260h32" stroke="{b}" stroke-width="7" stroke-linecap="round"/>
 <rect x="236" y="200" width="86" height="170" rx="18" fill="#fff" stroke="{b}" stroke-width="3"/><rect x="236" y="178" width="86" height="30" rx="10" fill="{b}"/>
 <rect x="252" y="250" width="54" height="8" rx="4" fill="{a}" opacity=".5"/><rect x="252" y="266" width="38" height="8" rx="4" fill="{a}" opacity=".3"/>
 <rect x="340" y="296" width="120" height="74" rx="22" fill="url(#g2)" stroke="{a}" stroke-width="3"/><rect x="334" y="280" width="132" height="28" rx="12" fill="{a}"/>
 <path d="M338 170c30-60 90-70 120-60-8 50-54 84-120 60z" fill="{b}" opacity=".85"/><path d="M338 170l80-40" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
</g>
<g fill="{a}" opacity=".6"><circle cx="100" cy="140" r="6"/><circle cx="470" cy="230" r="5"/><circle cx="300" cy="120" r="4"/></g>
</svg>'''

def build(S):
    slug=S['slug']; wa=S['wa']; th=S['theme']
    fam,furl=FONTS[S['font']]
    def walink(msg): return f'https://wa.me/{wa}?text='+quote(msg)
    cats=''.join(f'''<article class="cat reveal"><div class="ico">{CI[i]}</div><h3>{n}</h3><p>{d}</p><a href="{walink(f"Bonjour {S['name']}, je cherche un produit : {n}. Est-il disponible ?")}" target="_blank" rel="noopener">Demander sur WhatsApp →</a></article>''' for i,n,d in S['cats'])
    hours=''.join(f'<tr><td>{d}</td><td>{h}</td></tr>' for d,h in S['hours'])
    gal=''.join((f'<button type="button" data-full="img/{g}.jpg" aria-label="Agrandir"><img src="img/{g}.jpg" alt="{esc(a)}" loading="lazy"></button>' if g else f'<div class="ph-tile">{esc(a)}</div>') for g,a in S['gallery'])
    rent=S.get('rent_section','')
    site={'slug':slug,'wa':wa,'formIntro':{'fr':f"Bonjour {S['name']}, voici ma demande :"}}
    h=f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(S['title'])}</title>
<meta name="description" content="{esc(S['desc'])}">
<meta name="robots" content="noindex,nofollow">
<meta name="theme-color" content="{th['accent']}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{furl}" rel="stylesheet">
<link rel="stylesheet" href="site.css">
<style>:root{{--accent:{th['accent']};--accent-2:{th['accent2']};--accent-soft:{th['soft']};--bg:{th['bg']};--bg-alt:{th['bgalt']};--ink-strong:{th['ink']};--font-head:'{fam}',system-ui,sans-serif;--font-body:'Inter',system-ui,sans-serif}}h1,h2,h3{{letter-spacing:-.02em}}</style>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='{th['accent'].replace('#','%23')}'/%3E%3Cpath d='M32 16v32M16 32h32' stroke='white' stroke-width='9' stroke-linecap='round'/%3E%3C/svg%3E">
</head>
<body>
<div class="demo-ribbon"><b>Démo</b> — maquette non officielle réalisée par Synaris Labs à partir d'informations publiques, à valider par l'établissement.</div>
<header class="site-header">
 <div class="container nav">
  <a class="brand" href="#top"><span class="brand-mark"><svg width="20" height="20" viewBox="0 0 24 24"><path d="M12 4v16M4 12h16" stroke="#fff" stroke-width="4" stroke-linecap="round"/></svg></span><span>{S['short']}<small>{S['tagline']}</small></span></a>
  <ul class="nav-links"><li><a href="#categories">Catalogue</a></li>{'<li><a href="#location-materiel">Location</a></li>' if rent else ''}<li><a href="#commande">Commander</a></li><li><a href="#gallery">Boutique</a></li><li><a href="#location">Accès & horaires</a></li><li><a href="#contact">Contact</a></li></ul>
  <div class="nav-tools">
   <a class="btn btn-wa header-cta" href="{walink(f'Bonjour {S["name"]}, j’ai une question.')}" target="_blank" rel="noopener">{ico('wa')}WhatsApp</a>
   <button class="menu-btn" type="button" aria-label="Menu" aria-expanded="false"><span></span></button>
  </div>
 </div>
 <nav class="mobile-menu container"><a href="#categories">Catalogue</a>{'<a href="#location-materiel">Location de matériel</a>' if rent else ''}<a href="#commande">Commander</a><a href="#gallery">Boutique</a><a href="#location">Accès & horaires</a><a href="#contact">Contact</a></nav>
</header>
<main id="top">
<section class="hero-split">
 <div class="container">
  <div>
   <span class="eyebrow">{S['eyebrow']}</span>
   <h1>{S['h1']}</h1>
   <p class="lead">{S['lead']}</p>
   <div class="hero-actions"><a class="btn btn-wa" href="{walink(f'Bonjour {S["name"]}, je cherche un produit. Est-il disponible ?')}" target="_blank" rel="noopener">{ico('wa')}Demander un produit</a><a class="btn btn-light" style="border-color:rgba(0,0,0,.1)" href="#categories">Voir les rayons</a></div>
   <div class="badges"><span><i class="open-dot"></i>{S['open_badge']}</span><span>{ico('store')}Conseil en boutique</span><span>{ico('truck')}Livraison locale <em class="ph">à définir</em></span></div>
  </div>
  {hero_svg(th['accent'],th['accent2'],th['soft'])}
 </div>
</section>

<section class="section" id="how">
 <div class="container">
  <div class="center"><span class="eyebrow">Comment ça marche</span><h2>Commander chez vous, aussi simple qu'un message</h2><p class="lead">Plus besoin d'attendre une réponse en message privé : vos clients demandent, vous confirmez, ils récupèrent.</p></div>
  <div class="features" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr))">
   <div class="feature reveal"><div class="ico">{ico('chat')}</div><h3>1. Demandez</h3><p>Envoyez le nom ou une photo du produit sur WhatsApp.</p></div>
   <div class="feature reveal"><div class="ico">{ico('shield')}</div><h3>2. On confirme</h3><p>Disponibilité et prix confirmés par l'équipe.</p></div>
   <div class="feature reveal"><div class="ico">{ico('truck')}</div><h3>3. Livraison ou retrait</h3><p>Kélibia, Menzel Temime ou en boutique <span class="ph">zones & frais à définir</span></p></div>
   <div class="feature reveal"><div class="ico">{ico('clock')}</div><h3>Réponse rapide</h3><p>{S['hours_short']} <span class="ph">assistant WhatsApp option</span></p></div>
  </div>
 </div>
</section>

<section class="section alt" id="categories">
 <div class="container">
  <div class="center"><span class="eyebrow">Nos rayons</span><h2>{S['cat_h2']}</h2><p class="lead">Catégories génériques pour la démo : le catalogue réel (produits, prix, stock) sera ajouté avec vous.</p></div>
  <div class="cards cats">{cats}</div>
  <p class="form-note center" style="margin-top:1.2rem">Aucune marque ni promotion n'est affichée dans cette démo. Les informations ne remplacent pas l'avis d'un pharmacien ou d'un médecin.</p>
 </div>
</section>
{rent}
<section class="section" id="commande">
 <div class="container booking">
  <div class="reveal">
   <span class="eyebrow">Commande WhatsApp</span><h2>Réservez vos produits en 1 minute</h2>
   <p class="lead">Remplissez le formulaire : WhatsApp s'ouvre avec votre demande prête à envoyer à la {S['kind']}.</p>
   <ol class="steps"><li><span><b>Indiquez les produits</b>nom, marque ou simple description.</span></li><li><span><b>Choisissez livraison ou retrait</b>Kélibia, Menzel Temime ou en boutique.</span></li><li><span><b>Recevez la confirmation</b>prix et délai confirmés par l'équipe.</span></li></ol>
   <div class="notice">Démo : aucune donnée n'est enregistrée sur ce site. Version complète : mini e-boutique, suivi du stock, lots et dates de péremption, e-facture TTN.</div>
  </div>
  <form class="form reveal" id="req-form" novalidate>
   <label class="full"><span>Produit(s) recherché(s)</span><textarea name="produits" required placeholder="Ex. : crème solaire visage peau sensible, gel lavant bébé…"></textarea></label>
   <label><span>Quantité</span><input name="quantite" inputmode="numeric" placeholder="1"></label>
   <label><span>Mode de récupération</span><select name="mode"><option>Retrait en boutique</option><option>Livraison à Kélibia</option><option>Livraison à Menzel Temime</option><option>Autre zone (à préciser)</option></select></label>
   <label class="full"><span>Adresse (si livraison)</span><input name="adresse" autocomplete="street-address"></label>
   <label><span>Nom</span><input name="nom" autocomplete="name" required></label>
   <label><span>Téléphone</span><input name="telephone" type="tel" inputmode="tel" autocomplete="tel" required></label>
   <div class="form-actions full"><button class="btn btn-wa" type="submit">{ico('wa')}Envoyer sur WhatsApp</button></div>
   <p class="form-note full">Le formulaire ouvre WhatsApp avec votre message pré-rempli ; rien n'est envoyé sans votre validation.</p>
  </form>
 </div>
</section>

<section class="section alt" id="gallery">
 <div class="container">
  <div class="center"><span class="eyebrow">La boutique</span><h2>{S['gal_h2']}</h2><p class="lead">{S['gal_lead']} <span class="ph">emplacements réservés à vos photos</span></p></div>
  <div class="gallery">{gal}</div>
 </div>
</section>

<section class="section" id="location">
 <div class="container grid-2">
  <div class="map-wrap reveal"><iframe title="Carte {esc(S['name'])}" src="https://maps.google.com/maps?q={quote(S['map_q'])}&z=16&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
  <div class="reveal" id="contact">
   <span class="eyebrow">Accès & horaires</span><h2>{S['loc_h2']}</h2>{('<p class="muted">'+S['map_note']+'</p>') if S.get('map_note') else ''}
   <table class="hours">{hours}</table>
   <ul class="contact-list">
    <li><span class="ico">{ico('pin')}</span><div><small>Adresse</small><span>{S['address']}</span></div></li>
    <li><span class="ico">{ico('phone')}</span><div><small>Téléphone</small><a href="tel:{S['tel']}">{S['tel_disp']}</a></div></li>
    <li><span class="ico">{ico('wa')}</span><div><small>WhatsApp</small><a href="https://wa.me/{wa}" target="_blank" rel="noopener">{S['tel_disp']}</a></div></li>
    <li><span class="ico">{ico('fb')}</span><div><small>Facebook</small><a href="https://www.{S['fb']}" target="_blank" rel="noopener">{S['fb']}</a></div></li>
    <li><span class="ico">{ico('mail')}</span><div><small>Email</small><span class="ph">adresse email à ajouter</span></div></li>
   </ul>
   <a class="btn btn-primary" href="https://www.google.com/maps/search/?api=1&query={quote(S['map_q'])}" target="_blank" rel="noopener">{ico('map')}Itinéraire Google Maps</a>
  </div>
 </div>
</section>
</main>
<footer class="site-footer">
 <div class="container">
  <div class="foot-grid">
   <div><h3>{S['name']}</h3><p>{S['tagline']}</p><p style="font-size:.8rem;opacity:.75">Site de démonstration non officiel. Contenus indicatifs, à valider. Les informations de ce site ne remplacent pas l'avis d'un professionnel de santé.</p></div>
   <div><h3>Contact</h3><p><a href="tel:{S['tel']}">{S['tel_disp']}</a><br><a href="https://wa.me/{wa}" target="_blank" rel="noopener">WhatsApp</a></p></div>
   <div><h3>Horaires</h3><p>{S['hours_short']}</p></div>
  </div>
  <details><summary>Crédits images</summary><ul><li>Illustrations et icônes : créations originales Synaris Labs (SVG).</li>{credits_html(slug)}</ul></details>
  <p>© <span id="year">2026</span> {S['name']} · <a class="synaris-badge" href="https://github.com/islemyakoubi" target="_blank" rel="noopener"><i></i>Démo réalisée par Synaris Labs · Menzel Temime</a></p>
 </div>
</footer>
<a class="wa-float" href="{walink(f'Bonjour {S["name"]}, j’ai une question.')}" target="_blank" rel="noopener" aria-label="WhatsApp">{ico('wa')}<span>Une question ? WhatsApp</span></a>
<div class="lightbox" role="dialog" aria-modal="true"><button type="button" aria-label="Fermer">×</button><img alt=""></div>
<script>window.SITE={json.dumps(site,ensure_ascii=False)};</script>
<script src="site.js" defer></script>
</body>
</html>'''
    os.makedirs(os.path.join(ROOT,slug),exist_ok=True); open(os.path.join(ROOT,slug,'index.html'),'w').write(h); copy_assets(slug); print('built',slug,len(h))

CATS=[('face','Soins du visage','Nettoyants, hydratants, soins peaux sensibles.'),('sun','Protection solaire','Visage, corps, enfants : à choisir selon votre peau.'),
      ('soap','Hygiène & corps','Soins du corps, hygiène quotidienne, déodorants.'),('baby','Bébé & maman','Toilette, change, soins du quotidien.'),
      ('hair','Cheveux','Shampoings et soins selon le type de cheveux.'),('leaf','Bien-être & naturel','Huiles, tisanes et produits naturels.'),
      ('pill','Compléments alimentaires','Sur conseil, selon vos besoins.'),('chair','Matériel médical','Orthopédie, aide à la mobilité, auto-surveillance.')]
km=dict(slug='kelibia-medicale', name='Parapharmacie Kélibia Médicale', short='Kélibia Médicale', font='jakarta', kind='parapharmacie',
 title='Parapharmacie Kélibia Médicale — Kélibia (démo)', desc='Parapharmacie à Kélibia, ouverte 7j/7 de 9h à minuit. Demandez vos produits sur WhatsApp, retrait ou livraison locale.',
 tagline='Parapharmacie · Kélibia', theme=dict(accent='#0e8a74',accent2='#5cc8a8',soft='#dff4ee',bg='#f7fbfa',bgalt='#ecf5f2',ink='#0b2420'),
 wa='21641114200', tel='+21641114200', tel_disp='+216 41 114 200', fb='facebook.com/kelibiamedicale',
 address='11 Rue Razi, en face de Aziza, Avenue Ali Belhouane, 8090 Kélibia', map_q='Parapharmacie Kélibia Médicale, Rue Razi, Kélibia',
 eyebrow='Parapharmacie à Kélibia · 7j/7', h1='Vos soins du quotidien, à deux pas et sur WhatsApp',
 lead="Demandez un produit, vérifiez sa disponibilité et récupérez-le en boutique, ou faites-vous livrer à Kélibia et Menzel Temime. Ouvert tous les jours, de 9h à minuit.",
 open_badge='Ouvert 7j/7 · 9h – minuit', hours_short='Tous les jours, 9h – minuit.',
 cat_h2='Tout pour la peau, le corps et la famille', cats=CATS,
 hours=[('Lundi','09h00 – 00h00'),('Mardi','09h00 – 00h00'),('Mercredi','09h00 – 00h00'),('Jeudi','09h00 – 00h00'),('Vendredi','09h00 – 00h00'),('Samedi','09h00 – 00h00'),('Dimanche','09h00 – 00h00')],
 gal_h2='Kélibia Médicale, au centre de Kélibia', gal_lead="Rue Razi, face à Aziza, avenue Ali Belhouane.",
 gallery=[('town','Fort de Kélibia'),(None,'Photo de votre vitrine'),(None,'Photo des rayons soins'),('oil','Huiles et soins naturels (photo d\'ambiance)'),(None,'Photo de l\'équipe'),('port','Kélibia vue d\'en haut'),(None,'Photo du comptoir conseil'),(None,'Photo rayon bébé'),(None,'Votre logo / enseigne')],
 loc_h2='Au cœur de Kélibia')
cm=dict(slug='comptoir-medical-kelibia', name='Parapharmacie Comptoir Médical Kélibia', short='Comptoir Médical', font='outfit', kind='parapharmacie',
 title='Parapharmacie Comptoir Médical — Kélibia (démo)', desc='Parapharmacie et matériel médical à Kélibia : vente et location. Demande sur WhatsApp, retrait ou livraison locale.',
 tagline='Parapharmacie & matériel médical · Kélibia', theme=dict(accent='#2358c4',accent2='#ff8a65',soft='#e4ecfb',bg='#f7f9fd',bgalt='#edf1f9',ink='#0c1a33'),
 wa='21651130130', tel='+21651130130', tel_disp='+216 51 130 130', fb='facebook.com/parapharmacieCM',
 address='123 Avenue Ali Belhouane (en face de la SRTGN), 8090 Kélibia', map_q='SRTGN Kélibia', map_note='Repère sur la carte : la station SRTGN ; la parapharmacie est juste en face.',
 eyebrow='Parapharmacie & matériel médical · Kélibia', h1='Parapharmacie et matériel médical, vente & location',
 lead="Soins du quotidien et matériel médical à Kélibia. Demandez un produit ou une location sur WhatsApp, puis retrait en boutique ou livraison locale. Du lundi au samedi, de 8h30 à minuit.",
 open_badge='Lun – sam · 8h30 – minuit', hours_short='Du lundi au samedi, 8h30 – minuit. Fermé le dimanche.',
 cat_h2='Soins, hygiène et matériel pour toute la famille', cats=CATS[:6]+[('bp','Auto-surveillance','Appareils du quotidien, sur conseil.'),('chair','Matériel médical','Vente et location : mobilité, confort, maintien.')],
 hours=[('Lundi','08h30 – 00h00'),('Mardi','08h30 – 00h00'),('Mercredi','08h30 – 00h00'),('Jeudi','08h30 – 00h00'),('Vendredi','08h30 – 00h00'),('Samedi','08h30 – 00h00'),('Dimanche','Fermé')],
 gal_h2='Comptoir Médical, avenue Ali Belhouane', gal_lead="Face à la SRTGN, au centre de Kélibia.",
 gallery=[('town','Fort de Kélibia'),(None,'Photo de votre vitrine'),(None,'Photo du rayon soins'),(None,'Photo des rayons'),(None,'Photo du matériel en location'),('port','Kélibia et la mer'),(None,'Photo de l\'équipe'),(None,'Photo du comptoir'),(None,'Votre logo / enseigne')],
 loc_h2='Au centre de Kélibia')
cm['rent_section']=f'''<section class="section" id="location-materiel"><div class="container grid-2">
<div class="reveal"><span class="eyebrow">Location de matériel médical</span><h2>Besoin d'un équipement pour quelques semaines ?</h2>
<p class="lead">Après une opération, pour un proche âgé ou un séjour à Kélibia : demandez la disponibilité, la durée et le tarif sur WhatsApp.</p>
<div class="rent"><div>Fauteuil roulant<small>exemple</small></div><div>Déambulateur<small>exemple</small></div><div>Béquilles<small>exemple</small></div><div>Lit médicalisé<small>exemple</small></div><div>Chaise de douche<small>exemple</small></div><div>Autre besoin<small>sur demande</small></div></div>
<p class="form-note" style="margin-top:1rem"><span class="ph">Exemples génériques : liste, disponibilités, caution et tarifs à confirmer par la boutique</span>. Module Synaris : calendrier des locations, rappels de retour, caution.</p>
<a class="btn btn-wa" style="margin-top:1rem" href="https://wa.me/21651130130?text={quote("Bonjour Comptoir Médical, je souhaite louer du matériel médical. Matériel : ... / Durée : ... / À partir du : ...")}" target="_blank" rel="noopener">{ico('wa')}Demander une location</a></div>
<div class="about-img reveal" style="aspect-ratio:4/3;background:#fff"><img src="img/wheelchair.jpg" alt="Fauteuil roulant (photo d'ambiance)" loading="lazy" style="object-fit:contain;padding:1rem"></div>
</div></section>'''
for S in (km,cm): build(S)
