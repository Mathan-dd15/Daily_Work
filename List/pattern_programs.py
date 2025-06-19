'''     1

    ##

   333

  ####

 55555'''



a = 6
for i in range(1,a):
    if i % 2 == 0:
        print((' ' * (a-i-1)),('#' * i),end = '')
    else:
        print((' ' * (a-i-1)),(str(i) * i),end = '')
    print("\n")
        
