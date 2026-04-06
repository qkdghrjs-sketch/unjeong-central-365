const NAVIGATION = [
  {
    id: 'about',
    label: '병원소개',
    href: '/about/doctors',
    color: '#5F5E5A',
    children: [
      { label: '의료진 소개', href: '/about/doctors',    icon: 'stethoscope',  desc: '내과·소아청소년과 전문의 프로필' },
      { label: '시설 안내',   href: '/about/facility',   icon: 'building',     desc: '최신 장비와 쾌적한 진료 환경' },
      { label: '오시는길',    href: '/about/directions',  icon: 'map-pin',     desc: 'GTX-A 운정중앙역 도보 접근' },
      { label: '진료시간',    href: '/about/hours',       icon: 'clock',       desc: '평일·주말·공휴일 진료 안내' },
    ]
  },
  {
    id: 'endoscopy',
    label: '내시경센터',
    href: '/endoscopy/gastroscopy',
    color: '#378ADD',
    children: [
      { label: '위내시경',       href: '/endoscopy/gastroscopy',  icon: 'scan-eye',    desc: '정확한 위장 검사와 조기 발견' },
      { label: '대장내시경',     href: '/endoscopy/colonoscopy',  icon: 'scan-line',   desc: '대장 질환의 정밀 검사' },
      { label: '수면내시경',     href: '/endoscopy/sedation',     icon: 'moon',        desc: '편안한 수면 상태에서 검사' },
      { label: '역류성식도염',   href: '/endoscopy/gerd',         icon: 'flame',       desc: '위산 역류 증상 진단과 치료' },
      { label: '헬리코박터',     href: '/endoscopy/helicobacter', icon: 'bug',         desc: '헬리코박터균 검사 및 제균 치료' },
      { label: '대장용종절제술', href: '/endoscopy/polypectomy',  icon: 'scissors',    desc: '내시경 용종 절제 시술' },
    ]
  },
  {
    id: 'checkup',
    label: '건강검진센터',
    href: '/checkup/general',
    color: '#1D9E75',
    children: [
      { label: '종합건강검진', href: '/checkup/general',    icon: 'clipboard-check', desc: '국가검진·일반·기업·종합검진' },
      { label: '5대암검진',   href: '/checkup/cancer',     icon: 'shield-check',    desc: '위암·대장암·간암·유방암·자궁경부암' },
      { label: '초음파검사',  href: '/checkup/ultrasound', icon: 'radio',           desc: '복부·갑상선·심장·경동맥 초음파' },
    ]
  },
  {
    id: 'chronic',
    label: '만성질환클리닉',
    href: '/chronic/hypertension',
    color: '#D85A30',
    children: [
      { label: '고혈압',          href: '/chronic/hypertension',   icon: 'gauge',          desc: '혈압 관리 및 합병증 예방' },
      { label: '당뇨',            href: '/chronic/diabetes',       icon: 'droplets',       desc: '혈당 조절과 맞춤 치료' },
      { label: '고지혈증',        href: '/chronic/hyperlipidemia', icon: 'test-tubes',     desc: '콜레스테롤·중성지방 관리' },
      { label: '갑상선질환',      href: '/chronic/thyroid',        icon: 'scan',           desc: '갑상선 기능 이상 진단·치료' },
      { label: '수면장애·불면증', href: '/chronic/sleep',          icon: 'moon-star',      desc: '수면의 질 개선 상담·치료' },
      { label: '이비인후과',      href: '/chronic/ent',            icon: 'ear',            desc: '비염·축농증·인후 질환 진료' },
    ]
  },
  {
    id: 'pediatric',
    label: '소아청소년과',
    href: '/pediatric/general',
    color: '#BA7517',
    children: [
      { label: '소아 일반진료',   href: '/pediatric/general',  icon: 'baby',       desc: '감기·장염·피부질환 등 소아 진료' },
      { label: '소아 예방접종',   href: '/pediatric/vaccine',  icon: 'syringe',    desc: '국가필수·선택 예방접종' },
      { label: '소아이비인후과',   href: '/pediatric/ent',      icon: 'ear',        desc: '소아 비염·중이염·편도선염' },
      { label: '소아 알레르기',   href: '/pediatric/allergy',  icon: 'flower-2',   desc: '아토피·천식·식품 알레르기' },
      { label: '365일 진료',  href: '/pediatric/night',    icon: 'moon',       desc: '365일 소아 진료 안내' },
    ]
  },
  {
    id: 'growth',
    label: '우리아이 성장클리닉',
    href: '/growth/intro',
    color: '#7F77DD',
    children: [
      { label: '성장클리닉 안내',   href: '/growth/intro',       icon: 'ruler',       desc: '성장클리닉 진료 프로세스' },
      { label: '성장판·골연령검사', href: '/growth/bone-age',    icon: 'bone',        desc: '성장판 상태 및 골연령 측정' },
      { label: '성장호르몬치료',    href: '/growth/hormone',     icon: 'pill',        desc: '성장호르몬 주사 치료' },
      { label: '성조숙증',          href: '/growth/precocious',  icon: 'alert-circle',desc: '조기 사춘기 진단과 치료' },
      { label: '키성장 영양관리',   href: '/growth/nutrition',   icon: 'apple',       desc: '성장기 맞춤 영양 상담' },
    ]
  },
];

module.exports = { NAVIGATION };
