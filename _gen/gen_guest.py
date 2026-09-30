import json, sys
import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *

UI = {
 'nav_about':('À propos','About','Chi siamo'),
 'nav_gallery':('Galerie','Gallery','Galleria'),
 'nav_book':('Réserver','Book','Prenota'),
 'nav_location':('Accès','Location','Dove siamo'),
 'nav_contact':('Contact','Contact','Contatti'),
 'cta_book':('Réserver en direct','Book direct','Prenota direttamente'),
 'cta_wa':('WhatsApp','WhatsApp','WhatsApp'),
 'ribbon':('<b>Démo</b> — maquette non officielle réalisée par Synaris Labs à partir d\'informations publiques, à valider par l\'établissement.',
           '<b>Demo</b> — unofficial mock-up by Synaris Labs based on public information, to be validated by the property.',
           '<b>Demo</b> — prototipo non ufficiale di Synaris Labs basato su informazioni pubbliche, da validare dalla struttura.'),
 'ph':('à confirmer','to be confirmed','da confermare'),
 'from':('à partir de','from','da'),
 'photo_note':('Photos d\'ambiance sous licence libre (non contractuelles) — à remplacer par vos propres photos.',
               'Mood photos under free licences (non-contractual) — to be replaced with your own photos.',
               'Foto d\'atmosfera con licenza libera (non contrattuali) — da sostituire con le vostre foto.'),
 'book_eyebrow':('Réservation directe','Direct booking','Prenotazione diretta'),
 'book_title':('Réservez en direct, sans intermédiaire','Book direct, no middleman','Prenota direttamente, senza intermediari'),
 'book_lead':('Envoyez votre demande en 1 minute : la maison vous répond sur WhatsApp avec la disponibilité et le tarif.',
              'Send your request in 1 minute: the house replies on WhatsApp with availability and rates.',
              'Invia la richiesta in 1 minuto: la casa ti risponde su WhatsApp con disponibilità e tariffe.'),
 's1':('<b>Choisissez vos dates</b>et la chambre qui vous plaît.','<b>Pick your dates</b>and your favourite room.','<b>Scegli le date</b>e la camera che preferisci.'),
 's2':('<b>Envoyez la demande</b>WhatsApp s\'ouvre avec un message pré-rempli.','<b>Send the request</b>WhatsApp opens with a pre-filled message.','<b>Invia la richiesta</b>WhatsApp si apre con un messaggio precompilato.'),
 's3':('<b>Confirmez avec un acompte</b>Lien de paiement sécurisé (Konnect, Flouci ou virement) <span class="ph">module démo</span>','<b>Confirm with a deposit</b>Secure payment link (Konnect, Flouci or bank transfer) <span class="ph">demo module</span>','<b>Conferma con un acconto</b>Link di pagamento sicuro (Konnect, Flouci o bonifico) <span class="ph">modulo demo</span>'),
 'f_arr':('Arrivée','Check-in','Arrivo'),'f_dep':('Départ','Check-out','Partenza'),'f_guests':('Personnes','Guests','Ospiti'),
 'f_room':('Chambre souhaitée','Preferred room','Camera desiderata'),'f_any':('Peu importe / conseillez-moi','No preference / advise me','Indifferente / consigliatemi'),
 'f_name':('Nom complet','Full name','Nome e cognome'),'f_phone':('Téléphone / WhatsApp','Phone / WhatsApp','Telefono / WhatsApp'),
 'f_msg':('Message (optionnel)','Message (optional)','Messaggio (facoltativo)'),'f_msg_ph':('Heure d\'arrivée, table d\'hôtes, besoins particuliers…','Arrival time, dinner, special requests…','Orario di arrivo, cena, richieste particolari…'),
 'f_send':('Envoyer sur WhatsApp','Send via WhatsApp','Invia su WhatsApp'),'f_mail':('Envoyer par email','Send by email','Invia per email'),
 'f_note':('Démo : aucune donnée n\'est enregistrée sur ce site, le formulaire ouvre simplement WhatsApp (ou votre messagerie) avec la demande pré-remplie.',
           'Demo: no data is stored on this site; the form simply opens WhatsApp (or your mail app) with the pre-filled request.',
           'Demo: nessun dato viene salvato su questo sito; il modulo apre WhatsApp (o la tua email) con la richiesta precompilata.'),
 'loc_eyebrow':('Accès','Getting here','Come arrivare'),
 'contact_eyebrow':('Contact','Contact','Contatti'),
 'c_phone':('Téléphone','Phone','Telefono'),'c_wa':('WhatsApp','WhatsApp','WhatsApp'),'c_mail':('Email','Email','Email'),'c_addr':('Adresse','Address','Indirizzo'),'c_fb':('Facebook','Facebook','Facebook'),
 'c_nomail':('Adresse email à ajouter','Email address to be added','Indirizzo email da aggiungere'),
 'credits':('Crédits photos (licences libres, Wikimedia Commons)','Photo credits (free licences, Wikimedia Commons)','Crediti foto (licenze libere, Wikimedia Commons)'),
 'badge':('Démo réalisée par Synaris Labs','Demo made by Synaris Labs','Demo realizzata da Synaris Labs'),
 'f_sub':('Site de démonstration non officiel. Contenus et tarifs indicatifs, à valider.','Unofficial demo site. Content and rates are indicative, to be validated.','Sito demo non ufficiale. Contenuti e tariffe indicativi, da validare.'),
 'gal_eyebrow':('Galerie','Gallery','Galleria'),
 'wa_float':('Réponse sur WhatsApp','Reply on WhatsApp','Risposta su WhatsApp'),
 'nav_menu':('Menu','Menu','Menu'),
}

