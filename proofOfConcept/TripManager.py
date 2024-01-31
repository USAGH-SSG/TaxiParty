import Trip
import User

class TripManager:
    def __init__(self) -> None:
        self.trips = []
    
    def addTrip(self, trip: Trip) -> None:
        self.trips.append(trip)
    
    def findUsersTrip(self, user: User):
        usersTrip = []
        for trip in self.trips:
            if trip.isUserOnTrip(user):
                usersTrip.append(user)
        return usersTrip
