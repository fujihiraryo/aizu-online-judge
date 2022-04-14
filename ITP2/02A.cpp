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
            if (!a.at(t).empty()) {
                std::cout << a.at(t).back() << std::endl;
            }
        } else {
            std::cin >> t;
            if (!a.at(t).empty()) {
                a.at(t).pop_back();
            }
        }
    }
    return 0;
}
