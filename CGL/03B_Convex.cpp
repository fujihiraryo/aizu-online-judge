#include <cmath>
#include <iomanip>
#include <iostream>
#include <set>
#include <vector>

struct Point {
    int x, y;
};

Point operator-(Point p, Point q) {
    return Point{p.x - q.x, p.y - q.y};
}

int cross(Point p, Point q) {
    return p.x * q.y - p.y * q.x;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<Point> points;
    for (int i = 0; i < n; i++) {
        Point p;
        std::cin >> p.x >> p.y;
        points.push_back(p);
    }
    std::set<int> s;
    for (int i = 0; i < n; i++) {
        Point p0 = points[i];
        Point p1 = points[(i + 1) % n];
        Point p2 = points[(i + 2) % n];
        if (cross(p1 - p0, p2 - p0) < 0) {
            std::cout << 0 << std::endl;
            return 0;
        }
    }
    std::cout << 1 << std::endl;
}
