/**
 * Files: ArrayResizer.cpp
 * Author: Sanny Lin
 * 
 * The ArrayResizer class provides different methods to work with two-dimensional arrays.
 * It allows checking for non-zero rows, counting the number of rows with all non-zero values,
 * and resizing the two-dimensional array to contain only rows with no zeros.
 */

#include <iostream>
using namespace std;

class ArrayResizer{
public:
	static bool isNonZeroRow(int** arr, int rows, int cols, int r);
	static int numNonZeroRows(int** arr, int rows, int cols);
	static int** resize(int** arr, int rows, int cols);
};
// static method shall define outside class

/** 
 * Return true if and only if every value in row r of array2D is non-zero.
 * Precondition: r is a valid row index in array2D
 * Postcondition: array2D is unchanged
 * @param arr: the 2D array to check
 * @param rows: the amount of rows in arr
 * @param cols: the amount of cols in arr
 * @param r: the row index to check in array2D
 * @return: true if every value in row r is non-zero, false otherwise
 */
bool ArrayResizer::isNonZeroRow(int** arr, int rows, int cols, int r){
	for (int i=0; i<cols; i++){
		if (!arr[r][i]) return false;
	}
	return true;
}

/** 
 * Return the number of rows in array2D that contain all non-zero values.
 * Postcondition: array2D is unchanged
 * @param arr: the 2D array to check.
 * @param rows: the amount of rows in arr
 * @param cols: the amount of cols in arr
 * @return: the amount of rows with all non-zero values in array2D
 */
int ArrayResizer::numNonZeroRows(int** arr, int rows, int cols){
	int count = 0;
	for (int i=0; i<rows; i++){
		if (ArrayResizer::isNonZeroRow(arr, rows, cols, i)) count ++;
	}
	return count;
}

/** 
 * Return a new, possibly smaller, two-dimensional array that contains only rows from array2D with no zeros.
 * Precondition: array2D contains at least one column and at least one row with no zeros
 * Postcondition: array2D is unchanged
 * @param arr: the 2D array to resize
 * @param rows: the amount of rows in arr
 * @param cols: the amount of cols in arr
 * @return: new 2D array containing only rows with no zeros from the original array2D
 */
int** ArrayResizer::resize(int** arr, int rows, int cols){
	int newRows = ArrayResizer::numNonZeroRows(arr, rows, cols);
	int** arrNew = (int**)malloc(newRows*sizeof(int*));
	// malloc: front() -> for what
	// sizeof: counting "memory" size (not element quantity!!)
	int count = 0;
	for (int i=0; i<rows; i++){
		if (ArrayResizer::isNonZeroRow(arr, rows, cols, i)){
			arrNew[count] = (int*)malloc(cols*sizeof(int));
			for (int j=0; j<cols; j++){
				arrNew[count][j] = arr[i][j];
			}
			count ++;
		}
	}
	return arrNew;
}

// main
int main(){
	int arr[4][3] = {{2, 1, 0}, {1, 3, 2}, {0, 0, 0}, {4, 5, 6}};  
	int rows = (sizeof(arr)/sizeof(arr[0]));
	int cols = sizeof(arr[0])/sizeof(int*);
	// carry array to heap
	int** arrHeap = (int**)malloc(rows*sizeof(int*));
	for (int i=0; i<rows; i++){
		arrHeap[i] = (int*)malloc(cols*sizeof(int));
		for (int j=0; j<cols; j++){
			arrHeap[i][j] = arr[i][j];
		}
	}
	// check arrHeap
	// for (int i=0; i<rows; i++){
	// 	for (int j=0; j<cols; j++){
	// 		cout << arrHeap[i][j] << ',';
	// 	}
	// }

	cout << ArrayResizer::numNonZeroRows(arrHeap, rows, cols) << endl;

	int** newArr = ArrayResizer::resize(arrHeap, rows, cols);
	for (int i=0; i<ArrayResizer::numNonZeroRows(arrHeap, rows, cols); i++){
		for (int j=0; j<cols; j++){
			cout << newArr[i][j];
			if (j!=cols-1) cout << ',';
		}
		cout << endl;
	}
	// rows can't use "(sizeof(newArr)/sizeof(newArr[0]))": cause memory address is int -> always 4 bytes

	return 0;
}