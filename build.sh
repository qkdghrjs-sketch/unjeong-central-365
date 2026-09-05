#!/bin/sh
# blocks/ 안의 조각들을 이어붙여 미리보기용 index.html 을 만듭니다.
set -e
cd "$(dirname "$0")"
{
  cat blocks/_head.part
  for f in blocks/0*.html; do
    printf '\n\n'
    cat "$f"
  done
  cat blocks/_foot.part
} > index.html
echo "index.html 생성 완료"
