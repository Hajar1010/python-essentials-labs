x= float(input("Enter value for x: "))
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))

print("y =", y)

# if input x= 1 output y = 0.6000000000000001
# if input x=10 out y = 0.09901951266867294
# if input x=100 output y = y = 0.009999000199950014
# if input x=-5 output y = -0.19258202567760344
