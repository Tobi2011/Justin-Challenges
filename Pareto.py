#Pareto Distribution
import matplotlib.pyplot as plt

print(' Alpha is a positive parameter which determines\n\
the concentration of data towards the mode)'
alph = int(input('Provide an Alpha: ')) #is a positive parameter which determines the concentration of data towards the mode
print('x_m is the minimum possible value of X')
x_m = int(input('Prive a minimum X: ')) #is the minimum possible value of X
print ('x is a random variable (x>x_m)\n\
pick the lower an upper bounds')
x_lower = int(input('Lower bound: '))
x_higher = int(input('Upper bound: '))
pareto = alpha * (x_m ** alpha)/(x_lower ** (alpha+1))
variance = ((x_m**2)*alpha)/((alpha-1)**2)/(alpha-2)
cdf += 1-(x_m/x_lower)**alpha

while x_lower < 4000:
    pareto += alpha * (x_m ** alpha)/(x_lower ** (alpha+1))
    x_lower += 1


    
print(f'Probability = {pareto}')
print(f'Cumulative density = {cdf}')
print(f'Variance = {variance}')

y_axis = []
x_axis = []
x = x_m
x_high = 10000
while x < x_high:
    pareto += alpha * (x_m ** alpha)/(x ** (alpha+1))
    x += 1
    x_axis.append(x)
    y_axis.append(alpha * (x_m ** alpha)/(x ** (alpha+1)))


pareto_plot = plt.plot(x_axis,y_axis)
plt.xlim([x_m,x_high/2])
plt.ylim([0,y_axis[0]])
plt.show()
