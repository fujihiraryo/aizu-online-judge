#include <algorithm>
#include <iostream>
#include <vector>

int n, m, x;
std::vector<int> A, B, C;

int main() {
    std::cin >> n;
    while (n--) {
        std::cin >> x;
        A.push_back(x);
    }
    std::cin >> m;
    while (m--) {
        std::cin >> x;
        B.push_back(x);
    }
    std::set_difference(A.begin(), A.end(), B.begin(), B.end(),
                        std::back_inserter(C));
    for (int x : C) {
        std::cout << x << std::endl;
    }
    return 0;
}
