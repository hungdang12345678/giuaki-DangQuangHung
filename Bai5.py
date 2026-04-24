import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
kho_hang = {
    'Ban phim'    : 150,
    'Chuot': 80,
    'Man hinh'    : 120,
}
def hien_thi_kho(kho, tieu_de=" TRẠNG THÁI KHO HÀNG"):
    print(f"\n  {tieu_de}")
    print("  " + "-" * 35)
    tong = sum(kho.values())
    for mat_hang, so_luong in kho.items():
        ty_trong = (so_luong / tong) * 100 if tong > 0 else 0
        print(f"  {'•'} {mat_hang:<12}: {so_luong:>5} sp  ({ty_trong:.1f}%)")
    print("  " + "-" * 35)
    print(f"  {'Tổng cộng':<12}: {tong:>5} sp")
def nhap_so_luong(ten_mat_hang):
    while True:
        try:
            so_luong = int(input(f"\n  Nhập số lượng '{ten_mat_hang}': "))
            if so_luong < 0:
                print("   Số lượng >0. Vui lòng nhập lại.")
            else:
                return so_luong
        except ValueError:
            print("   Vui lòng nhập số nguyên hợp lệ!")
def ve_bieu_do_tron(kho, ten_file="bieu_do_kho_hang.png"):
    nhan       = list(kho.keys())
    gia_tri    = list(kho.values())
    tong       = sum(gia_tri)
    mau_sac = ["#4FA74E", "#F23F2B", "#14B6DF", "#D216E7", "#2117E2"]
    lon_nhat = gia_tri.index(max(gia_tri))
    tach_ra  = [0.07 if i == lon_nhat else 0 for i in range(len(gia_tri))]
    fig, ax = plt.subplots(figsize=(9, 6), facecolor="#F8F9FA")
    ax.set_facecolor("#F8F9FA")
    wedges, texts, autotexts = ax.pie(
        gia_tri,
        labels=None,
        autopct=lambda pct: f"{pct:.1f}%\n({int(round(pct * tong / 100))} sp)",
        startangle=140,
        colors=mau_sac[:len(nhan)],
        explode=tach_ra,
        pctdistance=0.72,
        wedgeprops=dict(edgecolor="white", linewidth=2.5),
        shadow=True,
    )
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_fontweight("bold")
        autotext.set_color("white")
    legend_nhan = [
        f"  {nhan[i]}  ({gia_tri[i]} sp)" for i in range(len(nhan))
    ]
    patches = [
        mpatches.Patch(color=mau_sac[i], label=legend_nhan[i])
        for i in range(len(nhan))
    ]
    ax.legend(
        handles=patches,
        loc="center left",
        bbox_to_anchor=(1.0, 0.5),
        fontsize=11,
        frameon=True,
        framealpha=0.9,
        edgecolor="#CCCCCC",
        title="Mặt hàng",
        title_fontsize=12,
    )
    ax.set_title(
        "TỶ TRỌNG TỒN KHO THEO MẶT HÀNG",
        fontsize=15,
        fontweight="bold",
        pad=20,
        color="#2C3E50",
    )
    fig.text(
        0.5, 0.02,
        f"Tổng tồn kho: {tong} sản phẩm",
        ha="center", fontsize=10, color="#7F8C8D"
    )
    plt.tight_layout()
    plt.savefig(ten_file, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\n  Biểu đồ đã được lưu thành file '{ten_file}'")
def main():
    print("=" * 45)
    print("    QUẢN LÝ KHO HÀNG & BIỂU ĐỒ TỶ TRỌNG")
    print("=" * 45)
    hien_thi_kho(kho_hang, " TỒN KHO BAN ĐẦU")
    print("\n    Thêm mặt hàng mới — 'Card do hoa'")
    so_luong_vi_da = nhap_so_luong("Card do hoa")
    kho_hang["Card do hoa"] = so_luong_vi_da
    print(f"   Đã thêm 'Card do hoa' với số lượng: {so_luong_vi_da} sp")
    print("\n    Xuất kho 'Ban phim' — giảm 30 đơn vị")
    kho_hang["Ban phim"] -= 30
    print(f"   Tồn kho 'Ban phim' còn lại: {kho_hang['Ban phim']} sp")
    hien_thi_kho(kho_hang, " TỒN KHO SAU CẬP NHẬT")
    print("\n   Vẽ biểu đồ tỷ trọng tồn kho...")
    ve_bieu_do_tron(kho_hang)
    print("\n" + "=" * 45)
    print("    Kiểm tra file ảnh biểu đồ.")
    print("=" * 45)
if __name__ == "__main__":
    main()
