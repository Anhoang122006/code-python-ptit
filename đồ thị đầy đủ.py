def solve():
    # 1. Đọc dữ liệu bằng input()
    # (Đề bài cho biết dòng 1 là N, dòng 2 là M)
    n_str = input().strip()
    if not n_str:
        return
    N = int(n_str)
    M = int(input().strip())

    # 2. Xây dựng bản đồ (Danh sách kề)
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # Sổ đánh dấu những người đã đếm
    visited = [False] * (N + 1)
    kich_thuoc_nhom = [] # Lưu số lượng người của từng nhóm

    # 3. QUÉT TÌM CÁC NHÓM
    for i in range(1, N + 1):
        if not visited[i]:
            # Phát hiện một nhóm mới!
            size = 0
            stack = [i]
            visited[i] = True

            # Khám phá xem nhóm này có bao nhiêu người
            while stack:
                curr = stack.pop()
                size += 1

                for hang_xom in adj[curr]:
                    if not visited[hang_xom]:
                        visited[hang_xom] = True
                        stack.append(hang_xom)

            kich_thuoc_nhom.append(size)

    # 4. CHỐT KẾT QUẢ THEO TOÁN HỌC
    # Phải có đúng 2 nhóm riêng biệt
    if len(kich_thuoc_nhom) == 2:
        s1 = kich_thuoc_nhom[0]
        s2 = kich_thuoc_nhom[1]

        # Sức chứa tối đa của 2 nhóm này
        so_canh_toi_da = (s1 * (s1 - 1) // 2) + (s2 * (s2 - 1) // 2)

        # Nếu số cạnh thực tế đúng bằng sức chứa tối đa -> Nó là đồ thị hoàn hảo
        if M == so_canh_toi_da:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

# Kích hoạt
if __name__ == '__main__':
    solve()
