class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def search_by_team(self, team_name):
        team_matches = []
        for match in self.matches:
            if team_name in [match.team1, match.team2]:
                team_matches.append(match)
        return team_matches

    def search_by_location(self, location):
        location_matches = []
        for match in self.matches:
            if match.location == location:
                location_matches.append(match)
        return location_matches

    def search_by_timing(self, timing):
        timing_matches = []
        for match in self.matches:
            if match.timing == timing:
                timing_matches.append(match)
        return timing_matches

def main():
    table = FlightTable()

    # Adding matches to the table
    table.add_match(Match("Mumbai", "India", "Sri Lanka", "DAY"))
    table.add_match(Match("Delhi", "England", "Australia", "DAY-NIGHT"))
    table.add_match(Match("Chennai", "India", "South Africa", "DAY"))
    table.add_match(Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
    table.add_match(Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
    table.add_match(Match("Delhi", "India", "Australia", "DAY"))

    while True:
        print("\nSearch Options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            team_name = input("Enter the team name: ")
            team_matches = table.search_by_team(team_name)
            print("\nMatches involving", team_name)
            for match in team_matches:
                print(match.location, match.team1, "vs", match.team2, match.timing)
        elif choice == 2:
            location = input("Enter the location: ")
            location_matches = table.search_by_location(location)
            print("\nMatches in", location)
            for match in location_matches:
                print(match.location, match.team1, "vs", match.team2, match.timing)
        elif choice == 3:
            timing = input("Enter the timing: ")
            timing_matches = table.search_by_timing(timing)
            print("\nMatches with timing", timing)
            for match in timing_matches:
                print(match.location, match.team1, "vs", match.team2, match.timing)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
