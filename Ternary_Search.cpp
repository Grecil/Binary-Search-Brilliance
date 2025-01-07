#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    int left = 0, right = n-1;
    while(right - left >= 3) {
        int m1 = left + (right - left)/3;
        int m2 = right - (right - left)/3;
        
        if(arr[m1] < arr[m2]) {
            left = m1;
        } else {
            right = m2;
        }
    }
    
    int peak = arr[left];
    for(int i = left; i <= right; i++) {
        peak = max(peak, arr[i]);
    }
    
    cout << peak << endl;
    return 0;
}
