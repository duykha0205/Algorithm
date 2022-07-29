// C++ program for insertion sort

#include <iostream>
using namespace std;

void printArray(int arr[], int n)
{
	int i;
	for (i = 0; i < n; i++)
		cout << arr[i] << " ";
	cout << endl;
}

// Function to sort an array using
// insertion sort
void insertionSort(int arr[], int n)
{
	int i, key, j;
	for (i = 1; i < n; i++)
	{
		key = arr[i];
		j = i - 1;

		// Move elements of arr[0..i-1],
		// that are greater than key, to one
		// position ahead of their
		// current position
        cout << "\n----------------------\n";
		while (j >= 0 && arr[j] > key)
		{
			arr[j + 1] = arr[j];
			j = j - 1;
            printArray(arr, n);
		}
        cout << "\n----------------------\n";

		arr[j + 1] = key;
	}
}

// A utility function to print an array
// of size n


// Driver code
int main()
{
	int arr[] = { 12, 11, 13, 5, 6 };
	int N = sizeof(arr) / sizeof(arr[0]);

	insertionSort(arr, N);
	printArray(arr, N);

	return 0;
}
// This is code is contributed by rathbhupendra