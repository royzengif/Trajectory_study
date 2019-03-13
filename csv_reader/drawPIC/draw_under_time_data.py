
from tqdm import tqdm
import pandas as pd
import numpy as np
import csv, os
import time, datetime
import matplotlib.pyplot as plt
import math as mh
from math import sin,cos
from scipy.interpolate import spline
from scipy.integrate import odeint
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import animation
from tkinter import *
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


#面倒くさいから、ワーニング閾値を1000に設定している
plt.rcParams['figure.max_open_warning'] = 1000



def getinput():      #入力をもたって、正しさを判断します。
    print ('Please input your choice 0 or 1, end with ENTER.')
    t = True
    while t:
        inp = int(input())
        if inp in range(2):
            t = False
            return inp
        else:
            print ('please input 0 or 1 !!!')

def getloc(t,id1,id2):      #row次第で、データを取ります。
    for i in range (id1,id2+1):
        float(i)
        i+= 1.0
        lx=['x','X']
        ly=['y','Y']
        lz=['z','Z']
        if t in lx:
            paceID=paceR[paceR.ID==i]           
            ##print(paceID.ix[:,['ID','px']])
            xlab=paceID.ix[:,['px']]
            return xlab
        elif t in ly:
            paceID=paceR[paceR.ID==i]
            ##print(paceID.ix[:,['ID','py']])       
            ylab=paceID.ix[:,['py']]
            return ylab
        elif t in lz:
            paceID=paceR[paceR.ID==i]
            print(paceID.ix[:,['ID','pz']])
            zlab=paceID.ix[:,['py','px']]
            return zlab
     
def viewlabel(): #データを表す為に作った部分だけど、最後に使わなくなってしまいました。
    print('get which label')
    g=input()
    gl=str(g)
    print('get which ID')
    id=input()
    id1=int(id)
    id2=input()
    id3=int(id2)
    getloc(g1,id1,id3)

def draw_plot(start,end,c):#（課題1）図を作成する。直接に数値を入れると、順番に作成する。リストを入れるとリストの順番に作成する。
    ran = []
    if isinstance(start,list):
        ran = start
        c+=1
        pp = PdfPages('trajectory_class%d.pdf'%c)
    else:
        sta = start
        start = start-1
        ran = range(start,end)       
        pp = PdfPages('trajectory_ID%d_ID%d.pdf'%(sta,end))
    row_num = end//5
    remain = end % 20
    fig = plt.figure(figsize = (6*5,5*(row_num+1)))
    for i in range(start,end):
        ax = fig.add_subplot(row_num+1, 5, i+1)

        data = data_get(i)
        px = data[0]
        py = data[1]
        plt.xlim((-2,2))
        plt.ylim((-2,2))
        ax.plot(px, py)
        id = i+1
        id_t = ID_translater(id)
        plt.title('ID%s'%id_t)
        plt.xlabel('x axis', fontsize = 13)
        plt.ylabel('y axis', fontsize = 13)
        pp.savefig()
        
    plt.subplots_adjust(left=0.1,right=0.95,top=0.95,bottom=0.05)
    
 
    pp.close()

def list_float(listx,times):
    x1111=[]
    for i in listx:
        x11 = i
        x111=x11[0]
        x111=x111*times
        x1111.append(x111)
    return x1111

def data_get(num):   #リストのリストである型のデータ単純なリスクにします。
    i = num   
    x = getloc('x',i,i)
    y = getloc('y',i,i)
    train_data=np.array(x)
    train_x_list=train_data.tolist()
    x1 = train_x_list

    train_data = np.array(y)
    train_y_list = train_data.tolist()
    y1 = train_y_list
    return x1,y1
        
def data_drop(list,list_d):    #分類する為に、同じクラスである全てのIDが含まれているリストによって、元のリストから消去します。残った部分を返します。
    l2_d = list_d
    l2 = list
    l2_d.sort(reverse = True)  
    class_x = []
    for t in l2_d:        
        l2.remove(l2[t])            
    return l2
    
def diff_len (l1,l2):#二つのリストの長さを割り算して、結果次第、調整する方を決めます。
    diff1 = l1/l2
    if diff1>1.0:
        x = l1//l2
        x1 = x+1        
        x2 = l2*x1
        diff2 = x2-l1
        return 0,x1,diff2
    elif diff1<1.0:
        x = l2//l1
        x1 = x+1      
        x2 = l1*x1
        diff2 = x2-l2
        return 1,x1,diff2
    else:
        return 1,1,0

