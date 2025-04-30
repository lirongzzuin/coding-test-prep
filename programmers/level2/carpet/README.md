# 카펫 (Carpet)

## ✅ 문제 설명

어떤 카펫은 갈색 격자와 노란색 격자로 이루어져 있습니다.
- 갈색 격자는 테두리
- 노란색 격자는 내부 영역을 구성합니다.

주어진 갈색 격자 수(`brown`)와 노란색 격자 수(`yellow`)를 이용해,
**가능한 카펫의 가로(width), 세로(height)** 크기를 구하세요.

조건:
- 가로 ≥ 세로
- 카펫은 직사각형 형태
- 항상 해가 존재

---

## 📥 입력

- `brown`: 갈색 격자의 개수 (8 이상 5,000 이하)
- `yellow`: 노란색 격자의 개수 (1 이상 2,000 이하)

---

## 📤 출력

- `[가로, 세로]` 형태의 정수 배열

---

## 💡 예제

```java
brown = 10;
yellow = 2;
// 출력: [4, 3]
```

→ 전체 면적: 12 (4 × 3) → 내부: 2 (2 × 1) → 조건 만족

---

## 🔍 풀이 흐름 및 설명

이 문제는 단순히 규칙을 찾는 게 아니라, 수학적인 아이디어와 **완전탐색**을 결합한 문제입니다.

### ✅ 핵심 아이디어

1. 전체 카펫의 면적은 `total = brown + yellow`
2. 전체 면적의 약수들로 가능한 가로/세로 쌍을 탐색
3. 해당 조합이 조건을 만족하는지 검사:
    - `(width - 2) * (height - 2) == yellow`

※ 내부 노란색은 테두리 한 칸씩을 제외한 영역이므로 `-2`

---

## ✅ 구현 순서

### 1️⃣ 전체 면적 계산

```java
int total = brown + yellow;
```

### 2️⃣ 전체 면적의 약수 쌍 탐색 (완전탐색)

```java
for (int height = 3; height <= total / height; height++) {
    int width = total / height;
    if ((width - 2) * (height - 2) == yellow) {
        return new int[]{width, height};
    }
}
```

- height는 최소 3 이상이어야 테두리를 만들 수 있음
- 반복 조건: `height <= total / height` → 중복 방지

---

## ⏱ 시간 복잡도 분석

| 연산 항목       | 시간 복잡도 |
|------------------|--------------|
| 전체 경우 탐색   | O(√n)         |

- 전체 면적의 약수 개수만큼 탐색하므로 빠르게 수행됨

---

## ✅ 전체 코드 (Java)

```java
public class Carpet {
    public static int[] solution(int brown, int yellow) {
        int total = brown + yellow;

        for (int height = 3; height <= total / height; height++) {
            int width = total / height;

            if ((width - 2) * (height - 2) == yellow) {
                return new int[]{width, height};
            }
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        int brown = 10, yellow = 2;
        int[] result = solution(brown, yellow);
        System.out.println("[" + result[0] + ", " + result[1] + "]");  // 출력: [4, 3]
    }
}
```

---

## ✅ 마무리 정리

- 문제를 수학적으로 분석하고 가능한 가로 × 세로 조합을 완전탐색합니다.
- 노란색 격자 수는 `(가로 - 2) * (세로 - 2)` 공식을 만족해야 합니다.
- 수학적 조건을 코드로 옮기는 연습과 완전탐색 설계 연습에 적합한 문제입니다.

