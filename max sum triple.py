def find_max_triplet_sum():
    # Đọc số lượng bộ test
    T = int(input())

    for _ in range(T):
        # Đọc N và toàn bộ mảng A
        N = int(input())
        A = list(map(int, input().split()))

        # Khởi tạo 3 bục Vàng, Bạc, Đồng với giá trị âm vô cùng
        # Dùng float('-inf') đảm bảo mọi số trong mảng đều lớn hơn nó ban đầu
        max1 = float('-inf') # Cao nhất
        max2 = float('-inf') # Cao nhì
        max3 = float('-inf') # Cao ba

        # Cho từng phần tử đi ngang qua bục
        for x in A:
            if x > max1:
                # Tìm được người cao kỷ lục mới, đẩy các người cũ xuống 1 bậc
                max3 = max2
                max2 = max1
                max1 = x
            elif x > max2:
                # Không cao bằng Vàng nhưng cao hơn Bạc, đẩy Bạc xuống Đồng
                max3 = max2
                max2 = x
            elif x > max3:
                # Chỉ cao hơn Đồng, thay thế vị trí Đồng
                max3 = x

        # In ra tổng của 3 số lớn nhất
        print(max1 + max2 + max3)

# Chạy chương trình
find_max_triplet_sum()
