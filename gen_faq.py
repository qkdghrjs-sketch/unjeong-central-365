# -*- coding: utf-8 -*-
"""자주 묻는 질문 페이지 본문을 만듭니다. 질문·답변은 원문 그대로입니다."""
import io, os, json, html

HERE = os.path.dirname(os.path.abspath(__file__))
core = json.load(io.open(os.path.join(HERE, '_core.json'), encoding='utf-8'))

TOPICS = ['지역', '투석', '만성질환', '진료', '예약·비용']
LABEL = {
    '지역': '위치 · 오시는 길',
    '투석': '혈액투석 · 야간투석',
    '만성질환': '고혈압 · 당뇨병 관리',
    '진료': '진료 안내',
    '예약·비용': '예약 · 비용 · 지원제도',
}
ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>')
e = lambda t: html.escape(t, quote=False)

secs = []
for i, topic in enumerate(TOPICS):
    items = [x for x in core if x['topic'] == topic]
    if not items:
        continue
    rows = []
    for n, it in enumerate(items):
        d = ' eum_d%d' % min(n + 1, 4) if n else ''
        more = ''
        if it['href']:
            more = ('\n          <a class="eum_ansmore" href="https://yium.kr%s">자세히 보기%s</a>'
                    % (it['href'], ARROW))
        rows.append(
            '        <article class="eum_ans eum_rv%s">\n'
            '          <h3><em>Q.</em>%s</h3>\n'
            '          <p>%s</p>%s\n'
            '        </article>' % (d, e(it['q']), e(it['a']), more))
    secs.append(
        '  <section class="eum_sec%s">\n'
        '    <div class="eum_narrow">\n'
        '      <div class="eum_shead eum_rv">\n'
        '        <span class="eum_eyebrow"><span class="eum_bar"></span>%s</span>\n'
        '        <h2 class="eum_h2">%s</h2>\n'
        '      </div>\n'
        '      <div class="eum_answers">\n%s\n      </div>\n'
        '    </div>\n  </section>'
        % (' eum_alt' if i % 2 == 1 else '', e(topic), e(LABEL[topic]), '\n'.join(rows)))

doc = '''<div id="eumSub">

  <!-- ═══════════ 서브 히어로 ═══════════ -->
  <section class="eum_hero">
    <div class="eum_wrap">
      <span class="eum_eyebrow eum_rv"><span class="eum_bar"></span>FREQUENTLY ASKED QUESTIONS</span>
      <h1 class="eum_h1 eum_rv eum_d1">이움내과의원<br><em>자주 묻는 질문 총정리</em></h1>
      <p class="eum_hsub eum_rv eum_d2">위치와 오시는 길, 야간투석 운영시간, 적정성평가 등급, 진료시간과 예약 방법까지<br>가장 많이 문의하시는 내용을 한 곳에 모았습니다.</p>
      <div class="eum_badges eum_rv eum_d3">
        <span class="eum_badge"><span class="eum_dot"></span>%d개 질문</span>
        <span class="eum_badge"><span class="eum_dot"></span>위치 · 투석 · 만성질환</span>
        <span class="eum_badge"><span class="eum_dot"></span>예약 · 비용</span>
      </div>
    </div>
  </section>

%s

  <!-- ═══════════ CTA ═══════════ -->
  <section class="eum_cta">
    <div class="eum_wrap">
      <span class="eum_ctitle eum_rv">찾으시는 답이 없다면<br>전화로 물어봐 주세요</span>
      <span class="eum_csub eum_rv eum_d1">경기도 고양시 덕양구 백양로 51 네이버타운 3층 301호, 305호<br>진료 문의 031-979-0875 · 혈액투석 문의 031-979-0873</span>
      <div class="eum_cbtns eum_rv eum_d2">
        <a class="eum_cbtn eum_p" href="tel:031-979-0875">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.13.96.36 1.9.7 2.8a2 2 0 0 1-.45 2.11L8.1 9.9a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.9z"/></svg>
          대표번호 031-979-0875
        </a>
        <a class="eum_cbtn eum_g" href="https://yium.kr/areas">
          일산 · 고양 오시는 길%s
        </a>
      </div>
    </div>
  </section>

</div>
''' % (len(core), '\n\n'.join(secs), ARROW)

out = os.path.join(HERE, 'repo', 'sub', 'body-17-faq.part')
io.open(out, 'w', encoding='utf-8', newline='\n').write(doc)
print('faq body written: %d questions in %d topics' % (len(core), len(secs)))
