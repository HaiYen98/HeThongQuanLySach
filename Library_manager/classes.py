# classes.py

class TaiLieu:
    def __init__(self, ma_tai_lieu, ten_nxb, so_ban_phat_hanh):
        self.ma_tai_lieu = ma_tai_lieu
        self.ten_nxb = ten_nxb
        self.so_ban_phat_hanh = so_ban_phat_hanh

    def getMaTaiLieu(self):
        return self.ma_tai_lieu

    def getTenNxb(self):
        return self.ten_nxb

    def getSoBanPhatHanh(self):
        return self.so_ban_phat_hanh


class Sach(TaiLieu):
    def __init__(self, ma_tai_lieu, ten_nxb, so_ban_phat_hanh, so_trang, ten_tg):
        super().__init__(ma_tai_lieu, ten_nxb, so_ban_phat_hanh)
        self.so_trang = so_trang
        self.ten_tg = ten_tg

    def getSoTrang(self):
        return self.so_trang

    def getTenTg(self):
        return self.ten_tg


class TapChi(TaiLieu):
    def __init__(self, ma_tai_lieu, ten_nxb, so_ban_phat_hanh, so_phat_hanh, thang_phat_hanh):
        super().__init__(ma_tai_lieu, ten_nxb, so_ban_phat_hanh)
        self.so_phat_hanh = so_phat_hanh
        self.thang_phat_hanh = thang_phat_hanh

    def getSoPhatHanh(self):
        return self.so_phat_hanh

    def getThangPhatHanh(self):
        return self.thang_phat_hanh


class Bao(TaiLieu):
    def __init__(self, ma_tai_lieu, ten_nxb, so_ban_phat_hanh, ngay_phat_hanh):
        super().__init__(ma_tai_lieu, ten_nxb, so_ban_phat_hanh)
        self.ngay_phat_hanh = ngay_phat_hanh

    def getNgayPhatHanh(self):
        return self.ngay_phat_hanh


class QuanLySach:
    def __init__(self):
        self.danhSach = []

    def themTaiLieu(self, tai_lieu):
        self.danhSach.append(tai_lieu)

    def xoaTaiLieu(self, ma_tai_lieu):
        self.danhSach = [tl for tl in self.danhSach if tl.getMaTaiLieu() != ma_tai_lieu]

    def timKiemTheoLoai(self, loai):
        return [tl for tl in self.danhSach if isinstance(tl, loai)]

    def maTaiLieuDuyNhat(self, ma):
        return all(tl.getMaTaiLieu() != ma for tl in self.danhSach)
