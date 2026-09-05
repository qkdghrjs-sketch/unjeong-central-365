# -*- coding: utf-8 -*-
"""core-answers.ts 에서 질문·답변을 뽑아 JSON 으로 저장합니다."""
import io, re, json, os
from collections import Counter

SRC = r'C:\Users\qkdgh\Downloads\홈페이지\이움내과_수정본\yium-board\src\lib\core-answers.ts'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_core.json')

s = io.open(SRC, encoding='utf-8').read()
s = s[s.index('export const CORE_ANSWERS'):]

PAT = re.compile(
    r'\{\s*topic:\s*"([^"]+)",\s*'
    r'q:\s*"((?:[^"\\]|\\.)*)",\s*'
    r'a:\s*"((?:[^"\\]|\\.)*)",'
    r'(?:\s*href:\s*"([^"]*)",)?\s*\}'
)

def unesc(t):
    return t.replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\')

items = []
for m in PAT.finditer(s):
    topic, q, a, href = m.groups()
    items.append({'topic': topic, 'q': unesc(q), 'a': unesc(a), 'href': href or ''})

io.open(OUT, 'w', encoding='utf-8').write(json.dumps(items, ensure_ascii=False, indent=1))
print('total %d' % len(items))
for k, v in Counter(i['topic'] for i in items).items():
    print('  %-10s %d' % (k, v))
