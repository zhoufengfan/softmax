import torch
import torch.nn.functional as F

if __name__ == '__main__':
    t1 = torch.tensor([1, 2, 3]).float()
    t2 = F.softmax(t1, dim=0)
    t3 = torch.exp(t1) / torch.sum(torch.exp(t1))
    print("t2为：\t", t2)
    print("t3为：\t", t3)
