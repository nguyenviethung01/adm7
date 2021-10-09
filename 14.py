nhập  numpy  dưới dạng  np

x  =  np . mảng ([[ 14 , 96 ],
              [ 46 , 82 ],
              [ 80 , 67 ],
              [ 77 , 91 ],
              [ 99 , 87 ]])

print ( "X =" , x )

print ( "Large value:" , np . amax ( x ))
print ( "Giá trị bé nhất:" , np . amin ( x ))

print ( "Giá trị lớn nhất (axis = 0):" , np . amax ( x , axis = 0 ))
print ( "Giá trị lớn nhất (axis = 1):" , np . amax ( x , axis = 1 ))