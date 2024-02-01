import TripManager
import Trip
import Route
import User

class Parser:
    tripManager = TripManager()

    def addTrip(user: User, date, startTime, origin, dest):
        newRoute = Route(origin, dest)
        newTrip = Trip.createTrip(date, startTime, newRoute, user)
        Parser.tripManager.addTrip(newTrip)