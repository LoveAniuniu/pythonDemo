import torch
import numpy as np

#a = torch.Tensor([1,2,3])
#print(a)
#print(a.dtype)
#print(a.device)
#print(a.shape)
#print(a.size()) 

# b= torch.Tensor(2,3)
# print(b)
 
# c=torch.arange(1,3)
# print(c)

# d=torch.linspace(2,6,4)
# print(d)

f=np.array([1,2,3])
print(f)
f=torch.from_numpy(f)
print(f)