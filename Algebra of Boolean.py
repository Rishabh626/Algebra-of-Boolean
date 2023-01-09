
#Question:1

#First i am forming an half adder called "hadd" in my function.
#a half adder returns a sum and a carry, which are defined in the function.
def hadd(a, b):
    sum = ((a and not b) or (not a and b))
    carry = a and b
    return sum,carry
# A binary full adder. which i call "add" in my function.
# The full adder can add 3 bits (can handle an incoming carry)
# Also returns a sum and carry
#getting carry from half adder i forwarded to full adder.
def add(a, b, c):
    sum1,carry1 = hadd(a,b)
    sum,carry2 = hadd(sum1,c)
    carry = carry1 or carry2
    return sum,carry

#Question:2

#A binary 4 bit adder adds two binary no. with 4 bits. called as "add4".
#it also returns the sum and a carry.
#getting carry from full adder i forwarded to 4 bit adder.
def add4(a0,a1,a2,a3, b0,b1,b2,b3, c):
    sum1,carry1 = add(a0,b0,c)
    sum2,carry2 = add(a1,b1,carry1)
    sum3,carry3 = add(a2,b2,carry2)
    sum4,carry4 = add(a3,b3,carry3)
    return sum1, sum2, sum3, sum4, carry4

#Question:3

### rem = 3
#My Enter Number is 2021CH10419, last two digits are 19 and when divided by 4 i
#got "3" as a remainder so my operater is ">=".
def cmp(a0,a1,a2,a3, b0,b1,b2,b3):
# This states that if i got a3>=b3; it returns true. similarly for others also.
    if(a3==True or (a3==False and  b3==False)):
        return(True)
        if(a2==True or (a2==False and b2==False)):
            return(True)
            if(a1==True or (a1==False and b1==False)):
                return(True)
                if(a0==True or (a0==False and b0==False)):
                    return (True)
    else:
        return(False)

#Question:4

#1st i am making an half subtractor, where a and b are inputs.
#it returns a difference and a borrow.
def hsub(a,b):
    diff = (not a and b) or (a and not b)
    borrow = not a and b
    return diff,borrow
#then this half subtractor is used to make a full subtractor.
def fsub(a,b,bin): #bin is borrow in.
    d1,b1 = hsub(a,b) #d1 is difference of a,b. b1 is borrow given by hsub(a,b).
    d2,b2 = hsub(d1,bin)
    fbow = b1 or b2 #fbow is the final borrow of fsub(a,b,bin).
    return d2,fbow
# Now i am making our required function --a 4 bit subtractor.
# by calling fsub many times and using their output.
# bo1,bo2,bo3,bo4 are respective borrows of fsub.
#d0,d1,d2,d3 are respective differences of fsub.
def sub4(a0,a1,a2,a3, b0,b1,b2,b3):
    d0,bo1 = fsub(a0,b0,False)#because initially borrow carry is False.
    d1,bo2 = fsub(a1,b1,bo1)
    d2,bo3 = fsub(a2,b2,bo2)
    d3,bo4 = fsub(a3,b3,bo3)
#the final sum is d0,d1,d2,d3 and borrow is bo4.
    return d0,d1,d2,d3, bo4 #bo4 is the final borrow or borrow of the sub4 function.
# it gives the sign of final answer, i.e if bo4=True=>(-), if bo4=False=>(+).

#Question:5

# A binary 8 bit adder adds two binary number with 8 bits called "add8".
def add8(a, b, c):
    (a0,a1,a2,a3,a4,a5,a6,a7) = a
    (b0,b1,b2,b3,b4,b5,b6,b7) = b
    s1,s2,s3,s4,carry1 = add4(a0,a1,a2,a3, b0,b1,b2,b3, c)
#By using "add4" i got a sum and a carry,now the carry is forwarded to next" add4".
    s5,s6,s7,s8,carry2 = add4(a4,a5,a6,a7, b4,b5,b6,b7, carry1)
# By combining sum1,sum2 and final carry "carry2",i got result of 8 bit adder.
    fsum = (s1,s2,s3,s4,s5,s6,s7,s8)
    return (fsum, carry2)

#Question:6

#it multiplies two 4 bit boolean numbers and gives 8bit number with a carry.

def mul4(a,b):
#as like a normal multiplication i 1st multiply b0 with (a0,a1,a2,a3),then b1
#with (a0,a1,a2,a3) ,then d2, then d3 and similarly made a list of that.
#also take False to fill up the empty space and to make it a 8bit number.
#by doing that i made lists l1,l2,l3,l4.
    (a0,a1,a2,a3) = a
    (b0,b1,b2,b3) = b
    l1 = (b0 and a0, b0 and a1, b0 and a2, b0 and a3,False,False,False,False)
    l2 = (False,b1 and a0, b1 and a1, b1 and a2, b1 and a3,False,False,False)
    l3 = (False,False,b2 and a0, b2 and a1, b2 and a2, b2 and a3,False,False)
    l4 = (False,False,False,b3 and a0, b3 and a1, b3 and a2, b3 and a3,False)
#then forward these lists to 8 bit adder.
    sum1, carry1 = add8(l1, l2, False) # becoz initially carry given is False.

    sum2, carry2 = add8(sum1, l3, carry1)

    sum3, carry3 = add8(sum2, l4, carry2)
# got sum3 as the final answer of "mul4" function.
    return sum3