def list_align(list,row,drop):   #リストの長さを調整する為の関数、追加したデータに過剰な部分をchoice関数が決めた番号で消します。
    l1len = len(list)
    l2 = list_extend(list,l1len,row)
    l2_drop = np.arange(l1len)*row   
    l2_drop = np.random.choice(l2_drop,drop,replace = False)
    l2_d = []
    for d in l2_drop:
        l2_d.append(d)
    l2 = data_drop(l2,l2_d)
    return l2       

def list_extend(list,lenth,times):#リストを伸ばす関数です。python3.0以降では、list[]*timesを実行しても、listを伸ばすことができない。
    l = list
    l_len = lenth
    l1 = []
    for a in range(0,l_len):
        for b in range(0,times):
            l1.append(l[a])
    return l1

def pearson(p1,p2):#ピアソン相関係数を算出します。
    data_std = dataset[p1]    #基準とするデータのｐｘとｐｙを手に入れます。
    x_stdf = data_std[1]     
    y_stdf = data_std[2] 
    #print(y_std)
    #x_stdf = list_float(x_std,1)
    #y_stdf = list_float(y_std,1)
       #比べたいデータのｐｘとｐｙを手に入れます。
    data = dataset[p2]
    x11 = data[1]
    y11 = data[2]
    #x11 = list_float(x1,1)
    #y11 = list_float(y1,1)
    #xy = pd.DataFrame(y11,x11)
    #dfstd = pd.DataFrame(x_std,y_std)
    pears = []
    for c in x11:
        pears.append(c)
    for a in y11:
        pears.append(a)
    std1 = []
    for d in x_stdf:
        std1.append(d)
    for b in y_stdf:
        std1.append(b)
    lstd = len(std1)
    lpears = len(pears)
    if lstd>lpears:
        std1 = list_extend(std1,lstd,4)
    elif lstd<lpears:
        pears = list_extend(pears,lpears,4)
    #lstd = len(std)
    #std=np.arange(lxy).reshape(lxy,1)
    #std = list_float(std,1)
    lstd1 = len(std1)
    lpears1 = len(pears)
    diff = diff_len(lpears1,lstd1)#両方の長さを等しくするために、先に長さを数えて伸ばすべきである方を決めます。
    sel = diff[0]
    row = diff[1]
    drop = diff[2]     
    if sel == 0:
        std1=list_align(std1,row,drop)
    elif sel == 1:
        pears = list_align(pears,row,drop)
    #xy1 = np.array(x11,y11)
    #std1 = np.array(std,std)
    #print(len(std1),' ',len(pears))
    #pears_xy = np.corrcoef(x11,x11)
    pears_cov = np.corrcoef(std1,pears)
    #print ('The figure %d and figure %d'%(p1,p2))
    r = pears_cov[0]
    #print ()
    #print ('Pearson r=%f'%r[1])
    #print ()
    return r
    
def vector(p1):#ベクトルとslopeを計算します。
    data_std = data_get(p1)    
    x_std = data_std[0]        
    y_std = data_std[1] 
    x_stdf = list_float(x_std,1)
    y_stdf = list_float(y_std,1)

    vector_std_x = x_stdf[-1] - x_stdf[0]
    vector_std_y = y_stdf[-1] - y_stdf[0]

    vector_std = [vector_std_x,vector_std_y]
    slope_std = vector_std_y/vector_std_x
    return slope_std

def mkdir(path):##ファイルを作る関数、クラス別で図を保存したいんですが、まだ完成していません。
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:

        print (path+' Done')

        os.makedirs(path)
        return True
    else:

        print (path+' Already exist')
        return False

def classify(p1,sel,lenth,list_all):  #クラスでデータを分別する、sel=0であれば、ピアソン相関係数の通りでする。1であれば、ベクトルでする。
    select = sel
    lenth = lenth
    all = list_all
    class1 = []
    class2 = []
    class3 = []
    class_x = []
    p = 0
    if select==0:
        for i in tqdm(all):
            r = pearson(p1,i)      
            if r[1]>0.80:
                class1.append(p)
            p+= 1
        for j in class1:     
            class_x.append(all[j])    
        data_drop(all,class1)
        #print(class1)
        return all,class_x
    elif select==1:
        for i in all:
            r = vector(i)
            if abs(r) >5:
                class2.append(i)
            elif r > 0:
                class1.append(i)
            elif r < 0:
                class3.append(i)
        class_x = [class1,class2,class3]
        return class_x
              
