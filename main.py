#python实现线性表抽象数据类型
#if __name__ == "__main__":#当此语句下的代码是主文件身份时运行，导入其他文件后不运行
def practice_class():
    class mysqlist():
        def __init__(self,size):
            self.size=size
            self.sqlist=[]
        def listinsert(self,i,x):#在i处插入x
            if i<1 or i>self.size:#判断i是否合法
                print("Insert Location Error！")
                return False
            else:
                self.sqlist.insert(i,x)#插入
                return True
        def listdelete(self,i):#删除i处
            if i<1 or i>self.size:#判断i是否合法
                print("Delete Location Error！")
                return False
            else:
                self.sqlist.pop(i)#删除i处
                return False
        def findelem(self,i):#查询i处数值
            if i<1 or i>self.size:#判断i是否合法
                print("search Location Error！")
                return False
            else:
                return self.sqlist[i]
        def showlist(self):#查询整体
            return self.sqlist
def practice_matplotlib_1():
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(-2,2,50)
    y1 = 2*x*x
    y2 = 2*x
    plt.figure(num=1)#以下直至另一个figure的plt操作属于这个figure？大概
    plt.plot(x,y1)#根据坐标绘图，与上一行figure绑定

    plt.figure(num=2)#(num,figsize,dpi, facecolor,edgecolor,frameon,FigureClass,clear）
    plt.plot(x,y2,color='red',linewidth=1,linestyle=':')#()
    plt.plot(x,y1)

    plt.xlim((-3,3))#限制的是初始视野，不是绘制区间
    plt.ylim((-3,3))#limit限制

    plt.xlabel('x')#给xy轴重命名
    plt.ylabel('y')#label标签

    new_ticks = np.linspace(0,2,5)
    plt.xticks(new_ticks)#将xy轴的坐标重命名
    plt.yticks([1,3,4],[r'$bad$',r'$good\ \alpha$','perfact'])#$转换字体  \显示空格与希腊字母

    plt.show()#show一次展示所有figure


import matplotlib.pyplot as plt
import numpy as np
import math
class heavenlyBodies():
    '''天体半径，轨迹半径，初始角度，公转周期，颜色'''
    def __init__(self,size,r,o,time,color):
        self.size = size*20
        self.xy = [int(r*5),o]
        self.speed = (2*math.pi)/time
        self.color = color

    def move(self):
        self.xy[1]+= self.speed
        while self.xy[1]>=2*math.pi:
            self.xy[1]-=2*math.pi

    def draw(self):
        solar_system.scatter(self.xy[1],self.xy[0],self.size,self.color)
def body_data():
    global body_radius
    global orbit_radius
    global orbit_time
    global body_color
    #太阳系天体半径适当化：太阳20水星1金星3地球3火星2木星7土星6天王星5海王星5
    body_radius = [20,1,3,3,2,7,6,5,5]
    #太阳系天体轨道半径适当化：太阳0水星4金星8地球10火星15木星20土星30天王星40海王星50
    orbit_radius = [0,4,8,10,15,20,30,40,50]
    #太阳系天体公转周期适当化：太阳0水星80金星200地球400火星800木星4000土星10000天王星30000海王星60000
    orbit_time = [1,80,200,400,800,4000,10000,30000,60000]
    #太阳系天体颜色适当化：太阳 深橙 水星 金黄 金星 金黄 地球 深蓝 火星 黄土赭 木星 秋麒麟 土星 耐火砖 天王星 浅蓝 海王星 蓝
    body_color = ['#FF8C00','#FFD700','#FFD700','#0000FF','#A0522D','#DAA520','#B22222','#00FFFF','#4682B4',]
body_data()#导入数据

sun_body = []
for i in range(9):#创建天体对象
    sun_body.append(heavenlyBodies(body_radius[i],orbit_radius[i],0,orbit_time[i],body_color[i]))
plt.ion()
solar_system = plt.figure(1, (10, 10))  # 打开画布
while 1:

    solar_system.subplot(projection='polar')#切换坐标系为极坐标
    solar_system.grid(False)#不显示格子
    therta = np.linspace(0,2*math.pi)#轨道角度数据
    for i in range(9):#绘制轨道
        r = sun_body[i].xy[0]*np.ones(50)#轨道半径数据
        solar_system.plot(therta, r,linewidth=1,color=body_color[i])#绘制轨道
    for i in range(9):
        sun_body[i].draw()#绘制天体
        sun_body[i].move()#计算天体下一位置
    solar_system.show()#展示全部对象
