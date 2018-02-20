roman={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IV",5:"V",4:"IV",1:"I"}
x=int(input("enter a number: "))
list=[]
for key in roman:
    phliko,upoloipo=divmod(x,key)
    list.append(phliko*roman[key])
    x= upoloipo
print("".join(list))
