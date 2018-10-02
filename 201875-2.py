import matplotlib.pyplot as plt
fig,ax=plt.subplots()
y1=[]
for i in range(50):
    y1.append(i**2)
    ax.cla()
    ax.plot(y1,label='test')
    ax.legend()
    plt.pause(0.1)

plt.show()