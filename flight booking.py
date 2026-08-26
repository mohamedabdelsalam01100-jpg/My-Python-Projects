flights = {"EG101": {
    "from": "cairo",
    "to": "dubai",
    "price": 5000,
    "seats": 5
},
"EG202": {
    "from": "cairo",
    "to": "istanbul",
    "price": 7000,
    "seats": 3},
    "EG303" : {
        "from": "alexandria",
        "to": "rome",
        "price": 8500,
        "seats": 2
        }}
print("="*50)
print("""                           Available Flights                      """)
print("="*50)

for flight in flights:
    print(flight)
    for key, value in flights[flight].items():
        if key == "from":
            print(value, end=("->"))
        elif key == "to":
            print(value)
        elif key == "price":
            print("price:", value, "EGP")
        elif key == "seats":
            print("seats:", value)     

passanger_name = input("Enter passanger name: ").title().strip()
passport_num = input("Enter passport number: ").strip().upper()
flight_id = input("Enter flight id: ").strip().upper()
tickets_num = int(input("Enter number of tickets: "))
discount =int(input("enter your discount: "))


booking = {
    "name": passanger_name,
    "passport": passport_num,
    "flight": flight_id,
    "tickets": tickets_num
}



price = flights[flight_id].get("price")
subtotal = price * tickets_num
discount_am = (subtotal * discount) / 100
total = subtotal - discount_am
if tickets_num <= flights[flight_id]["seats"]:
  l = flights[flight_id]["seats"] - tickets_num
  flights[flight_id]["seats"] = l
  print("Before:\n ",
  "Seats = ", flights[flight_id]["seats"] + tickets_num)
  print(f"After booking {tickets_num} tickets: "
        f"Seats = , {l}" )

  print("=" *50)
  print("""                                FLIGHT BOOKING                                       """ )
  print("=" *50)  

  print(f"""Passanger: {passanger_name}
Passport: {passport_num}
Flight: {flight_id}
Route: {flights[flight_id].get("from")} -> {flights[flight_id].get("to")}
Tickets: {tickets_num}
Price: {flights[flight_id].get("price")}

subtotal = {subtotal}
discount = {discount}%
Final = {total} EGP
Remaining seats = {l}""")

  print("=" *50)
  print("""                                BOOKING CONFIRMED                                             """)
  print("=" *50)
else:
    print("not enough seats!!!")  



  


    
    




                

