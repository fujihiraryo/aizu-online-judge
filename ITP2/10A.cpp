#include <bitset>
#include <iostream>

uint32_t x;

int main() {
    std::cin >> x;
    std::cout << std::bitset<32>(x) << std::endl;
    std::cout << std::bitset<32>(~x) << std::endl;
    std::cout << std::bitset<32>(x << 1) << std::endl;
    std::cout << std::bitset<32>(x >> 1) << std::endl;
    return 0;
}
