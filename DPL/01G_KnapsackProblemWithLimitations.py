n, m = map(int, input().split())
VWC = [tuple(map(int, input().split())) for i in range(n)]
V = [v for v, w, c in VWC]
W = [w for v, w, c in VWC]
C = [c for v, w, c in VWC]
