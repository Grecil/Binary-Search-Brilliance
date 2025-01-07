#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<vector<long long>> projects(n);
    vector<long long> end_times(n);
    
    for (int i = 0; i < n; i++) {
        projects[i].resize(3);
        cin >> projects[i][0] >> projects[i][1] >> projects[i][2];
        end_times[i] = projects[i][1];
    }
    
    // Sort projects by end time
    sort(projects.begin(), projects.end(), 
         [](const vector<long long>& a, const vector<long long>& b) {
             return a[1] < b[1];
         });
    sort(end_times.begin(), end_times.end());
    
    // dp[i] represents max profit considering projects [0...i]
    vector<long long> dp(n + 1, 0);
    for (int i = 0; i < n; i++) {
        // Find rightmost project that ends before current project starts
        int prev_project = lower_bound(end_times.begin(), end_times.end(), 
                                     projects[i][0]) - end_times.begin();
        
        // Take maximum of including or excluding current project
        dp[i + 1] = max(dp[i], dp[prev_project] + projects[i][2]);
    }
    
    cout << dp[n] << endl;
    return 0;
}
