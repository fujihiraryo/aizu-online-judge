#include <iostream>

int n, k, b, T;

int main() {
    std::cin >> n;
    std::cin >> k;
    while (k--) {
        std::cin >> b;
        T |= (1 << b);
    }
    for (int S = 0; S < (1 << n); S++) {
        if ((S & T) != T) {
            continue;
        }
        std::cout << S << ":";
        for (int i = 0; i < n; i++) {
            if ((1 << i) & S) {
                std::cout << " " << i;
            }
        }
        std::cout << std::endl;
    }
    return 0;
}
