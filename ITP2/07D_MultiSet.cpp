#include <iostream>
#include <set>

int q, t, x, y;
std::multiset<int> a;
std::multiset<int>::iterator it;

int main() {
    std::cin >> q;
    for (int i = 0; i < q; i++) {
        std::cin >> t >> x;
        if (t == 0) {
            a.insert(x);
            std::cout << a.size() << std::endl;
        } else if (t == 1) {
            std::cout << a.count(x) << std::endl;
        } else if (t == 2) {
            a.erase(x);
        } else {
            std::cin >> y;
            for (it = a.lower_bound(x); it != a.upper_bound(y); it++) {
                std::cout << *it << std::endl;
            }
        }
    }
    return 0;
}