def build(S):
    slug=S['slug']; T=dict(UI); T.update(S['t'])
    I18N={k:{'fr':v[0],'en':v[1],'it':v[2]} for k,v in T.items()}
    def t(k,tag='span',cls=''):
        c=f' class="{cls}"' if cls else ''
        return f'<{tag}{c} data-i18n="{k}">{T[k][0]}</{tag}>'
    fam,furl=FONTS[S['font']]
    wa=S['wa']; tel=S['tel']
    rooms=''.join(f'''<article class="card reveal"><div class="card-img"><img src="img/{r['img']}.jpg" alt="{esc(r['alt'])}" loading="lazy" width="800" height="600"></div><div class="card-body"><h3>{t(r['k']+'_n','span')}</h3><p>{t(r['k']+'_d','span')}</p><div class="tags">{''.join(f'<span class="tag">{t(x)}</span>' for x in r['tags'])}</div><div class="price"><span class="muted" style="font-size:.85rem">{t('from')}</span><span><b>{r['price']}</b> <span class="ph" data-i18n="ph">à confirmer</span></span></div></div></article>''' for r in S['rooms'])
    feats=''.join(f'<div class="feature reveal"><div class="ico">{ico(i)}</div><h3>{t(k+"_t","span")}</h3><p>{t(k+"_d","span")}</p></div>' for i,k in S['features'])
    gal=''.join(f'<button type="button" data-full="img/{g}.jpg" aria-label="Agrandir"><img src="img/{g}.jpg" alt="{esc(a)}" loading="lazy" width="600" height="600"></button>' for g,a in S['gallery'])
    opts=''.join(f'<option data-i18n="{r["k"]}_n">{T[r["k"]+"_n"][0]}</option>' for r in S['rooms'])+''.join(f'<option>{o}</option>' for o in S.get('extra_opts',[]))
    mail_btn=f'<button type="button" id="mail-btn" class="btn btn-light" style="border-color:#d9dde3">{ico("mail")}{t("f_mail")}</button>' if S.get('email') else ''
    mail_li=(f'<li><span class="ico">{ico("mail")}</span><div><small data-i18n="c_mail">Email</small><a href="mailto:{S["email"]}">{S["email"]}</a></div></li>' if S.get('email')
             else f'<li><span class="ico">{ico("mail")}</span><div><small data-i18n="c_mail">Email</small><span class="ph" data-i18n="c_nomail">Adresse email à ajouter</span></div></li>')
    wa_li=f'<li><span class="ico">{ico("wa")}</span><div><small data-i18n="c_wa">WhatsApp</small><a href="https://wa.me/{wa}" target="_blank" rel="noopener">{S["wa_disp"]}</a></div></li>'
    fb_li=f'<li><span class="ico">{ico("fb")}</span><div><small data-i18n="c_fb">Facebook</small><a href="https://{S["fb"]}" target="_blank" rel="noopener">{S["fb_disp"]}</a></div></li>' if S.get('fb') else ''
    extra=S.get('extra_section','')
    facts=''.join(f'<div class="fact"><b>{t(k+"_b","span")}</b><span data-i18n="{k}_s">{T[k+"_s"][0]}</span></div>' for k in S['facts'])
    spaces=''.join(f'<span>{t(k)}</span>' for k in S.get('spaces',[]))
    site={'slug':slug,'wa':wa,'email':S.get('email',''),'mailSubject':S['name']+' — demande de réservation','langs':['fr','en','it'],
          'formIntro':{'fr':f"Bonjour {S['name']}, je souhaite réserver :",'en':f"Hello {S['name']}, I would like to book:",'it':f"Buongiorno {S['name']}, vorrei prenotare:"}}
    h=f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(S['title'])}</title>
