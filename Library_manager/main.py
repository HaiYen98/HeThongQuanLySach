import tkinter as tk
from tkinter import ttk, messagebox
from classes import Sach, TapChi, Bao, QuanLySach

quan_ly = QuanLySach()

# Giao diện đăng nhập
def show_login():
    login_window = tk.Tk()
    login_window.title("Đăng nhập")

    tk.Label(login_window, text="Tên người dùng:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(login_window, text="Mật khẩu:").grid(row=1, column=0, padx=10, pady=5)

    username_entry = tk.Entry(login_window)
    password_entry = tk.Entry(login_window, show="*")
    username_entry.grid(row=0, column=1, padx=10, pady=5)
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    def login():
        if username_entry.get() == "admin" and password_entry.get() == "123":
            login_window.destroy()
            show_main_window()
        else:
            messagebox.showerror("Lỗi", "Sai thông tin đăng nhập.")

    tk.Button(login_window, text="Đăng nhập", command=login).grid(row=2, columnspan=2, pady=10)
    login_window.mainloop()

# Giao diện chính
def show_main_window():
    window = tk.Tk()
    window.title("Hệ thống quản lý thư viện")
    window.geometry("700x400")

    # Tabs
    tabControl = ttk.Notebook(window)
    tab_them = ttk.Frame(tabControl)
    tab_xoa = ttk.Frame(tabControl)
    tab_danh_sach = ttk.Frame(tabControl)
    tab_tim_kiem = ttk.Frame(tabControl)

    tabControl.add(tab_them, text="Thêm tài liệu")
    tabControl.add(tab_xoa, text="Xoá tài liệu")
    tabControl.add(tab_danh_sach, text="Danh sách tài liệu")
    tabControl.add(tab_tim_kiem, text="Tìm kiếm")
    tabControl.pack(expand=1, fill="both")

    # === Tab Thêm ===
    ttk.Label(tab_them, text="Loại tài liệu:").grid(row=0, column=0, padx=5, pady=5)
    loai_combobox = ttk.Combobox(tab_them, values=["Sách", "Tạp chí", "Báo"])
    loai_combobox.grid(row=0, column=1, padx=5, pady=5)

    entries = {}
    labels = ["Mã tài liệu", "Tên NXB", "Số bản phát hành", "Tác giả/Số phát hành/Ngày phát hành", "Số trang/Tháng phát hành"]
    for i, label in enumerate(labels, start=1):
        ttk.Label(tab_them, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
        entry = ttk.Entry(tab_them)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries[label] = entry

    def them_tai_lieu():
        loai = loai_combobox.get()
        ma = entries["Mã tài liệu"].get()
        nxb = entries["Tên NXB"].get()
        try:
            so_ban = int(entries["Số bản phát hành"].get())
        except ValueError:
            messagebox.showerror("Lỗi", "Số bản phát hành phải là số.")
            return

        if not quan_ly.maTaiLieuDuyNhat(ma):
            messagebox.showerror("Lỗi", "Mã tài liệu đã tồn tại.")
            return

        if loai == "Sách":
            tg = entries["Tác giả/Số phát hành/Ngày phát hành"].get()
            try:
                so_trang = int(entries["Số trang/Tháng phát hành"].get())
            except ValueError:
                messagebox.showerror("Lỗi", "Số trang phải là số.")
                return
            quan_ly.themTaiLieu(Sach(ma, nxb, so_ban, so_trang, tg))

        elif loai == "Tạp chí":
            so_ph = entries["Tác giả/Số phát hành/Ngày phát hành"].get()
            try:
                thang_ph = int(entries["Số trang/Tháng phát hành"].get())
            except ValueError:
                messagebox.showerror("Lỗi", "Tháng phát hành phải là số.")
                return
            quan_ly.themTaiLieu(TapChi(ma, nxb, so_ban, so_ph, thang_ph))

        elif loai == "Báo":
            ngay_ph = entries["Tác giả/Số phát hành/Ngày phát hành"].get()
            quan_ly.themTaiLieu(Bao(ma, nxb, so_ban, ngay_ph))
        else:
            messagebox.showerror("Lỗi", "Chọn loại tài liệu hợp lệ.")
            return

        messagebox.showinfo("Thành công", "Đã thêm tài liệu.")

    ttk.Button(tab_them, text="Thêm tài liệu", command=them_tai_lieu).grid(row=7, columnspan=2, pady=10)

    # === Tab Xoá ===
    ttk.Label(tab_xoa, text="Mã tài liệu cần xoá:").grid(row=0, column=0, padx=5, pady=5)
    xoa_entry = ttk.Entry(tab_xoa)
    xoa_entry.grid(row=0, column=1, padx=5, pady=5)

    def xoa_tai_lieu():
        ma = xoa_entry.get()
        quan_ly.xoaTaiLieu(ma)
        messagebox.showinfo("Thông báo", f"Đã xoá tài liệu (nếu có).")

    ttk.Button(tab_xoa, text="Xoá", command=xoa_tai_lieu).grid(row=1, columnspan=2, pady=10)

    # === Tab Danh sách ===
    danh_sach_text = tk.Text(tab_danh_sach, width=80, height=20)
    danh_sach_text.pack()

    def hien_thi_danh_sach():
        danh_sach_text.delete("1.0", tk.END)
        if not quan_ly.danhSach:
            danh_sach_text.insert(tk.END, "Danh sách rỗng.\n")
            return
        for tl in quan_ly.danhSach:
            if isinstance(tl, Sach):
                loai = "Sách"
            elif isinstance(tl, TapChi):
                loai = "Tạp chí"
            elif isinstance(tl, Bao):
                loai = "Báo"
            else:
                loai = "Khác"
            danh_sach_text.insert(tk.END, f"Loại: {loai}\n")
            thong_tin = f"Mã: {tl.getMaTaiLieu()}, NXB: {tl.getTenNxb()}, Số bản: {tl.getSoBanPhatHanh()}\n"
            if loai == "Sách":
                thong_tin += f"Tác giả: {tl.getTenTg()}, Số trang: {tl.getSoTrang()}\n"
            elif loai == "Tạp chí":
                thong_tin += f"Số phát hành: {tl.getSoPhatHanh()}, Tháng: {tl.getThangPhatHanh()}\n"
            elif loai == "Báo":
                thong_tin += f"Ngày phát hành: {tl.getNgayPhatHanh()}\n"
            danh_sach_text.insert(tk.END, thong_tin + "-------------------\n")

    ttk.Button(tab_danh_sach, text="Hiển thị", command=hien_thi_danh_sach).pack(pady=10)

    # === Tab Tìm kiếm ===
    ttk.Label(tab_tim_kiem, text="Thể loại (sach/tapchi/bao):").pack(pady=5)
    loai_entry = ttk.Entry(tab_tim_kiem)
    loai_entry.pack(pady=5)

    tim_kiem_text = tk.Text(tab_tim_kiem, width=80, height=20)
    tim_kiem_text.pack()

    def tim_kiem():
        loai = loai_entry.get().lower()
        tim_kiem_text.delete("1.0", tk.END)
        loai_map = {"sach": Sach, "tapchi": TapChi, "bao": Bao}
        if loai not in loai_map:
            tim_kiem_text.insert(tk.END, "Loại không hợp lệ.\n")
            return
        found = False
        for tl in quan_ly.danhSach:
            if isinstance(tl, loai_map[loai]):
                found = True
                tim_kiem_text.insert(tk.END, f"Mã: {tl.getMaTaiLieu()}, NXB: {tl.getTenNxb()}, Số bản: {tl.getSoBanPhatHanh()}\n")
        if not found:
            tim_kiem_text.insert(tk.END, "Không tìm thấy tài liệu phù hợp.\n")

    ttk.Button(tab_tim_kiem, text="Tìm", command=tim_kiem).pack(pady=10)

    window.mainloop()

# Khởi chạy
if __name__ == "__main__":
    show_login()
