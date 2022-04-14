#include <bitset>
#include <iostream>
#include <vector>

std::vector<std::bitset<64>> mask;
std::bitset<64> flag;
int n, k, b, q, t, x;

int main() {
    std::cin >> n;
    mask.resize(n, 0);
    for (int i = 0; i < n; i++) {
        std::cin >> k;
        while (k--) {
            std::cin >> b;
            mask[i].set(b, 1);
        }
    }
    std::cin >> q;
    while (q--) {
        std::cin >> t >> x;
        if (t == 0) {
            std::cout << flag.test(x) << std::endl;
        } else if (t == 1) {
            flag |= mask[x];
        } else if (t == 2) {
            flag &= ~mask[x];
        } else if (t == 3) {
            flag ^= mask[x];
        } else if (t == 4) {
            std::cout << (mask[x] == (flag & mask[x])) << std::endl;
        } else if (t == 5) {
            std::cout << (flag & mask[x]).any() << std::endl;
        } else if (t == 6) {
            std::cout << (flag & mask[x]).none() << std::endl;
        } else if (t == 7) {
            std::cout << (flag & mask[x]).count() << std::endl;
        } else {
            std::cout << (flag & mask[x]).to_ullong() << std::endl;
        }
    }
    return 0;
}
