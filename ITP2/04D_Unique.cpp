#include <algorithm>
#include <iostream>
#include <vector>

int n;
std::vector<int> a;
std::vector<int>::iterator it;

int main() {
    std::cin >> n;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a.at(i);
    }
    it = std::unique(a.begin(), a.end());
    a.erase(it, a.end());
    for (int i = 0; i < a.size() - 1; i++) {
        std::cout << a.at(i) << " ";
    }
    std::cout << a.back() << std::endl;
    return 0;
}