def run_class(sel):#（課題2）データを区別する関数、入力のSELによって、区別方法を決める。  ID00053の図がなくなったのバグがこちらに起こされました。
    all = []
    select = sel
    class_all = []
    i = 1
    for j in range(id_counter()):
        all.append(j)
    if select ==0:
        while len(all)>0: #前は　リストの長さが１である場合を忘れてしまいました。
            all_c = all
            #print(all)
            i = all_c[0]
            data = classify(i,sel,len(all_c),all_c)
            all = data[0]
            class1 = data[1]
            class_all.append(class1)
        #print(class_all)
        #print (lenclass)
        print('Classify successed!')
        print()
        #printclass(class_all)
        return class_all
    elif select == 1:
        class_all = classify(1,1,1,all)
        print('Classify successed!')
        #printclass(class_all)
        return class_all

def printclass(class_all):
    lenclass = len(class_all)
    for c in range(lenclass):
        c1=c+1
        print ('Class%d :'%c1,end=' ' )
        for d in class_all[c]:
            d1=d+1
            d1 = ID_translater(d1)
            print ('ID%s,'%d1,end=' ')
        print()

def ID_translater(id):#IDを'ID0000Ｘ’の形にします。
    id_int = id
    id_str = str(id_int)
    id_list = []
    for i in range (5):
        id_list.append('0')
    id_len = len(id_str)
    if id_len<5:
        for i in range(id_len):
            id_list[4-i] = id_str[id_len-i-1]
    id_s = ''
    id_s = id_s.join(id_list)
    return id_s

def get_drawID():
    flag = 1
    while flag == 1:
        print('Please input a ID as the begining. ')
        start = int(input())
        print('Please input a ID as the ending, this ID should not be less then the ID of begining. ')
        end = int(input())
        id_cnt = id_counter()
        if end > id_cnt or start > id_cnt:
            print('ERROR00001!!!    You should input a number no mo than %d.'%id_cnt)
            flag =1
        elif start == 0 or end ==0:
            print('ERROR00002!!!    0 is not a valid number, please input number from 1 to %d'%id_cnt)
        elif end< start:
            print('ERROR00003!!!    The end ID should not be less then the ID of begining.')
            flag = 1
        elif end == start:
            print ('You choose to creat only one plot at ID = %d'%end)
            return start,end
        elif start < end:
            print('Begin at ID%d    up to ID%d'%(start,end))
            return start,end

def main():   
    print('WHAT SHOULD I DO?')
    print ()
    print ('This CSV file is containing %d data.'%id_counter())
    print ()
    print ('0 for drawing plot.')
    print ()
    print ('1 for classifying.')
    print ()
    sel = getinput()
    if sel == 0:
        print ('The plots will be created and saved in one PDF file in order of ID. If you want to run it in the order of class, please do classify first.')
        print()
        DID = get_drawID()   
        start = DID[0]
        end = DID[1]
        draw_plot(start,end,0)
        print('SUCCESSE!!!')
    elif sel == 1:
        print ('The data are able to be classified under 2 rules.')
        print ()
        print ('Input 0 for classifying under Pearson correlation coefficient.')
        print ()
        print ('Input 1 for classifying under the slopes of vectors.')
        print ()
        sel = getinput()
        if sel == 0:
            class_all = run_class(0)
            return class_all
            print('Do you want to creat plots? YES or NO')
            sel1 = input()
            if sel1 == 'yes' or sel1 =='YES':
                for i in range(len(class_all)):
                    p = class_all[i]
                    print(p)
                    draw_plot(p,0,i)
                print('SUCCESSE!!!')
                return class_all
            else:
                return class_all
                
        elif sel == 1:
            class_all = run_class(1)
            print('Do you want to creat plots? YES or NO')
            sel1 = input()
            if sel1=='yes' or sel1=='YES':
                for i in range(len(class_all)):
                    print(i)
                    p = class_all[i]
                    draw_plot(p,0,i)
                print('SUCCESSE!!!')
            else:              
                return class_all

class_all = main()

#for i in tqdm(range(7690)):
    #dataset.append(get_data_time(0,52758,i))   
