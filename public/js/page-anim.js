// 페이지 진입 애니메이션
const animObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });

document.querySelectorAll('[data-anim]').forEach(el => {
  animObserver.observe(el);
});

// 히어로는 즉시
document.querySelectorAll('.page-hero [data-anim]').forEach(el => {
  setTimeout(() => el.classList.add('visible'), 150);
});
