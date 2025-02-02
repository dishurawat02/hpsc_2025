s = 1
x = int(input("Enter the number: "))
ea = 0.05
es = 100
i = 1
while ea<es:
	sold = s
	s =(s + x/s)*0.5
	es = abs((sold - s)/sold)
	i = i+1
print("Number of iteration is ",i)
print(s)
