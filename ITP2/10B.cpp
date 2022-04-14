#include <bitset>
#include <iostream>

uint32_t a, b;

int main() {
    std::cin >> a >> b;
    std::cout << std::bitset<32>(a & b) << std::endl;
    std::cout << std::bitset<32>(a | b) << std::endl;
    std::cout << std::bitset<32>(a ^ b) << std::endl;
    return 0;
}
