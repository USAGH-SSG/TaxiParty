class Route:
    def __init__(self, origin, dest) -> None:
        self.origin = origin
        self.dest = dest
    
    def isSameRoute(self, otherRoute: 'Route'):
        return self.origin == otherRoute.origin and self.dest == otherRoute.dest
    
    def __str__(self):
        return "Trip heading from " + self.origin + " to " + self.dest