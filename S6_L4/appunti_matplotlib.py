# Primo esempio

from matplotlib import pyplot as plt
from numpy import random as rnd
import humanize as h

data = rnd.randint(0, 100, 10)
x =[h.ordinal(i) for i in range(1, 11)]
plt.plot(x, data, color ="r", linewidth=4, linestyle="--", marker="x", markersize="10")

others = rnd.randint(0, 100, 15)
ox= [h.ordinal(i) for i in range(1, 16)]
plt.plot(ox, others, "m", linewidth=2, linestyle=":", marker="o")
plt.title("Il mio primo grafico", color = "g")
plt.xlabel("Asse delle etichette", color =(.8,.4,0))
plt.ylabel("Asse dei valori", color="#9999ff")
plt.grid(True)
plt.legend(loc=4, labels=['Elemento 1', 'Elemento 2'])
plt.show()


# Due grafici distinti con sublpot

from matplotlib import pyplot as plt
from numpy import random as rnd
import humanize as h

plt.subplot(1,2,1)

d1 = rnd.randint(0, 100, 10)
d1x = [h.ordinal(i) for i in range(1, 11)]
plt.plot(d1x, d1, "b^")

d2 = rnd.randint(0, 100, 15)
d2x = [h.ordinal(i) for i in range(1, 16)]
plt.plot(d2x, d2, "g*")

plt.subplot(1, 2, 2)

d3 = rnd.randint(0, 100, 15)
d3x = [h.ordinal(i) for i in range(1, 16)]
plt.plot(d3x, d3, "g*")

plt.show()

# SEABORN

import seaborn as sns
from matplotlib import pyplot as plt

anscombe = sns.load_dataset("anscombe")
print(anscombe.sample(10))

datasetI = anscombe[anscombe.dataset == "I"]
sns.lmplot(x='x', y='y', data=datasetI, ci=None)

plt.show()














