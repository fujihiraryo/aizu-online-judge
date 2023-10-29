#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <set>
#include <vector>

struct Point {
    int x, y;
};

Point operator-(Point p, Point q) {
    return Point{p.x - q.x, p.y - q.y};
}

bool operator<(Point p, Point q) {
    if (p.y != q.y) {
        return p.y < q.y;
    }
    return p.x < q.x;
}

std::ostream &operator<<(std::ostream &stream, const Point &p) {
    stream << p.x << " " << p.y;
    return stream;
}

int cross(Point p, Point q) {
    return p.x * q.y - p.y * q.x;
}

bool ccw(Point p0, Point p1, Point p2) {
    // counter clockwise
    return cross(p1 - p0, p2 - p0) > 0;
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
    std::sort(points.begin(), points.end());

    std::vector<Point> upper;
    for (const Point &p : points) {
        int k = upper.size();
        while (k >= 2 && ccw(upper[k - 2], upper[k - 1], p)) {
            upper.pop_back();
            k = upper.size();
        }
        upper.push_back(p);
    }
    upper.pop_back();
    std::reverse(upper.begin(), upper.end());
    upper.pop_back();

    std::reverse(points.begin(), points.end());
    std::vector<Point> lower;
    for (const Point &p : points) {
        int k = lower.size();
        while (k >= 2 && ccw(lower[k - 2], lower[k - 1], p)) {
            lower.pop_back();
            k = lower.size();
        }
        lower.push_back(p);
    }
    std::reverse(lower.begin(), lower.end());

    std::cout << upper.size() + lower.size() << std::endl;
    for (const Point &p : lower) {
        std::cout << p << std::endl;
    }
    for (const Point &p : upper) {
        std::cout << p << std::endl;
    }
}
