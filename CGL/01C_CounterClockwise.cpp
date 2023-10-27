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
bool is_clockwise(Point p, Point q) { return p.x * q.y < p.y * q.x; }
bool is_propotional(Point p, Point q) { return p.x * q.y == p.y * q.x; }

int main() {
    Point p0, p1, p2;
    int n;
    std::cin >> p0.x >> p0.y >> p1.x >> p1.y;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> p2.x >> p2.y;
        if (is_clockwise(p2 - p0, p1 - p0)) {
            std::cout << "COUNTER_CLOCKWISE" << std::endl;
        } else if (is_clockwise(p1 - p0, p2 - p0)) {
            std::cout << "CLOCKWISE" << std::endl;
        } else if (is_propotional(p1 - p0, p2 - p0)) {
            if ((p1 - p0, p2 - p0) < 0) {
                std::cout << "ONLINE_BACK" << std::endl;
            } else if ((p2 - p0, p2 - p0) > (p1 - p0, p1 - p0)) {
                std::cout << "ONLINE_FRONT" << std::endl;
            } else {
                std::cout << "ON_SEGMENT" << std::endl;
            }
        }
    }
}
