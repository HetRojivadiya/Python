from plyer import notification
import time


while True:
    t = time.localtime()
    formate = time.strftime("%S", t)
    print(int(formate))
    if(int(formate)/10)==0:
        notification.notify(
        title = 'Notifiction',
        message = 'Please Drink a Water',
        app_icon = 'notification.ico',
        timeout = 10,
        )