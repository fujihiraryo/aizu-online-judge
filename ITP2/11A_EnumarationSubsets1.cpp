#include <iostream>

int n;

int main() {
    std::cin >> n;
    for (int s = 0; s < (1 << n); s++) {
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
