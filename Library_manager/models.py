class TaiLieu:
    def __init__(self, maTaiLieu, tenNxb, soBanPhatHanh):
        self.maTaiLieu = maTaiLieu
        self.tenNxb = tenNxb
        self.soBanPhatHanh = soBanPhatHanh

    def getMaTaiLieu(self):
        return self.maTaiLieu

    def getTenNxb(self):
        return self.tenNxb

    def getSoBanPhatHanh(self):
        return self.soBanPhatHanh


class Sach(TaiLieu):
    def __init__(self, maTaiLieu, tenNxb, soBanPhatHanh, soTrang, tenTg):
        super().__init__(maTaiLieu, tenNxb, soBanPhatHanh)
        self.soTrang = soTrang
        self.tenTg = tenTg

    def getSoTrang(self):
        return self.soTrang

    def getTenTg(self):
        return self.tenTg

    def thongTinStr(self):
        return f"Mã TL: {self.getMaTaiLieu()}, NXB: {self.getTenNxb()}, Số bản: {self.getSoBanPhatHanh()}, Tác giả: {self.getTenTg()}, Số trang: {self.getSoTrang()}"


class TapChi(TaiLieu):
    def __init__(self, maTaiLieu, tenNxb, soBanPhatHanh, soPhatHanh, thangPhatHanh):
        super().__init__(maTaiLieu, tenNxb, soBanPhatHanh)
        self.soPhatHanh = soPhatHanh
        self.thangPhatHanh = thangPhatHanh

    def getSoPhatHanh(self):
        return self.soPhatHanh

    def getThangPhatHanh(self):
        return self.thangPhatHanh

    def thongTinStr(self):
        return f"Mã TL: {self.getMaTaiLieu()}, NXB: {self.getTenNxb()}, Số bản: {self.getSoBanPhatHanh()}, Số phát hành: {self.getSoPhatHanh()}, Tháng: {self.getThangPhatHanh()}"


class Bao(TaiLieu):
    def __init__(self, maTaiLieu, tenNxb, soBanPhatHanh, ngayPhatHanh):
        super().__init__(maTaiLieu, tenNxb, soBanPhatHanh)
        self.ngayPhatHanh = ngayPhatHanh

    def getNgayPhatHanh(self):
        return self.ngayPhatHanh

    def thongTinStr(self):
        return f"Mã TL: {self.getMaTaiLieu()}, NXB: {self.getTenNxb()}, Số bản: {self.getSoBanPhatHanh()}, Ngày phát hành: {self.getNgayPhatHanh()}"


class QuanLySach:
    def __init__(self):
        self.danhSach = []

    def maTaiLieuDuyNhat(self, ma):
        return all(tl.getMaTaiLieu() != ma for tl in self.danhSach)

    def themTaiLieu(self, tl):
        self.danhSach.append(tl)

    def xoaTaiLieu(self, ma):
        self.danhSach = [tl for tl in self.danhSach if tl.getMaTaiLieu() != ma]
