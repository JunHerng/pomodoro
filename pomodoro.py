"""
    The Pomodoro Technique is a time management method.
    It uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.
    Pomodoro script. Features:
    1. Windows notifications for rest and work times.

    Possible improvements:
    1. Notification freezes loop for (default) 5 seconds. Doesn't affect timer tracking.
       Could thread or something? But no need.
"""

from datetime import date, datetime
from win10toast import ToastNotifier
import time

toast = ToastNotifier()
start = datetime.now()

# Initialize pomodoro parameters
# work (w), short rest (sr), long rest (lr)
# w-sr-w-sr-w-sr-w-lr
# 0-1-2-3-4-5-6-7
# 8-9-10-11-12-13-14-15
# 8 cycle - odd = rest, even = work
pom_counter = 0
pom_work = 25 # mins
pom_rest_short = 5 # mins
pom_rest_long = 5 # mins

toast.show_toast("Pomodoro - {}".format(pom_counter), "Pomodoro started!\nWORK for {} minutes".format(pom_work))

while True:
    now = datetime.now()
    delta = now.timestamp() - start.timestamp()
    print(delta, end="\r")
    if pom_counter%2: # Odd - rest
        time_period = pom_rest_short * 60
        if not pom_counter%7: # Long break every 4th pomodoro
            time_period = pom_rest_long * 60
    elif not pom_counter%2: # Even - work
        time_period = pom_work * 60
    if time_period < delta: # End of current activity
        start = datetime.now()
        # Notify next action
        if pom_counter%2: # Work time!
            pom_counter += 1
            toast.show_toast("Pomodoro - {}".format(pom_counter), "WORK for {} minutes!".format(pom_work))
        elif pom_counter%8 == 6: # Long rest time!
            pom_counter += 1
            toast.show_toast("Pomodoro - {}".format(pom_counter), "LONG REST for {} minutes!".format(pom_rest_long))
        elif not pom_counter%2: # Short rest time!
            pom_counter += 1
            toast.show_toast("Pomodoro - {}".format(pom_counter), "SHORT REST for {} minutes!".format(pom_rest_short))
    time.sleep(3)
