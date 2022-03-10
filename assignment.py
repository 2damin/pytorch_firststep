import torch

#Quiz1
def quiz1():
    a = torch.arange(1,7)
    b = torch.arange(1,7)
    
    sum = a + b
    print("Sum : {}".format(sum))
    
    sub = a - b
    print("Sub : {}".format(sub))
    
    a_sum = a.sum()
    b_sum = b.sum()
    
    print("a_sum : {} , b_sum {}".format(a_sum, b_sum))

#Quiz2
def quiz2():
    a = torch.arange(1,46)
    a = a.view(1,5,3,3)
    b = torch.transpose(a, 1, 3)
    
    print("transposed : ", b[0,2,2,:])

#Quiz3
def quiz3():
    a = torch.arange(1,7).view(2,3)
    b = torch.arange(1,7).view(2,3)
    
    c = torch.cat((a,b), dim = 1)
    
    d = torch.stack((a,b), dim = 0)
    
    print("concat {} , stack {}". format(c, d))

if __name__ == "__main__":
    quiz1()
    quiz2()
    quiz3()
    