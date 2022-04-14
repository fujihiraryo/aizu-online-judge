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
    std::cout << std::includes(a.begin(), a.end(), b.begin(), b.end())
              << std::endl;
    return 0;
}
