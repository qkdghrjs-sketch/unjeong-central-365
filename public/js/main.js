// ===== 히어로 슬라이더 V2 =====
const slideBgs = document.querySelectorAll('.slide-bg');
const slideTexts = document.querySelectorAll('.slide-v2');
const spItems = document.querySelectorAll('.sp-item');
const slideNumEl = document.querySelector('.slide-num-current');
const prevBtn = document.querySelector('.slide-prev');
const nextBtn = document.querySelector('.slide-next');
let currentSlide = 0;
let slideInterval;

function goToSlide(index) {
  slideBgs.forEach(bg => bg.classList.remove('active'));
  slideTexts.forEach(text => text.classList.remove('active'));
  spItems.forEach(sp => sp.classList.remove('active'));

  currentSlide = index;
  slideBgs[currentSlide].classList.add('active');
  slideTexts[currentSlide].classList.add('active');
  spItems[currentSlide].classList.add('active');
  if (slideNumEl) slideNumEl.textContent = String(currentSlide + 1).padStart(2, '0');
}

function nextSlide() {
  goToSlide((currentSlide + 1) % slideBgs.length);
}

function prevSlide() {
  goToSlide((currentSlide - 1 + slideBgs.length) % slideBgs.length);
}

function startAutoSlide() {
  slideInterval = setInterval(nextSlide, 5000);
}

function resetAutoSlide() {
  clearInterval(slideInterval);
  startAutoSlide();
}

if (nextBtn) nextBtn.addEventListener('click', () => { nextSlide(); resetAutoSlide(); });
if (prevBtn) prevBtn.addEventListener('click', () => { prevSlide(); resetAutoSlide(); });

spItems.forEach(sp => {
  sp.addEventListener('click', () => {
    goToSlide(parseInt(sp.dataset.slide));
    resetAutoSlide();
  });
});

startAutoSlide();

// ===== 모바일 메뉴 (header-mega.js에서 처리) =====

// ===== 스크롤 시 헤더 스타일 변경 =====
const header = document.getElementById('header');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    header.classList.add('scrolled');
  } else {
    header.classList.remove('scrolled');
  }
});

// ===== 퀵 네비게이션 Stagger 애니메이션 =====
const qnObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      document.querySelectorAll('.qn-card').forEach(card => {
        card.classList.add('qn-visible');
      });
      qnObserver.disconnect();
    }
  });
}, { threshold: 0.2 });

const quicknavSection = document.querySelector('.quicknav');
if (quicknavSection) qnObserver.observe(quicknavSection);

// ===== 블로그 & 공지사항 섹션 애니메이션 =====
const bnSection = document.querySelector('.blog-notice-section');
if (bnSection) {
  const bnObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // 컬럼 슬라이드인
        document.querySelectorAll('.bn-column').forEach(col => {
          col.classList.add('bn-visible');
        });
        // 리스트 항목 stagger
        document.querySelectorAll('.bn-item').forEach(item => {
          const delay = parseInt(item.dataset.stagger) * 50;
          setTimeout(() => {
            item.classList.add('bn-item-visible');
          }, 300 + delay);
        });
        bnObserver.disconnect();
      }
    });
  }, { threshold: 0.15 });
  bnObserver.observe(bnSection);
}

// ===== Clinic 섹션 stagger 애니메이션 =====
const clinicObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      document.querySelectorAll('.clinic-card').forEach(card => {
        card.classList.add('clinic-visible');
      });
      clinicObserver.disconnect();
    }
  });
}, { threshold: 0.15 });

const clinicSection = document.querySelector('.clinic-section');
if (clinicSection) clinicObserver.observe(clinicSection);

// ===== Promise 섹션 애니메이션 =====
const pmObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('pm-visible');
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('[data-anim-promise]').forEach(el => {
  pmObserver.observe(el);
});

// ===== 스크롤 애니메이션 =====
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, observerOptions);

document.querySelectorAll('.info-table-wrap, .info-contact, .location-info, .map-placeholder').forEach(el => {
  el.classList.add('fade-in');
  observer.observe(el);
});

const style = document.createElement('style');
style.textContent = `
  .fade-in {
    opacity: 0;
    transform: translateY(24px);
    transition: opacity 0.6s ease, transform 0.6s ease;
  }
  .fade-in.visible {
    opacity: 1;
    transform: translateY(0);
  }
`;
document.head.appendChild(style);
