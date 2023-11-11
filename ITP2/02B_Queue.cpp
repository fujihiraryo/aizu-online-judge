#include <iostream>
#include <queue>

int n, q, s, t, x;
std::vector<std::queue<int>> a;

int main() {
    std::cin >> n >> q;
    a.resize(n);
    for (int i = 0; i < q; i++) {
        std::cin >> s;
        if (s == 0) {
            std::cin >> t >> x;
            a.at(t).push(x);
        } else if (s == 1) {
            std::cin >> t;
            if (!a.at(t).empty()) {
                std::cout << a.at(t).front() << std::endl;
            }
        } else {
            std::cin >> t;
            if (!a.at(t).empty()) {
                a.at(t).pop();
            }
        }
    }
    return 0;
}
