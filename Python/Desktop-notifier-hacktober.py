#hacktober2021




from plyer import notification

import time



title = 'Hi Amazing Yourself'

message= 'Pomodoro Method states:Taking Strategic Breaks Improves Productivity'

#app_icon = any ico file 

app_icon = 'notify.ico'

#timeout = time till which the notification stays
#time.sleep(t) = after every t secs notification shows up; eg: for 20 mins-> t=20*60

while True:

	notification.notify(title = title,message= message,app_icon = app_icon,timeout= 3)
	
	time.sleep(20*60)
                    

