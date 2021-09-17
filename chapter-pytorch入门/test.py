import os 
path = 'C:/Users/lenovo】/Desktop/总的句子-总新.txt'
file = open(path,'r')
filenames = file.readlines()
file.close()
max_line = 0
for fname in filenames:
    if len(fname.split('-')) > max_line:
        max_line = len(fname.split('-'))

print(max_line)



from torch.utils.data import BatchSampler
pseudo_dataset = list(range(10))

batchSampler1 = BatchSampler(pseudo_dataset, batch_size=3, drop_last=False)
batchSampler2 = BatchSampler(pseudo_dataset, batch_size=3, drop_last=True)

print("for batch sampler #1: ")
for data in batchSampler1:
    print(data, end=" ")

print("\n\nfor batch sampler #2: ")
for data in batchSampler2:
    print(data, end=" ")