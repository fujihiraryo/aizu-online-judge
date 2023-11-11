#include <iostream>
#include <vector>

int q, t, x, p;
std::vector<int> a;

int main() {
    std::cin >> q;
    for (int i = 0; i < q; i++) {
        std::cin >> t;
        if (t == 0) {
            std::cin >> x;
            a.push_back(x);
        } else if (t == 1) {
            std::cin >> p;
            std::cout << a.at(p) << std::endl;
        } else {
            a.pop_back();
        }
    }
    return 0;
}
