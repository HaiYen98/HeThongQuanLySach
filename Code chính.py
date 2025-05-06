class TaiLieu:
    def __init__(self, maTL, tenNXB, soBanPhatHanh):
        self.__maTaiLieu = maTL
        self.__tenNxb = tenNXB
        self.__soBanPhatHanh = soBanPhatHanh

    def getMaTaiLieu(self):
        return self.__maTaiLieu

    def setMaTaiLieu(self, ma):
        self.__maTaiLieu = ma

    def getTenNxb(self):
        return self.__tenNxb

    def setTenNxb(self, nxb):
        self.__tenNxb = nxb

    def getSoBanPhatHanh(self):
        return self.__soBanPhatHanh

    def setSoBanPhatHanh(self, soBan):
        self.__soBanPhatHanh = soBan

    def thongTin(self):
        print(f"Mã TL: {self.getMaTaiLieu()}, NXB: {self.getTenNxb()}, Số bản: {self.getSoBanPhatHanh()}")


class Sach(TaiLieu):
    def __init__(self, maTaiLieu, tenNxb, soBanPhatHanh, soTrang, tenTg):
        super().__init__(maTaiLieu, tenNxb, soBanPhatHanh)
        self.__soTrang = soTrang
        self.__tenTg = tenTg

    def getSoTrang(self):
        return self.__soTrang

    def setSoTrang(self, so):
        self.__soTrang = so

    def getTenTg(self):
        return self.__tenTg

    def setTenTg(self, ten):
        self.__tenTg = ten

    def thongTin(self):
        super().thongTin()
        print(f"Tác giả: {self.getTenTg()}, Số trang: {self.getSoTrang()}")


class TapChi(TaiLieu):
    def __init__(self, maTaiLieu, tenNxb, soBanPhatHanh, soPhatHanh, thangPhatHanh):
        super().__init__(maTaiLieu, tenNxb, soBanPhatHanh)
        self.__soPhatHanh = soPhatHanh
        self.__thangPhatHanh = thangPhatHanh

    def getSoPhatHanh(self):
        return self.__soPhatHanh

    def setSoPhatHanh(self, so):
        self.__soPhatHanh = so

    def getThangPhatHanh(self):
        return self.__thangPhatHanh

    def setThangPhatHanh(self, thang):
        self.__thangPhatHanh = thang

    def thongTin(self):
        super().thongTin()
        print(f"Số phát hành: {self.getSoPhatHanh()}, Tháng phát hành: {self.getThangPhatHanh()}")


class Bao(TaiLieu):
    def __init__(self, maTaiLieu, tenNxb, soBanPhatHanh, ngayPhatHanh):
        super().__init__(maTaiLieu, tenNxb, soBanPhatHanh)
        self.__ngayPhatHanh = ngayPhatHanh

    def getNgayPhatHanh(self):
        return self.__ngayPhatHanh

    def setNgayPhatHanh(self, ngay):
        self.__ngayPhatHanh = ngay

    def thongTin(self):
        super().thongTin()
        print(f"Ngày phát hành: {self.getNgayPhatHanh()}")


