#include <cmath>
#include <iomanip>
#include <iostream>

struct Point {
    double x, y;
};

Point operator+(Point p, Point q) { return Point{p.x + q.x, p.y + q.y}; }
Point operator-(Point p, Point q) { return Point{p.x - q.x, p.y - q.y}; }
Point operator*(double a, Point p) { return Point{a * p.x, a * p.y}; }
Point operator/(Point p, double a) { return Point{p.x / a, p.y / a}; }
Point operator~(Point p) { return Point{-p.y, p.x}; }
double operator,(Point p, Point q) { return p.x * q.x + p.y * q.y; }
std::ostream& operator<<(std::ostream& stream, const Point& p) {
    stream << std::fixed << std::setprecision(15) << p.x << " " << p.y;
    return stream;
}
Point reflection(Point p, Point q) { return q - 2 * ((~p, q) / (p, p)) * (~p); }

int main() {
    Point p0, p1, q, r;
    int n;
    std::cin >> p0.x >> p0.y >> p1.x >> p1.y;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> q.x >> q.y;
        std::cout << reflection(p1 - p0, q - p0) + p0 << std::endl;
    }
}
