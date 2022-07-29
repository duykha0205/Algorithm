#include<iostream>
using namespace std;

void MinMax_recur(int *arr, int l, int r, int& mn, int& mx){
    if(l>=r-1){
        if(arr[l] > arr[r]){
            mn = arr[r];
            mx = arr[l];
        }else{
            mn = arr[l];
            mx = arr[r];
        }
    }else{
        int m = int((l+r)/2);
        int mn_l = 0;
        int mx_l = 0;
        int mn_r = 0;
        int mx_r = 0;
        MinMax_recur(arr, l, m, mn_l, mx_l);
        MinMax_recur(arr, m+1, r, mn_r, mx_r);
        mn = mn_l < mn_r ? mn_l : mn_r;
        mx = mx_l > mx_r ? mx_l : mx_r;
    }
}

void MinMax_loop(int *arr, int l, int r, int& mn, int& mx){
    mn = mx = arr[0];
    // for (int i=0; i<n; i++){
    //     if (arr[i] < mn){
    //         mn = arr[i];
    //     }else if(arr[i] > mx){
    //         mx = arr[i];
    //     }
    // }
    if(l>=r-1){
        if(arr[l] > arr[r]){
            mn = arr[r];
            mx = arr[l];
        }else{
            mn = arr[l];
            mx = arr[r];
        }
    }else{
        int m = int((l+r)/2);
        int mn_l = 0;
        int mx_l = 0;
        int mn_r = 0;
        int mx_r = 0;
        MinMax_recur(arr, l, m, mn_l, mx_l);
        MinMax_recur(arr, m+1, r, mn_r, mx_r);
        mn = mn_l < mn_r ? mn_l : mn_r;
        mx = mx_l > mx_r ? mx_l : mx_r;
    }
    while(l<=r){
        if(arr[l] > arr[r]){
            mn = arr[r];
            mx = arr[l];
        }else{
            mn = arr[l];
            mx = arr[r];
        }
        l++y;
        r--;
    }
}

int main(){
    int* a = new int[5];
    a[0] = 1;
    a[1] = 5;
    a[2] = 3;
    a[3] = 7;
    a[4] = 3;

    int mn = 0;
    int mx = 0;
    MinMax_recur(a, 0, 4, mn, mx);
    cout << mn << "-" << mx << endl;

    MinMax_loop(a, 0, 4, mn, mx);
    cout << mn << "-" << mx << endl;

    return 0;
}