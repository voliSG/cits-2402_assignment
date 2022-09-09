import numpy as np
import matplotlib.pyplot as plt
# Data
states = ["15-24", "25-34", "35-44", "45-54", "55-64", "65-74", "over 75", "overall"]
staff = np.array([20, 30, 40, 10, 15, 35, 18, 25])
sales = staff * (20 + 10 * np.random.random(staff.size))

# Sort by number of sales staff
idx = staff.argsort()
states, staff, sales = [np.take(x, idx) for x in [states, staff, sales]]

y = np.arange(sales.size)

fig, axes = plt.subplots(ncols=2, sharey=True)
fig.suptitle('Gini Index by Age Group', fontsize=16)

axes[0].barh(y, staff, align='center', color='gray', zorder=10)
axes[0].set(title='United States')
axes[1].barh(y, sales, align='center', color='gray', zorder=10)
axes[1].set(title='Australia')

axes[0].invert_xaxis()
axes[0].set(yticks=y, yticklabels=states)
axes[0].yaxis.tick_right()

for ax in axes.flat:
    ax.margins(0.03)
    ax.grid(True)

fig.tight_layout()
fig.subplots_adjust(wspace=0.09)
plt.show()