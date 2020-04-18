from matplotlib import pyplot as plt

# Initialize random_walk
rw = [(0,0)]

for i in range(10000):
    delta_x = np.random.uniform(-1,1)
    sign=np.random.randint(0,2)
    if sign == 0:
        sign = -1 
    delta_y = sign*(1-delta_x**2)**(1/2)
    x = rw[i][0] + delta_x
    y = rw[i][1] + delta_y
    rw.append((x, y))
   
plt.plot([e[0] for e in rw], [e[1] for e in rw])