import java.util.*;

public class ArrayResizer{
	// methods
	public static boolean isNonZeroRow(int[][] array2D, int r){
		for (int col=0; col<array2D[r].length; col++){
			if (array2D[r][col]==0){
				return false;
			}
		}
		return true;
	}

	public static int numNonZeroRows(int[][] array2D){
		int nonZero = 0;
		for (int row=0; row<array2D.length; row++){
			int count = 0;
			for (int col=0; col<array2D[row].length; col++){
				if (array2D[row][col]==0){
					break;
				}
				count ++;
			}
			if (count==array2D[row].length){
				nonZero ++;
			}
		}
		return nonZero;
	}

	public static int[][] resize(int[][] array2D){
		int num = ArrayResizer.numNonZeroRows(array2D);
		int[][] smaller = new int[num][array2D[0].length];
		int newRow = 0;

		for (int row=0; row<array2D.length; row++){
			int count = 0;
			for (int col=0; col<array2D[row].length; col++){
				if (array2D[row][col]==0){
					break;
				}
				count ++;
			}
			if (count==array2D[row].length){
				int[] section = array2D[row];
				smaller[newRow] = section;
				newRow ++;
			}
		}
		return smaller;
	}

	// main
	public static void main(String[] args){
		int[][] arr = {{2, 1, 0},
					   {1, 3, 2},
					   {0, 0, 0},
					   {4, 5, 6}};
		// System.out.println(ArrayResizer.isNonZeroRow(arr, 0));
		// System.out.println(ArrayResizer.isNonZeroRow(arr, 1));
		// System.out.println(ArrayResizer.isNonZeroRow(arr, 2));
		// System.out.println(ArrayResizer.isNonZeroRow(arr, 3));

		int[][] smaller = ArrayResizer.resize(arr);
		for (int row=0; row<smaller.length; row++){
			for (int col=0; col<smaller[row].length; col++){
				System.out.println(smaller[row][col]);
			}
		}
	}
}