#include <iostream>

#include "boost/multiprecision/cpp_int.hpp"

int main() {
    boost::multiprecision::cpp_int a, b;
    std::cin >> a >> b;
    std::cout << a + b << std::endl;
    return 0;
}
