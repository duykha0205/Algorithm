#include<iostream>
#include <algorithm>
#include<queue>
using namespace std;

/*
    Link: https://www.geeksforgeeks.org/implementation-of-0-1-knapsack-using-branch-and-bound/ 

*/

struct Item
{
    float weight;
    int value;
};

struct Node
{
    int level, profit, bound;
    float weight;
};

bool cmp(Item a, Item b)
{
    double r1 = (double)a.value / a.weight;
    double r2 = (double)b.value / b.weight;
    return r1 > r2;
}

int bound(Node u, int n, int W, Item arr[]){
    if (u.weight >= W)
        return 0;
  
    
    int profit_bound = u.profit;
  
    
    int j = u.level + 1;
    float totweight = u.weight;

    while ((j < n) && (totweight + arr[j].weight <= W))
    {
        totweight    += arr[j].weight;
        profit_bound += arr[j].value;
        cout << profit_bound << " ";
        j++;
    }
    cout << endl;
  
    if (j < n)
        profit_bound += (W - totweight) * arr[j].value / arr[j].weight;
  
    return profit_bound;
}
void print_Q(queue<Node> Q){
    // for (int i=0; i<Q.size(); i++){
    //     cout <<  Q.front().profit << " ";
    //     Q.pop();
    // }

    while ( ! Q.empty() )
    {
        cout <<  Q.front().profit << " ";
        Q.pop();
    }
    cout << endl;
}

int knapsack(int W, Item arr[], int n){

    sort(arr, arr+n, cmp);
    cout << "arr: " << endl;
    for (int i=0; i< n; i++){
        cout << arr[i].weight << " ";
    }
    cout << endl;

    queue<Node> Q;
    Node u, v;

    u.level = -1;
    u.profit = u.weight = 0;
    Q.push(u);

    int maxProfit = 0;
    while (!Q.empty())
    {   
        cout << "\n----------------\n";
        print_Q(Q);
        u = Q.front();
        Q.pop();
        print_Q(Q);


        // if (u.level == -1)
        //     v.level = 0;

        if (u.level == n-1)
            continue; 

        v.level = u.level + 1;
        v.weight = u.weight + arr[v.level].weight;
        v.profit = u.profit + arr[v.level].value;

        if (v.weight <= W && v.profit > maxProfit)
            maxProfit = v.profit;

        v.bound = bound(v, n, W, arr);

        if (v.bound > maxProfit)
            Q.push(v);
        
        
        cout << "mxprofit: " << maxProfit << endl;
        cout << "v-level: " << v.level << " v-weight: " << v.weight << " v-profit: " << v.profit << " v-bound: " << v.bound << endl; 
  
        v.weight = u.weight;
        v.profit = u.profit;
        v.bound = bound(v, n, W, arr);
        if (v.bound > maxProfit)
            Q.push(v);

        cout << "v-level: " << v.level << " v-wright: " << v.weight << " v-profit: " << v.profit << " v-bound: " << v.bound << endl;  
        cout << "\n----------------\n";
    }
    

    return maxProfit;
}


int main()
{
    int W = 10;   // Weight of knapsack
    Item arr[] = {{2, 40}, {3.14, 50}, {1.98, 100},
                  {5, 95}, {3, 30}};
    int n = sizeof(arr) / sizeof(arr[0]);
  
    cout << "Maximum possible profit = "
         << knapsack(W, arr, n);
  
    return 0;
}
