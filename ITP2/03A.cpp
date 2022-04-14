#include <algorithm>
#include <iostream>

int a, b, c, min, max;

int main() {
    std::cin >> a >> b >> c;
    min = std::min(std::min(a, b), c);
    max = std::max(std::max(a, b), c);
    std::cout << min << " " << max << std::endl;
    return 0;
}
