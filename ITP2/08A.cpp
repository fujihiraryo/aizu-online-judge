#include <iostream>
#include <map>
#include <string>

int q, t, x;
std::string key;
std::map<std::string, int> m;

int main() {
    std::cin >> q;
    for (int i = 0; i < q; i++) {
        std::cin >> t >> key;
        if (t == 0) {
            std::cin >> x;
            m[key] = x;
        } else {
            std::cout << m[key] << std::endl;
        }
    }
    return 0;
}
