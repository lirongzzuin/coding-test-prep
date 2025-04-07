# 베스트 앨범 (Best Album)

## ✅ 문제 설명

각 곡의 장르와 재생 횟수가 주어집니다.
- `genres[i]`: i번째 곡의 장르 (예: "pop")
- `plays[i]`: i번째 곡의 재생 횟수 (예: 3100)

"베스트 앨범"을 만들기 위해 다음 기준을 따릅니다:

### 📌 수록 기준
1. 총 재생 횟수가 많은 장르를 먼저 선택합니다.
2. 장르 내에서 재생 횟수가 많은 곡을 우선으로 수록합니다.
3. 재생 횟수가 같을 경우 고유 번호(index)가 낮은 곡을 먼저 수록합니다.
4. 각 장르에서 최대 두 곡만 수록합니다.

---

## 📥 입력

- `genres.length == plays.length`
- 1 이상 10,000 이하의 정수 길이
- 장르 배열과 재생 횟수 배열이 주어집니다.

---

## 📤 출력

- 위 기준에 따라 수록된 곡들의 고유 번호(index)를 순서대로 담은 배열

---

## 💡 예제

```java
genres = ["classic", "pop", "classic", "classic", "pop"];
plays = [500, 600, 150, 800, 2500];
// 출력: [4, 1, 3, 0]
```

---

## 🔍 풀이 흐름 및 설명

### 1️⃣ 장르별 총 재생 횟수 계산
- **이유:** 장르 우선순위를 결정하기 위해 필요합니다.
```java
Map<String, Integer> genreToPlays = new HashMap<>();
for (int i = 0; i < genres.length; i++) {
    genreToPlays.put(genres[i], genreToPlays.getOrDefault(genres[i], 0) + plays[i]);
}
```

### 2️⃣ 장르별 곡 정보 저장
- **이유:** 각 장르 내 곡들을 정렬하고 선별하기 위함입니다.
```java
Map<String, List<int[]>> genreToSongs = new HashMap<>();
for (int i = 0; i < genres.length; i++) {
    genreToSongs.computeIfAbsent(genres[i], v -> new ArrayList<>())
                .add(new int[]{i, plays[i]});
}
```

### 3️⃣ 장르를 총 재생 횟수 기준으로 정렬
```java
List<String> sortedGenres = genreToPlays.entrySet().stream()
    .sorted((a, b) -> b.getValue() - a.getValue())
    .map(Map.Entry::getKey)
    .collect(Collectors.toList());
```

### 4️⃣ 각 장르 내 곡들을 재생 횟수 기준으로 정렬 후 최대 2곡 선택
```java
List<Integer> result = new ArrayList<>();
for (String genre : sortedGenres) {
    List<int[]> songs = genreToSongs.get(genre);
    songs.sort((a, b) -> b[1] == a[1] ? a[0] - b[0] : b[1] - a[1]);

    for (int i = 0; i < Math.min(2, songs.size()); i++) {
        result.add(songs.get(i)[0]);
    }
}
```

---

## ⏱️ 시간 복잡도

| 연산 항목             | 시간 복잡도    |
|----------------------|----------------|
| 총 재생 횟수 계산      | O(n)           |
| 정렬 및 선별           | O(n log n)     |

---

## ✅ 전체 코드 (Java)

```java
import java.util.*;
import java.util.stream.Collectors;

public class BestAlbum {
    public static int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> genreToPlays = new HashMap<>();
        Map<String, List<int[]>> genreToSongs = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            genreToPlays.put(genres[i], genreToPlays.getOrDefault(genres[i], 0) + plays[i]);
            genreToSongs.computeIfAbsent(genres[i], v -> new ArrayList<>())
                        .add(new int[]{i, plays[i]});
        }

        List<String> sortedGenres = genreToPlays.entrySet().stream()
            .sorted((a, b) -> b.getValue() - a.getValue())
            .map(Map.Entry::getKey)
            .collect(Collectors.toList());

        List<Integer> result = new ArrayList<>();
        for (String genre : sortedGenres) {
            List<int[]> songs = genreToSongs.get(genre);
            songs.sort((a, b) -> b[1] == a[1] ? a[0] - b[0] : b[1] - a[1]);

            for (int i = 0; i < Math.min(2, songs.size()); i++) {
                result.add(songs.get(i)[0]);
            }
        }

        return result.stream().mapToInt(i -> i).toArray();
    }

    public static void main(String[] args) {
        String[] genres = {"classic", "pop", "classic", "classic", "pop"};
        int[] plays = {500, 600, 150, 800, 2500};
        System.out.println(Arrays.toString(solution(genres, plays))); // [4, 1, 3, 0]
    }
}
```