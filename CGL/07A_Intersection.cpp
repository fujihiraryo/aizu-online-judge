#include <cmath>
#include <iostream>

struct Point {
    int x, y;
};

struct Circle {
    Point center;
    int radius;
};

Point operator-(Point p, Point q) {
    return Point{p.x - q.x, p.y - q.y};
}

double norm2(Point p) {
    return p.x * p.x + p.y * p.y;
}

int countCommonTangent(Circle c0, Circle c1) {
    int d2 = norm2(c0.center - c1.center);
    int r0 = c0.radius;
    int r1 = c1.radius;
    if (std::pow(r0 + r1, 2) < d2) {
        return 4;
    }
    if (std::pow(r0 + r1, 2) == d2) {
        return 3;
    }
    if (std::pow(r0 - r1, 2) < d2) {
        return 2;
    }
    if (std::pow(r0 - r1, 2) == d2) {
        return 1;
    }
    return 0;
}

int main() {
    Circle c0;
    Circle c1;
    std::cin >> c0.center.x >> c0.center.y >> c0.radius;
    std::cin >> c1.center.x >> c1.center.y >> c1.radius;
    std::cout << countCommonTangent(c0, c1) << std::endl;
    return 0;
}