class QuanLySach:
    def __init__(self):
        self.danhSach = []

    def maTaiLieuDuyNhat(self, maTaiLieu):
        return not any(tl.getMaTaiLieu() == maTaiLieu for tl in self.danhSach)

    def themTaiLieu(self, taiLieu):
        self.danhSach.append(taiLieu)

    def xoaTaiLieu(self, maTaiLieu):
        if not any(tl.getMaTaiLieu() == maTaiLieu for tl in self.danhSach):
            print("Không tìm thấy tài liệu với mã này.")
            return
        self.danhSach = [tl for tl in self.danhSach if tl.getMaTaiLieu() != maTaiLieu]
        print("Đã xoá tài liệu.")

    def hienThiThongTin(self):
        if not self.danhSach:
            print("Danh sách tài liệu trống.")
            return
        print("\n=== DANH SÁCH TẤT CẢ TÀI LIỆU ===")
        for tl in self.danhSach:
            if isinstance(tl, Sach):
                print("Loại: Sách")
            elif isinstance(tl, TapChi):
                print("Loại: Tạp chí")
            elif isinstance(tl, Bao):
                print("Loại: Báo")
            tl.thongTin()
            print("---------")

    def timKiemTheoLoai(self, loai):
        loaiTaiLieu = {
            "sach": Sach,
            "tapchi": TapChi,
            "bao": Bao
        }

        if loai not in loaiTaiLieu:
            print("Không tìm thấy loại tài liệu.")
            return

        found = False
        for tl in self.danhSach:
            if isinstance(tl, loaiTaiLieu[loai]):
                if not found:
                    print(f"\n=== DANH SÁCH {loai.upper()} ===")
                    found = True
                tl.thongTin()
                print("---------")
        if not found:
            print(f"Không tìm thấy {loai} nào trong danh sách.")


def menu():
    ql = QuanLySach()

    while True:
        print("\n--- DANH SÁCH TÀI LIỆU ---")
        print("1. Thêm tài liệu")
        print("2. Xoá tài liệu")
        print("3. Hiển thị thông tin tài liệu")
        print("4. Tìm kiếm theo loại")
        print("5. Thoát")

        luaChon = input("Chọn chức năng (1-5): ")

        if luaChon == "1":
            print("\n1. Sách | 2. Tạp chí | 3. Báo")
            loai = input("Chọn loại tài liệu: ")

            ma = input("Mã tài liệu: ")
            if not ql.maTaiLieuDuyNhat(ma):
                print("Mã tài liệu đã tồn tại. Vui lòng nhập mã khác.")
                continue

            nxb = input("Nhà xuất bản: ")
            try:
                soBan = int(input("Số bản phát hành: "))
                if soBan <= 0:
                    print("Số bản phát hành phải lớn hơn 0.")
                    continue
            except ValueError:
                print("Số bản phát hành phải là số nguyên.")
                continue

            if loai == "1":
                tacGia = input("Tên tác giả: ")
                try:
                    soTrang = int(input("Số trang: "))
                    if soTrang <= 0:
                        print("Số trang phải lớn hơn 0.")
                        continue
                except ValueError:
                    print("Số trang phải là số nguyên.")
                    continue
                sach = Sach(ma, nxb, soBan, soTrang, tacGia)
                ql.themTaiLieu(sach)
                print("Đã thêm sách.")

            elif loai == "2":
                try:
                    soPh = int(input("Số phát hành: "))
                    if soPh <= 0:
                        print("Số phát hành phải lớn hơn 0.")
                        continue
                except ValueError:
                    print("Số phát hành phải là số nguyên.")
                    continue
                try:
                    thangPh = int(input("Tháng phát hành (1-12): "))
                    if not 1 <= thangPh <= 12:
                        print("Tháng phát hành phải từ 1 đến 12.")
                        continue
                except ValueError:
                    print("Tháng phát hành phải là số từ 1 đến 12.")
                    continue
                tapChi = TapChi(ma, nxb, soBan, soPh, thangPh)
                ql.themTaiLieu(tapChi)
                print("Đã thêm tạp chí.")

            elif loai == "3":
                ngayPh = input("Ngày phát hành: ")
                bao = Bao(ma, nxb, soBan, ngayPh)
                ql.themTaiLieu(bao)
                print("Đã thêm báo.")

            else:
                print("Loại tài liệu không hợp lệ!")

        elif luaChon == "2":
            ma = input("Nhập mã tài liệu cần xoá: ")
            ql.xoaTaiLieu(ma)

        elif luaChon == "3":
            ql.hienThiThongTin()

        elif luaChon == "4":
            loai = input("Nhập thể loại (sach/tapchi/bao): ").lower()
            ql.timKiemTheoLoai(loai)

        elif luaChon == "5":
            print("Thoát chương trình")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    menu()
