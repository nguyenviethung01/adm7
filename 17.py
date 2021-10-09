nhập  numpy  dưới dạng  np

điểm số  =  np . mảng ([ 8 , 6 , 4 , 3 , 9 , 4 , 7 , 4 , 4 , 9 , 7 , 3 , 9 , 4 , 2 , 3 , 8 , 5 , 9 , 6 ])

print ( "Bách phân vị thứ 70:" , np . percentile ( điểm số , 70 , nội suy = 'thấp hơn' ))
in ( "Bách phân vị thứ 70:" , np . percentile ( điểm số , 70 , suy = 'cao' ))
in ( "Bách phân vị thứ 70:" , np . percentile ( điểm số , 70 , suy = 'thẳng' ))
in ( "Bách phân vị thứ 70:" , np . percentile ( điểm số , 70 , suy = 'gần' ))
print ( "Bách phân vị thứ 70:" , np . percentile ( điểm , 70 , interpolation = 'midpoint' ))