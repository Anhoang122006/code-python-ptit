import sys


def solve():
    # 1. Hút dữ liệu vào
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    M = int(input_data[1])
    X = int(input_data[2])

    # 2. XÂY DỰNG BẢN ĐỒ (Đồ thị vô hướng)
    # Tạo danh sách bạn bè trống cho tất cả N người
    adj = {i: [] for i in range(1, N + 1)}

    idx = 3
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])

        # Vì là đường 2 chiều, ta phải nối cả 2 đầu
        adj[u].append(v)
        adj[v].append(u)

        idx += 2

    # 3. QUÁ TRÌNH TRUYỀN TIN (DFS)
    # Cuốn sổ ghi nhớ ai đã biết bí mật (Ban đầu chưa ai biết -> False hết)
    visited = [False] * (N + 1)

    # Bắt đầu từ X
    stack = [X]
    visited[X] = True

    while stack:
        curr = stack.pop()

        # Kể cho tất cả bạn bè của curr
        for neighbor in adj[curr]:
            if not visited[neighbor]:  # Nếu người này chưa biết
                visited[neighbor] = True  # Đánh dấu đã biết
                stack.append(neighbor)  # Đưa vào danh sách để đi kể tiếp

    # 4. ĐIỂM DANH TÌM NGƯỜI TỐI CỔ (Không liên thông)
    danh_sach_mu_tit = []

    # Quét từ bạn số 1 đến bạn số N
    for i in range(1, N + 1):
        if not visited[i]:  # Nếu vẫn chưa biết bí mật
            danh_sach_mu_tit.append(i)

    # 5. IN KẾT QUẢ
    if not danh_sach_mu_tit:
        # Nếu danh sách trống -> Ai cũng biết bí mật rồi
        print(0)
    else:
        # In từng người ra mỗi dòng theo đúng yêu cầu đề bài
        for nguoi in danh_sach_mu_tit:
            print(nguoi)


if __name__ == '__main__':
    solve()