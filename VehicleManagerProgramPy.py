import datetime
from dateutil.relativedelta import relativedelta

class Vehicle(object):

    def __init__(self, brand, model, kilometers, servicedate):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers
        self.servicedate = servicedate

    def edit_km(self, new_kilometers):
        self.kilometers = new_kilometers

    def edit_servicedate(self, new_servicedate):
        self.servicedate = new_servicedate

    def get_full_name(self):
        return self.brand + " " + self.model


def list_all_vehicles(vehicles):
    for index, car in enumerate(vehicles):
        print("ID: " + str(index))  # index is an order number of the contact object in the contacts list
        print("Name: " + car.get_full_name())
        print("Mileage: " + str(car.kilometers) + " km")
        print("Service Date: " + str(car.servicedate))
        print("") # EMPTY LINE

    if not vehicles:
        print("### You don't have any vehicle in your list. ###")


def add_vehicle(vehicles):
    brand = raw_input("Enter the brand of the vehicle: ")
    model = raw_input("Enter the model of the vehicle: ")
    kilometers = None
    while kilometers is None:
        try:
            kilometers = int(raw_input("Enter the kilometers done so far with the vehicle: "))
        except ValueError:
            print("### /!\ ###")  # EMPTY LINE
            print("### Your entry wasn't an integer number. Please try again. ###")
    servicedate = None
    while servicedate is None:
        try:
            servicedate = datetime.datetime.strptime(raw_input("Enter the general service date of the vehicle in the format yyyy-mm-dd: "), "%Y-%m-%d")
        except ValueError:
            print("/!\ ") # EMPTY LINE
            print("Your entry didn't have the right format. Please try again.")

    new = Vehicle(brand=brand, model=model, kilometers=kilometers, servicedate=servicedate)
    vehicles.append(new)

    print("") # EMPTY LINE


def edit_mileage(vehicles):
    print("Select the id of the vehicle you'd like to edit the mileage of: ")

    for index, car in enumerate(vehicles):
        print(str(index) + ") " + car.get_full_name())

    print("") # EMPTY LINE
    selected_id = raw_input("What vehicles would you like to edit (enter id number): ")
    selected_vehicle = vehicles[int(selected_id)]

    new_kilometers = raw_input("Please update the kilometers done so far with the %s: " % selected_vehicle.get_full_name())
    selected_vehicle.edit_km(new_kilometers)
    print("")  # EMPTY LINE
    print("### Kilometers updated. ###")


def edit_servicedate(vehicles):
    print("Select the id of the vehicle you'd like to edit the general service date of: ")

    for index, car in enumerate(vehicles):
        print(str(index) + ") " + car.get_full_name())

    print("") # EMPTY LINE
    selected_id = raw_input("What vehicles would you like to edit (enter id number): ")
    selected_vehicle = vehicles[int(selected_id)]
    new_servicedate = None
    while new_servicedate is None:
        try:
            new_servicedate = datetime.datetime.strptime(raw_input("Enter a new general service date of the vehicle %s in the format yyyy-mm-dd: " % selected_vehicle.get_full_name()), "%Y-%m-%d")
        except ValueError:
            print("### /!\ ###") # EMPTY LINE
            print("### Your entry didn't have the right format. Please try again. ###")
    selected_vehicle.edit_servicedate(new_servicedate)
    print("")  # EMPTY LINE
    print("### Service date updated. ###")


def delete_vehicle(vehicles):
    print("Select the id of the vehicle you'd like to delete: ")

    for index, car in enumerate(vehicles):
        print(str(index) + ") " + car.get_full_name())

    print("") # EMPTY LINE
    selected_id = raw_input("What vehicles would you like to delete (enter id number): ")
    selected_vehicle = vehicles[int(selected_id)]
    vehicles.remove(selected_vehicle)
    print("")  # EMPTY LINE
    print("### Vehicle deleted. ###")


def save_list(vehicles):
    save_list = open("vehicles.txt", "w+") # create or open txt file
    save_list.write("##############################################################\n")  # write into the txt file
    save_list.write("### VEHICLE LIST ### Timestamp: " + str(datetime.datetime.today()) + " ###\n") # write into the txt file
    save_list.write("##############################################################\n")  # write into the txt file
    print("### /!\ ATTENTION /!\ ###")
    print("### Vehicles that should be in service soon! ###\n")
    save_list.write("\n")  # write into the txt file
    save_list.write("### /!\ ATTENTION /!\ ### \n")  # write into the txt file
    save_list.write("### Vehicles that should be in service soon! ###\n")  # write into the txt file
    for index, car in enumerate(vehicles):
            if datetime.datetime.strptime(car.servicedate, "%Y-%m-%d") <= datetime.datetime.today() + relativedelta(months=2) and datetime.datetime.strptime(car.servicedate, "%Y-%m-%d") >= datetime.datetime.today():
                print(str(index) + "\t" + car.get_full_name() + "\t" + car.kilometers + " km\t" + car.servicedate)
                save_list.write(str(index) + "\t" + car.get_full_name() + "\t" + car.kilometers + " km\t" + car.servicedate + "\n") # add items into the txt file
    print("\n")
    save_list.write("\n")  # write into the txt file
    print("### All vehicles ###\n")
    save_list.write("### All vehicles ###\n")  # write into the txt file
    for index, car in enumerate(vehicles):
        print(str(index) + "\t" + car.get_full_name() + "\t" + car.kilometers + " km\t" + car.servicedate)
        save_list.write(str(index) + "\t" + car.get_full_name() + "\t" + car.kilometers + " km\t" + car.servicedate + "\n") # add items into the txt file

    save_list.close() # close txt file


def main():
    print("####################################")
    print("### Welcome to your Vehicle List ###")
    print("####################################")

    car1 = Vehicle(brand="Volkswagen", model="Crafter", kilometers="40000", servicedate=datetime.datetime(2017,01,01))
    car2 = Vehicle(brand="Volkswagen", model="T5", kilometers="99000", servicedate=datetime.datetime(2017,03,01))
    car3 = Vehicle(brand="Volkswagen", model="T5", kilometers="88000", servicedate=datetime.datetime(2017,03,02))
    vehicles = [car1, car2, car3]

    while True:
        print("")  # empty line
        print("Please choose one of these options:")
        print("1) See all your vehicles")
        print("2) Add a new vehicle")
        print("3) Edit mileage of a vehicle")
        print("4) Edit general service date of a vehicle")
        print("5) Delete a vehicle")
        print("9) Save your vehicle list as txt-file.")
        print("0) Quit the program.")
        print("")  # empty line

        selection = raw_input("Enter your selection ('1', '2', '3', '4', '5', '9' or '0'): ")
        print("")  # empty line

        if selection == "1":
            list_all_vehicles(vehicles)
        elif selection == "2":
            add_vehicle(vehicles)
        elif selection == "3":
            edit_mileage(vehicles)
        elif selection == "4":
            edit_servicedate(vehicles)
        elif selection == "5":
            delete_vehicle(vehicles)
        elif selection == "9":
            save_list(vehicles)
        elif selection == "0":
            print("### Thank you for using Vehicle List. Goodbye! ###")
            break
        else:
            print("### /!\ ###")
            print("### Sorry, your selection wasn't found. Please try again. ###")
            continue


if __name__ == '__main__':
    main()