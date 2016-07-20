### Date and time lesson from Unit 2 on Codecademy
### https://www.codecademy.com/courses/python-beginner-en-zFPOx/0/1?curriculum_id=4f89dab3d788890003000096

from datetime import datetime

## getting the current date and time
now = datetime.now()
print now

# what if we don't want full date and time, just year, month or day?
current_year = now.year
current_month = now.month
current_day = now.day
print("Current year: " + str(current_year))
print("Current month: " + str(current_month))
print("Current day: " + str(current_day))

# Date format mm/dd/yyyy
print("%s/%s/%s" % (current_month, current_day, current_year))

# and let's do the same for the hour, minute and second
print "%s:%s:%s" % (now.hour, now.minute, now.second)


## Let's combine date and time together
print("%s/%s/%s %s:%s:%s" % (now.month, now.day, now.year, now.hour, now.minute, now.second))
