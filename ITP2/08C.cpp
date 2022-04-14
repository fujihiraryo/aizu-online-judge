#include <iostream>
#include <map>
#include <string>

int q, t, x;
std::string key, L, R;
std::map<std::string, int> m;
std::map<std::string, int>::iterator it;

int main() {
    std::cin >> q;
    for (int i = 0; i < q; i++) {
        std::cin >> t;
        if (t == 0) {
            std::cin >> key >> x;
            m[key] = x;
        } else if (t == 1) {
            std::cin >> key;
            std::cout << m[key] << std::endl;
        } else if (t == 2) {
            std::cin >> key;
            m.erase(key);
        } else {
            std::cin >> L >> R;
            for (it = m.lower_bound(L); it != m.upper_bound(R); it++) {
                if (it->second == 0) {
                    continue;
                }
                std::cout << it->first << " " << it->second << std::endl;
            }
        }
    }
    return 0;
}
