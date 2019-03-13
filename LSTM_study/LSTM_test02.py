# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 22:36:40 2019

@author: hasee
"""
 

import numpy as np
import tensorflow as tf
import tensorflow.contrib.rnn as rnn
import matplotlib.pyplot as plt



TIME_STEPS=10
BATCH_SIZE=128
HIDDEN_UNITS1=30
HIDDEN_UNITS=1
LEARNING_RATE=0.001
EPOCH=50

TRAIN_EXAMPLES=7491
TEST_EXAMPLES=1100



#三次元数据
def generate_train_id(dataset):
    X = []
    y = []

    for i in tqdm(range(7490-TIME_STEPS)):
        x1 = []
        y1 = []
        for j in range(TIME_STEPS):
            p = i + j
            x1.append(dataset[p][1])
            y1.append(dataset[p][2])
        X.append(x1)
        y.append(y1)
    X = np.array(X,dtype=np.float32)
    y = np.array(y,dtype=np.float32)
    print(X[0])
    
    return X,y

def generate_test_id(dataset):
    y = []
    X = []
    for i in class_all[1]:
        y.append([dataset[i][2]])
        X.append([dataset[i][1]])
    return np.array(X,dtype=np.float32),np.array(y,dtype=np.float32)

#________________________________________________________________________________________________________________________________________    
#s=[i for i in range(30)]
#X,y=generate(s)
#print(X)
#print(y)
#1次元数据按时间序列提取DATA
def generate(seq):
    X=[]
    for i in range(len(seq)-TIME_STEPS):
        X.append([seq[i:i+TIME_STEPS]])
    return np.array(X,dtype=np.float32)

def generate_y(seq):
    y = []
    for i in range(len(seq)-TIME_STEPS):
        y.append([seq[i+TIME_STEPS]])
    return np.array(y,dtype=np.float32)

seq_train_x = []
for i in range(7491):
    seq_train_x.extend(dataset[i][1])
seq_train_y = []
for i in range(7491):
    seq_train_y.extend(dataset[i][2])

seq_test_x =  [] 
for i in class_all[1]:
    seq_test_x.extend(dataset[i][1])
seq_test_y =  [] 
for i in class_all[1]:
    seq_test_y.extend(dataset[i][2])
#_________________________________________________________________________________________________________________________________________
#seq_train=np.array([triangle_wave(t, 0.6, 0.4, 1.0) for t in np.linspace(start=0,stop=100,num=TRAIN_EXAMPLES,dtype=np.float32)])
#seq_test=np.array([triangle_wave(t, 0.6, 0.4, 1.0) for t in np.linspace(start=100,stop=110,num=TRAIN_EXAMPLES,dtype=np.float32)])

#plt.plot(np.linspace(start=0,stop=100,num=10000,dtype=np.float32),seq_train)

#plt.plot(np.linspace(start=100,stop=110,num=1000,dtype=np.float32),seq_test)
#plt.show()

X_train,y_train = generate_train_id(dataset_400)
print('yes')
print(X_train.shape)
X_test,y_test = generate_test_id(dataset_400) 
print(X_test.shape,y_test.shape)
#reshape to (batch,time_steps,input_size)
X_train=np.reshape(X_train,newshape=(-1,TIME_STEPS,200))
y_train=np.reshape(y_train,newshape=(-1,TIME_STEPS,200))
X_test=np.reshape(X_test,newshape=(-1,TIME_STEPS,200))
y_test=np.reshape(y_test,newshape=(-1,TIME_STEPS,200))
#print(X_train[1])
print(X_train.shape, X_test.shape)
#draw y_test
plt.plot(range(1000),y_test[:1000,0],"r*")
#print(y_test.shape)
#print(X_test.shape)

graph=tf.Graph()
with graph.as_default():

    X_p=tf.placeholder(dtype=tf.float32,shape=(None,TIME_STEPS,200),name="input_placeholder")
    y_p=tf.placeholder(dtype=tf.float32,shape=(None,TIME_STEPS,200),name="pred_placeholder")

    #lstm instance
    lstm_cell1=rnn.BasicLSTMCell(num_units=HIDDEN_UNITS1)
    lstm_cell=rnn.BasicLSTMCell(num_units=HIDDEN_UNITS)

    multi_lstm=rnn.MultiRNNCell(cells=[lstm_cell1,lstm_cell])

    #initialize to zero
    init_state=multi_lstm.zero_state(batch_size=BATCH_SIZE,dtype=tf.float32)

    #dynamic rnn
    outputs,states=tf.nn.dynamic_rnn(cell=multi_lstm,inputs=X_p,initial_state=init_state,dtype=tf.float32)
    #print(outputs.shape)
    h=outputs#[:,-1,:]
    #print(h.shape)
    #--------------------------------------------------------------------------------------------#

    #---------------------------------define loss and optimizer----------------------------------#
    mse=tf.losses.mean_squared_error(labels=y_p,predictions=h)
    #print(loss.shape)
    optimizer=tf.train.AdamOptimizer(LEARNING_RATE).minimize(loss=mse)


    init=tf.global_variables_initializer()


#-------------------------------------------Define Session---------------------------------------#
with tf.Session(graph=graph) as sess:
    sess.run(init)
    for epoch in range(1,EPOCH+1):
        results = np.zeros(shape=(TEST_EXAMPLES,TIME_STEPS, 1))
        train_losses=[]
        test_losses=[]
        print("epoch:",epoch)
        for j in range(TRAIN_EXAMPLES//BATCH_SIZE):
            _,train_loss=sess.run(
                    fetches=(optimizer,mse),
                    feed_dict={
                            X_p:X_train[j*BATCH_SIZE:(j+1)*BATCH_SIZE],
                            y_p:y_train[j*BATCH_SIZE:(j+1)*BATCH_SIZE]
                        }
            )
            train_losses.append(train_loss)
        print("average training loss:", sum(train_losses) / len(train_losses))


        for j in range(TEST_EXAMPLES//BATCH_SIZE):
            result,test_loss=sess.run(
                    fetches=(h,mse),
                    feed_dict={
                            X_p:X_test[j*BATCH_SIZE:(j+1)*BATCH_SIZE],
                            y_p:y_test[j*BATCH_SIZE:(j+1)*BATCH_SIZE]
                        }
            )

            results[j*BATCH_SIZE:(j+1)*BATCH_SIZE]=result
            test_losses.append(test_loss)
        print("average test loss:", sum(test_losses) / len(test_losses))
        plt.plot(range(1000),results[:1000,0])
        print(result.shape)
    plt.show()
