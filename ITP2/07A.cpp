#include <iostream>
#include <set>

int q, t, x;
std::set<int> a;

int main() {
    std::cin >> q;
    for (int i = 0; i < q; i++) {
        std::cin >> t >> x;
        if (t == 0) {
            a.insert(x);
            std::cout << a.size() << std::endl;
        } else {
            std::cout << a.count(x) << std::endl;
        }
    }
    return 0;
}
