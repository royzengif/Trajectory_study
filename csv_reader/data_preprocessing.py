# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 00:21:15 2019

@author: hasee
"""
dataset_400 = dataset[ : ]
print(dataset[7490])
dimension = 200
data_over_size = []
lenth_list = []

for i in tqdm(range(7491)):
    if len(dataset_400[i][1]) < dimension:
        lenth = len(dataset_400[i][1])
        for j in range(dimension - lenth):
            dataset_400[i][1].append(0)
            dataset_400[i][2].append(0)


for i in range(7491):
    if len(dataset_400[i][1]) > dimension:
        data_over_size.append(i)
        lenth_list.append(len(dataset_400[i][1]))
for j in tqdm(range(len(data_over_size))):
    delete_list =[]
    delete = np.random.choice(lenth_list[j],lenth_list[j]-dimension,replace = False)
    for m in delete:
        delete_list.append(m)
    delete_list.sort(reverse = True)
    #print(delete_list)
    data_drop(dataset_400[data_over_size[j]][1],delete_list)
    data_drop(dataset_400[data_over_size[j]][2],delete_list)


for i in range(7491):
    if len(dataset_400[i][2]) != dimension:
        print(i)
print(data_over_size)
for i in data_over_size:
    print(len(dataset_400[i][1]))
print(dataset_400[7490])