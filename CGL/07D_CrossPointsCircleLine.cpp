#include <cmath>
#include <iomanip>
#include <iostream>

struct Point {
    double x, y;
};

struct Circle {
    Point center;
    int radius;
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
    Point c;
    double r;
    std::cin >> c.x >> c.y >> r;
    int n;
    std::cin >> n;
    std::cout << std::fixed << std::setprecision(8);
    for (int i = 0; i < n; i++) {
        Point p0, p1;
        std::cin >> p0.x >> p0.y >> p1.x >> p1.y;
        double h = det(p1 - p0, c - p0) / norm(p1 - p0);
        double d = dot(p1 - p0, c - p0) / norm(p1 - p0);
        double k0 = (d - std::sqrt(r * r - h * h)) / norm(p1 - p0);
        double k1 = (d + std::sqrt(r * r - h * h)) / norm(p1 - p0);
        Point q0 = p0 + k0 * (p1 - p0);
        Point q1 = p0 + k1 * (p1 - p0);
        if (!(q0 < q1)) {
            std::swap(q0, q1);
        }
        std::cout << q0.x << " " << q0.y << " " << q1.x << " " << q1.y << std::endl;
    }
    return 0;
}
