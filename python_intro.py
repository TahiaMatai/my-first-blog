name='Ola'
print(name)
if (3 > 2):
	print('It works')
else:
	print('3 n\'est pas plus grand que 2')

def hi(name):
	print ('Youhou ' + name + '!  Kimba ?')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola']
girls.sort ()
for name in girls:
	hi(name)
	print('Next girl')

for i in range(1,10):
	print(i)
