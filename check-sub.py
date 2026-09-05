# -*- coding: utf-8 -*-
"""세부페이지 본문 검사 : 이상 문자 / 질문 수 / 태그 균형"""
import io, re, glob, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
OK = re.compile(r'[\x00-\x7F\uAC00-\uD7A3\u3131-\u318E\u4E00-\u9FFF'
                r'\u00b7\u00b1\u00b2\u2013\u2014\u2018\u2019\u201c\u201d\u2026'
                r'\u203b\u2192\u2103\u2500-\u257F\s]')
bad = False
for f in sorted(glob.glob('sub/body-*.part')):
    s = io.open(f, encoding='utf-8').read()
    odd = sorted(set(c for c in s if not OK.match(c)))
    q = len(re.findall(r'class="eum_qt">', s))
    div = s.count('<div') + s.count('<section') - s.count('</div>') - s.count('</section>')
    note = []
    if odd: note.append('STRAY ' + ' '.join('U+%04X' % ord(c) for c in odd)); bad = True
    if div != 0: note.append('TAG UNBALANCED %+d' % div); bad = True
    print('%-34s Q=%-3d %s' % (os.path.basename(f), q, ' / '.join(note) if note else 'OK'))
print('ALL CLEAN' if not bad else '*** CHECK NEEDED ***')
