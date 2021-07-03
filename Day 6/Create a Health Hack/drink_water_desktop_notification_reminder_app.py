import time
from plyer import notification
if __name__ == '__main__':
 	while True:
 		notification.notify(
 			title = "Drink Water Now!!",
 			message ="This is your regular pop-up reminder to drink water.",
 			# path to your ico file
             app_icon = "Water_Icon.ico",
 			timeout = 10
 			)
 		time.sleep(60)