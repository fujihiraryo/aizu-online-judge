#include <iostream>
#include <map>
#include <string>

int q, t, x;
std::string key, L, R;
std::multimap<std::string, int> m;
std::multimap<std::string, int>::iterator it;

int main() {
    std::cin >> q;
    for (int i = 0; i < q; i++) {
        std::cin >> t;
        if (t == 0) {
            std::cin >> key >> x;
            m.insert(std::multimap<std::string, int>::value_type(key, x));
        } else if (t == 1) {
            std::cin >> key;
            for (it = m.equal_range(key).first; it != m.equal_range(key).second;
                 it++) {
                std::cout << it->second << std::endl;
            }
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
