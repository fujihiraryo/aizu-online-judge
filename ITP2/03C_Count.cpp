#include <iostream>
#include <vector>

int n, q, b, e, k;
std::vector<int> a;

int main() {
    std::cin >> n;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a.at(i);
    }
    std::cin >> q;
    while (q--) {
        std::cin >> b >> e >> k;
        int cnt = 0;
        for (int i = b; i < e; i++) {
            if (a.at(i) == k) {
                cnt++;
            }
        }
        std::cout << cnt << std::endl;
    }
    return 0;
}
