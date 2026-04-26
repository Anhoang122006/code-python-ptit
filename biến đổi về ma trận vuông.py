import sys

def solve():
    # 1. HÚT DỮ LIỆU BẢO MẬT
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    # 2. XÂY DỰNG MA TRẬN GỐC
    matrix = []
    idx = 2
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(data[idx]))
            idx += 1
        matrix.append(row)

    # 3. LẬP DANH SÁCH ĐEN (BLACK LIST)
    skip_rows = set()
    skip_cols = set()

    if n > m:
        # Cần loại bỏ (n - m) hàng lẻ
        # Tương đương với các index chẵn trong Python: 0, 2, 4...
        so_luong_can_xoa = n - m
        for i in range(so_luong_can_xoa):
            skip_rows.add(i * 2)

    elif m > n:
        # Cần loại bỏ (m - n) cột chẵn
        # Tương đương với các index lẻ trong Python: 1, 3, 5...
        so_luong_can_xoa = m - n
        for i in range(so_luong_can_xoa):
            skip_cols.add(i * 2 + 1)

    # 4. DUYỆT VÀ IN MA TRẬN ĐÃ LỌC
    for i in range(n):
        # Nếu hàng hiện tại nằm trong sổ đen -> Bỏ qua toàn bộ hàng này
        if i in skip_rows:
            continue

        new_row = []
        for j in range(m):
            # Nếu cột hiện tại nằm trong sổ đen -> Bỏ qua phần tử này
            if j in skip_cols:
                continue
            new_row.append(str(matrix[i][j]))

        # In các phần tử sống sót của hàng đó, cách nhau bằng khoảng trắng
        print(" ".join(new_row))

if __name__ == '__main__':
    solve()
