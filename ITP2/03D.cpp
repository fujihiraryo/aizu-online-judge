#include <algorithm>
#include <iostream>
#include <vector>

int n, m;
std::vector<int> a, b;

int main() {
    std::cin >> n;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a.at(i);
    }
    std::cin >> m;
    b.resize(m);
    for (int i = 0; i < m; i++) {
        std::cin >> b.at(i);
    }
    for (int i = 0; i < std::min(m, n); i++) {
        if (a.at(i) < b.at(i)) {
            std::cout << 1 << std::endl;
            return 0;
        } else if (a.at(i) > b.at(i)) {
            std::cout << 0 << std::endl;
            return 0;
        }
    }
    if (n < m) {
        std::cout << 1 << std::endl;
    } else {
        std::cout << 0 << std::endl;
    }
    return 0;
}
