import math

avg_list = []
print ("Hello this is the Math Formula Calculator. \nPlease type in the number that corresponds to the desired formula")
print(" 1. Quadratic Formula \n 2. Average \n 3. Distance Formula \n 4. Interest")
def choice_checker (x):
	if x != "1" and x != "2" and x != "3" and x != "4":
		print("That was not one of the choices.  Try again")
		user_input()
	elif x == "1":
		print("Welcome to the quadratic formula \nPlease put in the numbers for a,b, and c")
		quad_input()
	elif x == "2":
		print('Welcome to the average calculator \nEnter in the numbers and type "done" when all numbers are typed in')
		avg_input()
	elif x == "3":
		print("Welcome to the distance formula \nEnter in the coordiantes of the points appropiately")
		dist_input()
	elif x == "4":
		print('Welcome to the interest calculator \nType "simple" for simple interest and "compound" for compound interest')
		interest_selector()
		


def user_input ():
	form_num = input("Number:")
	choice_checker(form_num)

def interest_selector():
	interest_type = input(">")
	interest_checker(interest_type)

def interest_checker(x):
	if x == "simple":
		simple_input()
	elif x == "compound":
		compound_input()
	else:
		print("Not one of the choices. Try again")
		interest_selector()

def quad_formula (a,b,c):
	resultList = []
	x = (-b + math.sqrt((b**2) - (4*a*c))) / (2*a)
	resultList.append(x)
	z = (-b - math.sqrt((b**2) - (4*a*c))) / (2*a)
	resultList.append(z)
	return resultList

def quad_input():
	
	num_a = int(input("a:"))
	
	num_b = int(input("b:"))
	
	num_c = int(input("c:"))
	quad_answer = quad_formula(num_a, num_b, num_c)
	print("The answers are", quad_answer[0], "and", quad_answer[1])

def avg_input():
	
	avg_num = input(">")
	avg_checker(avg_num)

def avg_checker(x):
	if x != "done":
		avg_list.append(x)
		avg_input()
	else:
		
		avg_answer = (avg_formula()) / (len(avg_list))
		print("The average is", avg_answer)
	

def avg_formula():
	avg_total = 0
	for x in range(0, len(avg_list)):
		avg_total += int(avg_list[x])

	return avg_total

def dist_input():
	x_coord1 = int(input("X-coordinate of first point:"))
	y_coord1 = int(input("Y-coordinate of first point:"))
	x_coord2 = int(input("X-coordinate of second point:"))
	y_coord2 = int(input("Y-coordinate of second point:"))
	distance_ans = dist_formula(x_coord1, y_coord1, x_coord2, y_coord2)
	print("The distance between the two points is", distance_ans)

	
def dist_formula(w,x,y,z):
	distance  = math.sqrt(((y - w)**2) + ((z - x)**2))
	return distance

def simple_input():
	princ = int(input("Principle amount that you have:"))
	interest = int(input("Interest rate per period:"))
	time = int(input("The time for which the money is borrowed or lent:"))
	simple_ans = princ * (interest / 100) * time
	print("The total simple interest is", "$" + str(simple_ans))

def compound_input():
	princ = int(input("Principle amount that you have:"))
	interest = int(input("Compound interest rate per period:"))
	time = int(input("Number of periods:"))
	compound_ans = compound_interest(princ, interest, time)
	print("The compound interest is", "$" + str(compound_ans))

def compound_interest(x,y,z):
	comp_ans = x * (1 + (y / 100)) ** z - x
	return comp_ans

def min_to_sec():
    a=int(input("Enter no. of seconds :  "))
    if a%60==0:
        b=a//60
        print(b,"mins")
    elif a%60 <60 and a%60  >0:
        b=a//60
        c=a%60
        print(b,"mins and ",c,"secs")
    else:
        print ("enter valid command")
	
def even_odd_sum():
    s=int(input("enter the starting number : "))
    e=int(input("enter the ending number : "))
    c=s
    even_sum=odd_sum=0
    while c >=s and c <=e:
        if c%2==0:      #even
            even_sum=even_sum+c
        if c%2!=0:      #odd
            odd_sum=odd_sum+c
        c+=1
    print("sum of even no. : ",even_sum)
    print("sum of odd no. : ",odd_sum)
	
def circle_area(r):
    a=22/7
    b=a*(r**2)
    print("area of circle : ",b)

def marks():
    a=int(input("no. of subjects : "))
    for i in range (1,a):
        while a>0 and a<a+1:
            b=int(input("subject marks"))
            print("SUBJECT ",a,"MARKS : ",b)
            c=[b]
    print(c)
	
user_input()



