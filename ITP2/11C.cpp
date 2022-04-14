#include <iostream>
#include <stack>

int n, k, b, x, S, T;
std::stack<int> stack;

int main() {
    std::cin >> n;
    std::cin >> k;
    while (k--) {
        std::cin >> b;
        T |= (1 << b);
    }
    x = T;
    while (x > 0) {
        stack.push(x);
        x = (x - 1) & T;
    }
    stack.push(0);
    while (!stack.empty()) {
        S = stack.top();
        stack.pop();
        std::cout << S << ":";
        for (int i = 0; i < n; i++) {
            if ((1 << i) & S) {
                std::cout << " " << i;
            }
        }
        std::cout << std::endl;
    }
    return 0;
}
