import torch

t1 =torch.ones(2,16,10)
t2 = torch.zeros(2,4,10)
print(t1.shape)
print(t2.shape)
t3 = torch.cat((t1,t2),dim=1)
print(t3.shape)