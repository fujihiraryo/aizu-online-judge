#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

const double EPS = 1.0e-10;

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

double dot(Point p, Point q) {
    return p.x * q.x + p.y * q.y;
}

double det(Point p, Point q) {
    return p.x * q.y - p.y * q.x;
}

double areaTri(Point p, Point q) {
    return (p.x * q.y - p.y * q.x) / 2.0;
}

double areaFan(Point p, Point q) {
    if (norm(p - q) < EPS) {
        return 0;
    }
    double sgn = det(p, q) > 0 ? 1.0 : -1.0;
    double a = std::acos(dot(p, q) / (norm(p) * norm(q)));
    return sgn * norm(p) * norm(q) * a / 2.0;
}

Point intersection(Point p, Point q, double r) {
    double h = det(p - q, p) / norm(p - q);
    double d = dot(p - q, p) / norm(p - q);
    double k0 = (d - std::sqrt(r * r - h * h)) / norm(p - q);
    double k1 = (d + std::sqrt(r * r - h * h)) / norm(p - q);
    if (k0 > 0) {
        return p + k0 * (q - p);
    } else {
        return p + k1 * (q - p);
    }
}

std::pair<Point, Point> intersection2(Point p, Point q, double r) {
    double h = det(p - q, p) / norm(p - q);
    double d = dot(p - q, p) / norm(p - q);
    double k0 = (d - std::sqrt(r * r - h * h)) / norm(p - q);
    double k1 = (d + std::sqrt(r * r - h * h)) / norm(p - q);
    return std::make_pair<Point, Point>(p + k0 * (q - p), p + k1 * (q - p));
}

bool cross(Point p, Point q, double r) {
    double h = det(p - q, p) / norm(p - q);
    double d = dot(p - q, p) / norm(p - q);
    double k0 = (d - std::sqrt(r * r - h * h)) / norm(p - q);
    double k1 = (d + std::sqrt(r * r - h * h)) / norm(p - q);
    return 0 < k0 && k0 < 1 && 0 < k1 && k1 < 1;
}

double area(Point p, Point q, double r) {
    Point o{0, 0};
    if (norm(p) <= r && norm(q) <= r) {
        double tri = areaTri(p, q);
        return tri;
    } else if (norm(p) <= r && norm(q) > r) {
        Point s = intersection(p, q, r);
        Point t = intersection(o, q, r);
        double tri = areaTri(p, s);
        double fan = areaFan(s, t);
        return tri + fan;
    } else if (norm(p) > r && norm(q) <= r) {
        Point s = intersection(o, p, r);
        Point t = intersection(q, p, r);
        double fan = areaFan(s, t);
        double tri = areaTri(t, q);
        return fan + tri;
    } else if (cross(p, q, r)) {
        Point s = intersection(o, p, r);
        Point t = intersection2(p, q, r).first;
        Point u = intersection2(p, q, r).second;
        Point v = intersection(o, q, r);
        double fan0 = areaFan(s, t);
        double tri = areaTri(t, u);
        double fan1 = areaFan(u, v);
        return fan0 + tri + fan1;
    } else {
        Point s = intersection(o, p, r);
        Point t = intersection(o, q, r);
        double fan = areaFan(s, t);
        return fan;
    }
}

int main() {
    int n;
    double r;
    std::cin >> n >> r;
    std::vector<Point> points;
    for (int i = 0; i < n; i++) {
        Point p;
        std::cin >> p.x >> p.y;
        points.emplace_back(p);
    }
    double ans = 0;
    for (int i = 0; i < n; i++) {
        Point p = points[i];
        Point q = points[(i + 1) % n];
        ans += area(p, q, r);
    }
    std::cout << std::fixed << std::setprecision(15);
    std::cout << std::abs(ans) << std::endl;
}
