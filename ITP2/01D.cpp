#include <iostream>
#include <vector>

int n, q, s, t, x;
std::vector<std::vector<int>> a;

int main() {
    std::cin >> n >> q;
    a.resize(n);
    for (int i = 0; i < q; i++) {
        std::cin >> s;
        if (s == 0) {
            std::cin >> t >> x;
            a.at(t).push_back(x);
        } else if (s == 1) {
            std::cin >> t;
            if (a.at(t).empty()) {
                std::cout << std::endl;
            } else {
                for (int j = 0; j < a.at(t).size() - 1; j++) {
                    std::cout << a.at(t).at(j) << " ";
                }
                std::cout << a.at(t).back() << std::endl;
            }
        } else {
            std::cin >> t;
            a.at(t).clear();
        }
    }
    return 0;
}
