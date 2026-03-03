class RaceTime:
    def __init__(self, start_hrs, start_mins, end_hrs, end_mins, dist):
        """
        start_time: Race start time. String w/ format 'hours:minutes'.
        end_time: Race end time. String w/format 'hours:minutes'.
        distance: Distance of race in miles.
        """
        self.start_hrs = start_hrs
        self.start_mins = start_mins
        self.end_hrs = end_hrs
        self.end_mins = end_mins
        self.distance = dist

    def print_time(self):
        if self.end_mins >= self.start_mins:
            minutes = self.end_mins - self.start_mins
            hours = self.end_hrs - self.start_hrs
        else:
            minutes = 60 - self.start_mins - self.end_mins
            hours = self.end_hrs - self.start_hrs - 1

        print(f"Time to complete race {hours}:{minutes}")

    def print_pace(self):
        if self.end_mins >= self.start_mins:
            minutes = self.end_mins - self.start_mins
            hours = self.end_hrs - self.start_hrs
        else:
            minutes = 60 - self.start_mins + self.end_mins
            hours = self.end_hrs - self.start_hrs -1

        total_minutes = hours * 60 + minutes
        print(f"Avg pace (mins/mile): {total_minutes / self.distance:.2f}")

distance = 5.0

start_hrs = int(input("Enter the starting time hours: "))
start_mins = int(input("Enter the starting time minutes: "))
end_hrs = int(input("Enter the ending time hours: "))
end_mins = int(input("Enter the ending time minutes: "))

race_time = RaceTime(start_hrs, start_mins, end_hrs, end_mins, distance)

# The race times of the hurdles competition
time_Xaiden = RaceTime("3:15", "7:45", 26.21875)
time_Kainan = RaceTime("3:15", "10:02", 28.21875)
time_Sticky = RaceTime("3:15", "8:46", 26.21875)