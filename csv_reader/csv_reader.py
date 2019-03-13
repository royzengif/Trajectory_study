import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

#fig, ax = plt.subplots()

#x = np.arange(0, 2*np.pi, 0.01)
#line, = ax.plot(x, np.sin(x))

#def animate(i):
    #line.set_ydata(np.sin(x+i/100))
    #return line,

#def init():
    #line.set_ydata(np.sin(x))
    #return line

#ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=False)
#plt.show()




fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)
l = ax.plot(x, y)
dot, = ax.plot([], [], 'ro')

def init():
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    return l

def gen_dot():
    for i in len(px):
        newdot = [px[i], py[i]]
        yield newdot

def update_dot(newd):
    dot.set_data(newd[0], newd[1])
    return dot,

ani = animation.FuncAnimation(fig, update_dot, frames = gen_dot, interval = 100, init_func=init)
plt.show()





fig, ax = plt.subplots()

def ani_data(i):

    data = data_get(i)
    px = data[0]
    py = data[1]
    return px, py

def px(i):
    return ani_data(i)[0]

def py(i):
    return ani_data(i)[1]

plt.xlim((-4,4))
plt.ylim((-4,4))

l1, =ax.plot(px(1), py(1))
l2, =ax.plot(px(2), py(2))

dot, = ax.plot([], [], 'ro')

def init(i):
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    if i == 1:
        return l1
    if i == 2:
        return l2

def gen_dot(j):
    for i in range(len(px(j))):
        newdot = [px(j)[i], py(j)[i]]
        yield newdot

def update_dot(newd):
    dot.set_data(newd[0], newd[1])
    return dot,


ani1 = animation.FuncAnimation(fig, update_dot, frames = gen_dot(1), interval = 100, init_func=init(1))
#ani2 = animation.FuncAnimation(fig, update_dot, frames = gen_dot(2), interval = 100, init_func=init(2))
plt.show()




fig, ax = plt.subplots()
x = data_get(1)[0]
y = data_get(1)[1]
l = ax.plot(x, y)
dot, = ax.plot([], [], 'ro')

def init():
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    return l

def gen_dot():
    for i in range(len(x)):
        newdot = [x[i], y[i]]
        yield newdot

def update_dot(newd):
    dot.set_data(newd[0], newd[1])
    return dot,


x2 = data_get(2)[0]
y2 = data_get(2)[1]
l2 = ax.plot(x2, y2)
dot, = ax.plot([], [], 'ro')

def init2():
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    return l2

def gen_dot2():
    for i in range(len(x2)):
        newdot = [x2[i], y2[i]]
        yield newdot

def update_dot2(newd):
    dot.set_data(newd[0], newd[1])
    return dot,
ani2 = animation.FuncAnimation(fig, update_dot2, frames = gen_dot2, interval = 30, init_func=init2)

ani1 = animation.FuncAnimation(fig, update_dot, frames = gen_dot, interval = 30, init_func=init)



plt.show()





#tkinkerGUI绘图
def drawPic():
    try:id=int(inputEntry.get())
    except:
        id=50
        print ('请输入整数')
        inputEntry.delete(0,END)
        inputEntry.insert(0,'50')
       
    #清空图像，以使得前后两次绘制的图像不会重叠
    #drawPic.f.clf()
    drawPic.a=drawPic.f.add_subplot(111)

    #在[0,100]范围内随机生成sampleCount个数据点
    x=data_get(id)[0]
    y=data_get(id)[1]
    color=['b','r','y','g']
       
    #绘制这些随机点的散点图，颜色随机选取
    drawPic.a.plot(x,y,color='c')
    #drawPic.a.plot(x,y,color=color[np.random.randint(len(color))])
    print(color[np.random.randint(len(color))])
    drawPic.a.set_title('Demo: Draw N Random Dot')
    drawPic.canvas.show()
 
if __name__ == '__main__':    
	
	matplotlib.use('TkAgg')
	root = Tk()
    #在Tk的GUI上放置一个画布，并用.grid()来调整布局
	drawPic.f = Figure(figsize=(5,4), dpi=100)
 
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


#摆锤运动
g = 9.8
leng = 1.0
b_const = 0.2

# no decay case:
def pendulum_equations1(w, t, l):
    th, v = w
    dth = v
    dv  = - g/l * sin(th)
    return dth, dv

# the decay exist case:
def pendulum_equations2(w, t, l, b):
    th, v = w
    dth = v
    dv = -b/l * v - g/l * sin(th)
    return dth, dv

t = np.arange(0, 20, 0.1)
track = odeint(pendulum_equations1, (1.0, 0), t, args=(leng,))
#track = odeint(pendulum_equations2, (1.0, 0), t, args=(leng, b_const))
xdata = [leng*sin(track[i, 0]) for i in range(len(track))]
ydata = [-leng*cos(track[i, 0]) for i in range(len(track))]

fig, ax = plt.subplots()
ax.grid()
line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    time_text.set_text('')
    return line, time_text

def update(i):
    newx = [0, xdata[i]]
    newy = [0, ydata[i]]
    line.set_data(newx, newy)
    time_text.set_text(time_template %(0.1*i))
    return line, time_text

ani = animation.FuncAnimation(fig, update, range(1, len(xdata)), init_func=init, interval=100)

plt.show()

#main()

def drawPic():#对时间数据使用gui画图
    try:id=int(inputEntry.get())
    except:
        id=50
        print ('请输入整数')
        inputEntry.delete(0,END)
        inputEntry.insert(0,'50')
       
    #清空图像，以使得前后两次绘制的图像不会重叠
    
    #drawPic.f.clf()
    for i in range(400,id+2):
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
        dataset = get_data_time(1,3500,i)
        x = dataset[1]
        y = dataset[2]
        z = dataset[3]
        mpl.rcParams['legend.fontsize'] = 15
    #print(x)
    #print(y)
        #color=['darkslateblue','darkseagreen','darksalmon','cyan','chocolate','darkkhaki','darkmagenta','brown','azure','darkred','r','y','b','black']
        if y[len(y)-1] - y[0] >0:
            colors = 'r'
        else:
            colors = 'c'
        print(colors)
           
    #绘制这些随机点的散点图，颜色随机选取
    #drawPic.a.plot(x,y,color='c')
        label = [id]

        #drawPic.ax.set_title("", alpha=0.5, fontdict=font) #alpha参数指透明度transparent
        drawPic.ax.plot(x, y, z,color=colors, label='parametric curve')
        drawPic.ax.legend(label,loc='upper right')

        drawPic.canvas.show()
        #time.sleep(0.3)
 
if __name__ == '__main__':    
	
	mpl.use('TkAgg')
	root = Tk()
    #在Tk的GUI上放置一个画布，并用.grid()来调整布局
	drawPic.f = plt.figure(figsize=(9,7), dpi=100)
 
	drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=root) 
	drawPic.canvas.show() 
	drawPic.canvas.get_tk_widget().grid(row=0, columnspan=3)    
    
    #放置标签、文本框和按钮等部件，并设置文本框的默认值和按钮的事件函数
	Label(root,text='number of ID：').grid(row=1,column=0)
	inputEntry=Entry(root)
	inputEntry.grid(row=1,column=1)
	inputEntry.insert(0,'50')
	Button(root,text='draw',command=drawPic).grid(row=1,column=2,columnspan=3)
       
    #启动事件循环
	root.mainloop()


