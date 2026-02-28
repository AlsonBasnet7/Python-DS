# Driver and  admin management system.
#This is the CLI based backend simulation system.
# Driver & Admin Backend Simulation
# Save as: backend_system.py

class Driver:
    def __init__(self, driver_id, name):
        self.driver_id = driver_id
        self.name = name
        self.available = True
        self.trips = []

    def assign_trip(self, trip):
        self.trips.append(trip)
        self.available = False

    def __str__(self):
        status = "Available" if self.available else "On Trip"
        return f"ID: {self.driver_id} | Name: {self.name} | Status: {status}"


class Trip:
    def __init__(self, trip_id, source, destination):
        self.trip_id = trip_id
        self.source = source
        self.destination = destination

    def __str__(self):
        return f"Trip {self.trip_id}: {self.source} -> {self.destination}"


class System:
    def __init__(self):
        self.drivers = {}
        self.trips = {}

    # Admin features
    def add_driver(self, driver_id, name):
        self.drivers[driver_id] = Driver(driver_id, name)
        print("Driver added successfully.")

    def view_drivers(self):
        for d in self.drivers.values():
            print(d)

    def create_trip(self, trip_id, source, destination):
        self.trips[trip_id] = Trip(trip_id, source, destination)
        print("Trip created.")

    def assign_trip(self, driver_id, trip_id):
        driver = self.drivers.get(driver_id)
        trip = self.trips.get(trip_id)

        if not driver or not trip:
            print("Invalid driver or trip.")
            return

        if not driver.available:
            print("Driver is busy.")
            return

        driver.assign_trip(trip)
        print("Trip assigned successfully.")

    # Driver view
    def view_driver_trips(self, driver_id):
        driver = self.drivers.get(driver_id)
        if not driver:
            print("Driver not found.")
            return

        print(f"\nTrips for {driver.name}:")
        for t in driver.trips:
            print(t)


def menu():
    system = System()

    while True:
        print("\n===== Backend System =====")
        print("1. Add Driver")
        print("2. View Drivers")
        print("3. Create Trip")
        print("4. Assign Trip")
        print("5. View Driver Trips")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            i = input("Driver ID: ")
            n = input("Name: ")
            system.add_driver(i, n)

        elif choice == "2":
            system.view_drivers()

        elif choice == "3":
            t = input("Trip ID: ")
            s = input("Source: ")
            d = input("Destination: ")
            system.create_trip(t, s, d)

        elif choice == "4":
            di = input("Driver ID: ")
            ti = input("Trip ID: ")
            system.assign_trip(di, ti)

        elif choice == "5":
            di = input("Driver ID: ")
            system.view_driver_trips(di)

        elif choice == "6":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
