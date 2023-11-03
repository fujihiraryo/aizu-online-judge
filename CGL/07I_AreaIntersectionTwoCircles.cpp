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

bool operator<(Point p, Point q) {
    if (p.x != q.x) {
        return p.x < q.x;
    }
    return p.y < q.y;
}

std::ostream& operator<<(std::ostream& stream, const Point& p) {
    stream << std::fixed << std::setprecision(15) << p.x << " " << p.y;
    return stream;
}

double norm(Point p) {
    return std::sqrt(p.x * p.x + p.y * p.y);
}

double dot(Point p, Point q) {
    return p.x * q.x + p.y * q.y;
}

double det(Point p, Point q) {
    return p.x * q.y - p.y * q.x;
}

int main() {
    std::cout << std::fixed << std::setprecision(8);

    Point p0, p1;
    double r0, r1;
    std::cin >> p0.x >> p0.y >> r0;
    std::cin >> p1.x >> p1.y >> r1;

    double d = norm(p0 - p1);

    if (d >= r0 + r1) {
        std::cout << 0 << std::endl;
        return 0;
    }

    if (d <= std::abs(r0 - r1)) {
        // contain
        double r = std::min(r0, r1);
        std::cout << std::acos(-1) * r * r << std::endl;
        return 0;
    }

    double a0 = 2 * std::acos((r0 * r0 - r1 * r1 + d * d) / (2 * r0 * d));
    double a1 = 2 * std::acos((r1 * r1 - r0 * r0 + d * d) / (2 * r1 * d));
    double ans = (r0 * r0 * a0 + r1 * r1 * a1 - r0 * r0 * std::sin(a0) - r1 * r1 * std::sin(a1)) / 2;
    std::cout << ans << std::endl;
}
