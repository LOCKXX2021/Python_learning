import numpy as np
import random
import csv
import math
import matplotlib.pyplot as plt
from time import *



def change(address):
	x_address = ((address - 1) % 2500)
	y_address = ((address - 1) // 2500)
	return x_address,y_address

def change_back(x_address,y_address):
	address=(x_address+1)+(y_address*2500+1)
	return address

def check_map(built_map_temp,bags):
	

	
	for i in range(1,len(bags)):
		if bags[i]==1:
			x_map,y_map=change(i)
			built_map_temp[x_map][y_map]=1
	ok=1
	for i in range(2500):
		for j in range(2500):
			if built_map_temp[i][j]==1:
				for ii in range(-10,11,1):
					for jj in range(-10,11,1):
						if built_map_temp[i+ii][j+jj]==1 and pow(ii,2)+pow(jj,2)<100:
							ok=0
							return ok
	return ok

def count_works(built_map_temp,bags,works_map,typee):
	ans=0
	for i in np.arange(1, len(bags)):
		if bags[i] == 1:
			x_map, y_map = change(i)
			built_map_temp[x_map][y_map] = 1
	
	for i in range(2500):
		for j in range(2500):
			
			if built_map_temp[i][j]==1:
				
				if typee[change_back(i,j)]==10:
					for ii in range(-10,11,1):
						for jj in range(-10,11,1):
							if pow(ii,2)+pow(jj,2)<100:
								ans+=works_map[i+ii][j+jj]
								works_map[i+ii][j+jj]=0
								
				if typee[change_back(i, j)] == 30:
					for ii in range(-30, 31, 1):
						for jj in range(-30, 31, 1):
							if pow(ii, 2) + pow(jj, 2) < 900:
								ans += works_map[i + ii][j + jj]
								works_map[i + ii][j + jj] = 0
	return ans
	
	

def init_x(n, d):
	"""
	:param n: 粒子总数量
	:param d: 粒子种基因个数(维度)
	:return: 随机生成的种群(二维list)
	"""
	population = []
	for i in range(n):
		gene = []
		for j in range(d):
			a = np.random.randint(0, 2)
			gene.append(a)
		population.append(gene)
	return population


def init_v(n, d, V_max, V_min):
	"""
	:param n: 粒子总数量
	:param d: 粒子种基因个数(维度)
	:return: 随机生成的种群(二维list)
	"""
	v = []
	for i in range(n):
		vi = []
		for j in range(d):
			a = random.random() * (V_max - V_min) + V_min
			vi.append(a)
		v.append(vi)
	return v


def fitness(p, n, d, w, w_max, v, afa , built_map_temp,works_map):
	"""
	:param p: 粒子群
	:param n: 群体粒子个数
	:param d: 粒子维数
	:param w: 物品的重量列表
	:param w_max: 背包最大容量
	:param v: 物品的价值列表
	:param afa: 惩罚系数
	:return: pbest每一个粒子的适应度列表
	:return: fitweight每一个粒子的重量
	tips: 如果物品总重量大于背包最大容量时，引入惩罚系数
	"""
	

	fitvalue = []
	fitweight = []
	now=np.zeros((1,len(d)),dtype=int)
	for i in range(n):
		a = 0  # 每个粒子的重量/成本
		b = 0  # 每个粒子的价值(适应度)
		for j in range(d):
			if p[i][j] == 1:
				now[j] = 1
				
				a += w[j]
				
				##b += v[j]
			
		if check_map(built_map_temp,now)==0:
			b = 0
		if a > w_max:
			b = 0
		if check_map(built_map_temp,now)==1:
			
			b=count_works(built_map_temp,now,works_map)
			
			#b = b + afa * (w_max - a)  # 超重
		
		'''
		
		这里应该还要加上距离的判断？ljy
		
		'''
		fitvalue.append(b)
		fitweight.append(a)
	return fitvalue, fitweight


def update_pbest(p, fitvalue, pbest, px, m):
	"""
	更新个体最优
	:param p: 当前种群
	:param fitvalue: 当前每个粒子的适应度
	:param pbest: 更新前的个体最优
	:param px: 更新前的个体最优解
	:param m: 粒子数量
	:return: 更新后的个体最优值、个体最优解
	"""
	pb = pbest
	for i in range(m):
		if fitvalue[i] > pbest[i]:
			pbest[i] = fitvalue[i]
			px[i] = p[i]
	return pb, px


def update_gbest(p, pbest, gbest, g, m):
	"""
	更新全局最优解
	:param p: 粒子群
	:param pbest: 个体适应度(个体最优)
	:param gbest: 全局最优
	:param g: 全局最优解
	:param m: 粒子数量
	:return: gbest全局最优，g对应的全局最优解
	"""
	gb = gbest
	for i in range(m):
		if pbest[i] > gb:
			gb = pbest[i]
			g = p[i]
	return gb, g


def update_v(v, x, m, n, pbest, g, c1, c2, vmax, vmin):
	"""
	更新速度
	:param v:更新前的速度
	:param x: 更新前的位置
	:param m: 粒子数量
	:param n: 粒子维度
	:param pbest: 个体最优解(二维列表)
	:param g: 全局最优解(一维列表)
	:param c1: 加速因子
	:param c2: 加速因子
	:param vmax: 最大速度
	:param vmin: 最小速度
	:return: 更新后的速度二维列表
	"""
	for i in range(m):
		a = random.random()
		b = random.random()
		for j in range(n):
			v[i][j] = v[i][j] + c1 * a * (pbest[i][j] - x[i][j]) + c2 * b * (g[j] - x[i][j])
			if v[i][j] < vmin:
				v[i][j] = vmin
			if v[i][j] > vmax:
				v[i][j] = vmax
	return v


def update_x(x, v, m, n):
	"""
	更新x
	:param x:更新前的x
	:param v: 更新后的v
	:param m: 粒子数量
	:param n: 粒子维度
	:return: 更新后的x
	"""
	for i in range(m):
		for j in range(n):
			a = random.random()
			x[i][j] = 1 / (1 + math.exp(-v[i][j]))
			if x[i][j] > a:
				x[i][j] = 1
			else:
				x[i][j] = 0
	return x


# main()
if __name__ == '__main__':
	begin_time = time()
	"""
	这里应该用文件的读入，来获取弱覆盖和已经有的基站，同时进行数据的处理1、降噪，去除后90%+的业务基站2、消去已有基站的点的坐标
	"""
	
with open('附件1 弱覆盖栅格数据(筛选).csv', 'r', encoding='utf-8') as f:
	rfg = np.array(csv.reader(f))##print(rfg[0][0:3])


with open('附件2 现网站址坐标(筛选).csv', 'r', encoding='utf-8') as f:
	yyz = np.array(csv.reader(f))
	

	
	##降噪：形成新的地图
	rfg.sort(key=lambda ele: ele[2], reverse=True)
	
	new_map= np.zeros((2500,2500),dtype= int)
	
	for i in range(0,int(len(rfg)*0.95)):
		new_map[int(rfg[i][0])][int(rfg[i][1])]=eval(rfg[i][2])
	
	built_map = np.zeros((2500,2500),dtype= int)
	
	for i in range(0,int(len(yyz))):
		built_map[int(yyz[i][1])][int(yyz[i][2])]=1
		
	'''
	for i in range(0,2500):
		for j in range(0,2500):
			if new_map[i][j]>0:
				print("⬛",end=' ')
			else:
				print("⬜",end=' ')
				
	'''
	hong, wei = eval(input("bili:hong/wei "))
	max_cb = eval(input("max chengbeng"))
	new_map_cb = np.random.choice([0, 1], size=2500*2500, p=[hong, wei])##成本 一维
	new_map_ywl=[]
	
	for i in range(1,2500*2500+1):
		xx=((i-1)%2500)
		yy=((i-1)//2500)
		new_map_ywl=new_map[xx][yy]##业务量 一维
	
	Weight = new_map_cb
	Value = new_map_ywl
	
##Weight = [95,75,23,73,50,22,6,57,89,98]  # 物品体积!!
##Value = [89,59,19,43,100,72,44,16,7,64]  # 物品价值!!

N = 10000 # 群体粒子个数？

D = len(Weight)  # 粒子维数
T = 50  # 最大迭代次数
c1 = 1.5  # 学习因子1
c2 = 1.5  # 学习因子2
W_max = 0.8  # 惯性权重最大值
W_min = 0.4  # 惯性权重最小值
V_max = 10  # 速度最大值
V_min = -10  # 速度最小值

##Weight_max = 300  # 背包容量
Weight_max = max_cb  # 背包容量！！！

afa = 10  # 惩罚系数

item = []  # 用于记录每一次迭代的全局最优值
itemg = []  # 用于记录每一次迭代的全局最优解

x = init_x(N, D)  # 初始化x
v = init_v(N, D, V_max, V_min)  # 初始化v
fv, fw = fitness(x, N, D, Weight, Weight_max, Value, afa)  # 计算第一次迭代的适应度
pb, px = fv, x  # 由于是第一次迭代，个体最优为当前值
gb, g = update_gbest(x, pb, 0, [], N)  # 同理，寻找第一代的全局最优
item.append(gb)  # item列表记录每一次迭代的全局最优
itemg.append(g)
v = update_v(v, x, N, D, px, g, c1, c2, V_max, V_min)  # 更新下一代的速度
x = update_x(x, v, N, D)  # 更新下一代的位置

for i in range(T):
	
	built_map_temp = built_map
	works_map = new_map
	fv, fw = fitness(x, N, D, Weight, Weight_max, Value, afa , built_map_temp,works_map)
	
	pb, px = update_pbest(x, fv, pb, px, N)
	gb, g = update_gbest(x, pb, gb, g, N)
	item.append(gb)
	itemg.append(g)

	v = update_v(v, x, N, D, px, g, c1, c2, V_max, V_min)
	x = update_x(x, v, N, D)

print(gb)
 ##print(gb,g)!!
plt.plot(item)
plt.show()
end_time = time()
run_time = end_time - begin_time

print('粒子群算法计算时间为：', run_time," s ")

