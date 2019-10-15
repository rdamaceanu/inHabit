
# This is the habit class
class habit:

    def __init__(self, aName):
        self.name = aName        

    def add_dailyDuration(self, timeInMins):    
        self.dailyDuration = timeInMins

# This is the user class
class habiteer:
    habit_list = []

    def __init__(self, aName):
        self.name = aName

    def add_habit(self, habit):
        if hasattr(habit, 'name'):
            self.habit_list.append(habit.name)







new_habit = habit('jogging')    
print('My new habit is called {}'.format(new_habit.name))

new_habit.add_dailyDuration(20)
print('and it has a duration of {} minutes a day'.format(new_habit.dailyDuration))

new_user = habiteer('Radu')
print('We have a new user named {}'.format(new_user.name))

new_user.add_habit(new_habit)
print('He has a new habit called {} which takes {} minutes daily'.format(new_habit.name, new_habit.dailyDuration))

