#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    
    long long low = 1, high = (long long)n * m;
    while (low < high) {
        long long mid = (low + high) / 2;
        long long count = 0;
        
        // For each row i, count numbers <= mid by taking min of: column count (m) or mid/i
        for (int i = 1; i <= n; i++) {
            count += min((long long)m, mid / i);
        }
        
        // If we haven't found k numbers yet, search upper half; otherwise search lower half
        if (count < k) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    
    cout << low << endl;
    return 0;
}
