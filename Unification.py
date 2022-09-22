# code for unification it substitute constant with variable if they are at the same index in different predicate logic

# unification algorithm
import string

# creating array for variable
az_Upper = string.ascii_uppercase

variable = []
for i in az_Upper:
    variable.append(i)




# creating array for const
az_lower = string.ascii_lowercase
const = []
for i in az_lower:
    const.append(i)



def accept():
    a=input("Enter the value of pos1: ")
    b=input("Enter the value of pos2:- ")
    return a,b


print("\n")
print("For predicate 1")
i,j=accept()

print("For predicate 1")
print("\n")
k,l=accept()
print("\n")
print(f"The predicate one is p({i},{j})")

print("\n")

print(f"The predicate one is p({k},{l})")

print("\n")


# p1 p2 are predicate array
p1=[]
p2=[]
print("\n")
p1.append(i)
p1.append(j)

print("\n")
#

p2.append(k)
p2.append(l)

print("the predicate 1 :- ", p1)
print("the predicate 2 :- ", p2)


dict={}
print("\n")

print("Logic check")
def unification_logic(p1,p2):
    for i in p1:
        for j in p2:
            if(p1.index(i)==p2.index(j)):
                if((i in const) and (j in variable) ):
                    dict[j]=i
                elif((i in variable) and (j in const) ):
                    dict[i]=j
                elif(((i in variable) and (j in variable)) or ((i in const) and (j in const))):
                    print("as",i,j,"are of same class therefore it is not added")
                    print("There for it is not added")
       

# call of the logic
unification_logic(p1,p2)
       
print("\n")
print("The logic is",dict)
print("\n")
print("The substitution is as follows:- ")


for i in dict:
    print(f"{i} is subustited as {dict[i]}")
    


    
    




