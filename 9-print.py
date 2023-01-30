print('Khoa', 'Python', 'Course') # sep mặc định là 1 khoảng trắng
print('Khoa', 'Python', 'Course', sep='---')
print('Khoa', 'Python', 'Course', sep='|||')
print('Khoa', 'Python', 'Course', sep='\n')

with open('printtext.txt', 'w') as f:
     print('printed by print function', file=f)