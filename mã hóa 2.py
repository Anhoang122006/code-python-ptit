def solve():
    # Khai báo chuỗi P chuẩn (Không dùng ngoặc vuông [])
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

    while True:

        line = input()

        data = line.split()



        k = int(data[0])


        if k == 0:
            break


        s = data[1]

        res=""

        for char in s:
            # Tìm vị trí của ký tự trong P (Dùng find cho nhanh)
            idx = P.find(char)

            # Tính vị trí mới: (Vị trí cũ + k) chia lấy dư 28
            new_idx = (idx + k) % 28

            # Lấy ký tự ở vị trí mới ghép vào kết quả
            res += P[new_idx]

        # 5. In ra kết quả ĐẢO NGƯỢC (theo yêu cầu đề bài)
        print(res[::-1])


if __name__ == "__main__":
    solve()