<meta name="description" content="{esc(S['desc'])}">
<meta name="robots" content="noindex,nofollow">
<meta name="theme-color" content="{S['theme']['accent']}">
<meta property="og:title" content="{esc(S['title'])}"><meta property="og:description" content="{esc(S['desc'])}"><meta property="og:image" content="img/hero.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{furl}" rel="stylesheet">
<link rel="stylesheet" href="site.css">
<style>:root{{--accent:{S['theme']['accent']};--accent-2:{S['theme']['accent2']};--accent-soft:{S['theme']['soft']};--bg:{S['theme']['bg']};--bg-alt:{S['theme']['bgalt']};--ink-strong:{S['theme']['ink']};--font-head:'{fam}',Georgia,serif;--font-body:'Inter',system-ui,sans-serif}}</style>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='{S['theme']['accent'].replace('#','%23')}'/%3E%3Ctext x='32' y='43' font-size='30' text-anchor='middle' fill='white' font-family='Georgia'%3E{S['mark']}%3C/text%3E%3C/svg%3E">
</head>
<body>
<div class="demo-ribbon" data-i18n="ribbon">{T['ribbon'][0]}</div>
<header class="site-header">
 <div class="container nav">
  <a class="brand" href="#top"><span class="brand-mark">{S['mark']}</span><span>{S['name']}<small data-i18n="tagline">{T['tagline'][0]}</small></span></a>
  <ul class="nav-links"><li><a href="#about" data-i18n="nav_about">{T['nav_about'][0]}</a></li><li><a href="#rooms" data-i18n="nav_rooms">{T['nav_rooms'][0]}</a></li><li><a href="#gallery" data-i18n="nav_gallery">{T['nav_gallery'][0]}</a></li><li><a href="#booking" data-i18n="nav_book">{T['nav_book'][0]}</a></li><li><a href="#location" data-i18n="nav_location">{T['nav_location'][0]}</a></li><li><a href="#contact" data-i18n="nav_contact">{T['nav_contact'][0]}</a></li></ul>
  <div class="nav-tools">
   <div class="lang" role="group" aria-label="Langue"><button type="button" data-lang="fr" aria-pressed="true">FR</button><button type="button" data-lang="en" aria-pressed="false">EN</button><button type="button" data-lang="it" aria-pressed="false">IT</button></div>
   <a class="btn btn-primary header-cta" href="#booking" data-i18n="cta_book">{T['cta_book'][0]}</a>
   <button class="menu-btn" type="button" aria-label="Menu" aria-expanded="false"><span></span></button>
  </div>
 </div>
 <nav class="mobile-menu container"><a href="#about" data-i18n="nav_about">{T['nav_about'][0]}</a><a href="#rooms" data-i18n="nav_rooms">{T['nav_rooms'][0]}</a><a href="#gallery" data-i18n="nav_gallery">{T['nav_gallery'][0]}</a><a href="#booking" data-i18n="nav_book">{T['nav_book'][0]}</a><a href="#location" data-i18n="nav_location">{T['nav_location'][0]}</a><a href="#contact" data-i18n="nav_contact">{T['nav_contact'][0]}</a></nav>
