nhập  numpy  dưới dạng  np
xu  =  np . ngẫu nhiên . choice ([ 0 , 1 ], size = 1000 , p = [ 0.2 , 0.8 ]) # random.choice sẽ lấy ngẫu nhiên các phần tử trong mảng ở đầu số với xác suất ở tham số p
print ( "% số lần tung lên mặt:" , ( coins  ==  0 ). mean () *  100 )
print ( "% số lần tung ra mặt vợt:" , ( coins  ==  1 ). mean () *  100 )