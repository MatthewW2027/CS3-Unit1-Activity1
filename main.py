def engine_start_checklist(): 
    print("Master and alternator on")
    print("Beacon light on")
    print("prime")
    print("key to start")
    print("mixture full rich")
    print("throttle: 1000 RPM")

def takeoff_checklist():
    print("lights on")
    print("fuel both")
    print("mixture full rich")
    print("traffic clear left and right")

def checklist(flight_task1, flight_task2):
    print(f"Its time for the engine start checklist {flight_task1}")
    print(f"Its time for the takeoff checklist {flight_task2}")

def checklist_item(item1, item2):
    print(f"now I have to {item1} then {item2}")
    return f"{item1} then {item2}"

def add_item(item1, optional_item):
    print(f"after take off you have to {item1} then if your plane is equiped {optional_item}")

def checklists(flight_task1, flight_task2, item1, item2, optional_item):
    engine_start_checklist()
    takeoff_checklist()
    checklist(flight_task1,flight_task2)
    checklist_item(item1,item2)
    add_item(item1,optional_item)


def main():
    flight_task1 = "set altimeter"
    flight_task2 = "set heading"
    item1 = "clear prop"
    item2 = "check fuel"
    optional_item = "check oil"
    engine_start_checklist()
    takeoff_checklist()
    checklist(flight_task1, flight_task2)
    checklist_item(item1, item2)
    add_item(item1, optional_item)
    checklists(flight_task1, flight_task2, item1, item2, optional_item)

if __name__ == "__main__":
    main()
