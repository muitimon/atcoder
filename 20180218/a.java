import java.util.Scanner;

public class a{
    public static void main(String[] args){
			Scanner sc = new Scanner(System.in);
			int N = sc.nextInt();
			int A = sc.nextInt();
			int fdiv = N%500;
			if(A-fdiv>=0){
				System.out.println("Yes");
			}else{
				System.out.println("No");
			}
    }
}
