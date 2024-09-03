# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:09:03 2024

@author: tr
"""
print(" TÍNH S VÀ V CÁC HÌNH THE0 DANH SÁCH : ")
print("Nhập lựa ch0n của bạn")
print("1 nếu bạn mu0n tinh hình vu0ng ")
print("2 nếu bạn mu0n tinh hình chữ nhật ")
print("3 nếu bạn mu0n tinh hình chữ nhật")
option =input()
if option  == '1':
    a= float(input("Nhập cạnh hình vuong: "))
    cvv = a*a 
    dtv =a**4
    print(" Chu vi hình vuông: ", cvv )
    print(" Diện tích hình vuông= ", dtv )
elif option == '2':
    d= float(input("Nhập chiều dài hình chữ nhật: "))
    r= float(input("Nhập chiều rộng hình chữ nhật: ")) 
    cvcn = (d+r)*2
    print(" Chu vi hình chữ nhật: ",cvcn )
    dtcn = d*r 
    print(" Diện tích hình chữ nhật: ", dtcn )
elif  option == '3':
    r= float(input(" Nhập bán kính hình tròn: "))
    pi= 3.14       
    cvt = pi*r**2
    print(" Chu vi hình tròn: ", cvt)
    dtt=2*pi*r
    print(" Diện tích hình tròn: ", dtt)
else:
    print("Không thể thực hiện! Vui lòng chỉ nhập 1 2 hoặc 3 nhaaaaaaaa!!")



    
    
    
