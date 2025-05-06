# Tạo lớp TaiLieu (Tài Liệu)
class TaiLieu:
    # Phương thức khởi tạo
    def __init__(self, maTL, tenNXB, soBanPhatHanh):
        self.__maTaiLieu = maTL #Thuộc tính mã tài liệu (private)
        self.__tenNxb = tenNXB #Thuộc tính tên nhà xuất bản (private)
        self.__soBanPhatHanh = soBanPhatHanh #Thuộc tính số bản phát hành (private)


    # Phương thức getter và setter cho mã tài liệu
    def getMaTaiLieu(self):
        return self.__maTaiLieu
    def setMaTaiLieu(self, ma):
        self.__maTaiLieu = ma


    # Phương thức getter và setter cho tên nhà xuất bản
    def getTenNxb(self):
        return self.__tenNxb
    def setTenNxb(self, nxb):
        self.__tenNxb = nxb


    # Phương thức getter và setter cho số bản phát hành
    def getSoBanPhatHanh(self):
        return self.__soBanPhatHanh
    def setSoBanPhatHanh(self, soBan):
        self.__soBanPhatHanh = soBan


    # In thông tin tài liệu
    def thongTin(self):
        print(f"Mã TL: {self.getMaTaiLieu()}, NXB: {self.getTenNxb()}, Số bản: {self.getSoBanPhatHanh()}")


# Lớp Sach (Sách) kế thừa từ lớp TaiLieu
class Sach(TaiLieu):
    def __init__(self, maTaiLieu, tenNxb, soBanPhatHanh, soTrang, tenTg):
        super().__init__(maTaiLieu, tenNxb, soBanPhatHanh) # Gọi constructor lớp cha
        self.__soTrang = soTrang # Thuộc tính số trang (private)
        self.__tenTg = tenTg # Thuộc tính tên tác giả (private)


    # Phương thức getter và setter cho số trang
    def getSoTrang(self):
        return self.__soTrang
    def setSoTrang(self, so):
        self.__soTrang = so


    # Phương thức getter và setter cho tên tác giả
    def getTenTg(self):
        return self.__tenTg
    def setTenTg(self, ten):
        self.__tenTg = ten


    # Ghi đè phương thức in thông tin
    def thongTin(self):
        super().thongTin() # Gọi in thông tin từ lớp cha
        print(f"Tác giả: {self.getTenTg()}, Số trang: {self.getSoTrang()}")


# Lớp TapChi (Tạp Chí) kế thừa lớp TaiLieu
class TapChi(TaiLieu):
    def __init__(self, maTaiLieu, tenNxb, soBanPhatHanh, soPhatHanh, thangPhatHanh):
        super().__init__(maTaiLieu, tenNxb, soBanPhatHanh) # Gọi constructor lớp cha
        self.__soPhatHanh = soPhatHanh # Thuộc tính số phát hành (private)
        self.__thangPhatHanh = thangPhatHanh # Thuộc tính tháng phát hành (private)


    # Phương thức getter và setter cho số phát hành
    def getSoPhatHanh(self):
        return self.__soPhatHanh
    def setSoPhatHanh(self, so):
        self.__soPhatHanh = so


    # Phương thức getter và setter cho tháng phát hành
    def getThangPhatHanh(self):
        return self.__thangPhatHanh
    def setThangPhatHanh(self, thang):
        self.__thangPhatHanh = thang


    # Ghi đè phương thức in thông tin
    def thongTin(self):
        super().thongTin() # Gọi in thông tin từ lớp cha
        print(f"Số phát hành: {self.getSoPhatHanh()}, Tháng phát hành: {self.getThangPhatHanh()}")


