import string
def tach_tu(van_ban):
    dau_cau = string.punctuation 
    van_ban_sach = ""
    for ky_tu in van_ban:
        if ky_tu in dau_cau:
            van_ban_sach += " "
        else:
            van_ban_sach += ky_tu
    danh_sach_tu = []
    for tu in van_ban_sach.split():
        if tu != "":
            danh_sach_tu.append(tu)
    return danh_sach_tu
def dem_tong_so_tu(danh_sach_tu):
    return len(danh_sach_tu)
def tim_tu_xuat_hien_nhieu_nhat(danh_sach_tu):
    if not danh_sach_tu:
        return None, 0
    tu_thuong = []
    for tu in danh_sach_tu:
        tu_thuong.append(tu.lower())
    tan_so = {}
    for tu in tu_thuong:
        if tu in tan_so:
            tan_so[tu] += 1
        else:
            tan_so[tu] = 1
    tu_nhieu_nhat = ""
    so_lan_max = 0
    for tu, so_lan in tan_so.items():
        if so_lan > so_lan_max:
            so_lan_max = so_lan
            tu_nhieu_nhat = tu

    return tu_nhieu_nhat, so_lan_max
def hien_thi_ket_qua(van_ban_goc, danh_sach_tu, tong_tu, tu_max, so_lan):
    print("\n" + "=" * 50)
    print("       KẾT QUẢ ")
    print("=" * 50)
    print(f"\nVăn bản gốc:\n   \"{van_ban_goc}\"")
    print(f"\n Danh sách các từ đã tách:")
    print(f"   {danh_sach_tu}")
    print(f"\nTổng số từ: {tong_tu} từ")
    if tu_max:
        print(f"\n Từ xuất hiện nhiều nhất: \"{tu_max}\" ({so_lan} lần)")
    else:
        print("\n  Không có từ .")
    print("\n" + "=" * 50)
def main():
    print("=" * 50)
    print("    PHÂN TÍCH VĂN BẢN")
    print("=" * 50)
    print("Nhập đoạn văn bản để phân tích.")
    print("-" * 50)

    van_ban = input("\nNhập văn bản: ").strip()

    if van_ban == "":
        print("\n  Chưa nhập nội dung")
        return
    danh_sach_tu = tach_tu(van_ban)
    tong_tu = dem_tong_so_tu(danh_sach_tu)
    tu_max, so_lan = tim_tu_xuat_hien_nhieu_nhat(danh_sach_tu)
    hien_thi_ket_qua(van_ban, danh_sach_tu, tong_tu, tu_max, so_lan)
if __name__ == "__main__":
    main()
