#include <cmath>
#include <iomanip>
#include <iostream>

struct Point {
    double x, y;
};

Point operator-(Point p, Point q) {
    return Point{p.x - q.x, p.y - q.y};
}

Point operator+(Point p, Point q) {
    return Point{p.x + q.x, p.y + q.y};
}

Point operator*(double a, Point p) {
    return Point{a * p.x, a * p.y};
}

double norm(Point p) {
    return std::sqrt(p.x * p.x + p.y * p.y);
}

double cross(Point p, Point q) {
    return p.x * q.y - p.y * q.x;
}

double area(Point p0, Point p1, Point p2) {
    return std::abs(cross(p1 - p0, p2 - p0)) / 2;
}

int main() {
    Point p0, p1, p2;
    std::cin >> p0.x >> p0.y;
    std::cin >> p1.x >> p1.y;
    std::cin >> p2.x >> p2.y;
    double l0 = norm(p1 - p2);
    double l1 = norm(p2 - p0);
    double l2 = norm(p0 - p1);
    double l = l0 + l1 + l2;
    double s = area(p0, p1, p2);
    Point c = (l0 / l) * p0 + (l1 / l) * p1 + (l2 / l) * p2;
    double r = 2 * s / l;
    std::cout << std::fixed << std::setprecision(8);
    std::cout << c.x << " " << c.y << " " << r << std::endl;
}
