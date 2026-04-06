// ===== 모바일 메뉴 =====
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const nav = document.getElementById('nav');
const navWrap = nav.closest('.header-nav-wrap');

mobileMenuBtn.addEventListener('click', () => {
  mobileMenuBtn.classList.toggle('active');
  navWrap.classList.toggle('active');
});

nav.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    mobileMenuBtn.classList.remove('active');
    navWrap.classList.remove('active');
  });
});

// ===== 스크롤 애니메이션 =====
const animObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

// 히어로는 즉시 보이게
document.querySelectorAll('.ph-hero .anim-fade-up').forEach(el => {
  setTimeout(() => el.classList.add('visible'), 200);
});

// 나머지 data-anim 요소들
document.querySelectorAll('[data-anim]').forEach(el => {
  animObserver.observe(el);
});

// ===== 아코디언 =====
document.querySelectorAll('.ph-acc-header').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.ph-acc-item');
    const isActive = item.classList.contains('active');

    // 모두 닫기
    document.querySelectorAll('.ph-acc-item').forEach(i => {
      i.classList.remove('active');
      i.querySelector('.ph-acc-header').setAttribute('aria-expanded', 'false');
    });

    // 클릭한 항목 토글
    if (!isActive) {
      item.classList.add('active');
      btn.setAttribute('aria-expanded', 'true');
    }
  });
});
