from time import sleep
second = 0
minete = 0
hour = 0
for i in range(1000):
    second = second + 1
    sleep(1)
    if second== 59:
        minete +=1
        second == 0
        if minete == 59:
            hour +== 1



    print (minete, ":", second, ":", hour, ":")
