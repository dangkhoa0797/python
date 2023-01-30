file_object=open('b-example.txt')
data=file_object.read()
print(data)

file_object=open('b-example.txt', mode='w')
data=file_object.write("hoang dang khoa")
file_object.close()
print(data)

file_object=open('b-example.txt', mode='a+')
data=file_object.write("\n2hoang dang khoa")
file_object.close()
print(data)