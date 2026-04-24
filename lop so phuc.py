class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc  # phần thực
        self.ao = ao      # phần ảo

    # Phép cộng: (a+bi) + (c+di) = (a+c) + (b+d)i
    def __add__(self, other): #hàm add dùng để cộng còn mull dùng nhân
        return SoPhuc(self.thuc + other.thuc, self.ao + other.ao)

    # Phép nhân: (a+bi)*(c+di) = (ac-bd) + (ad+bc)i
    def __mul__(self, other):
        thuc_moi = self.thuc * other.thuc - self.ao * other.ao
        ao_moi   = self.thuc * other.ao   + self.ao * other.thuc
        return SoPhuc(thuc_moi, ao_moi)

    # In ra định dạng: a + bi hoặc a - bi
    def __str__(self):
        if self.ao >= 0:
            return f"{self.thuc} + {self.ao}i"
        else:
            return f"{self.thuc} - {abs(self.ao)}i"


T = int(input())

for _ in range(T):
    a, b, c, d = map(int, input().split())

    A = SoPhuc(a, b)  # A = a + bi
    B = SoPhuc(c, d)  # B = c + di

    C = (A + B) * A        # C = (A+B) x A
    D = (A + B) * (A + B)  # D = (A+B)^2

    print(f"{C}, {D}")
