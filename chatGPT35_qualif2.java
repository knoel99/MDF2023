package com.isograd.exercise;
import java.util.*;

public class IsoContest {
    public static void main( String[] argv ) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] seasons = new int[n];
        int totalDays = 0;
        for (int i = 0; i < n; i++) {
            seasons[i] = sc.nextInt();
            totalDays += seasons[i];
        }
        k = k % totalDays;
        if (k == 0) {
            k = totalDays;
        }
        int currentSeason = 0;
        while (k > seasons[currentSeason]) {
            k -= seasons[currentSeason];
            currentSeason = (currentSeason + 1) % n;
        }
        System.out.println(currentSeason + 1);
    }
}
