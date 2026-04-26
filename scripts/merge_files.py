import csv

source_files = [
    (r"C:\softwares\onedrive\Desktop\baseline\data_tahoe\scgen\c4.csv", "c4"),
    (r"C:\softwares\onedrive\Desktop\baseline\data_tahoe\scgen\c17.csv", "c17"),
    (r"C:\softwares\onedrive\Desktop\baseline\data_tahoe\scgen\c18.csv", "c18"),
    (r"C:\softwares\onedrive\Desktop\baseline\data_tahoe\scgen\c19.csv", "c19"),
    (r"C:\softwares\onedrive\Desktop\baseline\data_tahoe\scgen\c20.csv", "c20"),
    # (r"C:\softwares\onedrive\Desktop\baseline\data_tahoe\scgen\c22.csv", "c22"),
    (r"C:\softwares\onedrive\Desktop\baseline\data_tahoe\scgen\c23.csv", "c23"),
    (r"C:\softwares\onedrive\Desktop\baseline\data_tahoe\scgen\c24.csv", "c24"),
    (r"C:\softwares\onedrive\Desktop\baseline\data_tahoe\scgen\c31.csv", "c31"),
    (r"C:\softwares\onedrive\Desktop\baseline\data_tahoe\scgen\c38.csv", "c38"),
]

output_file = r"C:\softwares\onedrive\Desktop\baseline\data_tahoe\scgen\scgen_merged.csv"

# ---- 1. 从第一个源文件读取表头行（第 1 行） ----
header = None
with open(source_files[0][0], "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # 第 1 行即表头

# 在表头最前面插入自定义列名
header = ["cell_name"] + header

# ---- 2. 收集两个源文件各自的第 4 行 ----
rows_to_write = []
for file_path, label in source_files:
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 3:          # 第 4 行（索引 3）
                rows_to_write.append([label] + row)
                break
            elif i > 3:
                break

# ---- 3. 写入目标文件：表头 + 两行数据 ----
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)           # 第 1 行：表头
    writer.writerows(rows_to_write)   # 第 2~3 行：数据

print(f"写入完成，目标文件：{output_file}")