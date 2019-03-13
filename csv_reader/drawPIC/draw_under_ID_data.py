def drawPic():
    try:id=int(inputEntry.get())
    except:
        id=50
        print ('请输入整数')
        inputEntry.delete(0,END)
        inputEntry.insert(0,'50')
       
    #清空图像，以使得前后两次绘制的图像不会重叠
    drawPic.f.clf()
    drawPic.a=drawPic.f.add_subplot(111)
    drawPic.a.set_xlim((-2,2))
    drawPic.a.set_ylim((-2,2))

    #在[0,100]范围内随机生成sampleCount个数据点
    x=dataset[id][1]
    y=dataset[id][2]


    if y[len(y)-1] - y[0] >0:
            colors = 'r'
    else:
            colors = 'c'

       
    #绘制这些随机点的散点图，颜色随机选取
    #drawPic.a.plot(x,y,color='c')
    drawPic.a.plot(x,y,colors)

    drawPic.a.set_title('ID00187')
    drawPic.canvas.show()
 
if __name__ == '__main__':    
	
	mpl.use('TkAgg')
	root = Tk()
    #在Tk的GUI上放置一个画布，并用.grid()来调整布局
	drawPic.f = Figure(figsize=(5,5), dpi=100)
 
	drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=root) 
	drawPic.canvas.show() 
	drawPic.canvas.get_tk_widget().grid(row=0, columnspan=3)    
    
    #放置标签、文本框和按钮等部件，并设置文本框的默认值和按钮的事件函数
	Label(root,text='ID：').grid(row=1,column=0)
	inputEntry=Entry(root)
	inputEntry.grid(row=1,column=1)
	inputEntry.insert(0,'50')
	Button(root,text='DRAW',command=drawPic).grid(row=1,column=2,columnspan=3)
       
    #启动事件循环
	root.mainloop()
