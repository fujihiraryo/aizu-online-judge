#include <cmath>
#include <iomanip>
#include <iostream>

const double EPS = 0.00001;
const double INF = 1000000;

struct Point {
    double x, y;
    double norm() {
        return std::sqrt(x * x + y * y);
    };
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
Point operator/(Point p, double a) {
    return Point{p.x / a, p.y / a};
}
double operator,(Point p, Point q) {
    return p.x * q.x + p.y * q.y;
}

// 線分p0,p1とp2の距離
double distance(Point p0, Point p1, Point p2) {
    double k = (p2 - p0, p1 - p0) / (p1 - p0, p1 - p0);
    if (-EPS < k && k < 1 + EPS) {
        Point q = p0 + k * (p1 - p0);
        return (p2 - q).norm();
    }
    return INF;
}

double cross(Point p, Point q) {
    return p.x * q.y - p.y * q.x;
}

// 直線p0,p1に対してp2,p3が互いに逆の位置
bool opposite(Point p0, Point p1, Point p2, Point p3) {
    return cross(p2 - p0, p1 - p0) * cross(p3 - p0, p1 - p0) < -EPS;
}

bool intersect(Point p0, Point p1, Point p2, Point p3) {
    return opposite(p0, p1, p2, p3) && opposite(p2, p3, p0, p1);
}

int main() {
    Point p0, p1, p2, p3;
    int n;
    std::cin >> n;
    while (n--) {
        std::cin >> p0.x >> p0.y >> p1.x >> p1.y;
        std::cin >> p2.x >> p2.y >> p3.x >> p3.y;
        if (intersect(p0, p1, p2, p3)) {
            std::cout << 0 << std::endl;
            continue;
        }
        double ans = INF;
        ans = std::min(ans, distance(p0, p1, p2));
        ans = std::min(ans, distance(p0, p1, p3));
        ans = std::min(ans, distance(p2, p3, p0));
        ans = std::min(ans, distance(p2, p3, p1));
        ans = std::min(ans, (p0 - p2).norm());
        ans = std::min(ans, (p0 - p3).norm());
        ans = std::min(ans, (p1 - p2).norm());
        ans = std::min(ans, (p1 - p3).norm());
        std::cout << std::fixed << std::setprecision(8);
        std::cout << ans << std::endl;
    }
}
