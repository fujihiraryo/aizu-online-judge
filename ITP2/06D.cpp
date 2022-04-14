#include <algorithm>
#include <iostream>
#include <vector>

int n, q, k;
std::vector<int> a;

int main() {
    std::cin >> n;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a.at(i);
    }
    std::cin >> q;
    while (q--) {
        std::cin >> k;
        std::cout << std::lower_bound(a.begin(), a.end(), k) - a.begin() << " ";
        std::cout << std::upper_bound(a.begin(), a.end(), k) - a.begin()
                  << std::endl;
    }
    return 0;
}
