#include <algorithm>
#include <iostream>
#include <string>
#include <tuple>
#include <vector>

int n;
std::vector<std::tuple<int, int, std::string, long, std::string>> a;

int main() {
    std::cin >> n;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        std::cin >> std::get<0>(a.at(i));
        std::cin >> std::get<1>(a.at(i));
        std::cin >> std::get<2>(a.at(i));
        std::cin >> std::get<3>(a.at(i));
        std::cin >> std::get<4>(a.at(i));
    }
    std::sort(a.begin(), a.end());
    for (int i = 0; i < n; i++) {
        std::cout << std::get<0>(a.at(i)) << " ";
        std::cout << std::get<1>(a.at(i)) << " ";
        std::cout << std::get<2>(a.at(i)) << " ";
        std::cout << std::get<3>(a.at(i)) << " ";
        std::cout << std::get<4>(a.at(i)) << std::endl;
    }
    return 0;
}
