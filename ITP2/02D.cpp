#include <iostream>
#include <list>
#include <vector>

int n, q, s, t, x, t1, t2;
std::vector<std::list<int>> a;
std::list<int>::iterator it;

int main() {
    std::cin >> n >> q;
    a.resize(n);
    for (int i = 0; i < q; i++) {
        std::cin >> s;
        if (s == 0) {
            std::cin >> t >> x;
            a.at(t).insert(a.at(t).end(), x);
        } else if (s == 1) {
            std::cin >> t;
            if (!a.at(t).empty()) {
                it = a.at(t).begin();
                std::cout << *it;
                it++;
                while (it != a.at(t).end()) {
                    std::cout << " " << *it;
                    it++;
                }
            }
            std::cout << std::endl;
        } else {
            std::cin >> t1 >> t2;
            a.at(t2).splice(a.at(t2).end(), a.at(t1));
            a.at(t1).empty();
        }
    }
    return 0;
}
