#include <iomanip>
#include <iostream>

struct Point {
    double x, y;
};

Point operator+(Point p, Point q) { return Point{p.x + q.x, p.y + q.y}; }
Point operator-(Point p, Point q) { return Point{p.x - q.x, p.y - q.y}; }
Point operator/(Point p, double a) { return Point{p.x / a, p.y / a}; }
double operator,(Point p, Point q) { return p.x * q.x + p.y * q.y; }
double operator^(Point p, Point q) { return p.x * q.y - p.y * q.x; }
int ccw(Point p0, Point p1, Point p2) {
    double cross = (p1 - p0) ^ (p2 - p0);
    if (cross > 0) {
        return 1;
    } else if (cross < 0) {
        return -1;
    }
    return 0;
}

Point findCross(Point p0, Point p1, Point p2, Point p3) {
    if (ccw(p0, p1, p2) == 0) {
        return p2;
    }
    if (ccw(p0, p1, p3) == 0) {
        return p3;
    }
    int cnt = 100;
    Point pc, pl, pr;
    if (ccw(p0, p1, p2) < 0) {
        pl = p2;
        pr = p3;
    } else {
        pl = p3;
        pr = p2;
    }
    while (cnt--) {
        pc = (pl + pr) / 2;
        if (ccw(p0, p1, pc) < 0) {
            pl = pc;
        } else {
            pr = pc;
        }
    }
    return pc;
}

Point findCross2(Point p0, Point p1, Point p2, Point p3) {
    double det = (p0.x - p1.x) * (p2.y - p3.y) - (p0.y - p1.y) * (p2.x - p3.x);
    Point p;
    p.x = -(p2.x - p3.x) * (p1.x * p0.y - p0.x * p1.y) +
          (p0.x - p1.x) * (p3.x * p2.y - p2.x * p3.y);
    p.y = -(p2.y - p3.y) * (p1.x * p0.y - p0.x * p1.y) +
          (p0.y - p1.y) * (p3.x * p2.y - p2.x * p3.y);
    return p / det;
}

int main() {
    Point p0, p1, p2, p3, p;
    int n;
    std::cin >> n;
    while (n--) {
        std::cin >> p0.x >> p0.y >> p1.x >> p1.y;
        std::cin >> p2.x >> p2.y >> p3.x >> p3.y;
        p = findCross2(p0, p1, p2, p3);
        std::cout << std::fixed << std::setprecision(8);
        std::cout << p.x << " " << p.y << std::endl;
    }
}
