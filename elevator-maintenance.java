import java.util.Comparator;
import java.util.PriorityQueue;

public class Solution {
    public static void main(String args[]) {
        String[] l = {"1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"};
        l = solution(l);
        for(int i=0;i<l.length;i++) {
            System.out.println(l[i]);
        }
    }
    public static String[] solution(String[] l) {
        String[] out = new String[l.length];
        PriorityQueue<String> pq = new PriorityQueue<String>(l.length,new VersionComparator());
        for (String lStr : l) {
            pq.add(lStr);
        }
        for (int i=l.length-1;i>=0;i--) {
            out[i]=pq.poll();
        }
        return out;
    }
}

class VersionComparator implements Comparator<String> {
    public int compare(String ver1, String ver2) {
        Integer[] ver1_split = fillAndPad(ver1.split("\\."));
        Integer[] ver2_split = fillAndPad(ver2.split("\\."));
        for(int i=0;i<3;i++) {
            if(ver1_split[i]<ver2_split[i]) {
                return 1;
            }
            else if(ver1_split[i]>ver2_split[i]) {
                return -1;
            }
        }
        return 0;
    }

    Integer[] fillAndPad(String str_array[]) {
        Integer[] init = {-1,-1,-1};
        for(int i=0;i<str_array.length;i++) {
            init[i]=Integer.valueOf(str_array[i]);
        }
        return init;
    } 
}
