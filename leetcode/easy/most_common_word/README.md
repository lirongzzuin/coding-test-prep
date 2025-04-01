# 가장 흔한 단어 (Most Common Word)

## 문제 설명
문자열 `paragraph`가 주어졌을 때, **금지된 단어(banned)**를 제외하고  
가장 많이 등장한 단어를 소문자로 반환하세요.  

- 대소문자는 구분하지 않으며, 단어는 알파벳으로만 구성됩니다.  
- 문장 부호는 모두 무시해야 합니다.

## 입력
- `String paragraph`: 영문 문장 (쉼표, 마침표 등 특수문자 포함)  
- `String[] banned`: 금지된 단어 목록

## 출력
- 가장 많이 등장한 단어 (소문자)

## 예제
```java
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
// 출력: "ball"
```

## 풀이 흐름 및 설명
이 문제는 **문자열 전처리 → 단어 필터링 → 등장 횟수 카운트 → 최빈값 추출** 흐름으로 해결할 수 있습니다. 각 단계에서 **왜 그렇게 접근했는지**에 대해서도 함께 설명합니다.

---

### 1️⃣ 금지된 단어를 Set으로 정리하기
- **이유:** 금지 단어는 매우 빠르게 탐색하고 걸러야 하므로 `HashSet`에 저장하여 O(1) 시간에 필터링할 수 있도록 합니다.
```java
Set<String> bannedSet = new HashSet<>(Arrays.asList(banned));
```

---

### 2️⃣ 문장을 전처리하여 단어만 추출하기
- **이유:** 단어를 제대로 분리하려면 특수문자, 구두점 등을 제거해야 하며 대소문자 구분 없이 처리해야 합니다.
- 소문자로 변환한 후 정규식 `[^a-z]`를 사용하여 알파벳 외 문자를 공백으로 치환하고, 공백 기준으로 분리합니다.
```java
String[] words = paragraph.toLowerCase().replaceAll("[^a-z]", " ").split("\\s+");
```

---

### 3️⃣ 금지되지 않은 단어들의 등장 횟수를 세기
- **이유:** 등장 횟수를 효율적으로 저장하기 위해 `HashMap`을 사용합니다.
- 금지된 단어는 Set에 들어 있으므로 해당 여부만 확인하면 됩니다.
```java
Map<String, Integer> countMap = new HashMap<>();

for (String word : words) {
    if (!bannedSet.contains(word)) {
        countMap.put(word, countMap.getOrDefault(word, 0) + 1);
    }
}
```

---

### 4️⃣ 가장 많이 등장한 단어 찾기
- **이유:** 등장 횟수 카운트를 마친 후, 가장 큰 값을 가진 key를 찾기 위해 `Collections.max`를 사용합니다.
- Map의 EntrySet을 순회하며 비교 기준을 value로 설정합니다.
```java
return Collections.max(countMap.entrySet(), Map.Entry.comparingByValue()).getKey();
```

---

## 시간 복잡도 분석
| 연산 | 시간 복잡도 | 공간 복잡도 |
|------|--------------|--------------|
| 전체 처리 | **O(n)** | O(n) |

- `n`은 paragraph의 길이입니다.
- HashMap과 HashSet을 사용해 각 연산을 효율적으로 처리합니다.

## 추가할 수 있는 내용
- [ ] 전체 단어 등장 횟수를 내림차순으로 출력
- [ ] 단어 길이나 알파벳 범위 제한 추가 가능성 고려