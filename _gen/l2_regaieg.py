# Dr Hamadi Regaieg, ophtalmologue (Hammamet) : page bilingue en miroir FR | AR (colonne arabe RTL), hero « iris » en cercles concentriques CSS autour de la photo.
# Noto Serif + Noto Naskh Arabic ; bleu nuit / turquoise iris / ivoire.
import gen_lot2 as K
FONTS = 'family=Noto+Serif:wght@400;600&family=Noto+Naskh+Arabic:wght@400;600;700&family=Noto+Sans:wght@400;600'
CSS = '''
:root{--nv:#14213D;--tq:#1B9AAA;--iv:#FBF8F1;--mut:#5d6778;--line:#e4e0d4;--gold:#C8A04A}
body{background:var(--iv);color:var(--nv);font:400 1rem/1.7 'Noto Sans',system-ui,sans-serif}h1,h2,h3{font-family:'Noto Serif',serif;font-weight:600;line-height:1.1;margin:0 0 .5rem}
[lang=ar]{font-family:'Noto Naskh Arabic',serif;line-height:1.9}[lang=ar] h1,[lang=ar] h2,[lang=ar] h3{font-family:'Noto Naskh Arabic',serif;font-weight:700}
.w{width:min(1120px,100% - 2rem);margin-inline:auto}.ph{font:600 .72rem/1 'Noto Sans';color:var(--tq);background:#e0f2f4;border-radius:4px;padding:.2rem .45rem;white-space:nowrap}
.rb{background:var(--nv);color:#b9c1d6;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:#fff}
.hd{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;padding:1.1rem 0;border-bottom:1px solid var(--line)}.hd .fr{font:600 1.05rem 'Noto Serif'}.hd .ar{justify-self:end;font-size:1.15rem}.hd .c{display:flex;gap:.4rem}
.bt{display:inline-flex;gap:.5rem;align-items:center;background:var(--nv);color:#fff;text-decoration:none;font-weight:600;padding:.75rem 1.1rem;border-radius:99px}.bt svg{width:18px}.bt.t{background:var(--tq)}
.hero{display:grid;gap:2rem;padding:3rem 0;align-items:center;text-align:center}.iris{position:relative;width:min(380px,80vw);aspect-ratio:1;margin:0 auto;border-radius:50%;
background:repeating-radial-gradient(circle,transparent 0 18px,rgba(27,154,170,.14) 18px 19px);display:grid;place-items:center}
.iris:before{content:'';position:absolute;inset:8%;border-radius:50%;border:2px solid var(--tq);opacity:.5}.iris:after{content:'';position:absolute;inset:-4%;border-radius:50%;border:1px dashed var(--gold)}
.iris img{width:62%;aspect-ratio:1;border-radius:50%;object-fit:cover;box-shadow:0 0 0 10px var(--iv),0 0 0 12px var(--nv)}
.side h1{font-size:clamp(2rem,4vw,3rem)}.side .k{font-size:.8rem;letter-spacing:.18em;text-transform:uppercase;color:var(--tq);font-weight:600}.side[lang=ar] .k{letter-spacing:0;font-size:1rem}.side p{color:var(--mut)}
.mir{display:grid;gap:0;border-top:1px solid var(--line)}.row{display:grid;gap:1rem;padding:2.2rem 0;border-bottom:1px solid var(--line)}.row .lab{font:600 .78rem 'Noto Sans';letter-spacing:.2em;color:var(--gold);text-transform:uppercase;text-align:center}
.col h2{font-size:1.6rem}.col[lang=ar]{text-align:right}.tb{width:100%;border-collapse:collapse}.tb td{padding:.45rem 0;border-bottom:1px dotted var(--line)}.tb td+td{text-align:end}.tb .today td{color:var(--tq);font-weight:600}
.pics{display:grid;grid-template-columns:1fr 1fr;gap:1rem;padding:2.5rem 0}.pics img{width:100%;aspect-ratio:3/2;object-fit:cover;border-radius:10px}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}.form label{display:grid;gap:.3rem;font-weight:600;font-size:.84rem}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;border:1px solid var(--line);border-radius:10px;padding:.7rem;min-height:46px;width:100%;background:#fff}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--tq);color:#fff;border:0;border-radius:99px;padding:1rem;font:600 1rem 'Noto Sans';cursor:pointer}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.76rem;color:var(--mut);margin:0}.map{height:340px;border-radius:12px;overflow:hidden;margin:2rem 0}.note{font-size:.8rem;color:var(--mut)}.ft{padding:1rem 0 3rem;font-size:.82rem;color:var(--mut)}
@media(min-width:880px){.hero{grid-template-columns:1fr auto 1fr}.side[lang=fr]{text-align:left}.side[lang=ar]{text-align:right}.row{grid-template-columns:1fr 140px 1fr;align-items:start}.row .lab{padding-top:.5rem}}
@media(max-width:600px){.hd{grid-template-columns:1fr 1fr}.hd .c{display:none}}
'''
AR_DAYS = ['الاثنين', 'الثلاثاء', 'الأربعاء', 'الخميس', 'الجمعة', 'السبت', 'الأحد']
def build(F, M):
    H = K.hours(F)
    hfr = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else K.ph()}</td></tr>' for n, d, v, k in H)
    har = ''.join(f'<tr data-d="{n}"><td>{AR_DAYS[n - 1]}</td><td>{"إلى الساعة 17:30" if k else K.ph("للتأكيد")}</td></tr>' for n, d, v, k in H)
    wa = K.walink(F['wa'], 'Bonjour Docteur, je souhaite prendre rendez-vous en ophtalmologie. / مرحبا، أرغب في حجز موعد.')
    tel = f'<a href="{K.telhref(F["tel"])}" dir="ltr">{F["tel"]}</a>'
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<header class="w hd"><span class="fr">Dr Hamadi Regaieg</span><span class="c"><a class="bt" href="{K.telhref(F['tel'])}">{K.I['phone']}Appeler · اتصل</a></span><span class="ar" lang="ar" dir="rtl">{F['ar']}</span></header>
<main id="main" class="w"><section class="hero"><div class="side" lang="fr"><p class="k">Ophtalmologie · Hammamet</p><h1>Dr Hamadi Regaieg</h1><p>Médecin ophtalmologue à Hammamet. Consultations sur rendez-vous.</p><a class="bt t" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}Rendez-vous WhatsApp</a></div>
<div class="iris">{M.img('hero', 'Iris d’un œil humain (photo d’illustration)', sizes='240px', lazy=False)}</div>
<div class="side" lang="ar" dir="rtl"><p class="k">طب العيون · الحمامات</p><h1>{F['ar']}</h1><p>طبيب مختص في أمراض العيون بالحمامات. الاستشارة بموعد مسبق.</p><a class="bt t" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}موعد عبر واتساب</a></div></section>
<div class="mir"><div class="row"><div class="col" lang="fr"><h2>Le cabinet</h2><p>{F['sector']}<br>{F['addr']}<br>Tél. {tel}<br>N° d'Ordre : {K.ph()} · Langues : {K.ph()} · CNAM : {K.ph()}</p></div><p class="lab">Cabinet</p>
<div class="col" lang="ar" dir="rtl"><h2>العيادة</h2><p>طبيب مختص في أمراض العيون<br>الحمامات — العنوان الدقيق : {K.ph('للتأكيد')}<br>الهاتف : {tel}<br>رقم التسجيل بالهيئة : {K.ph('للتأكيد')} · الكنام : {K.ph('للتأكيد')}</p></div></div>
<div class="row"><div class="col" lang="fr"><h2>Horaires</h2><table class="tb">{hfr}</table><p class="note">{K.HOURS_NOTE}</p></div><p class="lab">Horaires</p>
<div class="col" lang="ar" dir="rtl"><h2>أوقات العمل</h2><table class="tb">{har}</table><p class="note">حسب بطاقة Google بتاريخ 30/09/2026. بقية الأوقات للتأكيد مع العيادة.</p></div></div>
<div class="row"><div class="col" lang="fr"><h2>Avant la consultation</h2><p>Apportez votre carte CNAM ou d'assurance, vos lunettes ou lentilles actuelles et vos ordonnances ou comptes rendus récents.</p></div><p class="lab">Conseils</p>
<div class="col" lang="ar" dir="rtl"><h2>قبل الاستشارة</h2><p>يُرجى إحضار بطاقة الكنام أو التأمين، والنظارات أو العدسات الحالية، والوصفات أو التقارير الطبية الحديثة.</p></div></div>
<div class="row" id="rdv"><div class="col" lang="fr"><h2>Demande de rendez-vous</h2>{K.form(F, 'Bonjour, je souhaite un rendez-vous chez le Dr Hamadi Regaieg (ophtalmologie) :', K.MED_FORM, 'Envoyer sur WhatsApp')}</div><p class="lab">Rendez-vous</p>
<div class="col" lang="ar" dir="rtl"><h2>حجز موعد</h2><p>اتصلوا بالعيادة على الرقم {tel} أو أرسلوا رسالة عبر واتساب. تؤكد العيادة موعدكم.</p><p><a class="bt" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}واتساب</a></p><p class="note">في حالة الطوارئ : 190</p></div></div></div>
<div class="pics">{M.img('refracteur', 'Réfracteur dans un cabinet d’ophtalmologie (photo d’illustration)', sizes='(max-width: 880px) 50vw, 540px')}{M.img('fort', 'Le fort de Hammamet (photo d’illustration)', sizes='(max-width: 880px) 50vw, 540px')}</div>
<div class="map">{K.mapframe(F)}</div><p style="text-align:center"><a class="bt" href="{F['maps']}" target="_blank" rel="noopener">{K.I['pin']}Itinéraire · الاتجاهات</a></p></main>
<footer class="ft w">{M.credits()}{K.footer_legal(F)}</footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' fill='#FBF8F1'/><circle cx='32' cy='32' r='26' fill='none' stroke='#14213D' stroke-width='4'/><circle cx='32' cy='32' r='15' fill='#1B9AAA'/><circle cx='32' cy='32' r='6' fill='#14213D'/></svg>"
    return K.page(F, 'Dr Hamadi Regaieg — Ophtalmologue à Hammamet | طبيب عيون الحمامات (démo)', 'Cabinet d’ophtalmologie du Dr Hamadi Regaieg à Hammamet : informations en français et en arabe, horaires, accès et rendez-vous.', FONTS, CSS, body, '#14213D', fav)
