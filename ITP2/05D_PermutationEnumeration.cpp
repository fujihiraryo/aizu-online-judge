#include <algorithm>
#include <iostream>
#include <vector>

int n;
std::vector<int> a;

int main() {
    std::cin >> n;
    for (int i = 1; i <= n; i++) {
        a.push_back(i);
    }
    for (int i = 0; i < n - 1; i++) {
        std::cout << a.at(i) << " ";
    }
    std::cout << a.back() << std::endl;
    while (std::next_permutation(a.begin(), a.end())) {
        for (int i = 0; i < n - 1; i++) {
            std::cout << a.at(i) << " ";
        }
        std::cout << a.back() << std::endl;
    }
    return 0;
}
