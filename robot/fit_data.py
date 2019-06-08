import matplotlib.pyplot as plt
from scipy import stats
### carspeed = 100
time = [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
distance = [11.5,15,17.8,21,24.3,26,30.5,33.5,35.5]
### carspeed = 80
slope, intercept, r_value, p_value, std_err = stats.linregress(time, distance)
print("slope: %f    intercept: %f" % (slope, intercept))
fit = [slope*x + intercept for x in time]
plt.plot(time,distance)
plt.plot(time,fit)
plt.show()
