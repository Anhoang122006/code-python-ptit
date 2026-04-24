import math

def circle_center(A, B, C):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    d = 2 * (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

    if d == 0:
        return None  # thẳng hàng

    ux = ((x1**2 + y1**2)*(y2 - y3) +
          (x2**2 + y2**2)*(y3 - y1) +
          (x3**2 + y3**2)*(y1 - y2)) / d

    uy = ((x1**2 + y1**2)*(x3 - x2) +
          (x2**2 + y2**2)*(x1 - x3) +
          (x3**2 + y3**2)*(x2 - x1)) / d

    return (ux, uy)


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    found = False

    for i in range(n):
        for j in range(i+1, n):
            for l in range(j+1, n):
                center = circle_center(points[i], points[j], points[l])

                if center is None:
                    continue

                R = dist(center, points[i])

                cnt = 0
                for p in points:
                    d = dist(center, p)
                    if d < R - 1e-6:  # tránh sai số float
                        cnt += 1

                if cnt == k:
                    found = True
                    break
            if found:
                break
        if found:
            break

    print("YES" if found else "NO")
