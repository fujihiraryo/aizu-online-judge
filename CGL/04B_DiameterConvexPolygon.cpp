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

bool operator<(Point p, Point q) {
    if (p.x != q.x) {
        return p.x < q.x;
    }
    return p.y < q.y;
}

double cross(Point p, Point q) {
    return p.x * q.y - p.y * q.x;
}

double distance(const Point &p, const Point &q) {
    return std::sqrt(std::pow(p.x - q.x, 2) + std::pow(p.y - q.y, 2));
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

    int i = 0;
    int j = 0;
    for (int k = 0; k < n; k++) {
        if (points[k] < points[i]) {
            i = k;
        }
        if (points[j] < points[k]) {
            j = k;
        }
    }

    double ans = 0;
    int i0 = i;
    int j0 = j;
    while (i != j0 || j != i0) {
        ans = std::max(ans, distance(points[i], points[j]));
        if (cross(points[(i + 1) % n] - points[i % n], points[(j + 1) % n] - points[j % n]) < 0) {
            i = (i + 1) % n;
        } else {
            j = (j + 1) % n;
        }
    }
    std::cout << std::fixed << std::setprecision(12) << ans << std::endl;
    return 0;
}
