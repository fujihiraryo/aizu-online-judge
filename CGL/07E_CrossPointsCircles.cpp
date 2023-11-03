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

int main() {
    Point p0, p1;
    double r0, r1;
    std::cin >> p0.x >> p0.y >> r0;
    std::cin >> p1.x >> p1.y >> r1;

    double d = norm(p0 - p1);
    double d0 = (d + (r0 * r0 - r1 * r1) / d) / 2;

    Point t = p0 + (d0 / d) * (p1 - p0);
    Point h;
    h.x = (p1 - p0).y / norm(p1 - p0);
    h.y = -(p1 - p0).x / norm(p1 - p0);

    Point q0 = t + std::sqrt(r0 * r0 - d0 * d0) * h;
    Point q1 = t - std::sqrt(r0 * r0 - d0 * d0) * h;

    if (!(q0 < q1)) {
        std::swap(q0, q1);
    }
    std::cout << q0 << " " << q1 << std::endl;
}
