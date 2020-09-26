import re

print("#################################")
print("## Welcome to Magic Calculator ##")
print("#################################\n")
print("Type exit to quit")
last_no = 0
def calculation() :
 global last_no
 equation = ""
 if last_no == 0 :
  equation = input("Enter an equation = ")
 else :
  equation = input(float(last_no))
 if equation == 'exit' :
  print("Thank you")
  quit()
 else :
  equation = re.sub('[A-Za-z:()" "]' , " " , equation)
 if last_no == 0 :
  last_no = eval(equation)
 else :
  last_no = eval(str(last_no) + equation)
while True :
 calculation() 