</header>
<main id="top">
<section class="hero">
 <img class="hero-bg" src="img/hero.jpg" alt="{esc(S['hero_alt'])}" fetchpriority="high">
 <div class="container">
  {t('hero_eyebrow','span','eyebrow')}
  {t('hero_h1','h1')}
  {t('hero_lead','p','lead')}
  <div class="hero-actions"><a class="btn btn-light" href="#booking">{ico('calendar')}<span data-i18n="cta_book">{T['cta_book'][0]}</span></a><a class="btn btn-wa" href="https://wa.me/{wa}?text={S['wa_text']}" target="_blank" rel="noopener">{ico('wa')}<span data-i18n="cta_wa">WhatsApp</span></a></div>
  <div class="facts">{facts}</div>
 </div>
</section>

<section class="section" id="about">
 <div class="container grid-2">
  <div class="reveal">
   {t('about_eyebrow','span','eyebrow')}
   {t('about_h2','h2')}
   {t('about_p1','p','lead')}
   {t('about_p2','p')}
   <div class="spaces">{spaces}</div>
  </div>
  <div class="about-img reveal"><img src="img/{S['about_img']}.jpg" alt="{esc(S['about_alt'])}" loading="lazy" width="800" height="1000"></div>
 </div>
</section>

<section class="section alt" id="rooms">
 <div class="container">
  <div class="center">{t('rooms_eyebrow','span','eyebrow')}{t('rooms_h2','h2')}{t('rooms_lead','p','lead')}</div>
  <div class="cards {S.get('rooms_cols','c4')}">{rooms}</div>
  {S.get('rooms_after','')}
  <p class="form-note center" style="margin-top:1.2rem" data-i18n="photo_note">{T['photo_note'][0]}</p>
 </div>
</section>

<section class="section">
 <div class="container">
  <div class="center">{t('feat_eyebrow','span','eyebrow')}{t('feat_h2','h2')}</div>
  <div class="features">{feats}</div>
 </div>
</section>
{extra}
<section class="section alt" id="gallery">
 <div class="container">
  <div class="center">{t('gal_eyebrow','span','eyebrow')}{t('gal_h2','h2')}{t('gal_lead','p','lead')}</div>
  <div class="gallery">{gal}</div>
 </div>
</section>

<section class="section" id="booking">
 <div class="container booking">
  <div class="reveal">
   {t('book_eyebrow','span','eyebrow')}{t('book_title','h2')}{t('book_lead','p','lead')}
   <ol class="steps"><li><span data-i18n="s1">{T['s1'][0]}</span></li><li><span data-i18n="s2">{T['s2'][0]}</span></li><li><span data-i18n="s3">{T['s3'][0]}</span></li></ol>
   {t('book_extra','div','notice')}
  </div>
  <form class="form reveal" id="req-form" novalidate>
   <label><span data-i18n="f_arr">Arrivée</span><input type="date" name="arrivee" required></label>
   <label><span data-i18n="f_dep">Départ</span><input type="date" name="depart" required></label>
   <label><span data-i18n="f_guests">Personnes</span><select name="personnes">{''.join(f'<option>{i}</option>' for i in range(1,S.get('max_guests',6)+1))}</select></label>
   <label><span data-i18n="f_room">Chambre souhaitée</span><select name="chambre"><option data-i18n="f_any">Peu importe / conseillez-moi</option>{opts}</select></label>
   <label class="full"><span data-i18n="f_name">Nom complet</span><input name="nom" autocomplete="name" required></label>
   <label class="full"><span data-i18n="f_phone">Téléphone / WhatsApp</span><input name="telephone" type="tel" autocomplete="tel" inputmode="tel" required></label>
   <label class="full"><span data-i18n="f_msg">Message (optionnel)</span><textarea name="message" data-i18n-ph="f_msg_ph" placeholder="{esc(T['f_msg_ph'][0])}"></textarea></label>
   <div class="form-actions full"><button class="btn btn-wa" type="submit">{ico('wa')}<span data-i18n="f_send">Envoyer sur WhatsApp</span></button>{mail_btn}</div>
   <p class="form-note full" data-i18n="f_note">{T['f_note'][0]}</p>
  </form>
 </div>
