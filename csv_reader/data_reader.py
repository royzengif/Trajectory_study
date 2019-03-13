# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 06:35:00 2019

@author: hasee
"""

from tqdm import tqdm
import pandas as pd
import numpy as np
import csv, os


with open('20120813-200004.csv','rt')as csvfile:
    reader = csv.reader(csvfile)
    row1 = [row for row in reader]
    columns = [column for column in reader]
    print(len(row1))
    rows = row1
def locate_header():

    i = 0
    for i in range(100):
        if rows[i][2] == ''  :
            i += 1
        else:
            break
    header = []
    for j in range(len(rows[i])):

        header.append(rows[i][j])
    return i, header

#['# DATE-TIME', 'frame', 'no', 'ID', 'x', 'y', 'px', 'py', 'pz', 'ox', 'oy', 'oz', 'NS', 'wx', 'EW', 'wy', 'wz', 'subject', 'feature', 'gender', 'attribute', 'group', 'action', 'state', 'free']
time_loc = []
px = []
py = []
id = []
times = []

for s in tqdm(np.arange(3, len(rows))):#時間のデータをロケットする
    if rows[s][0] == '':
        s = s
    else:
        time_loc.append(s)
        #dt = rows[s][0]
        #ts = int(time.mktime(time.strptime(dt, "%Y:%m:%d-%H:%M:%S:%f")))
        #times.append(ts)
    time_label = [time_loc]

print('Load time data successed')

def get_data_time(start, end, ids):
    px = []
    py = []
    pz = []
    id = []


    for j in range(start, end):
        k = time_loc[j] + 1
        while rows[k][0] == '':
            #print('yes')
            if rows[k][3] == str(ids):
                #print('2-1yes')
                id.append(rows[k][3])
                px.append(float(rows[k][6]))
                py.append(float(rows[k][7]))
                pz.append(float(rows[k][8]))

                k += 1
                
            else:
                #print('2-2yes')
                k += 1     

    return id, px, py, pz

def locate_data(start, end, ids):
    px = []
    id = []
    time_location = []

    for j in range(start, end):
        k = time_loc[j] + 1
        #print('k=%d'%k)
        while rows[k][0] == '':
            if rows[k][3] == str(ids):
                time_location.append(j)
                k += 1
                
            else:
                #print('2-2yes')
                k += 1     

    return  time_location

#earlier version IDに基づいて動くシステム

pacedata = pd.read_csv('20120813-200004.csv', header =locate_header()[0])  #ファイルを開きます。

paceR = pacedata[pacedata.subject == 'HUMAN'] #NOISEを除き、人間だけを残します。


def id_counter():#　データに含まれているIDの数を数えます。
    data_id = paceR['ID']
    l2 = list(set(data_id))
    return len(l2)



#dataset00()
batch_size = 100

def read_data_batch():
    dataset = []
    num_id = id_counter()
    print(num_id)
    num_of_cutline = num_id//batch_size
    num_timeloc = len(time_loc)
    len_list = []
    loc_start = []
    loc_end = []
    cut_line = []
    for i in range(num_of_cutline+1):
        cut_line.append(i*batch_size)

    del cut_line[0]
    cut_line.append(num_id)
    for i in cut_line:
        loc = locate_data(0,num_timeloc-1,i)
        lenth = len(loc) - 1
        loc_start.append(loc[0])
        loc_end.append(loc[lenth]+1)
    cut_line.insert(0,0)
    loc_start.insert(0,0)
    for i in tqdm(range(len(cut_line)-1)):
        for j in range(cut_line[i]+1,cut_line[i+1]+1):
            dataset.append(get_data_time(loc_start[i],loc_end[i],j))
            len_list.append(len(dataset[j-1][1]))
    return dataset,len_list

dataset, len_list = read_data_batch()
