def tinh_bmi(can_nang, chieu_cao):
    return can_nang / (chieu_cao ** 2)
def phan_loai_bmi(bmi):
    if bmi < 18.5:
        return "GẦY"
    elif 18.5 <= bmi <= 24.9:
        return "BÌNH THƯỜNG"
    else:
        return "THỪA CÂN"
def nhap_so_thuc(thong_bao):
    while True:
        try:
            gia_tri = float(input(thong_bao))
            return gia_tri
        except ValueError:
            print(" Nhập một số hợp lệ \n")
def hien_thi_ket_qua(can_nang, chieu_cao, bmi, nhan, bieu_tuong, loi_khuyen):
    print("\n" + "=" * 50)
    print("           KẾT QUẢ TÍNH CHỈ SỐ BMI")
    print("=" * 50)
    print(f"    Cân nặng   : {can_nang} kg")
    print(f"   Chiều cao  : {chieu_cao} m")
    print(f"   Chỉ số BMI : {bmi:.2f}")
    print("-" * 50)
    print(f"  {bieu_tuong} Phân loại    : {nhan}")
    print(f"   Lời khuyên : {loi_khuyen}")
    print("=" * 50)
def hien_thi_bang_phan_loai():
    print("\n   BẢNG PHÂN LOẠI BMI THAM KHẢO:")
    print("  " + "-" * 35)
    print("    Gầy          : BMI < 18.5")
    print("   Bình thường  : 18.5 – 24.9")
    print("   Thừa cân     : BMI ≥ 25.0")
    print("  " + "-" * 35)
def main():
    print("=" * 50)
    print("     CÔNG CỤ TÍNH CHỈ SỐ BMI")
    print("=" * 50)
    hien_thi_bang_phan_loai()
    print("\n  Nhập thông tin của bạn:\n")
    can_nang = nhap_so_thuc("  Cân nặng (kg): ")
    while True:
        chieu_cao = nhap_so_thuc("  Chiều cao (m): ")
        try:
            bmi = tinh_bmi(can_nang, chieu_cao)
            break  
        except ZeroDivisionError:
            print("  Chiều cao không thể bằng 0\n")
    nhan, bieu_tuong, loi_khuyen = phan_loai_bmi(bmi)
    hien_thi_ket_qua(can_nang, chieu_cao, bmi, nhan, bieu_tuong, loi_khuyen)
if __name__ == "__main__":
    main()
