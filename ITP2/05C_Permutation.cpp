#include <algorithm>
#include <iostream>
#include <vector>

int n, x;
std::vector<int> a;

int main() {
    std::cin >> n;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a.at(i);
    }
    if (!std::is_sorted(a.begin(), a.end())) {
        std::prev_permutation(a.begin(), a.end());
        for (int i = 0; i < n - 1; i++) {
            std::cout << a.at(i) << " ";
        }
        std::cout << a.back() << std::endl;
        std::next_permutation(a.begin(), a.end());
    }
    for (int i = 0; i < n - 1; i++) {
        std::cout << a.at(i) << " ";
    }
    std::cout << a.back() << std::endl;
    if (!std::is_sorted(a.begin(), a.end(), std::greater<int>())) {
        std::next_permutation(a.begin(), a.end());
        for (int i = 0; i < n - 1; i++) {
            std::cout << a.at(i) << " ";
        }
        std::cout << a.back() << std::endl;
    }
    return 0;
}
