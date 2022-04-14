#include <bitset>
#include <iostream>

int n, k;

int main() {
    std::cin >> n >> k;
    for (int s = 0; s < (1 << n); s++) {
        if (std::bitset<20>(s).count() != k) {
            continue;
        }
        std::cout << s << ":";
        for (int i = 0; i < n; i++) {
            if ((1 << i) & s) {
                std::cout << " " << i;
            }
        }
        std::cout << std::endl;
    }
    return 0;
}
