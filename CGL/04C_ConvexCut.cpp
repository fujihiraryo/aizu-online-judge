#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

struct Point {
    double x, y;
};

Point operator+(Point p, Point q) {
    return Point{p.x + q.x, p.y + q.y};
}

Point operator-(Point p, Point q) {
    return Point{p.x - q.x, p.y - q.y};
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

double area(const std::vector<Point> &points) {
    double res = 0.0;
    int n = points.size();
    for (int i = 0; i < n; i++) {
        res += cross(points[i], points[(i + 1) % n]);
    }
    return res / 2;
}

Point intersect(Point p0, Point p1, Point q0, Point q1) {
    double d0 = std::abs(cross(q0 - p0, p1 - p0)) / norm(p1 - p0);
    double d1 = std::abs(cross(q1 - p1, p0 - p1)) / norm(p0 - p1);
    double a0 = d1 / (d0 + d1);
    double a1 = d0 / (d0 + d1);
    return a0 * q0 + a1 * q1;
}

std::vector<Point> cut(const std::vector<Point> &points, Point q0, Point q1) {
    std::vector<Point> res;
    int n = points.size();
    for (int i = 0; i < n; i++) {
        Point p0 = points[i];
        Point p1 = points[(i + 1) % n];
        if (cross(q1 - q0, p0 - q0) > 0) {
            res.push_back(p0);
            if (cross(q1 - q0, p1 - q0) <= 0) {
                res.push_back(intersect(q0, q1, p0, p1));
            }
        } else {
            if (cross(q1 - q0, p1 - q0) > 0) {
                res.push_back(intersect(q0, q1, p0, p1));
            }
        }
    }
    return res;
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

    int m;
    std::cin >> m;
    std::vector<double> ans;
    for (int i = 0; i < m; i++) {
        Point q0, q1;
        std::cin >> q0.x >> q0.y >> q1.x >> q1.y;
        ans.push_back(area(cut(points, q0, q1)));
    }

    std::cout << std::fixed << std::setprecision(8);
    for (double x : ans) {
        std::cout << x << std::endl;
    }
}
