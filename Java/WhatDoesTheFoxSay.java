import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

/**
 * Template for "What does the fox say?"
 * Problem ID: whatdoesthefoxsay
 * https://open.kattis.com/problems/whatdoesthefoxsay
 */
public class WhatDoesTheFoxSay {
public static void main(String[] args) {
    // We need to create and scanner and get the number of cases to be read in.
    Scanner in = new Scanner(System.in);
    int cases = Integer.parseInt(in.nextLine());
    String fox = "what does the fox say?";
    for (int x = 0; x < cases; x++) {
    // Order matters for this problem, so we will use an ArrayList to store the second line of input.
      ArrayList<String> allSoundsHeard = new ArrayList<String>(Arrays.asList(in.nextLine().split(" ")));
      String animalSound = in.nextLine();
      while (!(animalSound.equals(fox))) {
        String sound = animalSound.split(" ")[2];
        while (allSoundsHeard.contains(sound)) {
          allSoundsHeard.remove(sound);
        }
        animalSound = in.nextLine();
      }
      

      // This will output what is left in the ArrayList after filtering out the other sounds.
      System.out.println(String.join(" ", allSoundsHeard));
    }
  }
}