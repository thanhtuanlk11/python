# có 2 loại mode r= read , w= write
file = open("student.csv",mode ="r", encoding="utf-8-sig") 
file_new = open("student_new.csv",mode="w",encoding="utf-8-sig")

header =file.readline()
#.stip() là hàm loại bỏ kí tự xuống dòng ở cuối 
file_new.write(header.strip() + ",Điểm trung bình, Học Lực")

# mỗi cái readline là đọc từng hàng 
row = file.readline()
row_list = row.split(",") 

math = float(row_list[2])
lit = float(row_list[3])

ave = (math+lit)/2
# làm tròn 1 chữ số phần thập phân 
ave = round(ave,1)

print(ave)
