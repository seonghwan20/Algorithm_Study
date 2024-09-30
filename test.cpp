#include <iostream>
#include <algorithm>

int *argSwapSort(int *a, const int n)
{
    int swaps;
    int *arr = new int [n];
    for (int i = 0; i<n; i++){
        arr[i] = i;
    }
    do {
        swaps = 0;
        for (int i = n - 1; i >= 1; i--)  
            if (a[arr[i]] < a[arr[i-1]]) {          
                swap(arr[i], arr[i-1]);       
                swaps += 1;
            }
    } while (swaps > 0);

    return arr;
}

