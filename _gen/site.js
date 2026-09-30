(function(){
  var I18N=window.I18N||null, SITE=window.SITE||{};
  // mobile menu
  var mb=document.querySelector('.menu-btn'), mm=document.querySelector('.mobile-menu');
  if(mb&&mm){mb.addEventListener('click',function(){var o=mm.classList.toggle('open');mb.setAttribute('aria-expanded',o)});
    mm.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){mm.classList.remove('open')})});}
  // i18n
  var lang='fr';
  function t(k){return (I18N&&I18N[k]&&I18N[k][lang])||(I18N&&I18N[k]&&I18N[k].fr)||'';}
  function applyLang(l){ if(!I18N) return; lang=l; document.documentElement.lang=l;
    document.querySelectorAll('[data-i18n]').forEach(function(el){var v=t(el.getAttribute('data-i18n')); if(v) el.innerHTML=v;});
    document.querySelectorAll('[data-i18n-ph]').forEach(function(el){var v=t(el.getAttribute('data-i18n-ph')); if(v) el.setAttribute('placeholder',v);});
    document.querySelectorAll('.lang button').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.lang===l)});
    try{localStorage.setItem('lang-'+SITE.slug,l)}catch(e){} }
  document.querySelectorAll('.lang button').forEach(function(b){b.addEventListener('click',function(){applyLang(b.dataset.lang)})});
  if(I18N){var saved=null;try{saved=localStorage.getItem('lang-'+SITE.slug)}catch(e){}
    var nav=(navigator.language||'fr').slice(0,2); applyLang(saved||'fr');}
  // gallery lightbox
  var lb=document.querySelector('.lightbox');
  if(lb){var lbi=lb.querySelector('img');
    document.querySelectorAll('.gallery button').forEach(function(b){b.addEventListener('click',function(){lbi.src=b.dataset.full;lbi.alt=b.querySelector('img').alt;lb.classList.add('open')})});
    lb.addEventListener('click',function(e){if(e.target!==lbi) lb.classList.remove('open')});
    document.addEventListener('keydown',function(e){if(e.key==='Escape') lb.classList.remove('open')});}
  // form -> WhatsApp / mailto
  var f=document.getElementById('req-form');
  function build(){var fd=new FormData(f), lines=[SITE.formIntro?SITE.formIntro[lang]||SITE.formIntro.fr:''];
    f.querySelectorAll('[name]').forEach(function(el){var v=(fd.get(el.name)||'').toString().trim(); if(v){var lab=el.closest('label'); var n=lab?lab.childNodes[0].textContent.trim():el.name; lines.push('• '+n+' : '+v);}});
    return lines.join('\n');}
  if(f){
    f.addEventListener('submit',function(e){e.preventDefault(); if(!f.reportValidity()) return;
      window.open('https://wa.me/'+SITE.wa+'?text='+encodeURIComponent(build()),'_blank','noopener');});
    var m=document.getElementById('mail-btn');
    if(m) m.addEventListener('click',function(){ if(!f.reportValidity()) return;
      location.href='mailto:'+SITE.email+'?subject='+encodeURIComponent(SITE.mailSubject||'Demande')+'&body='+encodeURIComponent(build());});
    var d1=f.querySelector('[name=arrivee]'), d2=f.querySelector('[name=depart]');
    if(d1){var today=new Date().toISOString().slice(0,10); d1.min=today; if(d2){d2.min=today; d1.addEventListener('change',function(){d2.min=d1.value; if(d2.value&&d2.value<=d1.value) d2.value='';});}}
    f.querySelectorAll('input[type=date]').forEach(function(i){if(!i.min) i.min=new Date().toISOString().slice(0,10);});
  }
  // reveal
  if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target)}})},{threshold:.12});
    document.querySelectorAll('.reveal').forEach(function(el){io.observe(el)});} else document.querySelectorAll('.reveal').forEach(function(el){el.classList.add('in')});
  var y=document.getElementById('year'); if(y) y.textContent=new Date().getFullYear();
})();
