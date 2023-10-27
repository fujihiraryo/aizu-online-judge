#include <iostream>

struct Point {
    int x, y;
};

Point operator-(Point p, Point q) {
    return Point{p.x - q.x, p.y - q.y};
}
int operator,(Point p, Point q) {
    return p.x * q.x + p.y * q.y;
}
int operator^(Point p, Point q) {
    return p.x * q.y - p.y * q.x;
}
int ccw(Point p0, Point p1, Point p2) {
    int cross = (p1 - p0) ^ (p2 - p0);
    int dot = (p1 - p0, p2 - p0);
    int norm1 = (p1 - p0, p1 - p0);
    int norm2 = (p2 - p0, p2 - p0);
    if (cross > 0) {
        return 1;
    } else if (cross < 0) {
        return -1;
    }
    if (dot < 0) {
        return -1;
    } else if (norm1 < norm2) {
        return 1;
    }
    return 0;
}

int main() {
    Point p0, p1, p2, p3;
    int n;
    std::cin >> n;
    while (n--) {
        std::cin >> p0.x >> p0.y >> p1.x >> p1.y;
        std::cin >> p2.x >> p2.y >> p3.x >> p3.y;
        int c0 = ccw(p0, p1, p2) * ccw(p0, p1, p3);
        int c1 = ccw(p2, p3, p0) * ccw(p2, p3, p1);
        std::cout << ((c0 <= 0) && (c1 <= 0)) << std::endl;
    }
}