</section>

<section class="section alt" id="location">
 <div class="container grid-2">
  <div class="map-wrap reveal"><iframe title="Carte {esc(S['name'])}" src="https://maps.google.com/maps?q={S['map_q']}&z=15&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
  <div class="reveal" id="contact">
   {t('loc_eyebrow','span','eyebrow')}{t('loc_h2','h2')}{t('loc_p','p','lead')}
   <ul class="contact-list">
    <li><span class="ico">{ico('pin')}</span><div><small data-i18n="c_addr">Adresse</small><span>{S['address']}</span></div></li>
    <li><span class="ico">{ico('phone')}</span><div><small data-i18n="c_phone">Téléphone</small><a href="tel:{tel}">{S['tel_disp']}</a></div></li>
    {wa_li}{mail_li}{fb_li}
   </ul>
   <a class="btn btn-primary" href="https://www.google.com/maps/search/?api=1&query={S['map_q']}" target="_blank" rel="noopener">{ico('map')}<span data-i18n="loc_btn">{T['loc_btn'][0]}</span></a>
  </div>
 </div>
</section>
</main>

<footer class="site-footer">
 <div class="container">
  <div class="foot-grid">
   <div><h3>{S['name']}</h3><p data-i18n="tagline">{T['tagline'][0]}</p><p style="font-size:.8rem;opacity:.75" data-i18n="f_sub">{T['f_sub'][0]}</p></div>
   <div><h3 data-i18n="nav_contact">Contact</h3><p><a href="tel:{tel}">{S['tel_disp']}</a><br><a href="https://wa.me/{wa}" target="_blank" rel="noopener">WhatsApp {S['wa_disp']}</a>{'<br><a href="mailto:'+S['email']+'">'+S['email']+'</a>' if S.get('email') else ''}</p></div>
   <div><h3 data-i18n="nav_location">Accès</h3><p>{S['address']}</p></div>
  </div>
  <details><summary data-i18n="credits">Crédits photos</summary><ul>{credits_html(slug)}</ul></details>
  <p>© <span id="year">2026</span> {S['name']} · <a class="synaris-badge" href="https://github.com/islemyakoubi" target="_blank" rel="noopener"><i></i><span data-i18n="badge">Démo réalisée par Synaris Labs</span> · Menzel Temime</a></p>
 </div>
</footer>
<a class="wa-float" href="https://wa.me/{wa}?text={S['wa_text']}" target="_blank" rel="noopener" aria-label="WhatsApp">{ico('wa')}<span data-i18n="wa_float">Réponse sur WhatsApp</span></a>
<div class="lightbox" role="dialog" aria-modal="true"><button type="button" aria-label="Fermer">×</button><img alt=""></div>
<script>window.SITE={json.dumps(site,ensure_ascii=False)};window.I18N={json.dumps(I18N,ensure_ascii=False)};</script>
<script src="site.js" defer></script>
</body>
</html>'''
    os.makedirs(os.path.join(ROOT,slug),exist_ok=True); open(os.path.join(ROOT,slug,'index.html'),'w').write(h)
    copy_assets(slug)
    print('built',slug,len(h))
