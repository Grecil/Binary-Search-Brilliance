#include <bits/stdc++.h>
using namespace std;

bool canPlaceCows(vector<int>& stalls, int n, int cows, int minDist) {
    int count = 1;
    int lastPos = stalls[0];
    
    for(int i = 1; i < n; i++) {
        if(stalls[i] - lastPos >= minDist) {
            count++;
            lastPos = stalls[i];
            if(count >= cows) return true;
        }
    }
    return false;
}

int main() {
    int n, k;
    cin >> n >> k;
    
    vector<int> stalls(n);
    for(int i = 0; i < n; i++) {
        cin >> stalls[i];
    }
    
    sort(stalls.begin(), stalls.end());
    
    int left = 0;
    int right = stalls[n-1] - stalls[0];
    int result = 0;
    
    while(left <= right) {
        int mid = left + (right - left)/2;
        
        if(canPlaceCows(stalls, n, k, mid)) {
            result = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    cout << result << endl;
    return 0;
}
