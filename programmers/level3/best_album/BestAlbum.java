package programmers.level3.best_album;

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