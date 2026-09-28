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

def 
    


def main():
    flight_taks1 = "set altimeter"
    flight_task2 = "set heading"
    item1 = "clear prop"
    item2 = "check fuel"
    engine_start_checklist()
    takeoff_checklist()
    checklist(flight_taks1, flight_task2)
    checklist_item(item1, item2)
   
if __name__ == "__main__":
    main()
