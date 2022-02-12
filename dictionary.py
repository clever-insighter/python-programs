
# write a program to print items in  the dictionary

def func():
    dict={1:"python",2:"datascience",3:"pandas"}
    for x,y in dict.items():
        print(x,'-->',y)
func()    


# write a program to print key  in the dictionary


def func():
    dict = {1:"python",2:"datascience",3:"pandas"}
    for  x in dict.keys():
        print(x)
func()


# write a program to print values in the dictionary

def func():
    dict = {1:"python",2:"datascience",3:"pandas"}
    for  y in dict.values():
        print(y)
func()


#  write a program to print items in the dictionary

def func():
    dict = {1:"python",2:"datascience",3:"pandas"}
    for  x,y in dict.items():
        print(x,".",y)
func()