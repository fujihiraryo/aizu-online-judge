#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

enum Type { left = 0, bottom = 1, top = 2, right = 3 };

struct Point {
    int id, x, y;
    int type = Type::left;
    int yEnd;
};

bool operator<(Point p, Point q) {
    if (p.x != q.x) {
        return p.x < q.x;
    }
    return p.type < q.type;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<Point> points;
    for (int i = 0; i < n; i++) {
        Point p, q;
        p.id = i;
        q.id = i;
        std::cin >> p.x >> p.y >> q.x >> q.y;
        if (p.x == q.x) {
            if (p.y > q.y) {
                std::swap(p, q);
            }
            p.type = Type::bottom;
            q.type = Type::top;
        } else {
            if (p.x > q.x) {
                std::swap(p, q);
            }
            p.type = Type::left;
            q.type = Type::right;
        }
        p.yEnd = q.y;
        points.emplace_back(p);
        points.emplace_back(q);
    }
    std::sort(points.begin(), points.end());
    std::set<int> list;
    int ans = 0;
    for (Point p : points) {
        if (p.type == Type::right) {
            list.erase(p.y);
        } else if (p.type == Type::left) {
            list.insert(p.y);
        } else if (p.type == Type::bottom) {
            std::set<int>::iterator i = std::lower_bound(list.begin(), list.end(), p.y);
            std::set<int>::iterator j = std::upper_bound(list.begin(), list.end(), p.yEnd);
            ans += std::distance(i, j);
        }
    }
    std::cout << ans << std::endl;
}