# Lớp Bao (Báo) kế thừa lớp TaiLieu
class Bao(TaiLieu):
    def __init__(self, maTaiLieu, tenNxb, soBanPhatHanh, ngayPhatHanh):
        super().__init__(maTaiLieu, tenNxb, soBanPhatHanh) # Gọi constructor lớp cha
        self.__ngayPhatHanh = ngayPhatHanh # Thuộc tính ngày phát hành (private)


    # Phương thức getter và setter cho ngày phát hành
    def getNgayPhatHanh(self):
        return self.__ngayPhatHanh
    def setNgayPhatHanh(self, ngay):
        self.__ngayPhatHanh = ngay


    # Ghi đè phương thức in thông tin
    def thongTin(self):
        super().thongTin() # Gọi in thông tin từ lớp cha
        print(f"Ngày phát hành: {self.getNgayPhatHanh()}")


# Lớp QuanLySach (Quản Lý Sách)
class QuanLySach:
    def __init__(self):
        self.danhSach = [] # Danh sách (list) lưu các tài liệu


    # Kiểm tra mã tài liệu có duy nhất không
    def maTaiLieuDuyNhat(self, maTaiLieu):
        return not any(tl.getMaTaiLieu() == maTaiLieu for tl in self.danhSach)


    # Phương thức thêm tài liệu
    def themTaiLieu(self, taiLieu):
        self.danhSach.append(taiLieu) # Thêm tài liệu vào cuối danh sách


    # Phương thức xóa tài liệu bằng mã tài liệu
    def xoaTaiLieu(self, maTaiLieu):
        # Trường hợp không tìm thấy tài liệu có mã nhập vào
        if not any(tl.getMaTaiLieu() == maTaiLieu for tl in self.danhSach):
            print("Không tìm thấy tài liệu với mã này.")
            return
        # Tạo danh sách mới (không có tài liệu cần xóa)
        self.danhSach = [tl for tl in self.danhSach if tl.getMaTaiLieu() != maTaiLieu]
        print("Đã xoá tài liệu.")


    # Phương thức hiển thị thông tin tài liệu
    def hienThiThongTin(self):
        # Trường hợp không có tài liệu nào trong danh sách
        if not self.danhSach:
            print("Danh sách tài liệu trống.")
            return
        # Trường hợp có tài liệu trong danh sách
        print("\n=== DANH SÁCH TẤT CẢ TÀI LIỆU ===")
        for tl in self.danhSach: # Duyệt qua từng phần tử tl (tài liệu) trong danh sách
            # Xác định loại tài liệu (sách/tạp chí/báo) bằng isinstance()
            if isinstance(tl, Sach):
                print("Loại: Sách")
            elif isinstance(tl, TapChi):
                print("Loại: Tạp chí")
            elif isinstance(tl, Bao):
                print("Loại: Báo")
            # In thông tin cụ thể của tài liệu
            tl.thongTin()
            print("---------")


    # Phương thức tìm kiếm tài liệu theo thể loại
    def timKiemTheoLoai(self, loai):
        loaiTaiLieu = {
            "sach": Sach,
            "tapchi": TapChi,
            "bao": Bao
        }
        # Trường hợp loại không hợp lệ (không phải sách/tạp chí/báo)
        if loai not in loaiTaiLieu:
            print("Không tìm thấy loại tài liệu.")
            return
        found = False # Biến found kiểm tra xem có ít nhất một tài liệu phù hợp không
        for tl in self.danhSach:
            if isinstance(tl, loaiTaiLieu[loai]): # Kiểm tra xem tl có phải đối tượng của lớp không
                # Kiểm tra xem có phải đây là tài liệu phù hợp đầu tiên mà vòng lặp gặp phải hay không
                if not found:
                    print(f"\n=== DANH SÁCH {loai.upper()} ===")
                    found = True
                tl.thongTin()
                print("---------")
        if not found:
            print(f"Không tìm thấy {loai} nào trong danh sách.")


