import sys; import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from gen_guest import build
from urllib.parse import quote

# ---------------- L'HIRONDELLE ----------------
hir = dict(slug='hirondelle-kelibia', name="L'Hirondelle de Kélibia", mark='H', font='fraunces',
 title="L'Hirondelle de Kélibia — Chez Amou · Maison d'hôtes & restaurant (démo)",
 desc="Maison d'hôtes et restaurant en bord de mer à Kélibia (Aïn Grenz) : 7 suites climatisées, patio à arcades, cuisine maison. Réservation directe.",
 theme=dict(accent='#1d5fa6',accent2='#ffc15e',soft='#e3edf8',bg='#f8fafc',bgalt='#eef3f8',ink='#0d1b2e'),
 wa='21696194187', tel='+21623105706', tel_disp='+216 23 105 706', wa_disp='+216 96 194 187',
 email='hirondelledekelibia@gmail.com',
 wa_text=quote("Bonjour L'Hirondelle (Chez Amou), je souhaite des informations pour un séjour."),
 address="Avenue de l'Environnement (Aïn Grenz), 8090 Kélibia, Tunisie",
 map_q=quote("L'Hirondelle de Kelibia Chez Amou, Ain Grenz, Kelibia"),
 hero_alt="Vue sur la mer et le port de Kélibia depuis le fort", about_img='patio', about_alt="Patio tunisien (photo d'ambiance)",
 facts=['fa','fb','fc','fd'], max_guests=8, spaces=['sp1','sp2','sp3','sp4'],
 rooms=[
  dict(k='r1',img='door',alt='Suite classique (ambiance)',price='170 DT',tags=['tg_2ch','tg_ac','tg_fridge']),
  dict(k='r2',img='suite',alt='Grande suite (ambiance)',price='— DT',tags=['tg_2ch','tg_salon','tg_bath']),
 ],
 rooms_cols='',
 features=[('waves','ft1'),('food','ft2'),('coffee','ft3'),('snow','ft4'),('key','ft5'),('home','ft6'),('chat','ft7'),('map','ft8')],
 gallery=[('g1','Barques au port de Kélibia'),('hero','Mer et fort de Kélibia'),('g2','Port de Kélibia vu du fort'),('g3','Fort de Kélibia'),('g4','Plage au coucher du soleil'),('fish','Sardines grillées'),('couscous','Couscous aux sardines'),('sweets','Pâtisseries tunisiennes'),('g5','Kélibia et son port')],
 extra_section='',
 t={
  'tagline':("Chez Amou · Maison d'hôtes & restaurant","Chez Amou · Guesthouse & restaurant","Chez Amou · Casa vacanze & ristorante"),
  'nav_rooms':('Suites','Suites','Suite'),
  'hero_eyebrow':("Maison d'hôtes & restaurant · Kélibia, Cap Bon","Guesthouse & restaurant · Kélibia, Cap Bon","Casa vacanze & ristorante · Kélibia, Cap Bon"),
  'hero_h1':("L'Hirondelle de Kélibia, chez Amou","L'Hirondelle de Kélibia, at Amou's","L'Hirondelle de Kélibia, da Amou"),
  'hero_lead':("Une demeure familiale typiquement tunisienne en bord de mer : suites climatisées pour 4 personnes, patio à arcades et restaurant maison.",
               "A typical Tunisian family home by the sea: air-conditioned suites for up to 4, an arcaded patio and a home-style restaurant.",
               "Una tipica casa di famiglia tunisina sul mare: suite climatizzate fino a 4 persone, patio con archi e ristorante casalingo."),
  'fa_b':('7 suites','7 suites','7 suite'),'fa_s':('climatisées','air-conditioned','climatizzate'),
  'fb_b':('4 pers.','4 guests','4 ospiti'),'fb_s':('par suite, 2 chambres','per suite, 2 bedrooms','per suite, 2 camere'),
  'fc_b':('dès 170 DT','from 170 TND','da 170 TND'),'fc_s':('par suite / nuit*','per suite / night*','per suite / notte*'),
  'fd_b':('Restaurant','Restaurant','Ristorante'),'fd_s':('sur place','on site','in loco'),
  'about_eyebrow':('La maison','The house','La casa'),
  'about_h2':('Comme à la maison, au bord de la mer','Like home, by the sea','Come a casa, sul mare'),
  'about_p1':("L'Hirondelle est une maison familiale tunisienne qui propose des suites à louer en bord de mer, à Aïn Grenz.",
              "L'Hirondelle is a Tunisian family house offering seaside suites in Aïn Grenz.",
              "L'Hirondelle è una casa di famiglia tunisina che offre suite sul mare ad Aïn Grenz."),
  'about_p2':("Les hébergements sont à l'étage, desservis par une entrée indépendante et un joli patio avec arcades. Au rez-de-chaussée, le restaurant accueille petits-déjeuners et repas.",
              "The suites are upstairs, with an independent entrance and a pretty arcaded patio. Downstairs, the restaurant serves breakfast and meals.",
              "Le suite sono al piano superiore, con ingresso indipendente e un bel patio con archi. Al piano terra il ristorante serve colazioni e pasti."),
  'sp1':('Entrée indépendante','Private entrance','Ingresso indipendente'),'sp2':('Patio à arcades','Arcaded patio','Patio con archi'),'sp3':('Restaurant','Restaurant','Ristorante'),'sp4':('Bord de mer','Seafront','Fronte mare'),
  'rooms_eyebrow':('Les suites','The suites','Le suite'),
  'rooms_h2':('Deux formules, jusqu\'à 4 personnes','Two options, up to 4 guests','Due soluzioni, fino a 4 ospiti'),
  'rooms_lead':("Toutes climatisées, sans cuisine. Tarif par suite et par nuitée (max 4 personnes), hors repas.",
                "All air-conditioned, no kitchen. Rate per suite per night (max 4 guests), meals not included.",
                "Tutte climatizzate, senza cucina. Tariffa per suite a notte (max 4 ospiti), pasti esclusi."),
  'r1_n':('Suite classique (×6)','Classic suite (×6)','Suite classica (×6)'),
  'r1_d':('2 chambres séparées avec lits doubles, réfrigérateur, salle de douche et WC.','2 separate bedrooms with double beds, fridge, shower room and WC.','2 camere separate con letto matrimoniale, frigo, doccia e WC.'),
  'r2_n':('Grande suite','Grand suite','Grande suite'),
  'r2_d':('2 chambres doubles, grand salon TV privé avec balcon, salle de bain avec baignoire.','2 double bedrooms, large private TV lounge with balcony, bathroom with bathtub.','2 camere matrimoniali, ampio salotto TV privato con balcone, bagno con vasca.'),
  'tg_2ch':('2 chambres','2 bedrooms','2 camere'),'tg_ac':('Climatisation','Air-con','Aria condizionata'),'tg_fridge':('Frigo','Fridge','Frigo'),
  'tg_salon':('Salon + balcon','Lounge + balcony','Salotto + balcone'),'tg_bath':('Baignoire','Bathtub','Vasca'),
  'feat_eyebrow':('Services','Services','Servizi'),'feat_h2':('Simple, familial, pratique','Simple, friendly, practical','Semplice, familiare, pratico'),
  'ft1_t':('Bord de mer','Seafront','Fronte mare'),'ft1_d':("Plages d'Aïn Grenz.","Aïn Grenz beaches.","Spiagge di Aïn Grenz."),
  'ft2_t':('Restaurant maison','Home restaurant','Ristorante casalingo'),'ft2_d':('Repas sur réservation.','Meals on request.','Pasti su prenotazione.'),
  'ft3_t':('Petit-déjeuner','Breakfast','Colazione'),'ft3_d':('Dès 13 DT, sur réservation <span class="ph">à confirmer</span>','From 13 TND, on request <span class="ph">to be confirmed</span>','Da 13 TND, su prenotazione <span class="ph">da confermare</span>'),
  'ft4_t':('Climatisation','Air-con','Aria condizionata'),'ft4_d':('Dans toutes les suites.','In every suite.','In tutte le suite.'),
  'ft5_t':('Entrée indépendante','Private entrance','Ingresso indipendente'),'ft5_d':('Liberté totale.','Total freedom.','Massima libertà.'),
  'ft6_t':('Idéal familles','Great for families','Ideale per famiglie'),'ft6_d':('2 chambres par suite.','2 bedrooms per suite.','2 camere per suite.'),
  'ft7_t':('WhatsApp','WhatsApp','WhatsApp'),'ft7_d':('Réponse en FR/EN/IT <span class="ph">assistant option</span>','Replies in FR/EN/IT <span class="ph">assistant option</span>','Risposte in FR/EN/IT <span class="ph">opzione</span>'),
  'ft8_t':('Kélibia','Kélibia','Kélibia'),'ft8_d':('Fort, port, plages de Mansoura.','Fort, port, Mansoura beaches.','Forte, porto, spiagge di Mansoura.'),
  'gal_h2':('Kélibia, ses barques et ses saveurs','Kélibia, its boats and flavours','Kélibia, le sue barche e i suoi sapori'),
  'gal_lead':("Port de pêche, fort et cuisine de la mer. <span class=\"ph\">Photos d'ambiance — à remplacer par vos photos et vos plats</span>","Fishing port, fort and seafood. <span class=\"ph\">Mood photos — to be replaced with your photos and dishes</span>","Porto, forte e cucina di mare. <span class=\"ph\">Foto d'atmosfera — da sostituire</span>"),
  'book_extra':("* Tarif « à partir de 170 DT (≈ 55 €) par suite et par nuit » repris de votre site actuel <span class=\"ph\">à confirmer pour 2027</span>. Demande aussi possible par email.",
                "* “From 170 TND (≈ €55) per suite per night” taken from your current site <span class=\"ph\">to be confirmed for 2027</span>. Requests by email also possible.",
                "* “Da 170 TND (≈ 55 €) per suite a notte” ripreso dal vostro sito attuale <span class=\"ph\">da confermare per il 2027</span>. Richieste anche via email."),
  'loc_h2':('À Aïn Grenz, Kélibia','In Aïn Grenz, Kélibia','Ad Aïn Grenz, Kélibia'),
  'loc_p':("Avenue de l'Environnement, quartier d'Aïn Grenz, à Kélibia. Environ 1h45 de Tunis.","Avenue de l'Environnement, Aïn Grenz area, Kélibia. About 1h45 from Tunis.","Avenue de l'Environnement, zona Aïn Grenz, Kélibia. Circa 1h45 da Tunisi."),
  'loc_btn':('Itinéraire Google Maps','Directions on Google Maps','Indicazioni su Google Maps'),
 })

