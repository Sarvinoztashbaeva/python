import numpy as np

l1 =[12.23, 13.32, 100, 36.32]
print(np.array(l1))

a = np.array([[2,3,4],[5,6,7],[8,9,10]])
print(a)

vector = np.zeros(10)
print(vector)
vector[6]=11
print(vector)

b =np.arange(12,38)
print(b)

c = np.array([1,2,3,4,5])
print(c.dtype)
s= c.astype(float)
print(s.dtype)

sample_array = np.array([
    [0, 12, 45.21, 34, 99.91],
    [-17.78, -11.11, 7.34, 1.11, 37.73 ]
])
print('Values in Fahrenheit degrees:',sample_array[0])
print('Values in Centigrade degrees:',sample_array[1])

aray = np.array([10,20,30])
new_array = np.append(aray,[40,50,60,70,80,90])
print(new_array)

array = np.array([43,62,9,32,64,7,15,4,50,82])
print('Mean:',np.mean(array))
print('Median:',np.median(array))
print('Standard deviation:',np.std(array))

random_array = np.random.rand(10,10)
print('Min:',np.min(random_array))
print('Max:',np.max(random_array))

array = np.random.rand(3,3)
print(array)
