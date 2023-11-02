#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

struct Point {
    double x, y;
};

Point operator-(Point p, Point q) {
    return Point{p.x - q.x, p.y - q.y};
}

double norm(Point p) {
    return std::sqrt(p.x * p.x + p.y * p.y);
}

double closest(const std::vector<Point> &points, const std::vector<int> &xSorted, const std::vector<int> &ySorted) {
    if (xSorted.size() <= 4) {
        double d = 100000;
        for (int i : xSorted) {
            for (int j : xSorted) {
                if (i == j) {
                    continue;
                }
                d = std::min(d, norm(points[i] - points[j]));
            }
        }
        return d;
    }

    std::vector<int> xSortedL;
    std::vector<int> xSortedR;
    std::unordered_set<int> sSortedL;
    std::unordered_set<int> sSortedR;
    for (int i : xSorted) {
        if (xSortedL.size() * 2 < xSorted.size()) {
            xSortedL.emplace_back(i);
            sSortedL.insert(i);
        } else {
            xSortedR.emplace_back(i);
            sSortedR.insert(i);
        }
    }

    std::vector<int> ySortedL;
    std::vector<int> ySortedR;
    std::unordered_map<int, int> iySorted;
    for (int k = 0; k < ySorted.size(); k++) {
        int i = ySorted[k];
        if (sSortedL.find(i) != sSortedL.end()) {
            ySortedL.emplace_back(i);
        } else {
            ySortedR.emplace_back(i);
        }
        iySorted[i] = k;
    }

    double dL = closest(points, xSortedL, ySortedL);
    double dR = closest(points, xSortedR, ySortedR);
    double dM = std::min(dL, dR);

    double xM = (points[xSortedL.back()].x + points[xSortedR.front()].x) / 2;
    for (int i : xSorted) {
        if (std::abs(points[i].x - xM) > dM) {
            continue;
        }
        for (int k = iySorted[i] + 1; k < ySorted.size(); k++) {
            int j = ySorted[k];
            if (points[j].y > points[i].y + dM) {
                break;
            }
            dM = std::min(dM, norm(points[i] - points[j]));
        }
        for (int k = iySorted[i] - 1; k >= 0; k--) {
            int j = ySorted[k];
            if (points[j].y < points[i].y - dM) {
                break;
            }
            dM = std::min(dM, norm(points[i] - points[j]));
        }
    }
    return dM;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<Point> points;
    for (int i = 0; i < n; i++) {
        Point p;
        std::cin >> p.x >> p.y;
        points.emplace_back(p);
    }
    std::vector<int> xSorted;
    std::vector<int> ySorted;
    for (int i = 0; i < n; i++) {
        xSorted.push_back(i);
        ySorted.push_back(i);
    }
    std::sort(xSorted.begin(), xSorted.end(), [&](int i, int j) { return points[i].x < points[j].x; });
    std::sort(ySorted.begin(), ySorted.end(), [&](int i, int j) { return points[i].y < points[j].y; });
    std::cout << std::fixed << std::setprecision(8);
    std::cout << closest(points, xSorted, ySorted) << std::endl;
    return 0;
}
