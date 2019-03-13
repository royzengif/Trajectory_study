# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 03:11:50 2019

@author: hasee
"""

def creatDir(cla):
    path = 'e:\dataset\\' + 'class'+ str(cla)
    os.makedirs(path)
    
def drawPic():
    try:id=int(inputEntry.get())
    except:
        id=50
        print ('请输入整数')
        inputEntry.delete(0,END)
        inputEntry.insert(0,'50')       
    #清空图像，以使得前后两次绘制的图像不会重叠
    ##drawPic.f.clf()
    ##drawPic.a=drawPic.f.add_subplot(111)
    errpic = []
    label = []
    drawPic.f.clf()
    for i in tqdm(range(1,id)):
        #drawPic.f.clf()
        font = {
           'color': 'r',
           'style': 'oblique',
           'size': 10,
           'weight': 'bold'
        }
    
        drawPic.ax = drawPic.f.gca(projection='3d')
        drawPic.ax.set_xlim((-2,2))
        drawPic.ax.set_ylim((-2,2))
        drawPic.ax.set_zlim((0,2))
        drawPic.ax.set_xlabel("X", fontdict=font)
        drawPic.ax.set_ylabel("Y", fontdict=font)
        drawPic.ax.set_zlabel("Z", fontdict=font)


        x = dataset[i][1]
        y = dataset[i][2]
        z = dataset[i][3]
        
        mpl.rcParams['legend.fontsize'] = 20

        if y[len(y)-1] - y[0] > 0:
            colors = 'r'
            errpic.append(i+1)
        else:
            colors = 'c'
        color_8 = ['c','beige','black','brown','gold','r','green','gray']
    #drawPic.a.plot(x,y,color='c')
        
        label.append(i)
        drawPic.ax.set_title("trajectory", alpha=0.5, fontdict=font) #alpha²ÎÊýÖ¸Í¸Ã÷¶Ètransparent
        drawPic.ax.plot(x, y, z,color=color_8[np.random.randint(0,8)], label='parametric curve',linewidth=0.2)
    #drawPic.ax.legend(label,loc='upper right')

    drawPic.canvas.show()

        



       
    #绘制这些随机点的散点图，颜色随机选取
    #drawPic.a.plot(x,y,color='c')
    ##drawPic.a.plot(x,y,colors)

    ##drawPic.a.set_title('Demo: Draw N Random Dot')
    ##drawPic.canvas.show()
 
if __name__ == '__main__':    
	
	mpl.use('TkAgg')
	root = Tk()
    #在Tk的GUI上放置一个画布，并用.grid()来调整布局
	drawPic.f = Figure(figsize=(16,10), dpi=100)
 
	drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=root) 
	#drawPic.canvas.show() 
	drawPic.canvas.get_tk_widget().grid(row=0, columnspan=3)    
    
    #放置标签、文本框和按钮等部件，并设置文本框的默认值和按钮的事件函数
	Label(root,text='请输入样本数量：').grid(row=1,column=0)
	inputEntry=Entry(root)
	inputEntry.grid(row=1,column=1)
	inputEntry.insert(0,'50')
	Button(root,text='画图',command=drawPic).grid(row=1,column=2,columnspan=3)
       
    #启动事件循环
	root.mainloop()