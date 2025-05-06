class TaiLieu:
        self.__soBanPhatHanh = soBanPhatHanh

    def getMaTaiLieu(self): return self.__maTaiLieu
    def setMaTaiLieu(self, ma): self.__maTaiLieu = ma

    def getTenNxb(self): return self.__tenNxb
    def setTenNxb(self, nxb): self.__tenNxb = nxb

    def getSoBanPhatHanh(self): return self.__soBanPhatHanh
    def setSoBanPhatHanh(self, soBan): self.__soBanPhatHanh = soBan

    def thongTin(self):
        return f"Mã TL: {self.getMaTaiLieu()}, NXB: {self.getTenNxb()}, Số bản: {self.getSoBanPhatHanh()}"


class Sach(TaiLieu):
    def __init__(self, maTaiLieu, tenNxb, soBanPhatHanh, soTrang, tenTg):
        super().__init__(maTaiLieu, tenNxb, soBanPhatHanh)
        self.__soTrang = soTrang
        self.__tenTg = tenTg

    def getSoTrang(self): return self.__soTrang
    def setSoTrang(self, so): self.__soTrang = so

    def getTenTg(self): return self.__tenTg
    def setTenTg(self, ten): self.__tenTg = ten

    def thongTin(self):
        return f"{super().thongTin()}, Tác giả: {self.getTenTg()}, Số trang: {self.getSoTrang()}"


class TapChi(TaiLieu):
    def __init__(self, maTaiLieu, tenNxb, soBanPhatHanh, soPhatHanh, thangPhatHanh):
        super().__init__(maTaiLieu, tenNxb, soBanPhatHanh)
        self.__soPhatHanh = soPhatHanh
        self.__thangPhatHanh = thangPhatHanh

    def getSoPhatHanh(self): return self.__soPhatHanh
    def setSoPhatHanh(self, so): self.__soPhatHanh = so

    def getThangPhatHanh(self): return self.__thangPhatHanh
    def setThangPhatHanh(self, thang): self.__thangPhatHanh = thang

    def thongTin(self):
        return f"{super().thongTin()}, Số PH: {self.getSoPhatHanh()}, Tháng PH: {self.getThangPhatHanh()}"


class Bao(TaiLieu):
    def __init__(self, maTaiLieu, tenNxb, soBanPhatHanh, ngayPhatHanh):
        super().__init__(maTaiLieu, tenNxb, soBanPhatHanh)
        self.__ngayPhatHanh = ngayPhatHanh

    def getNgayPhatHanh(self): return self.__ngayPhatHanh
    def setNgayPhatHanh(self, ngay): self.__ngayPhatHanh = ngay

    def thongTin(self):
        return f"{super().thongTin()}, Ngày PH: {self.getNgayPhatHanh()}"


class QuanLySach:
    def __init__(self):
        self.danhSach = []

    def maTaiLieuDuyNhat(self, ma):
        return not any(tl.getMaTaiLieu() == ma for tl in self.danhSach)

    def themTaiLieu(self, tl):
        self.danhSach.append(tl)

    def xoaTaiLieu(self, ma):
        self.danhSach = [tl for tl in self.danhSach if tl.getMaTaiLieu() != ma]

    def getTatCaTaiLieu(self):
        return self.danhSach

    def timKiemTheoLoai(self, loai):
        loaiDict = {"sach": Sach, "tapchi": TapChi, "bao": Bao}
        return [tl for tl in self.danhSach if isinstance(tl, loaiDict.get(loai, TaiLieu))]
