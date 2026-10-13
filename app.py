import pandas as pd
import matplotlib.pyplot as plt

# 1. Tạo dữ liệu sinh viên
data = {
    "họ và tên": [
        "Nguyễn Văn A", "Nguyễn Văn B", "Nguyễn Văn C",
        "Nguyễn Văn D", "Nguyễn Văn E", "Nguyễn Văn F",
        "Nguyễn Văn G", "Nguyễn Văn K", "Nguyễn Văn N",
        "Nguyễn Văn M"
    ],
    "điểm chuyên cần": [7, 8, 9, 9, 7, 6, 8, 9, 6, 5],
    "điểm giữa kỳ": [8, 6, 8, 5, 6, 9, 10, 6, 8, 9],
    "điểm cuối kỳ": [8, 9, 6, 8, 6, 9, 7, 5, 5, 9]
}

Bang_diem = pd.DataFrame(data)

# 2. Tính điểm tổng kết
Bang_diem["tổng kết"] = (
    0.2 * Bang_diem["điểm chuyên cần"]
    + 0.3 * Bang_diem["điểm giữa kỳ"]
    + 0.5 * Bang_diem["điểm cuối kỳ"]
)

# 3. Hàm xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

# 4. Xếp loại sinh viên
Bang_diem["xếp loại"] = Bang_diem["tổng kết"].apply(xep_loai)

# 5. Hiển thị bảng điểm
print("BẢNG ĐIỂM SINH VIÊN:")
print(Bang_diem.round(2).to_string(index=False))

# 6. Thống kê điểm
diem_tb = Bang_diem["tổng kết"].mean()
diem_max = Bang_diem["tổng kết"].max()
diem_min = Bang_diem["tổng kết"].min()
so_sv_dat = (Bang_diem["tổng kết"] >= 5).sum()
so_sv_khong_dat = (Bang_diem["tổng kết"] < 5).sum()

print("\nTHỐNG KÊ:")
print(f"Điểm trung bình: {diem_tb:.2f}")
print(f"Điểm cao nhất: {diem_max:.2f}")
print(f"Điểm thấp nhất: {diem_min:.2f}")
print(f"Số sinh viên đạt: {so_sv_dat}")
print(f"Số sinh viên không đạt: {so_sv_khong_dat}")

# 7. Vẽ biểu đồ điểm tổng kết
plt.figure(figsize=(12, 6))

plt.bar(
    Bang_diem["họ và tên"],
    Bang_diem["tổng kết"],
    color="skyblue",
    edgecolor="black"
)

plt.title("Điểm tổng kết của 10 sinh viên")
plt.xlabel("Tên sinh viên")
plt.ylabel("Điểm tổng kết")
plt.ylim(0, 10)
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
st.pyplot(plt.gcf())
