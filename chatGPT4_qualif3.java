package com.isograd.exercise;
import java.util.*;

public class IsoContest {
    public static void main(String[] argv) throws Exception {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(); // Nombre d'étages
        int m = sc.nextInt(); // Nombre d'ascenseurs
        int e = sc.nextInt(); // Étage où est situé Jacques
        sc.nextLine(); // Lire la fin de la ligne

        int[] accessible = new int[n];
        accessible[e - 1] = 1;

        for (int i = 0; i < m; i++) {
            int l = sc.nextInt();
            int r = sc.nextInt();
            sc.nextLine(); // Lire la fin de la ligne

            for (int j = l - 1; j < r; j++) {
                if (accessible[j] > 0) {
                    for (int k = l - 1; k < r; k++) {
                        if (j != k && (accessible[k] == 0 || accessible[j] + 1 < accessible[k])) {
                            accessible[k] = accessible[j] + 1;
                        }
                    }
                }
            }
        }

        System.out.println(accessible[n - 1] > 0 ? "YES" : "NO");
    }
}
