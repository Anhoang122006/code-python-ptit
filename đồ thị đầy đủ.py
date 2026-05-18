import sys


def solve():
    # 1. Đọc dữ liệu
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    M = int(input_data[1])

    # Dùng Ma trận kề để kiểm tra kết nối siêu tốc O(1)
    # adj[i][j] = True nghĩa là i và j có cạnh nối
    adj = [[False] * (N + 1) for _ in range(N + 1)]

    # Bảng đếm số bậc (số bạn bè) của mỗi đỉnh
    degree = [0] * (N + 1)

    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u][v] = adj[v][u] = True
        degree[u] += 1
        degree[v] += 1
        idx += 2

    # 2. KIỂM TRA TỪNG ĐỈNH X
    # Thử giả sử đỉnh i là đỉnh được chọn để thực hiện thao tác
    for i in range(1, N + 1):
        # Sau khi đảo cạnh của i:
        # Số cạnh mới của i sẽ là (N - 1) - degree[i]
        # Tổng số cạnh của toàn đồ thị sau khi thao tác với i:
        # Tổng = (M - degree[i]) + [(N - 1) - degree[i]]

        moi_quan_he_moi = (N - 1) - degree[i]
        tong_canh_sau_khi_dao = M - degree[i] + moi_quan_he_moi

        # ĐIỀU KIỆN CẦN: Một đồ thị đầy đủ N đỉnh luôn có đúng N*(N-1)/2 cạnh
        if tong_canh_sau_khi_dao == N * (N - 1) // 2:
            print("YES")
            return

    print("NO")


if __name__ == '__main__':
    solve()