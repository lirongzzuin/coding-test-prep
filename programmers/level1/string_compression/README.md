# 문자열 압축 (Run-Length Encoding)

## 문제 설명
연속으로 반복되는 문자를 압축하는 **Run-Length Encoding** 방식을 구현하세요.  
예를 들어 `"aaabbcddd"`라는 문자열이 주어지면, `"a3b2c1d3"`로 압축해야 합니다.  

## 입력
- `s`: 길이 `n` (1 ≤ `n` ≤ 10⁶) 의 문자열 (영문 소문자로만 구성)

## 출력
- 문자열을 압축한 결과를 반환

## 예제
```python
compress_string("aaabbcddd")  # 출력: "a3b2c1d3"
compress_string("abcd")  # 출력: "a1b1c1d1"
compress_string("aaabbaa")  # 출력: "a3b2a2"
```

## 해결 방법
### 1️⃣ 투 포인터 활용 - O(n)
- 문자열을 순회하며 연속된 문자의 개수를 센 후, 압축된 형태로 변환
- 효율적인 접근 방식으로, **O(n)** 의 시간 복잡도를 가짐

```python
def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(f"{s[i - 1]}{count}")
            count = 1

    compressed.append(f"{s[-1]}{count}")  # 마지막 문자 처리
    return "".join(compressed)
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 투 포인터 활용 | **O(n)** | O(n) |

## 추가할 수 있는 내용
- [ ] 입력 검증 추가 (예: 빈 문자열 예외 처리)
- [ ] 압축률이 낮을 경우 원본 문자열 반환