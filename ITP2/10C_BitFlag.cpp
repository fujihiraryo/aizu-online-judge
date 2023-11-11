#include <bitset>
#include <iostream>

std::bitset<64> flag;
int q, t, x;

int main() {
    flag = 0;
    std::cin >> q;
    while (q--) {
        std::cin >> t;
        if (t < 4) {
            std::cin >> x;
        }
        if (t == 0) {
            std::cout << flag.test(x) << std::endl;
        } else if (t == 1) {
            flag.set(x, true);
        } else if (t == 2) {
            flag.set(x, false);
        } else if (t == 3) {
            flag.flip(x);
        } else if (t == 4) {
            std::cout << flag.all() << std::endl;
        } else if (t == 5) {
            std::cout << flag.any() << std::endl;
        } else if (t == 6) {
            std::cout << flag.none() << std::endl;
        } else if (t == 7) {
            std::cout << flag.count() << std::endl;
        } else {
            std::cout << flag.to_ullong() << std::endl;
        }
    }
    return 0;
}
