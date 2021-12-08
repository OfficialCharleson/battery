#THE PSUTIL LIBRARY CAN BE USED TO ACCESS SENSORS ON YOUR COMPUTER, BATTERY SENSORS BEING ONE OF THEM
#WE WILL NEED THE NOTIFICATION MODULE IN THE PLYER LIBRARY TO SEND NOTIFICATIONS TO THE COMPUTER

from plyer import notification
import psutil

battery= psutil.sensors_battery()
timeleft=battery.secsleft/3600
plugged= battery.power_plugged

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
checker=plugged
while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    if(plugged!=checker):
        checker=plugged
        print(plugged)
        if(plugged==False):
            notification.notify(
                # title of notification
                title="Plugged Out",

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
