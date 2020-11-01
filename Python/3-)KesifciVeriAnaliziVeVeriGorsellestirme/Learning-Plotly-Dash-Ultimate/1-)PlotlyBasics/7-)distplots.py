import plotly.figure_factory as ff
import plotly.offline as pyo
import numpy as np

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
x4 = np.random.randn(200) + 4
hist_data = [x1, x2, x3, x4]  # hangi verilerin dağılımını inceleyeceğiz
group_labels = ['X1', 'X2', 'X3', 'X4']  # sırasıyla başlıklar

fig = ff.create_distplot(
    hist_data=hist_data,
    group_labels=group_labels,
    bin_size=[.2, .1, .3, .4]  # sırasıyla bin size'lar
)

pyo.plot(figure_or_data=fig, filename='7-)distplots.html')
