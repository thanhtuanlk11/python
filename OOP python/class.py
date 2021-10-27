def nhap():
	for i in range(n):
		a[i]=hocsinh(0,0,0,0)
		print('Nhập học sinh thứ',i+1)
		a[i].ten=input('Nhập tên:')
		a[i].lop=input('Nhập lớp:')
		a[i].diem=float(input('Nhập điểm:'))
		a[i].truong=input('Nhập trường:')
def xuat():
	for i in range(n):
		a[i].show()
def diemmax():
	diemmax=a[0].diem
	imax=0
	for i in range(n):
		if a[i].diem>dmax:
			dmax=a[i].diem
			imax=i
	a[imax].show()  
def sxtang():
	for i in range(n):
		for j in range(i):
			if a[i].diem < a[j].diem:
				a[i].diem,a[j].diem =a[j].diem,a[i].diem 
				a[i].ten,a[j].ten =a[j].ten,a[i].ten 
				a[i].diem,a[j].diem =a[j].lop,a[i].lop
				a[i].truong,a[j].truong =a[j].truong,a[i].truong  
	xuat()
def sxtang():
	for i in range(n):
		for j in range(i):
			if a[i].diem > a[j].diem:
				a[i].diem,a[j].diem =a[j].diem,a[i].diem 
				a[i].ten,a[j].ten =a[j].ten,a[i].ten 
				a[i].diem,a[j].diem =a[j].lop,a[i].lop
				a[i].truong,a[j].truong =a[j].truong,a[i].truong  
	xuat()
def diem9():
	for i in range(n):
		 if a[i].diem >= 9:
		 	a[i].show()

class hocsinh(object):
	"""docstring for hocsinh"""
	def __init__(self,ten,lop,diem,truong):
		self.ten=ten
		self.lop=lop
		self.diem=diem
		self.truong=truong
	def show(self):
		print("tên: ",self.ten)
		print("lớp: ",self.lop)
		print("điểm: ",self.diem)
		print("trường: ",self.truong)
		print("---------------")

# viết chương trình quản lý học sinh theo yêu cầu :
# 1.Nhập danh sách học sinh
# 2.In danh sách học sinh
# 3.Tìm học sinh có điểm cao nhất
# 4.Sắp xếp học sinh tăng dần theo điểm 
# 5.Sắp xếp học sinh giảm dần theo điểm 
# 6.Liệt kê học sinh có điểm từ 9
# 0.Thoát 
	chon = int(input('chọn chức năng:'))
	if chon==1:
		n=int(input('Nhập số học sinh cần quản lý:'))
		a=[0]*n
		nhap()
	if chon==2:
		xuat()
	if chon ==3:
		diemmax()
	if chon ==4:
		sxtang()
	if chon ==5:
		sxgiam()
	if chon ==6:
		diem9()
	if chon==0:
		thoat()