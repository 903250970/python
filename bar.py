import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1,1,1)

x=np.array(["东区","北区","南区","西区"])
y=np.array([100,300,200,400])

plt.bar(x,y,width=0.5,align="center",label="任务量")

plt.title("全国各分区任务量",loc="center")

for a,b in zip(x,y):
    plt.text(a,b,b,ha='center',va="bottom",fontsize=12)

plt.xlabel('分区')

plt.ylabel('任务量')

plt.legend()

plt.savefig("F:/python/excel/bar.jpg")