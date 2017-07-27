import matplotlib.pyplot as plt

x1 = list()
y1 = list()

xy1 = open('XYlog.txt', 'r')

for line in xy1:
	temp1 = line.split(' ')
	y1.append(int(temp1[0]))
	x1.append(float(temp1[1].strip('\n')))

plt.plot(x1, y1)

# label plot axis
plt.xlabel('Time(sec)')
plt.ylabel('Window Size')
plt.title('Window Size At Any Period of Program Execution')
plt.legend()

plt.show()
