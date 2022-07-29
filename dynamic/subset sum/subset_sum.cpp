// A Dynamic Programming solution 
// for subset sum problem 
#include <iostream> 
using namespace std; 

// Returns true if there is a subset of set[] 
// with sum equal to given sum 
bool isSubsetSum(int set[], int n, int sum) 
{ 
	// The value of subset[i][j] will be true if 
	// there is a subset of set[0..j-1] with sum 
	// equal to i 
	bool subset[n + 1][sum + 1]; 

	// If sum is 0, then answer is true 
	for (int i = 0; i <= n; i++) 
		subset[i][0] = true; 

	// If sum is not 0 and set is empty, 
	// then answer is false 
	for (int i = 1; i <= sum; i++) 
		subset[0][i] = false; 

	// Fill the subset table in bottom up manner 
	for (int i = 1; i <= n; i++) { 
		for (int j = 1; j <= sum; j++) { 
			if (j < set[i - 1]) 
				subset[i][j] = subset[i - 1][j]; 
			if (j >= set[i - 1]) 
				subset[i][j] = subset[i - 1][j] 
							|| subset[i - 1][j - set[i - 1]]; 
		} 
	} 

	// uncomment this code to print table 
	cout << "\t";
	for (int j = 0; j <= sum; j++) {
		cout << j << "\t";
	}
	cout << "\n\t------------------------------------------------------------------------\n";
	for (int i = 0; i <= n; i++) 
	{
		cout << (i-1 < 0 ? 0 : set[i-1]) << "\t";
		for (int j = 0; j <= sum; j++)  
			cout << subset[i][j] << "\t";
		cout <<"\n"; 
	}

    // print path
	if (subset[n][sum]){
		cout << "----PATH----\n";
		int tem = sum;
		int n_tem = n;
		for (int i = n; i > 0; i--){
			if (i-1 >= 0)
				if (subset[i-1][tem] == 1)
					continue;

			cout << set[i-1] <<  " ";
			tem -= set[i-1];
		}
		cout << "\n------------------\n";
	}


	return subset[n][sum]; 
} 

// Driver code 
int main() 
{ 
	int set[] = { 3, 34, 4, 12, 5, 2 }; 
	int sum = 9; 
	int n = sizeof(set) / sizeof(set[0]); 
	if (isSubsetSum(set, n, sum) == true) 
		cout <<"Found a subset with given sum"; 
	else
		cout <<"No subset with given sum"; 
	return 0; 
} 
