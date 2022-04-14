#include <algorithm>
#include <iostream>
#include <vector>

int n;
std::vector<std::pair<int, int>> a;

int main() {
    std::cin >> n;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a.at(i).first >> a.at(i).second;
    }
    std::sort(a.begin(), a.end());
    for (int i = 0; i < n; i++) {
        std::cout << a.at(i).first << " " << a.at(i).second << std::endl;
    }
    return 0;
}
