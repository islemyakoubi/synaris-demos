# Dr Dorra Fenina, médecin dentiste (Hammamet) : « bento ». Menthe, blanc, sarcelle profonde. Hero en grille bento (titre, photo, horaires, téléphone, adresse, mer),
# italiques Lora en contrepoint d'Urbanist, cartes de soins indicatives, bande défilante, formulaire, carte. Urbanist + Lora. Informatif uniquement (CNOMDT).
import lux; K = lux.K; IC = lux.IC; ph = K.ph
FONTS = 'family=Urbanist:wght@300;400;500;600;700;800&family=Lora:ital,wght@1,400;1,500'
CSS = '''
:root{--bg:#EEF7F3;--fg:#0F3A38;--acc:#0F4C4A;--onacc:#fff;--line:rgba(15,58,56,.12);--hbg:rgba(238,247,243,.9);--disp:Urbanist,system-ui,sans-serif;--sans:Urbanist,system-ui,sans-serif;--r:18px;--mint:#BFE8D6;--mapbg:#DCEFE6;--rbg:#0F3A38}
h1,h2,h3{font-weight:700;letter-spacing:-.035em}em{font:italic 400 1em Lora,Georgia,serif;letter-spacing:-.01em;color:#1C8C7C}.brand .mono{width:44px;height:44px;border-radius:14px;display:grid;place-items:center;background:var(--mint);color:var(--acc)}.brand .mono svg{width:24px;height:24px}
.bento{display:grid;grid-template-columns:1.5fr 1fr 1fr;grid-template-rows:auto 220px;gap:1rem;padding:8.5rem 0 3rem}
.b{border-radius:28px;background:#fff;padding:2rem;position:relative;overflow:hidden;box-shadow:0 1px 0 var(--line)}.b small{display:block;font:700 .64rem/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.55;margin-bottom:.7rem}
.b.t{grid-row:span 2;display:flex;flex-direction:column;justify-content:flex-end;background:var(--acc);color:#fff;padding:3rem;min-height:600px}.b.t em{color:var(--mint)}
.b.t h1{font-size:clamp(3rem,6vw,6.2rem);line-height:.92}.b.t .lede{opacity:.85;max-width:30rem;margin:1.4rem 0 2rem}.b.t .btn.p{background:var(--mint);color:var(--acc)}.b.t .btn.o{color:#fff}.acts{display:flex;gap:.8rem;flex-wrap:wrap}
.b.t:before{content:'';position:absolute;right:-120px;top:-120px;width:380px;height:380px;border-radius:50%;border:1px solid rgba(191,232,214,.3);box-shadow:0 0 0 60px rgba(191,232,214,.05),0 0 0 120px rgba(191,232,214,.04)}
.b.p0{grid-column:span 2;padding:0;min-height:380px}.b.p0 img,.b.sea img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.6s var(--ease)}.b.p0:hover img{transform:scale(1.04)}
.b.p0 figcaption{position:absolute;left:1rem;bottom:1rem;background:#fff;border-radius:99px;padding:.35rem .8rem;font-size:.72rem}
.b.h{background:var(--mint)}.b.h p{margin:0;font:700 1.9rem/1.05 var(--disp)}.b.h .note{font-size:.72rem}
.b.sea{padding:0}.b.sea span{position:absolute;left:1.4rem;bottom:1.2rem;color:#fff;font:700 1.4rem var(--disp);text-shadow:0 2px 12px rgba(0,0,0,.35)}
.sec{padding:7rem 0}.sec h2{font-size:clamp(2.4rem,5vw,4.6rem);line-height:.98}
.care{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin-top:3.6rem}.care article{background:#fff;border-radius:28px;padding:2.2rem 1.8rem;transition:transform .6s var(--ease),box-shadow .6s}.care article:hover{transform:translateY(-8px);box-shadow:0 30px 60px rgba(15,58,56,.1)}
.care svg{width:60px;height:60px;color:#1C8C7C;margin-bottom:2.4rem}.care h3{font-size:1.45rem;margin-bottom:.5rem}.care p{opacity:.72;margin:0 0 1rem;font-size:.95rem}
.mq{background:var(--acc);color:var(--mint);padding:1.4rem 0;font:700 clamp(1.8rem,3.4vw,3rem)/1 var(--disp);--mqs:34s}.mq span:nth-child(even){font:italic 400 1em Lora,serif;color:#fff}
.two{display:grid;grid-template-columns:1fr 1fr;gap:1rem}.card{background:#fff;border-radius:28px;padding:2.6rem}.card h3{font-size:1.8rem;margin-bottom:1.2rem}
.dl{margin:0}.dl div{display:grid;grid-template-columns:10rem 1fr;gap:1rem;padding:.9rem 0;border-bottom:1px solid var(--line)}.dl dt{font:700 .62rem/1.7 var(--sans);letter-spacing:.2em;text-transform:uppercase;opacity:.55}.dl dd{margin:0}
.rdv{display:grid;grid-template-columns:.9fr 1.1fr;gap:1rem}.rdv .l{background:var(--mint);border-radius:28px;padding:3rem;display:flex;flex-direction:column;justify-content:space-between;overflow:hidden;position:relative}
.rdv .l figure{margin:2rem -3rem -3rem;height:260px;position:relative}.rdv .l img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.mapw{border-radius:28px}
@media(max-width:1020px){.bento{grid-template-columns:1fr 1fr;grid-template-rows:auto}.b.t{grid-column:span 2;grid-row:auto;min-height:0;padding-top:4rem}.b.p0{grid-column:span 2;min-height:300px}.care{grid-template-columns:1fr 1fr}.two,.rdv{grid-template-columns:1fr}}
@media(max-width:760px){.bento{grid-template-columns:1fr;padding-top:7.4rem}.b.t,.b.p0{grid-column:auto}.b.t{padding:2.2rem 1.6rem}.b.sea{min-height:180px}.care{grid-template-columns:1fr}.sec{padding:5rem 0}.card,.rdv .l{padding:1.8rem}.rdv .l figure{margin:2rem -1.8rem -1.8rem}.dl div{grid-template-columns:1fr;gap:.1rem}}
'''
def build(F, M):
    msg = 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet dentaire.'
    brand = f'<span class="mono">{IC["tooth"]}</span><span><b>Dr Dorra Fenina</b><small>Médecin dentiste · Hammamet</small></span>'
    links = [('Le cabinet', '#cabinet'), ('Soins', '#soins'), ('Horaires', '#horaires'), ('Accès', '#acces')]
    care = [('tooth', 'Consultation', 'Examen bucco-dentaire au cabinet, sur rendez-vous.'), ('shield', 'Prévention', 'L’hygiène bucco-dentaire et le suivi régulier.'), ('spark', 'Soins dentaires', 'Soins courants de médecine dentaire.'), ('doc', 'Autres actes', 'Liste des actes pratiqués au cabinet.')]
    ch = ''.join(f'<article data-rv style="--d:{i*.1:.1f}s">{IC[k]}<h3>{t}</h3><p>{p}</p>{ph()}</article>' for i, (k, t, p) in enumerate(care))
    mq = ''.join(f'<span>{w}</span>' for w in ['Médecine dentaire', 'Hammamet', 'Immeuble Émeraude', 'sur rendez-vous'] * 2)
    body = f'''{lux.header(brand, links)}<main id="main">
<section class="w bento" id="top"><div class="b t rise"><p class="kick" style="color:var(--mint)">Médecin dentiste · Hammamet</p><h1>Dr Dorra <em>Fenina</em></h1><p class="lede">Cabinet dentaire au 2e étage de l'immeuble Émeraude, avenue Habib Bourguiba, à Hammamet. Consultations sur rendez-vous.</p>
<div class="acts"><a class="btn p" href="#rdv">Prendre rendez-vous {IC['arrow']}</a><a class="btn o" href="{K.telhref(F['tel'])}">{K.I['phone']}{F['tel']}</a></div></div>
<figure class="b p0 rise d1" style="margin:0">{M.img('hero', 'Fauteuil dentaire (photo d’illustration)', sizes='(max-width: 760px) 100vw, 50vw', lazy=False)}<figcaption>Illustration · ne montre pas le cabinet</figcaption></figure>
<div class="b h rise d2"><small>Mercredi</small><p>{F['wed']}</p><p class="note">Autres jours à confirmer</p></div>
<figure class="b sea rise d3" style="margin:0">{M.img('mer', 'Mer à Hammamet (photo d’illustration)', sizes='(max-width: 760px) 100vw, 25vw')}<span>Hammamet</span></figure></section>
<div class="mq" aria-hidden="true"><div>{mq}{mq}</div></div>
<section class="sec" id="soins"><div class="w"><p class="kick" data-rv>Soins</p><h2 data-rv>La médecine dentaire, <em>au quotidien</em>.</h2><div class="care">{ch}</div>
<p class="note" data-rv style="margin-top:2rem">Présentation générale, à titre informatif. Les actes pratiqués sont à confirmer par le cabinet avant publication.</p></div></section>
<section class="sec" id="cabinet" style="padding-top:0"><div class="w two"><figure class="b" data-rv style="margin:0;padding:0;min-height:460px">{M.img('unit', 'Unit dentaire (photo d’illustration)', sizes='(max-width: 1020px) 92vw, 600px', extra=' style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"')}</figure>
<div class="card" data-rv style="--d:.1s"><h3>Fiche du cabinet</h3><dl class="dl"><div><dt>Praticienne</dt><dd>Dr Dorra Fenina</dd></div><div><dt>Exercice</dt><dd>Médecine dentaire</dd></div><div><dt>Qualification</dt><dd>{ph()}</dd></div><div><dt>Adresse</dt><dd>{F['addr']}</dd></div></dl></div></div></section>
<section class="sec" id="horaires" style="padding-top:0"><div class="w two"><div class="card" data-rv><h3>Horaires</h3>{lux.hours(F)}</div><div class="card" data-rv style="--d:.1s"><h3>Contact</h3>{lux.contacts(F, wa_msg=msg)}</div></div></section>
<section class="sec" id="rdv" style="padding-top:0"><div class="w rdv"><div class="l" data-rv><div><p class="kick">Rendez-vous</p><h2>Demander un <em>rendez-vous</em></h2><p style="margin-top:1.2rem;opacity:.8">Le message s'ouvre dans WhatsApp ; le cabinet confirme le créneau.</p></div>
<figure>{M.img('sonde', 'Instrument dentaire (photo d’illustration)', sizes='(max-width: 1020px) 92vw, 520px')}</figure></div><div class="card" data-rv style="--d:.1s">{lux.form(F, 'Bonjour Docteur, je souhaite un rendez-vous au cabinet dentaire.', lux.MED_FORM)}</div></div></section>
<section class="sec" id="acces" style="padding-top:0;padding-bottom:4rem"><div class="w"><p class="kick" data-rv>Accès</p><h2 data-rv style="margin-bottom:1rem">Immeuble <em>Émeraude</em>.</h2><p data-rv>{F['addr']}. <a href="{F['maps']}" target="_blank" rel="noopener" style="color:#1C8C7C;text-decoration:underline">Ouvrir dans Google Maps</a></p>{lux.mapblock(F)}</div></section>
</main>{lux.footer(F, M, brand, links)}{lux.dock(F)}'''
    return lux.page(F, 'Dr Dorra Fenina · Médecin dentiste à Hammamet (démo)', 'Cabinet dentaire du Dr Dorra Fenina, immeuble Émeraude, Hammamet : coordonnées, horaires et demande de rendez-vous.', FONTS, CSS, body, '#EEF7F3', lux.fav('#0F4C4A', '#BFE8D6', 'DF', 'Arial', 'rect'))
