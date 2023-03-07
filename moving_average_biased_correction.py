import matplotlib.pyplot as plt
import numpy as np

shape = [500]

data = np.random.randint(-100, 100, shape)
m_avg = np.zeros(shape)  # store means computed by moving average
no_biased_m_avg = np.zeros(shape)  # store means computed by corrected bias moving average
normal_avg = np.zeros(shape)  # store means computed by normal averaging

vt, t = 0, 0
beta = 0.98


def no_bias_mv(number):
    global vt, t

    t += 1
    vt = vt * beta + (1 - beta) * number
    no_biased_m_avg[t - 1] = (vt / (1 - (beta ** t)))
    m_avg[t - 1] = vt
    normal_avg[t-1] = np.sum(data[:t]) / t


for num in data:
    no_bias_mv(num)

# plt.scatter(range(len(data)), data, marker='.', color='pink')
plt.plot(normal_avg, label="Normal Average")
plt.plot(m_avg, label="Exponentially weighted Moving Average")
plt.plot(no_biased_m_avg, label="Corrected biased Moving Average")
plt.legend()
plt.show()