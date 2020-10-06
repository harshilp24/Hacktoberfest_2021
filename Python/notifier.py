
import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "***Please drink water now ***",
            message = "Hey, I know you are busy right now but now so that you can't have a glass of water.",
            timeout = 18, #displays notification for 8 seconds

        )
        time.sleep(60 * 60)
      
