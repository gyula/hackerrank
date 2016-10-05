import java.io.*;
import java.util.*;
import java.text.*;
import java.util.Date;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String inTime = scan.next();
        SimpleDateFormat readDate = new SimpleDateFormat("hh:mm:ssa");
        SimpleDateFormat convertDate = new SimpleDateFormat("HH:mm:ss");
        Date d = new Date();
        try {
           d = readDate.parse(inTime);
           String outDate = convertDate.format(d);
           System.out.println(outDate);
        } catch (ParseException e) {
           e.printStackTrace();
        }
    }
}
