import pandas as pd
data = {"họ và tên": ["Nguyễn Văn A",
                      "Nguyễn Văn B",
                      "Nguyễn Văn C",
                      "Nguyễn Văn D",
                      "Nguyễn Văn E",
                      "Nguyễn Văn F",
                      "Nguyễn Văn G",
                      "Nguyễn Văn K",
                      "Nguyễn Văn N",
                      "Nguyễn Văn M",
                      ], "điểm chuyên cần": [7,8,9,9,7,6,8,9,6,5], "điểm giữa kỳ": [8,6,8,5,6,9,10,6,8,9], "điểm cuối kỳ": [8,9,6,8,6,9,7,5,5,9]}
Bang_diem = pd.DataFrame(data)

Bang_diem["tổng kết"] = 0.2 * Bang_diem["điểm chuyên cần"] + 0.3 * Bang_diem["điểm giữa kỳ"] + 0.5 * Bang_diem["điểm cuối kỳ"]
print(Bang_diem)

def xep_loai(diem):
  if diem >= 8.5:
    return "giỏi"
  elif diem >= 7:
    return "khá"
  elif diem >= 5:
    return "trung bình"
  else:
    return "yếu"

Bang_diem["xep_loai"] = Bang_diem["tổng kết"].apply(xep_loai)
print(Bang_diem)
print("điểm trung bình: ",Bang_diem["tổng kết"].mean())
print("điểm cao nhất: ", Bang_diem["tổng kết"].max())
print("điểm thấp nhất: ", Bang_diem["tổng kết"].min())
print((Bang_diem["tổng kết"] >= 5).sum())
import matplotlib.pyplot as plt
plt.bar(Bang_diem["họ và tên"],Bang_diem["tổng kết"])
plt.title("điểm tổng kết của 10 sinh viên")
plt.xlabel("tên sinh viên")
plt.ylabel("điểm tổng kết")
plt.xticks(rotation=30)
plt.show()
