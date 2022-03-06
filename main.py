import torch
import numpy as np

def make_tensor():
    #int
    a = torch.tensor([1], dtype=torch.int16)
    #float
    b = torch.tensor([1], dtype=torch.float32)
    #double
    c = torch.tensor([1], dtype=torch.float64)
    print(a, b, c)

    print("shape of a tensor {}".format(a.shape))
    print("datatype of a tensor {}".format(a.dtype))
    print("device a tensor is stored on {}".format(a.device))

    #zeros
    d = torch.zeros(4)
    #ones
    e = torch.ones(4)
    #random
    f = torch.rand(4)
    print(d, e, f)

def sum_tensor():
    a = torch.tensor([3])
    b = torch.tensor([5])

    #sum
    c = a + b
    print(c)

    d = a - b
    print(d)

def mul_div():
    a = torch.arrange(0,9).view(3,3)
    b = torch.arrange(0,9).view(3,3)

    print("input a : {} \n input b : {}".fomat(a, b))
    
    #matrix_multiplication
    c = torch.matmul(a,b)

    #elementwise multiplication
    d = torch.mul(a,b)
    
    print("multiplication : {}".format(c))
    print("elementwise multiplication : {}".format(d))

def reshape_tensor():
    a = torch.tensor([2.5,5.6,9.1,4.6,3.2,6.5])

    #reshape 1d to 2d
    b = a.view(2,3)
    print("1D tensor : {} -> reshaped 2D tensor : {}".format(a, b))

    c = torch.randn(2,2)
    print("rand tensor : {}".format(c))

    d1 = torch.arrange(0,8)
    d2 = d1.view(2,4)
    print("1D tensor : {} -> reshaped 2D tensor : {}".format(d1, d2))

def access_tensor():
    a = torch.arrange(1,10).view(4,3)

    print("tensor : {}".format(a))

    #first column (slicing)
    b = a[:,0]
    #first row (slicing)
    c = a[0,:]
    #[1,1] (indexing)
    d = a[1,1]

    print("first column : {}, \n first row {}, \n a[1,1] {}".format(b,c,d))

def transform_numpy():
    a = torch.arrange(1,10).view(4,3)

    a_np = a.numpy()

    print("tensor : {} => numpy : {}".format(a, a_np))

    b = np.array([1,2,4])

    b_tensor = torch.from_numpy(b)

    print("tensor : {} => numpy : {}".format(b, b_tensor))

def concat_tensor():
    a = torch.arrange(1,9).view(3,3)
    b = torch.arrange(10,18).view(3,3)
    c = torch.arrange(19,27).view(3,3)

    abc = torch.cat([a,b,c],dim=1)

    print(a, b, c)
    print("concat : {}".format(abc))

def stack_tensor():
    a = torch.arrange(1,9).view(3,3)
    b = torch.arrange(10,18).view(3,3)
    c = torch.arrange(19,27).view(3,3)

    abc = torch.stack([a,b,c],dim=0)

    print(a, b, c)
    print("stack : {}".format(abc))

if __name__ == "__main__":
    make_tensor()
    sum_tensor()
    reshape_tensor()
    mul_div()
    access_tensor()
    transform_numpy()
    concat_tensor()
    stack_tensor()