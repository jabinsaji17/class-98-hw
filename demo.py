def files():
    filename = input("enter the file name")
    file=open(filename,'r')
    print(file.read())
files()