#include <iostream>
#include <list>

int q, t, x, d;
std::list<int> a;
std::list<int>::iterator c;

int main() {
    c = a.end();
    std::cin >> q;
    for (int i = 0; i < q; i++) {
        std::cin >> t;
        if (t == 0) {
            std::cin >> x;
            c = a.insert(c, x);
        } else if (t == 1) {
            std::cin >> d;
            if (d > 0) {
                for (int j = 0; j < d; j++) {
                    c++;
                }
            } else {
                for (int j = 0; j < -d; j++) {
                    c--;
                }
            }
        } else {
            c = a.erase(c);
        }
    }
    c = a.begin();
    while (c != a.end()) {
        std::cout << *c << std::endl;
        c++;
    }
    return 0;
}
