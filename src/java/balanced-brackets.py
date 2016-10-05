import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            String s = in.next();
            Stack<Character> brackets = new Stack<Character>();
            for ( int i = 0 ; i < s.length() ; i++) {
                char bracket = s.charAt(i);
                if ( bracket == '(' || bracket == '{' || bracket == '[' ){
                    brackets.push(bracket);
                }
                if ( bracket == ')' || bracket == '}' || bracket == ']' ) {
                    if ( brackets.size() > 0 ) {
                      char topElement = brackets.peek();
                      if ( (topElement == '('  && bracket == ')' ) ||
                           (topElement == '{'  && bracket == '}' ) ||
                           (topElement == '['  && bracket == ']' )
                         ) {
                           brackets.pop();
                           }
                    }
                }
            }
            String answer = "NO";
            if ( brackets.empty() ) {
                answer = "YES";
            }
            System.out.println(answer);
       }
    }
}
