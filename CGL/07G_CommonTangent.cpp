#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

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

Point operator/(Point p, double a) {
    return Point{p.x / a, p.y / a};
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

Point rotate(Point p, double a) {
    Point q;
    q.x = p.x * std::cos(a) - p.y * std::sin(a);
    q.y = p.x * std::sin(a) + p.y * std::cos(a);
    return q;
}

int main() {
    Point p0, p1;
    double r0, r1;
    std::cin >> p0.x >> p0.y >> r0;
    std::cin >> p1.x >> p1.y >> r1;

    double d = norm(p0 - p1);
    double a0 = std::acos((r0 - r1) / d);
    double a1 = std::acos((r0 + r1) / d);
    Point u = (p1 - p0) / norm(p1 - p0);

    Point q0 = p0 + r0 * rotate(u, a0);
    Point q1 = p0 + r0 * rotate(u, -a0);
    Point q2 = p0 + r0 * rotate(u, a1);
    Point q3 = p0 + r0 * rotate(u, -a1);

    std::vector<Point> ans;
    if (r0 + r1 < d) {
        ans.push_back(q0);
        ans.push_back(q1);
        ans.push_back(q2);
        ans.push_back(q3);
    } else if (r0 + r1 == d) {
        ans.push_back(q0);
        ans.push_back(q1);
        ans.push_back(q2);
    } else if (std::abs(r0 - r1) < d) {
        ans.push_back(q0);
        ans.push_back(q1);
    } else if (std::abs(r0 - r1) == d) {
        ans.push_back(q0);
    }
    std::sort(ans.begin(), ans.end());

    for (Point p : ans) {
        std::cout << p << std::endl;
    }
}
