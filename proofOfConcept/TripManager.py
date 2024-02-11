import Trip
import User
import Route
import datetime


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

    def findTripOnDay(self, date: datetime.date):
        return [x for x in self.trips if x.isTripOnDate(date)].sort()

    def findTripWithRoute(self, route: Route):
        return [x for x in self.trips if x.isSameRoute(route)].sort()
