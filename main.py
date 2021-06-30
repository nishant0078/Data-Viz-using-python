import matplotlib.pyplot as plt
import numpy as np


np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
country = ('Saudi Arabia', 'China', 'India', 'Germany', 'USA')
y_pos = np.arange(len(country))
performance = 3 + 10000 * np.random.rand(len(country))
error = np.random.rand(len(country))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(country)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Defence Budgets in Billions')
ax.set_title('Countries with most spendings')

plt.show()
