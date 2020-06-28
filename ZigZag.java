public class ZigZag {
    public static int longestZigZag(int[] sequence){
        if (sequence.length == 0){return 0;}
        if (sequence.length == 1){return 1;}

        int count = 2;
        int base = sequence[1];
        int old_diff = sequence[1] - sequence[0];
        if (old_diff == 0) {
            count = 1;
        }

        for (int k=2;k<sequence.length;k++){
            int new_diff = sequence[k] - base;
            int indicator = old_diff*new_diff;
            if (indicator < 0) {
                count ++;
                old_diff = new_diff;
                base = sequence[k];
            }
            else{
                if (old_diff > 0){
                    base = Math.max(base, sequence[k]);
                } else {
                    base = Math.min(base, sequence[k]);
                }
            }
        }
        return count;
    }
}
