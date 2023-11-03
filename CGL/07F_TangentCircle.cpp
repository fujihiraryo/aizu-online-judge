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

Point ortho(Point p) {
    return Point{p.y, -p.x};
}

int main() {
    Point p, c;
    double r;
    std::cin >> p.x >> p.y;
    std::cin >> c.x >> c.y >> r;

    double d = norm(p - c);
    double k0 = r * r / (d * d);
    double k1 = r * std::sqrt(d * d - r * r) / (d * d);
    Point q0 = c + k0 * (p - c) + k1 * ortho(p - c);
    Point q1 = c + k0 * (p - c) - k1 * ortho(p - c);

    if (!(q0 < q1)) {
        std::swap(q0, q1);
    }
    std::cout << q0 << std::endl;
    std::cout << q1 << std::endl;
}
