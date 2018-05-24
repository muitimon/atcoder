import java.util.regex.Pattern;
import java.util.Scanner;
import java.util.Arrays;

public class d{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        long N = sc.nextInt();
	sc.nextLine();
	String memo1 = sc.nextLine();
	String memo2 = sc.nextLine();
	for(int i=0; i<N; i++){
	    //String tmp = memo1.charAt(i);
	    if(Pattern.compile("^-?[0-9]+$").matcher((String)memo1.charAt(i)).find()){
		System.out.println("suji");
	    }else{
		System.out.println("moji");
	    }
	}
	//	boolean ans = boolean[N];
	
    }
}
