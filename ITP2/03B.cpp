#include <algorithm>
#include <iostream>
#include <vector>

std::vector<int> a;
int n, q, c, b, e, min, max;

int main() {
    std::cin >> n;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a.at(i);
    }
    std::cin >> q;
    while (q--) {
        std::cin >> c >> b >> e;
        if (c == 0) {
            min = INT32_MAX;
            for (int i = b; i < e; i++) {
                min = std::min(min, a.at(i));
            }
            std::cout << min << std::endl;
        } else {
            max = -INT32_MAX;
            for (int i = b; i < e; i++) {
                max = std::max(max, a.at(i));
            }
            std::cout << max << std::endl;
        }
    }
    return 0;
}
