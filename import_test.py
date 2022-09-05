import time

starttime  = time.time()
lasttime = starttime
lapnum = 1
value = ""

while value.lower() != "q":
    value = input()
    laptime = round((time.time() - lasttime),2)
    totaltime = round((time.time() - starttime), 2)

    print("Lap.No. " + str(lapnum))
    print ("Total time: " + str(totaltime))
    print ("Lap Time: " + str(laptime))

    print ("*" * 20)

    lasttime = time.time()
    lapnum +=1

print ("Completed")