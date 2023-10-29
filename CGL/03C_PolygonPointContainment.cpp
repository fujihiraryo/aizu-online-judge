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

int dot(Point p, Point q) {
    return p.x * q.x + p.y * q.y;
}

int cross(Point p, Point q) {
    return p.x * q.y - p.y * q.x;
}

bool contain(Point p0, Point p1, Point q) {
    // Segment p0p1 contains q
    bool onLine = cross(p1 - p0, q - p0) == 0;
    bool direction = dot(p1 - p0, q - p0) >= 0;
    bool length = dot(p1 - p0, q - p0) <= dot(p1 - p0, p1 - p0);
    return onLine && direction && length;
}

bool on(const std::vector<Point> &polygon, Point q) {
    bool res = false;
    for (int i = 0; i < polygon.size(); i++) {
        Point p0 = polygon[i];
        Point p1 = polygon[(i + 1) % polygon.size()];
        if (contain(p0, p1, q)) {
            res = true;
        }
    }
    return res;
}

int sgn(int x) {
    if (x > 0) {
        return 1;
    }
    if (x < 0) {
        return -1;
    }
    return 0;
}

bool intersect(Point p0, Point p1, Point q0, Point q1) {
    bool cond0 = sgn(cross(p1 - p0, q0 - p0)) * sgn(cross(p1 - p0, q1 - p0)) < 0;
    bool cond1 = sgn(cross(q1 - q0, p0 - q0)) * sgn(cross(q1 - q0, p1 - q0)) < 0;
    return cond0 && cond1;
}

bool contain(const std::vector<Point> &polygon, Point q) {
    int n = polygon.size();
    int count = 0;
    Point q1{10001, 10002};
    for (int i = 0; i < n; i++) {
        Point p0 = polygon[i];
        Point p1 = polygon[(i + 1) % n];
        if (intersect(p0, p1, q, q1)) {
            count += 1;
        }
    }
    return count % 2;
}

int main() {
    // polygon
    int n;
    std::cin >> n;
    std::vector<Point> points;
    for (int i = 0; i < n; i++) {
        Point p;
        std::cin >> p.x >> p.y;
        points.push_back(p);
    }

    // query
    int m;
    std::cin >> m;
    std::vector<int> ans;
    for (int i = 0; i < m; i++) {
        Point q;
        std::cin >> q.x >> q.y;
        if (on(points, q)) {
            ans.push_back(1);
        } else if (contain(points, q)) {
            ans.push_back(2);
        } else {
            ans.push_back(0);
        }
    }

    // answer
    for (int x : ans) {
        std::cout << x << std::endl;
    }
}
