package com.isograd.exercise;
import java.util.*;

public class IsoContest {
    public static void main( String[] argv ) throws Exception {
        String line;
        Scanner sc = new Scanner(System.in);
        line = sc.nextLine();
        /* Lisez les données et effectuez votre traitement */
        int length = line.length();
        if (length == 1) {
            System.out.println(line);
        } else {
            char winner = line.charAt(0);
            for (int i = 1; i < length; i++) {
                char current = line.charAt(i);
                if (current == 'C' && winner == 'F') {
                    winner = current;
                } else if (current == 'F' && winner == 'P') {
                    winner = current;
                } else if (current == 'P' && winner == 'C') {
                    winner = current;
                }
            }
            System.out.println(winner);
        }
    }
}
