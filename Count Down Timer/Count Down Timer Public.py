from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz

# Parse the start datetime string into a datetime object
start_datetime_str = "05-13-24 9:00 AM"
start_datetime = datetime.strptime(start_datetime_str, "%m-%d-%y %I:%M %p")

# Get today's date and time
current_datetime = datetime.now()

# Set the timezone to Pacific Standard Time
pst_timezone = pytz.timezone("America/Los_Angeles")
start_datetime_pst = pst_timezone.localize(start_datetime)

# Add the number of months to complete from the start datetime
future_datetime = start_datetime_pst + relativedelta(months=+24)

# Calculate the difference between start and future datetime
time_difference = future_datetime.date() - start_datetime_pst.date()

time_remain = future_datetime.date() - current_datetime.date()

# Print the future date as a date value and the time difference
print("Quitting Date:", future_datetime.date())
print("Time Difference (in days):", time_difference.days)
print("Time Remaining in days:", time_remain.days)

role = input("Enter your role: ")
dream = input("Enter your dream goal: ")

if time_remain.days >= 0 and time_remain.days <= 73:
    message = "Start to lockdown new job, only 10% of time left remains!"
elif time_remain.days >= 74 and time_remain.days <= 146:
    message = "Begin exit planning and casually applying for roles. Keep grinding for interview prep!"
elif time_remain.days >= 147 and time_remain.days <= 219:
    message = "Almost quitting time! Start prepping for interviews and casually applying. You need more money to fund your {dream}!"
elif time_remain.days >= 220 and time_remain.days <= 292:
    message = "Time to decide if you want to give them another year. Did you get a raise, a title bump, do you like the work, and most importantly how is WLB?"
elif time_remain.days >= 293 and time_remain.days <= 365:
    message = f"You made it a year! You get to say you are an {role}, even if you don't feel like one." \
              "Hopefully you have been learning well this past year. You are further ahead than last year. Get ready for interviews and prove it!"
elif time_remain.days >= 366 and time_remain.days <= 438:
    message = "Getting close to a year. Decide if you need to bail or not. If you do, grind leet code and dsa, and make dua! You will be needing it!"
elif time_remain.days >= 439 and time_remain.days <= 513:
    message = "You are a year in, how is the likelyhood of promotion and or growth? Are you well compensated? How far are you off from market rate for your skill and business value?" \
              "Almost a year in, try and keep holding on. Much easier to grab a job with a year for the title than not." \
              "If you are here still because you havent found anything, start prepping to include this on your resume depending on the role. You have been through, might as well get some credit for time served!"
elif time_remain.days >= 514 and time_remain.days <= 586:
    message = "A half year in, are you learning and building skills that translate? How is your self learning for ultimate goal going? Hold yourself accountable for your targets!" \
              "If you don't take responsibility for yourself who will? Love and respect yourself enough to do so!"\
              "If you are here out of circumstance, keep looking, rough markets eventually turn, and it will turn in your favor!"
elif time_remain.days >= 587 and time_remain.days <= 659:
    message = "You have made the decison to stay or you are stuck." \
              "If you are stuck keep looking, keep upskilling. Something will pan out or maybe you chnage your mind and this place is not as bad as you thought." \
              "Ifyou stayed hopefully there is goodness in this, find out, hold on to it, and keep learning as you stay prepared to pull the rip cord."
elif time_remain.days >= 660 and time_remain.days <= 730:
    message = "You just started. Make the decision to stay or bail. If you stay, grind it out, maximize your time and learning." \
              "If you are bailing make the commitment to bail, prepare not to have a new place to hang your hat or make the search for a new plce priority!" \
              "If you are willing to be annoyed, stressed and in discomfort get the most benefit that sets you up for the future!"
else:
    message = "Keep your head down, grind it out, keep upskilling and keep learning. You are in the right place at the right time."

print(message)

