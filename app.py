
import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CẤU HÌNH TRANG WEB
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 QUẢN LÝ ĐIỂM SINH VIÊN")
st.caption("Ứng dụng quản lý và thống kê kết quả học tập - UTH")

# 2. DỮ LIỆU 10 SINH VIÊN
data = {
    "MSSV": [
        "22510001", "22510002", "22510003", "22510004",
        "22510005", "22510006", "22510007", "22510008",
        "22510009", "22510010"
    ],
    "Họ tên": [
        "Nguyễn Văn An", "Trần Thị Bình",
        "Lê Hoàng Nam", "Nguyễn Văn Luật",
        "Võ Quốc Bảo", "Đặng Thu Hà",
        "Bùi Thành Công", "Hoàng Ngọc Linh",
        "Đỗ Minh Quân", "Tống Nguyễn Anh TÀi"
    ],
    "Chuyên cần": [9, 8, 7, 10, 6, 9, 8, 7, 5, 10],
    "Giữa kỳ":    [8, 7, 6, 9, 5, 8, 7, 6, 4, 9],
    "Cuối kỳ":    [9, 8, 7, 10, 6, 9, 8, 7, 5, 10]
}

df = pd.DataFrame(data)

# 3. TÍNH ĐIỂM TỔNG KẾT
# Công thức minh họa: Chuyên cần 10%, giữa kỳ 30%, cuối kỳ 60%
df["Tổng kết"] = (
    df["Chuyên cần"] * 0.1
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.6
).round(2)

# 4. XẾP LOẠI SINH VIÊN
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# 5. HIỂN THỊ BẢNG ĐIỂM
st.subheader("📋 Bảng điểm của 10 sinh viên")

st.dataframe(
    df[[
        "Họ tên", "Chuyên cần", "Giữa kỳ",
        "Cuối kỳ", "Tổng kết", "Xếp loại"
    ]],
    use_container_width=True,
    hide_index=True
)

# 6. THỐNG KÊ ĐIỂM LỚP
diem_tb = df["Tổng kết"].mean()
sv_cao_nhat = df.loc[df["Tổng kết"].idxmax()]
sv_thap_nhat = df.loc[df["Tổng kết"].idxmin()]
so_sv_dat = int((df["Tổng kết"] >= 5.0).sum())

st.subheader("📊 Thống kê kết quả học tập")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Điểm trung bình lớp", f"{diem_tb:.2f}")
c2.metric("Số sinh viên đạt", f"{so_sv_dat}/10")
c3.metric("Điểm cao nhất", f"{sv_cao_nhat['Tổng kết']:.2f}")
c4.metric("Điểm thấp nhất", f"{sv_thap_nhat['Tổng kết']:.2f}")

st.success(
    f"Sinh viên cao nhất: {sv_cao_nhat['Họ tên']} "
    f"({sv_cao_nhat['Tổng kết']:.2f} điểm)"
)

st.warning(
    f"Sinh viên thấp nhất: {sv_thap_nhat['Họ tên']} "
    f"({sv_thap_nhat['Tổng kết']:.2f} điểm)"
)

# 7. SELECTBOX CHỌN SINH VIÊN
st.subheader("🔎 Tra cứu điểm sinh viên")

ten_sv = st.selectbox(
    "Chọn sinh viên:",
    df["Họ tên"].tolist()
)

sv = df[df["Họ tên"] == ten_sv].iloc[0]

st.write(f"**MSSV:** {sv['MSSV']}")

d1, d2, d3, d4, d5 = st.columns(5)

d1.metric("Chuyên cần", f"{sv['Chuyên cần']:.1f}")
d2.metric("Giữa kỳ", f"{sv['Giữa kỳ']:.1f}")
d3.metric("Cuối kỳ", f"{sv['Cuối kỳ']:.1f}")
d4.metric("Tổng kết", f"{sv['Tổng kết']:.2f}")
d5.metric("Xếp loại", sv["Xếp loại"])

# 8. BIỂU ĐỒ CỘT ĐIỂM TỔNG KẾT
st.subheader("📈 Biểu đồ điểm tổng kết của 10 sinh viên")

fig = px.bar(
    df,
    x="Họ tên",
    y="Tổng kết",
    color="Tổng kết",
    text="Tổng kết",
    title="So sánh điểm tổng kết giữa các sinh viên",
    color_continuous_scale="Blues"
)

fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

fig.update_layout(
    xaxis_title="Họ tên sinh viên",
    yaxis_title="Điểm tổng kết",
    yaxis_range=[0, 11],
    xaxis_tickangle=-35,
    coloraxis_showscale=False
)

st.plotly_chart(fig, use_container_width=True)

# 9. THÔNG TIN NGƯỜI TẠO ỨNG DỤNG
st.divider()

st.markdown(
    """
    <div style="text-align:center; color:gray; font-size:12px;">
        Người thực hiện: Tống Nguyễn Ngọc Thành <br>
        MSSV: THAY_BANG_MSSV_CUA_BAN<br>
        Môn học: Trí tuệ nhân tạo và ứng dụng - UTH
    </div>
    """,
    unsafe_allow_html=True
)
  
