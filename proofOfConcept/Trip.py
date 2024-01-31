class Trip:
    def __init__(self, date, startTime, location, users) -> None:
        self.date = date
        self.startTime = startTime
        self.location = location
        self.users = users
    
    def isUserOnTrip(self, user):
        return user in self.users

    def createTrip(date, startTime, location, users):
        return Trip(date, startTime, location, users)

    def __str__(self) -> str:
        return "Trip departing from " + self.location + " @ " + self.startTime + ", " + self.date + "\n" \
            "with riders " + self.users

    def addUser(self, newUser):
        if len(self.users) == 4:
            raise Exception("New rider can't be added. Trip Full.")
        else:
            self.users.append(newUser)
