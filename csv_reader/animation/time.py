import time
import datetime
#realtime to timestamp
dt= '2012:08:13-21:00:04:395'
timeArray = time.strptime(dt, "%Y:%m:%d-%H:%M:%S:%f")
timestamp = time.mktime(timeArray)
print(timestamp)
#timestamp to realtime
time_local = time.localtime(int(timestamp))
#转换成新的时间格式(2016-05-05 20:28:54)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

print (dt)
