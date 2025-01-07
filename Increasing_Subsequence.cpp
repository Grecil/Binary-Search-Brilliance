#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    // dp[i] stores smallest value that can end an increasing subsequence of length i
    vector<int> dp(n + 2);
    dp[0] = INT_MIN;
    fill(dp.begin() + 1, dp.end(), INT_MAX);
    
    for(int i = 0; i < n; i++) {
        // Find the position where current element should be inserted to maintain increasing order
        int x = upper_bound(dp.begin(), dp.end(), arr[i]) - dp.begin();
        // If current element can create a better increasing subsequence of length x, update dp
        if(dp[x-1] < arr[i] && arr[i] < dp[x]) {
            dp[x] = arr[i];
        }
    }
    
    // First infinity position minus 1 gives the length of longest increasing subsequence
    int ans = lower_bound(dp.begin(), dp.end(), INT_MAX) - dp.begin() - 1;
    cout << ans << endl;
    
    return 0;
}
