from copy import copy

class Time:
    """ a class that represents the time of day """
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

time1 = Time() # Creates a instance of time class called time1
time1.hours = 7
time1.minutes = 15

time2 = Time() # Creates a instance of time class called time2
time2.hours = 12
time2.minutes = 45

print("\n")
print(f"{time1.hours} hours and {time1.minutes} minutes")
print(f"{time2.hours} hours and {time2.minutes} minutes")
print(type(time1))
print("\n")

lunch = Time() # A new instance of Time()
lunch.hours = 11
lunch.minutes = 30
lunch.seconds = 10

print(lunch.hours)

total_minutes = lunch.hours * 60 + lunch.minutes
print(total_minutes)
print("\n")
print("Expanded functions example:")
def print_time(time):
    s = f'{time.hours:02d}:{time.minutes:02d}:{time.seconds:02d}'
    print(s)
print_time(lunch)
print("\n")

def make_time(hour, minute, second):
    time = Time()
    time.hours = hour
    time.minutes = minute
    time.seconds = second
    return time

def increment_time(time, hours, minutes, seconds):
    time.hours += hours
    time.minutes += minutes
    time.seconds += seconds

    if time.seconds >= 60:
        time.seconds -= 60
        time.minutes += 1

    if time.minutes >= 60:
        time.minutes -= 60
        time.hours += 1

def add_time(time, hours, minutes, seconds):
    total = copy(time)
    increment_time(total, hours, minutes, seconds)
    return total

start = make_time(9, 21, 0)
print_time(start)
print("\n")

# Mutability, Copying, and Pure Functions
start = make_time(9, 20, 0)

# Modify the object directly
start.hours += 1
start.minutes += 30
print_time(start) # 10:50:00

# Copy a class instance
start = make_time(9, 20, 0)
end = copy(start) # Create a new independent object

print("\n")
print(start is end) # False - these are different objects
print(start == end) # False - checks identity for custom classes by default

def increment_time(time, hours, minutes, seconds):
    time.hours += hours
    time.minutes += minutes
    time.seconds += seconds
    
    if time.seconds >= 60:
        time.seconds -= 60
        time.minutes += 1

    if time.minutes >= 60:
        time.minutes -= 60
        time.hours += 1

def add_time(time, hours, minutes, seconds):
    total = copy(time) # Copy first
    increment_time(total, hours, minutes, seconds)
    return total # Return the modified copy

end = add_time(start, 1, 32, 0)
print_time(end) # 10:52:00
print_time(start) # 09:20:00

print("\nPrototype and Patch")

start = make_time(9, 40, 0)
end = add_time(start, 1, 32, 0)
print_time(end)