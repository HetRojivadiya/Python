l = ["\nQues 1 : \nThe International Literacy Day is observed on \nA.Sep 8\nB.Nov 28\nC.May 2\nD.Sep 22","\nQues 2:\nAThe language of Lakshadweep. a Union Territory of India, is\nA.Tamil\nB.Hindi\nC.Malayalam\nD.Telugu","\nQue 3 :\nBahubali festival is related to\nA.Islam\nB.Hinduism\nC.Buddhism\nD.Jainism"]
ans = ["A","C","D"]
sum = 0
x=0
q=0

for que in range(len(l)):
    print(l[que])
    while(True):
        Ians = input("If you want to Quit Press- Q else Select Option :")
        if(Ians == "Q"):
            q = 1
            break
        if(Ians == "A" or Ians == "B" or Ians == "C" or Ians == "D"):
            break
    if(q == 1):
        break   
    elif(Ians == ans[que]):
        sum=sum+1   
    else:
        print("sorry your anwser is wrong")
        x=1
        exit()
        
if(x==0):
    print("Congratulations You win :",sum*10000000)
        


