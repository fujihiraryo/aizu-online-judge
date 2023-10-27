#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

struct Point {
    double x, y;
};

int main() {
    int n;
    std::cin >> n;
    std::vector<Point> points;
    for (int i = 0; i < n; i++) {
        Point p;
        std::cin >> p.x >> p.y;
        points.push_back(p);
    }
    double ans = 0;
    for (int i = 0; i < n; i++) {
        Point p = points[i];
        Point q = points[(i + 1) % n];
        ans += p.x * q.y - p.y * q.x;
    }
    std::cout << std::fixed << std::setprecision(1);
    std::cout << std::abs(ans) / 2 << std::endl;
}
