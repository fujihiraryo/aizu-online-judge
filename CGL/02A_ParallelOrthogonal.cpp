#include <iostream>

struct Point {
  double x, y;
};

Point operator+(Point p, Point q) { return Point{p.x + q.x, p.y + q.y}; }
Point operator-(Point p, Point q) { return Point{p.x - q.x, p.y - q.y}; }
double operator,(Point p, Point q) { return p.x * q.x + p.y * q.y; }
double operator^(Point p, Point q) { return p.x * q.y - p.y * q.x; }

Point p0, p1, p2, p3;
int n;

int main() {
  std::cin >> n;
  while (n--) {
    std::cin >> p0.x >> p0.y >> p1.x >> p1.y;
    std::cin >> p2.x >> p2.y >> p3.x >> p3.y;
    if (((p0 - p1) ^ (p2 - p3)) == 0) {
      std::cout << 2 << std::endl;
    } else if ((p0 - p1, p2 - p3) == 0) {
      std::cout << 1 << std::endl;
    } else {
      std::cout << 0 << std::endl;
    }
  }
}
