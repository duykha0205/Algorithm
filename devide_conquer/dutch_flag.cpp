#include<iostream>
using namespace std;

void swap(char arr[], int a, int b){
    int t = arr[a];
    arr[a] = arr[b];
    arr[b] = t;
}

void dutch_flag1(char arr[], int n){
    int l = 0;
    int r = n-1;
    int m = 0;

    while( m <= r){
        if (arr[m] == 'R'){
            swap(arr, m++, l++);
            continue;
        }
        if (arr[m] == 'W'){
            m++;
            continue;
        }
        if (arr[m] == 'B'){
            swap(arr, m, r--);
            continue;
        }
    }

}
void dutch_flag(char arr[], int n){

    int mid = 0;
    int left = 0;
    int right = n-1;
     while (mid <= right)  
    {  
        switch (arr[mid])  
        {  
        case 'R':  
            swap(arr[left], arr[mid]); 
            left++;
            mid++;
            break;  

        case 'W':  
            mid++;  
            break;  
              
        case 'B':  
            swap(arr[mid], arr[right]);  
            right--;
            break;  
        }  
    }  
}



int main(){
    char arr[] = {'R','W','R','W','B','R','W','B'};    
    //char arr[] = {'W','R','W','R','W','R','W','B','R','W','B'};    
    //char arr[] = {'R','R','W','R','W','B','R','W'};    
    //char arr[] = {'B','B','B','B','B','R','R','R','B','B','W','B','R','W','B'};    
    int n = sizeof(arr)/sizeof(arr[0]);

    cout << "size array: " << n << endl;

    for (int i = 0; i < n; i++)    
        cout << arr[i] << " ";

    cout << endl;
    cout << "-------------------" << endl;
    dutch_flag1(arr, n);
    //swap(arr, 0, 1);

    for (int i = 0; i < n; i++)    
        cout << arr[i] << " ";

    cout << endl;
    cout << "-------------------" << endl;

    if(arr[0] == 'R'){
        cout << "Kha";
    }


    return 0;
}