#include <algorithm>
#include <iostream>
#include <vector>

int n, q, b, m, e;
std::vector<int> a;

int main() {
    std::cin >> n;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a.at(i);
    }
    std::cin >> q;
    while (q--) {
        std::cin >> b >> m >> e;
        std::rotate(a.begin() + b, a.begin() + m, a.begin() + e);
    }
    for (int i = 0; i < n - 1; i++) {
        std::cout << a.at(i) << " ";
    }
    std::cout << a.back() << std::endl;
    return 0;
}