# Hàm menu() - Giao diện điều khiển chương trình cho người dùng
def menu():
    ql = QuanLySach() # Khởi tạo đối tượng quản lý sách (danh sách tài liệu)


    while True: # Vòng lặp chính cho menu
        print("\n--- DANH SÁCH TÀI LIỆU ---")
        print("1. Thêm tài liệu")
        print("2. Xoá tài liệu")
        print("3. Hiển thị thông tin tài liệu")
        print("4. Tìm kiếm theo loại")
        print("5. Thoát")
        # Nhập lựa chọn từ bàn phím
        luaChon = input("Chọn chức năng (1-5): ")


        # Chức năng 1: Thêm tài liệu
        if luaChon == "1":
            # Chọn loại tài liệu từ bàn phím
            print("\n1. Sách | 2. Tạp chí | 3. Báo")
            loai = input("Chọn loại tài liệu (1-3): ")


            # Nhập mã tài liệu từ bàn phím
            ma = input("Mã tài liệu: ")
            # Trường hợp mã tài liệu đã tồn tại
            if not ql.maTaiLieuDuyNhat(ma):
                print("Mã tài liệu đã tồn tại. Vui lòng nhập mã khác.")
                continue


            # Nhập tên nhà xuất bản
            nxb = input("Nhà xuất bản: ")
            # Sử dụng khối try-except để bắt và xử lý lỗi kiểu dữ liệu không hợp lệ
            try:
                # Nhập số bản phát hành
                soBan = int(input("Số bản phát hành: "))
                # Trường hợp số bản phát hành không hợp lệ
                if soBan <= 0:
                    print("Số bản phát hành phải lớn hơn 0.")
                    continue
            except ValueError:
                print("Số bản phát hành phải là số nguyên.")
                continue


            # Thêm sách
            if loai == "1":
                # Nhập tên tác giả từ bàn phím
                tacGia = input("Tên tác giả: ")
                # Sử dụng khối try-except để bắt và xử lý lỗi kiểu dữ liệu không hợp lệ
                try:
                    soTrang = int(input("Số trang: "))
                    # Trường hợp số trang không hợp lệ
                    if soTrang <= 0:
                        print("Số trang phải lớn hơn 0.")
                        continue
                except ValueError:
                    print("Số trang phải là số nguyên.")
                    continue
                sach = Sach(ma, nxb, soBan, soTrang, tacGia) # Tạo đối tượng sách
                ql.themTaiLieu(sach) # Thêm đối tượng vào danh sách
                print("Đã thêm sách.")


            # Thêm tạp chí
            elif loai == "2":
                try:
                    # Nhập số phát hành từ bàn phím
                    soPh = int(input("Số phát hành: "))
                    # Trường hợp số phát hành không hợp lệ
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
                tapChi = TapChi(ma, nxb, soBan, soPh, thangPh) # Tạo đối tượng tạp chí
                ql.themTaiLieu(tapChi) # Thêm đối tượng vào danh sách
                print("Đã thêm tạp chí.")


            # Thêm báo
            elif loai == "3":
                # Nhập ngày phát hành từ bàn phím
                ngayPh = input("Ngày phát hành: ")
                bao = Bao(ma, nxb, soBan, ngayPh) # Tạo đối tượng báo
                ql.themTaiLieu(bao) # Thêm đối tượng vào danh sách
                print("Đã thêm báo.")


            # Trường hợp nhập sai loại tài liệu
            else:
                print("Loại tài liệu không hợp lệ!")


        # Chức năng 2: Xóa tài liệu theo mã
        elif luaChon == "2":
            # Nhập mã tài liệu từ bàn phím
            ma = input("Nhập mã tài liệu cần xoá: ")
            ql.xoaTaiLieu(ma)


        # Chức năng 3: hiển thị toàn bộ thông tin tài liệu
        elif luaChon == "3":
            ql.hienThiThongTin()


        # Chức năng 4: Tìm kiếm tài liệu theo thể loại (sách/tạp chí/báo)
        elif luaChon == "4":
            loai = input("Nhập thể loại (sach/tapchi/bao): ").lower()
            ql.timKiemTheoLoai(loai)


        # Chức năng 5: Thoát chương trình
        elif luaChon == "5":
            print("Thoát chương trình")
            break # Dừng vòng lặp, kết thúc chương trình


        # Trường hợp nhập sai lựa chọn
        else:
            print("Lựa chọn không hợp lệ!")


# Đảm bảo hàm menu() chạy trực tiếp
if __name__ == "__main__":
    menu()


