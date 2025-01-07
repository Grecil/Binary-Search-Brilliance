#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n, goal;
    cin >> n >> goal;
    
    vector<long long> machines(n);
    for(long long& x : machines) {
        cin >> x;
    }
    
    long long lo = 0;
    long long hi = 1e18;
    long long ans = 0;
    
    while(lo <= hi) {
        long long mid = (lo + hi) / 2;
        
        long long n_produced = 0;
        for(const long long& machine : machines) {
            n_produced += mid / machine;
            // Check for overflow
            if(n_produced >= goal) break;
        }
        
        if(n_produced >= goal) {
            ans = mid;
            hi = mid - 1;
        }
        else {
            lo = mid + 1;
        }
    }
    
    cout << ans << endl;
    return 0;
}
