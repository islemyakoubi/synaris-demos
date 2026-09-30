# Dr Ichrak Hammami, médecin dentiste (Nabeul) : page « questions pratiques ». Hero typographique en colonne étroite, bloc de réponses rapides, accordéons <details> (pratique uniquement, aucun contenu médical).
# Young Serif + Albert Sans ; olive / crème citron.
import gen_lot2 as K
FONTS = 'family=Young+Serif&family=Albert+Sans:wght@400;600;800'
CSS = '''
:root{--ol:#4A5A1F;--lem:#FBF7DF;--ink:#23261a;--mut:#666b55;--line:#e3dfbf;--acc:#C9D65A}
body{background:var(--lem);color:var(--ink);font:400 1.02rem/1.7 'Albert Sans',system-ui,sans-serif}h1,h2,h3{font-family:'Young Serif',serif;font-weight:400;line-height:1.1;margin:0 0 .6rem}
.w{width:min(860px,100% - 2.4rem);margin-inline:auto}.ph{font:600 .72rem/1 'Albert Sans';color:var(--ol);background:#eef0cf;border-radius:99px;padding:.2rem .5rem;white-space:nowrap}
.rb{background:var(--ol);color:#e6eac4;font-size:.74rem;text-align:center;padding:.4rem 1rem}.rb b{color:#fff}
.hd{display:flex;justify-content:space-between;align-items:center;padding:1.2rem 0}.lg{font:1.2rem 'Young Serif';text-decoration:none}.lg i{font-style:normal;color:var(--ol)}
.bt{display:inline-flex;gap:.5rem;align-items:center;background:var(--ol);color:#fff;text-decoration:none;font-weight:800;padding:.8rem 1.15rem;border-radius:99px}.bt svg{width:18px}.bt.o{background:transparent;color:var(--ol);box-shadow:inset 0 0 0 2px var(--ol)}
.hero{padding:3rem 0 2rem;text-align:center}.hero h1{font-size:clamp(2.6rem,7vw,4.6rem)}.hero h1 span{display:block;font-size:.42em;color:var(--ol);margin-top:.6rem}.hero p{color:var(--mut);max-width:34rem;margin:0 auto 1.4rem}
.acts{display:flex;gap:.6rem;justify-content:center;flex-wrap:wrap}.pic{margin:2.5rem 0;border-radius:200px 200px 24px 24px;overflow:hidden;aspect-ratio:16/9}.pic img{width:100%;height:100%;object-fit:cover}
.qa{display:grid;grid-template-columns:repeat(2,1fr);gap:.7rem;margin:0 0 3rem}.qa div{background:#fff;border-radius:18px;padding:1rem 1.1rem;border:1px solid var(--line)}.qa small{display:block;color:var(--mut);font-size:.74rem;text-transform:uppercase;letter-spacing:.12em}.qa b{font-size:1.05rem}
.faq h2{font-size:clamp(2rem,5vw,2.8rem);color:var(--ol)}.faq details{background:#fff;border-radius:18px;margin:.6rem 0;border:1px solid var(--line)}
.faq summary{cursor:pointer;list-style:none;padding:1.1rem 3rem 1.1rem 1.2rem;font-weight:800;font-size:1.08rem;position:relative}.faq summary::-webkit-details-marker{display:none}
.faq summary:after{content:'+';position:absolute;right:1.1rem;top:50%;transform:translateY(-50%);width:28px;height:28px;border-radius:50%;background:var(--acc);display:grid;place-items:center;font-size:1.2rem;line-height:28px;text-align:center}
.faq details[open] summary:after{content:'−'}.faq .in{padding:0 1.2rem 1.2rem}.tb{width:100%;border-collapse:collapse}.tb td{padding:.5rem 0;border-bottom:1px dashed var(--line)}.tb td+td{text-align:right}.tb .today td{font-weight:800;color:var(--ol)}
.form{display:grid;grid-template-columns:1fr 1fr;gap:.7rem}.form label{display:grid;gap:.25rem;font-weight:600;font-size:.84rem}.form .full{grid-column:1/-1}
.form input,.form select,.form textarea{font:inherit;border:1.5px solid var(--line);border-radius:12px;padding:.7rem;min-height:46px;width:100%;background:var(--lem)}
.form button{grid-column:1/-1;display:flex;gap:.5rem;justify-content:center;align-items:center;background:var(--ol);color:#fff;border:0;border-radius:99px;padding:.95rem;font:800 1rem 'Albert Sans';cursor:pointer}.form button svg{width:20px}
.fnote{grid-column:1/-1;font-size:.76rem;color:var(--mut);margin:0}.map{height:300px;border-radius:14px;overflow:hidden;margin-top:.8rem}.note{font-size:.8rem;color:var(--mut)}
.city{display:grid;grid-template-columns:120px 1fr;gap:1rem;align-items:center;margin:3rem 0}.city img{width:120px;height:120px;border-radius:50%;object-fit:cover}.ft{padding:1rem 0 3rem;font-size:.82rem;color:var(--mut)}
@media(max-width:560px){.qa{grid-template-columns:1fr}.hd .bt{display:none}}
'''
def build(F, M):
    hrs = ''.join(f'<tr data-d="{n}"><td>{d}</td><td>{v if k else K.ph()}</td></tr>' for n, d, v, k in K.hours(F))
    wa = K.walink(F['wa'], 'Bonjour Docteur, je souhaite prendre rendez-vous au cabinet.')
    def q(t, inner, op=False): return f'<details{" open" if op else ""}><summary>{t}</summary><div class="in">{inner}</div></details>'
    faq = ''.join([
        q('Comment prendre rendez-vous ?', f'<p>Par téléphone au <a href="{K.telhref(F["tel"])}">{F["tel"]}</a>, ou en envoyant le formulaire ci-dessous : il ouvre WhatsApp avec votre demande. Le cabinet vous confirme le jour et l\'heure.</p>{K.form(F, "Bonjour, je souhaite prendre rendez-vous au cabinet du Dr Ichrak Hammami :", K.MED_FORM, "Envoyer sur WhatsApp")}', True),
        q('Quels sont les horaires ?', f'<table class="tb">{hrs}</table><p class="note">{K.HOURS_NOTE}</p>'),
        q('Où se trouve le cabinet ?', f'<p>{F["addr"]}</p>{K.mapframe(F)}<p><a class="bt o" href="{F["maps"]}" target="_blank" rel="noopener">{K.I["pin"]}Ouvrir l\'itinéraire</a></p>'),
        q('Que faut-il apporter ?', '<p>Votre pièce d\'identité, votre carte CNAM ou d\'assurance si vous en avez une, et vos radiographies ou ordonnances récentes s\'il y en a.</p>'),
        q('Le cabinet accepte-t-il la CNAM ?', f'<p>Conventionnement CNAM et assurances : {K.ph()}. Posez la question au cabinet lors de la prise de rendez-vous.</p>'),
        q('Quelles langues sont parlées ?', f'<p>Langues de consultation : {K.ph()}.</p>'),
        q('En cas de douleur ou d\'urgence ?', '<p>Appelez d\'abord le cabinet. En cas d\'urgence vitale, composez le 190 (SAMU).</p>'),
    ])
    body = f'''<a class="skip" href="#main">Aller au contenu</a><div class="rb">{K.RIBBON}</div>
<header class="w hd"><a class="lg" href="#top">Dr Ichrak <i>Hammami</i></a><a class="bt" href="{K.telhref(F['tel'])}">{K.I['phone']}Appeler</a></header>
<main id="main" class="w"><section class="hero" id="top"><h1>Cabinet dentaire à Nabeul<span>Dr Ichrak Hammami · {F['sector']}</span></h1><p>Les réponses aux questions pratiques avant votre visite : rendez-vous, horaires, accès et documents à apporter.</p>
<div class="acts"><a class="bt" href="{wa}" target="_blank" rel="noopener">{K.I['wa']}WhatsApp</a><a class="bt o" href="#faq">{K.I['cal']}Questions pratiques</a></div>
<div class="pic">{M.img('hero', 'Poste de travail dentaire avec instruments (photo d’illustration, ne montre pas le cabinet)', sizes='(max-width: 860px) 100vw, 860px', lazy=False)}</div></section>
<div class="qa"><div><small>Téléphone</small><b><a href="{K.telhref(F['tel'])}">{F['tel']}</a></b></div><div><small>Aujourd'hui</small><b>{K.hours_short(F)}</b></div><div><small>Ville</small><b>Nabeul</b></div><div><small>N° d'Ordre</small><b>{K.ph()}</b></div></div>
<section class="faq" id="faq"><h2>Questions pratiques</h2>{faq}</section>
<div class="city">{M.img('ville', 'Nabeul (photo d’illustration)', sizes='120px')}<p>Le cabinet reçoit à Nabeul. L'adresse exacte et l'étage seront précisés ici après validation par le cabinet.</p></div></main>
<footer class="ft w">{M.credits()}{K.footer_legal(F)}</footer>'''
    fav = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='32' fill='#4A5A1F'/><text x='32' y='43' font-size='30' text-anchor='middle' fill='#FBF7DF' font-family='Georgia'>?</text></svg>"
    return K.page(F, 'Dr Ichrak Hammami — Médecin dentiste à Nabeul (démo)', 'Cabinet dentaire du Dr Ichrak Hammami à Nabeul : rendez-vous, horaires, accès et questions pratiques.', FONTS, CSS, body, '#4A5A1F', fav)
