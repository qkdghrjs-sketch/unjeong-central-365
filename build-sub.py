# -*- coding: utf-8 -*-
"""
세부페이지 빌드
  sub/body-*.part  (본문)  +  sub/_css.part  +  sub/_js.part
    → sub/<번호>-<한글명>.html      아임웹 코드 위젯에 붙여넣는 파일
    → preview/<슬러그>.html          미리보기용 (헤더·오시는길·푸터 포함)
"""
import io, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

def read(p):
    return io.open(p, encoding='utf-8').read()

CSS = read('sub/_css.part')
JS  = read('sub/_js.part')

# (번호, 슬러그, 한글명, 브라우저 탭 제목, 설명)
PAGES = [
    ('13', 'night-dialysis', '야간투석',
     '야간투석 | 이움내과의원',
     '고양시 덕양구 야간 혈액투석. 이움내과의원은 월·수·금 저녁 6시부터 밤 10시 30분까지 야간투석을 운영합니다. 화정역 도보 5분, 퇴근 후 투석받고 귀가하실 수 있습니다.'),
]

IMWEB_HEAD = (
"<!-- ══════════════════════════════════════════════════════════════\n"
"     [이움내과] 세부페이지 — %s\n"
"     ─────────────────────────────────────────────────────────────\n"
"     아임웹 [%s] 페이지의 코드 위젯에 통째로 붙여넣으세요.\n"
"     ※ 글(내용)은 기존 페이지 그대로입니다. 디자인만 새로 만들었습니다.\n"
"     ※ 상단 메뉴와 푸터는 아임웹 공통 영역을 그대로 쓰시면 됩니다.\n"
"     ※ 페이지 아래 '진료시간·오시는 길'이 필요하면\n"
"        blocks/08-location.html 을 같은 페이지 아래쪽 섹션에 넣으세요.\n"
"     ══════════════════════════════════════════════════════════════ -->\n\n")

PRE_HEAD = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>%s</title>
<meta name="description" content="%s">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#0C2D37">
<link rel="icon" href="https://cdn.imweb.me/upload/S20260108b9005a7eb2710/9f85a9eebaa26.png">
<link rel="preconnect" href="https://cdn.imweb.me">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<style>
html{-webkit-text-size-adjust:100%%;scroll-behavior:smooth;}
body{margin:0;padding:0;background:#fff;overflow-x:hidden;}
</style>
</head>
<body>
<!-- 미리보기용 페이지입니다. 아임웹에는 sub/ 폴더의 파일을 넣으세요. -->
"""

PRE_FOOT = "\n</body>\n</html>\n"

if not os.path.isdir('preview'):
    os.makedirs('preview')

made = []
for no, slug, kor, title, desc in PAGES:
    body = read('sub/body-%s-%s.part' % (no, slug))

    # 1) 아임웹 붙여넣기용
    out = IMWEB_HEAD % (kor, kor) + CSS + '\n\n' + body + '\n\n' + JS
    p1 = 'sub/%s-%s.html' % (no, kor)
    io.open(p1, 'w', encoding='utf-8', newline='\n').write(out)

    # 2) 미리보기용 (헤더 + 본문 + 오시는 길 + 푸터 + 플로팅)
    parts = [PRE_HEAD % (title, desc),
             read('blocks/01-header.html'), '\n\n',
             CSS, '\n\n', body, '\n\n', JS, '\n\n',
             read('blocks/08-location.html'), '\n\n',
             read('blocks/09-footer.html'), '\n\n',
             read('blocks/10-floating.html'),
             PRE_FOOT]
    p2 = 'preview/%s.html' % slug
    io.open(p2, 'w', encoding='utf-8', newline='\n').write(''.join(parts))

    made.append((kor, slug, os.path.getsize(p1), os.path.getsize(p2)))

# 미리보기 목록 페이지
ALL = [('13','night-dialysis','야간투석')]
DONE = {p[1] for p in PAGES}
TODO = [
 ('01','about','병원소개'),('02','doctors','의료진 소개'),('03','location','진료시간 · 오시는 길'),
 ('04','areas','일산 · 고양 오시는 길'),('05','tour','둘러보기'),('06','internal-medicine','일반 내과 진료'),
 ('07','chronic-care','일차의료 만성질환관리'),('08','diabetes','당뇨'),('09','hypertension','고혈압'),
 ('10','dyslipidemia','고지혈증'),('11','dialysis-center','인공신장센터 안내'),('12','hemodialysis','혈액투석'),
 ('13','night-dialysis','야간투석'),('14','iv-therapy','영양수액'),('15','obesity','비만'),
 ('16','vaccination','예방접종'),('17','faq','자주 묻는 질문'),('18','fees','비급여진료비'),
]
rows = []
for no, slug, kor in TODO:
    if slug in DONE:
        rows.append('<a class="row done" href="./%s.html"><b>%s</b><span>%s</span><i>완성</i></a>' % (slug, no, kor))
    else:
        rows.append('<span class="row"><b>%s</b><span>%s</span><i>준비중</i></span>' % (no, kor))

idx = """<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>이움내과 세부페이지 미리보기</title>
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="https://cdn.imweb.me/upload/S20260108b9005a7eb2710/9f85a9eebaa26.png">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/sun-typeface/suit@2/fonts/variable/woff2/SUIT-Variable.css">
<style>
*{box-sizing:border-box;margin:0;padding:0;font-family:'SUIT Variable',-apple-system,sans-serif;word-break:keep-all}
body{background:#F6F9F9;color:#0F2027;padding:64px 20px 90px;line-height:1.8}
.wrap{max-width:760px;margin:0 auto}
.eyebrow{font-size:12px;font-weight:700;letter-spacing:.18em;color:#36B8A5}
h1{margin:16px 0 12px;font-size:34px;font-weight:800;letter-spacing:-.045em;color:#0C2D37;line-height:1.4}
.desc{font-size:15.5px;color:#3F565F;margin-bottom:14px}
.home{display:inline-flex;align-items:center;gap:8px;height:46px;padding:0 22px;border-radius:999px;background:#0C2D37;color:#fff;font-size:14px;font-weight:700;text-decoration:none;margin-bottom:36px}
.list{border-top:1.5px solid #0C2D37;background:#fff;border-radius:0 0 6px 6px}
.row{display:flex;align-items:center;gap:16px;padding:18px 20px;border-bottom:1px solid #E4EBED;text-decoration:none;color:inherit}
.row b{font-size:12px;font-weight:700;color:#7A8E96;width:22px;flex:none}
.row>span{flex:1;font-size:16px;font-weight:700;letter-spacing:-.04em;color:#0C2D37}
.row i{font-style:normal;font-size:11.5px;font-weight:700;padding:5px 11px;border-radius:999px;background:#F0F4F5;color:#7A8E96}
.row.done i{background:#36B8A5;color:#fff}
.row.done:hover{background:#E9F7F4}
.row.done:hover>span{color:#2A9B8B}
</style></head><body><div class="wrap">
<span class="eyebrow">PREVIEW</span>
<h1>이움내과 세부페이지 미리보기</h1>
<p class="desc">디자인만 새로 만들었습니다. 글(내용)은 기존 페이지 그대로입니다.</p>
<a class="home" href="../">← 메인페이지 보기</a>
<div class="list">
%s
</div>
</div></body></html>
""" % ('\n'.join(rows))
io.open('preview/index.html', 'w', encoding='utf-8', newline='\n').write(idx)

for kor, slug, a, b in made:
    print('%-10s 아임웹용 %7d bytes   미리보기 %7d bytes  → /preview/%s.html' % (kor, a, b, slug))
print('preview/index.html 생성')
