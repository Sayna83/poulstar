from time import sleep
second = 0
while True:
    second += 1
    sleep(1)
    if second % 7 == 0 :
        print("hop")
    else :
        print(second)