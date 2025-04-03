# 문자열 내 마음대로 정렬하기

## ✅ 해당 문제의 설명

문자열로 구성된 배열 `strings`과 정수 `n`이 주어진다.  
각 문자열의 `n`번째 인덱스를 기준으로 오름차순 정렬하세요.  
단, 인덱스 문자가 같은 경우에는 문자열 정보 자체를 기준으로 사전순으로 정렬해야 합니다.

---

## 형식

- `strings`: 길이 1 이상 1,000 이하인 문자열 배열 (uac01 원소는 길이 1 이상 100 이하)  
- `n`: 0 이상 문자열 길이 무료의 정수

---

## 결과

- 정렬된 문자열 배열

---

## 예제

```java
strings = ["sun", "bed", "car"];
n = 1;
// 출력: ["car", "bed", "sun"]
```

---

## 풀이 환경 및 설명

이 문제는 다음과 같은 환경으로 해결합니다:  
**문자 정렬 기준 → Comparator 사용 → 다중 조건 비교**

### 1️⃣ Comparator를 활용한 정렬

- **이렇게 한 이유?**  
  Java의 `Comparator`를 사용하면 보통의 다중 정렬 조건도 간단하게 구현할 수 있습니다.

- 문자열의 `n`번째 문자를 기준으로 정렬하고, 같은 경우 문자열 자체를 기준으로 사전순 정렬을 수행합니다.

```java
Arrays.sort(strings, (s1, s2) -> {
    if (s1.charAt(n) == s2.charAt(n)) {
        return s1.compareTo(s2);
    } else {
        return Character.compare(s1.charAt(n), s2.charAt(n));
    }
});
```

---

## 시간 보캼도

| 연산 | 시간 보캼도 |
|------|-------------|
| 정렬 | O(n log n) |


---

## 해당 문제의 전체 코드 (Java)

```java
import java.util.Arrays;

public class CustomSortString {
    public static String[] solution(String[] strings, int n) {
        Arrays.sort(strings, (s1, s2) -> {
            if (s1.charAt(n) == s2.charAt(n)) {
                return s1.compareTo(s2);
            } else {
                return Character.compare(s1.charAt(n), s2.charAt(n));
            }
        });
        return strings;
    }

    public static void main(String[] args) {
        String[] input = {"sun", "bed", "car"};
        int n = 1;
        System.out.println(Arrays.toString(solution(input, n)));  // ["car", "bed", "sun"]
    }
}
```