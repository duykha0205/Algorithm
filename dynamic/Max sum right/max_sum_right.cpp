// C++ program for Dynamic
// Programming implementation of
// Min Sum Path in a Triangle
#include <bits/stdc++.h>
using namespace std;

// Util function to find minimum sum for a path
int helper(vector<vector<int>>& tri, int i, int j, vector<vector<int>>& dp){
	// Base Case
	if(i == tri.size() ){
	return 0 ;
	}

	// To avoid solving overlapping subproblem
	if(dp[i][j] != -1){
		return dp[i][j] ;
	}


	// Add current to the minimum of the next paths
	// and store it in dp matrix
	return dp[i][j] = tri[i][j] + max(helper(tri, i+1,j, dp), helper(tri,i+1, j+1, dp)) ;
	
	
}


int maxSumPath(vector<vector<int>>& tri) {
	int n = tri.size() ;
	// Initializating of dp matrix
	vector<vector<int>> dp(n, vector<int>(n, -1) ) ;
	// calling helper function
	return helper(tri, 0, 0, dp) ;
}

/* Driver program to test above functions */
int main()
{
	vector<vector<int> > tri{ { 1 },
							{ 2, 1 },
							{ 3, 3, 2 } };
	cout << maxSumPath(tri);
	return 0;
}
