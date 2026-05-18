import sys


def solve():
    # 1. Hút toàn bộ dữ liệu (Bỏ qua mọi khoảng trắng, xuống dòng)
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    idx = 1

    out = []

    for _ in range(T):
        N = int(input_data[idx])
        M = int(input_data[idx + 1])
        u = int(input_data[idx + 2])
        v = int(input_data[idx + 3])
        idx += 4

        # 2. XÂY DỰNG BẢN ĐỒ (Danh sách kề)
        # adj[i] sẽ chứa danh sách các thành phố có thể đi trực tiếp từ i
        adj = {i: [] for i in range(1, N + 1)}
        for _ in range(M):
            x = int(input_data[idx])
            y = int(input_data[idx + 1])
            adj[x].append(y)
            idx += 2

        # --- HÀM PHỤ TRỢ: TÌM ĐƯỜNG ĐI (DFS) ---
        # Hàm này trả về True nếu có đường từ start đến end MÀ KHÔNG ĐI QUA skip_node
        def can_reach(start, end, skip_node):
            if start == skip_node:
                return False

            visited = [False] * (N + 1)
            stack = [start]
            visited[start] = True

            # Quá trình lan truyền của DFS
            while stack:
                curr = stack.pop()
                if curr == end:
                    return True  # Đã tìm thấy đích!

                # Điểm danh các hàng xóm
                for neighbor in adj[curr]:
                    # Nếu hàng xóm chưa từng đến VÀ không phải là thành phố bị phong tỏa
                    if not visited[neighbor] and neighbor != skip_node:
                        visited[neighbor] = True
                        stack.append(neighbor)

            return False  # Đi hết mọi ngõ ngách mà không thấy đích

        # 3. KIỂM TRA ĐIỀU KIỆN GỐC
        # Nếu ngay từ đầu, bản đồ đã không có đường từ u đến v (không bị cấm ai cả)
        # thì chắc chắn không tồn tại đỉnh thắt nào.
        if not can_reach(u, v, -1):
            out.append("0")
            continue

        # 4. TRUY TÌM ĐỈNH THẮT
        count = 0
        for k in range(1, N + 1):
            # Đỉnh thắt không được tính là điểm xuất phát hoặc điểm đích
            if k == u or k == v:
                continue

            # Đóng vai kẻ phá bĩnh: Cấm đi qua đỉnh k.
            # Xem thử còn đường từ u đến v không?
            if not can_reach(u, v, k):
                # Nếu không còn đường -> k là chốt chặn sinh tử (Đỉnh thắt)
                count += 1

        out.append(str(count))

    # In toàn bộ kết quả siêu tốc
    print('\n'.join(out))


if __name__ == '__main__':
    solve()