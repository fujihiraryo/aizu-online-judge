#include <deque>
#include <iostream>

int q, t, d, x, p;
std::deque<int> a;

int main() {
    std::cin >> q;
    for (int i = 0; i < q; i++) {
        std::cin >> t;
        if (t == 0) {
            std::cin >> d;
            std::cin >> x;
            if (d == 0) {
                a.push_front(x);
            } else {
                a.push_back(x);
            }
        } else if (t == 1) {
            std::cin >> p;
            std::cout << a.at(p) << std::endl;
        } else {
            std::cin >> d;
            if (d == 0) {
                a.pop_front();
            } else {
                a.pop_back();
            }
        }
    }
    return 0;
}
