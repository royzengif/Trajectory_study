# -*- coding: cp936 -*-



def drawPic():#对时间数据使用gui画图
    try:id=int(inputEntry.get())
    except:
        id=50
        print ('请输入整数')
        inputEntry.delete(0,END)
        inputEntry.insert(0,'50')
       
    #清空图像，以使得前后两次绘制的图像不会重叠
    errpic = []
    drawPic.f.clf()
    for i in tqdm(range(1,id)):
        #drawPic.f.clf()
        font = {
           'color': 'y',
           'style': 'oblique',
           'size': 20,
           'weight': 'bold'
        }
    
        drawPic.ax = drawPic.f.gca(projection='3d')
        drawPic.ax.set_xlim((-2,2))
        drawPic.ax.set_ylim((-2,2))
        drawPic.ax.set_zlim((0,2))
        drawPic.ax.set_xlabel("X", fontdict=font)
        drawPic.ax.set_ylabel("Y", fontdict=font)
        drawPic.ax.set_zlabel("Z", fontdict=font)

 
    #x=data_get(id)[0]
    #y=data_get(id)[1]
        #dataset = get_data_time(3,5000,i)
        x = dataset[i][1]
        y = dataset[i][2]
        z = dataset[i][3]
        mpl.rcParams['legend.fontsize'] = 20
    #print(x)
    #print(y)
        #color=['darkslateblue','darkseagreen','darksalmon','cyan','chocolate','darkkhaki','darkmagenta','brown','azure','darkred','r','y','b','black']
        if y[len(y)-1] - y[0] >0:
            colors = 'r'
            errpic.append(i+1)
        else:
            colors = 'c'

    #绘制这些随机点的散点图，颜色随机选取
    #drawPic.a.plot(x,y,color='c')
        label = [i]
        drawPic.ax.set_title("Line Plot", alpha=0.5, fontdict=font) #alpha参数指透明度transparent
        drawPic.ax.plot(x, y, z,color=colors, label='parametric curve')
        drawPic.ax.legend(label,loc='upper right')

        #drawPic.canvas.show()
        #time.sleep(0.3)
    print(errpic)
if __name__ == '__main__':    
	
	mpl.use('TkAgg')
	root = Tk()
    #在Tk的GUI上放置一个画布，并用.grid()来调整布局
	drawPic.f = plt.figure(figsize=(9,7), dpi=100)
 
	drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=root) 
	drawPic.canvas.show() 
	drawPic.canvas.get_tk_widget().grid(row=0, columnspan=3)    
    
    #放置标签、文本框和按钮等部件，并设置文本框的默认值和按钮的事件函数
	Label(root,text='请输入样本数量：').grid(row=1,column=0)
	inputEntry=Entry(root)
	inputEntry.grid(row=1,column=1)
	inputEntry.insert(0,'50')
	Button(root,text='画图',command=drawPic).grid(row=1,column=2,columnspan=3)
       
    #启动事件循环
	root.mainloop()