# restaurant section for Hirondelle
hir['extra_section'] = '''<section class="section alt" id="restaurant"><div class="container grid-2">
<div class="about-img reveal" style="aspect-ratio:4/3"><img src="img/fish2.jpg" alt="Poisson grillé (photo d'ambiance)" loading="lazy"></div>
<div class="reveal"><span class="eyebrow" data-i18n="rest_e">Le restaurant</span><h2 data-i18n="rest_h">La table de Chez Amou</h2><p class="lead" data-i18n="rest_p">Petits-déjeuners et repas servis sur place, pour les hôtes de la maison comme pour les gourmands de passage.</p>
<ul class="menu-list"><li><b data-i18n="m1">Petit-déjeuner</b><span data-i18n="m1p">dès 13 DT</span></li><li><b data-i18n="m2">Poisson du jour</b><span class="ph" data-i18n="ph">à confirmer</span></li><li><b data-i18n="m3">Plat tunisien maison</b><span class="ph" data-i18n="ph">à confirmer</span></li><li><b data-i18n="m4">Dessert maison</b><span class="ph" data-i18n="ph">à confirmer</span></li></ul>
<p class="form-note" style="margin-top:.8rem" data-i18n="m_note">Exemple de carte : à remplacer par votre menu réel. Menu QR et commande WhatsApp activables.</p></div></div></section>'''
hir['t'].update({
 'rest_e':('Le restaurant','The restaurant','Il ristorante'),'rest_h':('La table de Chez Amou','The Chez Amou table','La tavola di Chez Amou'),
 'rest_p':("Petits-déjeuners et repas servis sur place, pour les hôtes de la maison comme pour les gourmands de passage.","Breakfast and meals served on site, for guests and passing food lovers alike.","Colazioni e pasti serviti in loco, per gli ospiti e per i buongustai di passaggio."),
 'm1':('Petit-déjeuner','Breakfast','Colazione'),'m1p':('dès 13 DT','from 13 TND','da 13 TND'),
 'm2':('Poisson du jour','Catch of the day','Pesce del giorno'),'m3':('Plat tunisien maison','Home-made Tunisian dish','Piatto tunisino fatto in casa'),'m4':('Dessert maison','Home-made dessert','Dolce fatto in casa'),
 'm_note':("Exemple de carte : à remplacer par votre menu réel. Menu QR et commande WhatsApp activables.","Sample menu: to be replaced with your real menu. QR menu and WhatsApp ordering available.","Menu di esempio: da sostituire con il vostro menu reale. Menu QR e ordini WhatsApp attivabili."),
})
for S in (hir,): build(S)
