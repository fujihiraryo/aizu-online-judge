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
        } else if (t == 1) {
            std::cout << m[key] << std::endl;
        } else {
            m.erase(key);
        }
    }
    return 0;
}
