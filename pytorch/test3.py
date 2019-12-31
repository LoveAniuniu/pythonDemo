from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import torch

class Mydataset(Dataset):
    def __init__(self):
        self.xs=torch.Tensor([[0,0],[0,1],[1,0],[1,1]])
        self.ys=torch.Tensor([[0],[0],[1]])
    
    def __len__(self):
        return len(self.xs)
    
    def __getitem__(self, index):
        x=self.xs[index]
        y=self.ys[index]

        return x,y

mydataset = Mydataset();
print(mydataset[0])

train_data = DataLoader(mydataset,batch_size=2,shuffle=False)
