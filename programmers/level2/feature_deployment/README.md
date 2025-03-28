# 기능 개발 (Feature Deployment)

## 문제 설명
소프트웨어 기능이 여러 개 개발되고 있으며, 각 기능은 진도가 100%일 때 배포됩니다.  
**앞에 있는 기능이 아직 완료되지 않으면 뒤의 기능은 배포되지 못합니다.**  
각 기능마다 매일 작업 속도가 정해져 있을 때, **각 배포일마다 몇 개의 기능이 배포되는지** 구하는 프로그램을 작성하세요.

## 입력
- `int[] progresses`: 각 기능의 현재 개발 진도 (0 ≤ 진도 ≤ 100)  
- `int[] speeds`: 각 기능의 하루 작업 속도 (1 ≤ 속도 ≤ 100)

## 출력
- 각 배포일마다 배포되는 기능 수를 배열로 반환

## 예제 입력
```java
int[] progresses = {93, 30, 55};
int[] speeds = {1, 30, 5};
```

## 예제 출력
```java
[2, 1]
```

## 해결 방법
### 1️⃣ 작업 일수 계산 + 큐 시뮬레이션 - O(n)
- 각 기능마다 완료까지 걸리는 일수를 먼저 계산
- 가장 앞의 기능부터 순서대로 배포 가능한지 확인 (큐 활용)
- 현재 기능보다 늦게 끝나는 작업이 나오면 그 이전까지 배포 처리

```java
import java.util.*;

public class FeatureDeployment {
    public static int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> days = new LinkedList<>();
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < progresses.length; i++) {
            int remain = 100 - progresses[i];
            int day = (int) Math.ceil((double) remain / speeds[i]);
            days.offer(day);
        }

        while (!days.isEmpty()) {
            int current = days.poll();
            int count = 1;
            while (!days.isEmpty() && days.peek() <= current) {
                days.poll();
                count++;
            }
            result.add(count);
        }

        return result.stream().mapToInt(i -> i).toArray();
    }
}
```

## 시간 복잡도 분석
| 연산 | 시간 복잡도 |
|------|--------------|
| 전체 처리 | **O(n)** |

## 추가할 수 있는 내용
- [ ] 기능 배포 날짜를 함께 출력하는 버전
- [ ] 병렬 개발 가능 시뮬레이션 버전 비교

