import java.util.Scanner;

public class Main{
    Scanner sc = new Scanner(System.in);
    public static void main(String[] args){
	Main app = new Main();
	app.init();
    }
    private int[][] init(){
	int h = sc.nextInt();
	int w = sc.nextInt();
	sc.nextLine();
	int[][] masu = new int[h+2][w+2];
	for(int i = 0;i < h; i++){
	    String[] line = sc.nextLine().split("");
	    for(int j = 0;j < w; j++){
		//System.out.println(line[0]);
		if(line[j].equals("#")){
		    masu[i+1][j+1] = 1;
		}
	    }
	}
	return masu;
    }

    private void judge(int[][] masu){
	for(int i = 0;i < h; i++){
	    for(int j = 0;j < w; j++){
		System.out.print(masu[i][j]);
	    }
	    System.out.println();
	}


    }
}
