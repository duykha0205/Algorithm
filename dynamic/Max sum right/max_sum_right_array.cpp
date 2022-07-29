#include<iostream>
#include<vector>
using namespace std;

int max_sum_right(vector<vector<int> > tri){
	int n = tri.size();
	int m = tri[n-1].size();
	vector<vector<int>> S(n+1, vector<int>(m+1, 0) ) ;

	cout << n << " " << m << endl;

	for (int i=1; i<=n; i++){
		for (int j=1; j<=i; j++){
			cout << "s i-1 j-1: " << S[i-1][j-1] << " " <<S[i-1][j] << " " << tri[i-1][j-1] << endl;
			S[i][j] = max(S[i-1][j-1], S[i-1][j]) + tri[i-1][j-1];
			cout << "i: " << i << " j: " << j << " S: " << S[i][j] << endl;
		}
	}

	int Max = 0;
	int MaxId = 0;
	for (int i=1; i<=m; i++){
		if (Max < S[n][i]){
			Max = S[n][i];
			MaxId = i;
		}
	}

	int *path = new int[n];
	path[n-1] = Max;
	int temp;
	cout << "-----\n";
	for (int i=n; i>1; i--){
		cout << S[i-1][MaxId-1] << " " << S[i-1][MaxId] << endl;
		if (S[i-1][MaxId-1] > S[i-1][MaxId]){
			temp = S[i-1][MaxId-1];
			MaxId--;
		}else{
			temp = S[i-1][MaxId];
		}
		path[i-2] = temp;
	}

	cout << "---path---\n";
	for (int i=0; i<n; i++){
		cout << path[i] << " ";
	}
	cout << endl;
	cout << path[n-1] <<endl;

	return Max;
}


int main(){
	vector<vector<int> > tri{ { 7 },
							{ 8, 8 },
							{ 4, 6, 0 },
							{ 7, 0, 8, 5 }, 
							{ 0, 5, 4, 9, 4 }, 
							};

	cout << "max sum right: " << max_sum_right(tri) << endl;

	return 0;
}