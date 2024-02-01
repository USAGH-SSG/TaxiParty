import datetime
import Route

class Trip:
    def __init__(self, date, startTime, route: Route, user) -> None:
        self.date = date
        self.startTime = startTime
        self.route = route
        self.users = [user]
    
    def isUserOnTrip(self, user):
        return user in self.users
    
    def isTripOnDate(self, date: datetime.date):
        return self.date == date

    def createTrip(date, startTime, route: Route, user):
        return Trip(date, startTime, route, user)

    def __str__(self) -> str:
        return self.route + " @ " + self.startTime + ", " + self.date + "\n" \
            "with riders " + self.users

    def addUser(self, newUser):
        if len(self.users) == 4:
            raise Exception("New rider can't be added. Trip Full.")
        else:
            self.users.append(newUser)
    
    def __eq__(self, otherTrip): 
        if not isinstance(otherTrip, Trip):
            # don't attempt to compare against unrelated types
            return NotImplemented

        if self.date != otherTrip.date:
            return self.date < otherTrip.date
        return self.startTime < otherTrip.startTime
