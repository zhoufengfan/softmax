import torch
import torch.nn.functional as F

if __name__ == '__main__':
    t1 = torch.tensor([1, 2, 3]).float()
    t2 = F.softmax(t1, dim=0)
    t3 = torch.exp(t1) / torch.sum(torch.exp(t1))
    print("t2 is:\t", t2)
    print("t3 is:\t", t3)
