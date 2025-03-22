# this class contains all variables relative to a location
class Location:
    def __init__(self, x, y, info):
        self.x = x
        self.y = y
        self.info = info
    
    def coordinates(self):
        return (self.x, self.y)
    
    def contains_info(self):
        return self.info != None


# this class is used to store the location history of a user
# it contains the user name, location class instance, and the timestamp of the visit
class LocationHistory:
    def __init__(self, user, location, timestamp):
        self.user = user
        self.location = location
        self.timestamp = timestamp
    
    def get_user(self):
        return self.user
    
    def get_location(self):
        return self.location
    
    def get_timestamp(self):
        return self.timestamp


# this class is used to store the travel history of a user
# it contains a list of LocationHistory instances
class TravelHistory:
    def __init__(self):
        self.location_histories = []
    
    # Add a location to the travel history
    def add_history(self, location_history):
        self.location_histories.append(location_history)
    
    # return a list of unique locations visited
    def get_unique_locations(self):
        unique_locations = set()
        for history in self.location_histories:
            unique_locations.add(history.get_location().coordinates())
        return list(unique_locations)
    
    # return a list of the most visited locations
    # if there are multiple locations with the same number of visits, return a list of those locations
    def get_most_visited_locations(self):
        location_visits = {}
        for history in self.location_histories:
            location = history.get_location().coordinates()
            if location in location_visits:
                location_visits[location] += 1
            else:
                location_visits[location] = 1
        return [location for location, visits in location_visits.items() if visits == max(location_visits.values())]
    
    # return dict of every visited location and its number of visits
    def get_visit_counts(self):
        location_visits = {}
        for history in self.location_histories:
            location = history.get_location().coordinates()
            if location in location_visits:
                location_visits[location] += 1
            else:
                location_visits[location] = 1
        return location_visits




locations = []
location_histories = []
travel_history = TravelHistory()

# this function generates a location object
def generate_location(x, y, info):
    locations.append(Location(x, y, info))
    return locations[-1]

# this function generates a location history object
def generate_location_history(location, timestamp):
    location_histories.append(LocationHistory(location, timestamp))
    travel_history.add_history(location_histories[-1].location) # update travel history
    return location_histories[-1]