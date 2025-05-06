import wx
from logic import Sach, TapChi, Bao, QuanLySach

USERS = {
    "admin": "1234",
    "user": "pass"
}

class LoginFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Đăng nhập", size=(300, 200))
        panel = wx.Panel(self)

        wx.StaticText(panel, label="Tên đăng nhập:", pos=(20, 30))
        self.txtUser = wx.TextCtrl(panel, pos=(120, 25), size=(150, -1))

        wx.StaticText(panel, label="Mật khẩu:", pos=(20, 70))
        self.txtPass = wx.TextCtrl(panel, pos=(120, 65), style=wx.TE_PASSWORD, size=(150, -1))

        self.btnLogin = wx.Button(panel, label="Đăng nhập", pos=(100, 110))
        self.btnLogin.Bind(wx.EVT_BUTTON, self.onLogin)

    def onLogin(self, event):
        username = self.txtUser.GetValue()
        password = self.txtPass.GetValue()
        if USERS.get(username) == password:
            self.Hide()
            frame = MainFrame()
            frame.Show()
        else:
            wx.MessageBox("Sai tài khoản hoặc mật khẩu", "Lỗi", wx.OK | wx.ICON_ERROR)


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Quản lý tài liệu", size=(600, 400))
        panel = wx.Panel(self)
        self.ql = QuanLySach()

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.listbox = wx.ListBox(panel)
        vbox.Add(self.listbox, 1, wx.EXPAND | wx.ALL, 10)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.btnAdd = wx.Button(panel, label="Thêm")
        self.btnDel = wx.Button(panel, label="Xoá")
        self.btnShow = wx.Button(panel, label="Hiển thị")
        self.btnSearch = wx.Button(panel, label="Tìm kiếm")

        hbox.AddMany([(self.btnAdd, 1), (self.btnDel, 1), (self.btnShow, 1), (self.btnSearch, 1)])
        vbox.Add(hbox, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)

        panel.SetSizer(vbox)

        self.btnAdd.Bind(wx.EVT_BUTTON, self.onAdd)
        self.btnDel.Bind(wx.EVT_BUTTON, self.onDel)
        self.btnShow.Bind(wx.EVT_BUTTON, self.onShow)
        self.btnSearch.Bind(wx.EVT_BUTTON, self.onSearch)

    def onAdd(self, event):
        dlg = wx.TextEntryDialog(self, "Nhập loại (sach/tapchi/bao):", "Loại")
        if dlg.ShowModal() == wx.ID_OK:
            loai = dlg.GetValue().lower()
            ma = wx.GetTextFromUser("Mã tài liệu:")
            if not self.ql.maTaiLieuDuyNhat(ma):
                wx.MessageBox("Mã đã tồn tại!")
                return
            nxb = wx.GetTextFromUser("Tên NXB:")
            soBan = int(wx.GetTextFromUser("Số bản phát hành:"))

            if loai == "sach":
                tg = wx.GetTextFromUser("Tác giả:")
                soTrang = int(wx.GetTextFromUser("Số trang:"))
                self.ql.themTaiLieu(Sach(ma, nxb, soBan, soTrang, tg))
            elif loai == "tapchi":
                soPH = wx.GetTextFromUser("Số phát hành:")
                thangPH = int(wx.GetTextFromUser("Tháng phát hành:"))
                self.ql.themTaiLieu(TapChi(ma, nxb, soBan, soPH, thangPH))
            elif loai == "bao":
                ngayPH = wx.GetTextFromUser("Ngày phát hành:")
                self.ql.themTaiLieu(Bao(ma, nxb, soBan, ngayPH))
            else:
                wx.MessageBox("Loại không hợp lệ.")
        dlg.Destroy()

    def onDel(self, event):
        ma = wx.GetTextFromUser("Nhập mã cần xoá:")
        self.ql.xoaTaiLieu(ma)

    def onShow(self, event):
        self.listbox.Clear()
        for tl in self.ql.getTatCaTaiLieu():
            self.listbox.Append(tl.thongTin())

    def onSearch(self, event):
        loai = wx.GetTextFromUser("Nhập loại (sach/tapchi/bao):")
        ketQua = self.ql.timKiemTheoLoai(loai)
        self.listbox.Clear()
        for tl in ketQua:
            self.listbox.Append(tl.thongTin())


if __name__ == "__main__":
    app = wx.App()
    frame = LoginFrame()
    frame.Show()
    app.MainLoop()
