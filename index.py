#THE PSUTIL LIBRARY CAN BE USED TO ACCESS SENSORS ON YOUR COMPUTER, BATTERY SENSORS BEING ONE OF THEM
#WE WILL NEED THE NOTIFICATION MODULE IN THE PLYER LIBRARY TO SEND NOTIFICATIONS TO THE COMPUTER

from plyer import notification
import psutil

battery= psutil.sensors_battery()
timeleft=battery.secsleft/3600
plugged= battery.power_plugged

#FIRST OFF: You check the initial status of the plugged in status and notify the laptop
if (plugged == False):
    notification.notify(
        # title of notification
        title="Plugged In",

        # message of notification
        message="You just unplugged your charger!",

        # displaying time
        timeout=2
    )
else:
    notification.notify(
        # title of notification
        title="Plugged In",

        # message of notification
        message="You just plugged your charger in!",

        # displaying time
        timeout=2
    )
   
#Now we need to store the initial plugged in status so we can know when the status is changed
checker=plugged

#Using a loop isnt the most ideal way. A thread is better but for the purpose of this we will use a loop
while True:
   #we need to recheck the status of the battery and plugged in every loop
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    #Now we check if the status is different from the stored status
    if(plugged!=checker):
        #Since its different we reset the stored status to the new status
        checker=plugged        
        if(plugged==False):
            notification.notify(
                # title of notification
                title="Plugged Out",

                # message of notification
                message="You just unplugged your charger! {}%".format(battery.percentage),

                # displaying time
                timeout=2
            )
        else:
            notification.notify(
                # title of notification
                title="Plugged In",

                # message of notification
                message="You just plugged your charger in!",

                # displaying time
                timeout=2
            )
