print("Simple calculator")
print("select an operation")
print("1.additon")
print("2.sub")
print("3.multiplication")
print("4.division")

while True:
     operation = int(input("enter choice(1/2/3/4/0)>>"))
     num1=float(input("enter the num1 >>"))
     num2=float(input("enter the num2 >>"))

     if operation == 1:
          print(num1+num2)
     elif operation == 2: 
          print(num1-num2)
     elif operation == 3: 
          print(num1*num2)  
     elif operation == 4: 
          print(num1/num2)    
     elif operation ==0:
         print("stop")
     else:
      print("invalid option . pls try again!")
  
   
