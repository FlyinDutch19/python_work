
#myfile = open("/Users/zhangji/desktop/python_work/files/test.txt",mode="a") #r代表只读，w代表可写(overwrite原有的内容，如果没有相同文件，可以新建一个文件)，a代表在最后add新的内容
#myfile.write("\nFourth Line")
#myfile = open("/Users/zhangji/desktop/python_work/files/newtest.txt",mode="w") 
#myfile.write("Haha")
myfile = open("/Users/zhangji/desktop/python_work/files/newtest.txt",mode="r") 
test_file = myfile.read()
print(test_file)
