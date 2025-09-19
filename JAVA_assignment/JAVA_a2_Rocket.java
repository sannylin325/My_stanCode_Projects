public class Rocket{
	public static final int SIZE = 3;

	public static void head(int times){
		for (int i=0; i<times; i++){
			for (int j=0; j<times-i; j++){
				System.out.print(' ');
			}
			for (int j=0; j<i+1; j++){
				System.out.print('/');
			}
			for (int j=0; j<i+1; j++){
				System.out.print('\\');
			}
			System.out.println("");
		}
	}

	public static void belt(int times){
		System.out.print('+');
		for (int i=0; i<times*2; i++){
			System.out.print('=');
		}
		System.out.println('+');
	}

	public static void upper(int times){
		for (int i=0; i<times; i++){
			System.out.print('|');
			for (int j=0; j<times-i-1; j++){
				System.out.print('.');
			}
			for (int j=0; j<i+1; j++){
				System.out.print('/');
			}
			for (int j=0; j<i+1; j++){
				System.out.print('\\');
			}
			for (int j=0; j<times-i-1; j++){
				System.out.print('.');
			}		
			System.out.println('|');
		}
	}

	public static void lower(int times){
		for (int i=0; i<times; i++){
			System.out.print('|');
			for (int j=0; j<i; j++){
				System.out.print('.');
			}
			for (int j=0; j<times-i; j++){
				System.out.print('\\');
			}
			for (int j=0; j<times-i; j++){
				System.out.print('/');
			}
			for (int j=0; j<i; j++){
				System.out.print('.');
			}		
			System.out.println('|');
		}
	}

	public static void main(String[] args){
		head(SIZE);
		belt(SIZE);
		upper(SIZE);
		lower(SIZE);
		belt(SIZE);
		head(SIZE);
	}
}