nhập  numpy  dưới dạng  np

n  =  10   # tung 10 đồng xu trong 1 lần
p  =  0.2   # bias for face
l  =  1000   # số lần lặp lại

b  =  np . ngẫu nhiên . nhị thức ( n , p , l )
print ( "Trung bình số mặt phẳng nhận được:" , b . mean ())