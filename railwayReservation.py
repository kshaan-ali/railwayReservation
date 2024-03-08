import random
import time

from datetime import date, timedelta


class user:
  bogi = [
      "none", "A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "S1", "S2", "S3"
  ]

  classes = [
      "none", "General", "AC-1st tier", "AC-2nd tier", "AC-3rd tier", "Sleeper"
  ]

  times = ["12:29", "6:15", "8:00", "3:45", "23:00", "15:00", "1:00", "17:30"]

  trains = [
      "none", "Rajdhani Express", "Shatabdi Express", "Duronto Express",
      "Gareeb Rath", "Chennai Express", "Fast Express"
  ]
  train_pricez=0
  place = [
      "none", "Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore",
      "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Surat", "Lucknow", "Goa",
      "Nagpur", "Kanpur", "Indore", "Bhopal", "Patna"
  ]

  def book(self):
    global train_no
    global times
    global timeslot
    global ticket_id
    global name
    global age
    global gender
    global train
    global source
    global destination
    global destination_temp
    global day
    global end_day

    global place
    global trains
    global train_pricez
    global classes
    global bogi
    global bogi_no
    global seat_no
    global class_name

    print("----------------Booking Ticket----------------------")
    print("\nEnter details of the passengers\n")
    name = input("Full Name of the passenger: ")
    age = int(input("Age of the passenger: "))
    gender = input("Gender of the passenger: ")

    print(
        "--------------------------------------------------------------------------------"
    )

    for i in range(1, len(self.place)):
      print(i, self.place[i])

    source_temp = int(input("Enter the boarding source: "))

    for i in range(1, len(self.place)):
      if source_temp == i:
        source = self.place[i]
      elif (source_temp > len(self.place) - 1):
        print("\nInvalid input")
        print("redirecting to main menu in 5 seconds")
        time.sleep(5)
        main()

    print(
        "--------------------------------------------------------------------------------------------"
    )
    for i in range(1, len(self.place)):
      print(i, self.place[i])
    destination_temp = int(input("Enter the destination: "))

    for i in range(1, len(self.place)):
      if destination_temp == i:
        destination = self.place[i]
      elif (destination_temp > len(self.place) - 1):
        print("\nInvalid input")
        print("redirecting to main menu in 5 seconds")
        time.sleep(5)
        main()

    day_temp = int(
        input(
            "\n\n1.Monday\t2.Tuesday\t3.Wednesday\n4.Thursday\t5.Frinday\t6.Saturday\t7.Sunday\n\nEnter the day of travel: "
        ))
    if (day_temp == 1):
      day = "Monday"
      end_day = "wednesday"
    elif (day_temp == 2):
      day = "Tuesday"
      end_day = "thursday"
    elif (day_temp == 3):
      day = "Wednesday"
      end_day = "friday"
    elif (day_temp == 4):
      day = "Thursday"
      end_day = "saturday"
    elif (day_temp == 5):
      day = "Friday"
      end_day = "sunday"
    elif (day_temp == 6):
      day = "Saturday"
      end_day = "monday"
    elif (day_temp == 7):
      day = "Sunday"
      end_day = "tuesday"
    else:
      print("Invalid input")
      main()
    print(
        "--------------------------------------------------------------------------------------------"
    )
    print("Available Time Slots")
    for i in range(1, len(self.times)):
      print(self.times[i], end="\t")
    check_time = input("\nEnter the time slot: ")
    timeslot = "00:00"
    if (check_time == "6:15"):
      timeslot = self.times[0]
    elif (check_time == "8:00"):
      timeslot = self.times[1]
    elif (check_time == "3:45"):
      timeslot = self.times[2]
    elif (check_time == "23:00"):
      timeslot = self.times[3]
    elif (check_time == "15:00"):
      timeslot = self.times[4]
    elif (check_time == "1:00"):
      timeslot = self.times[5]
    elif (check_time == "17:30"):
      timeslot = self.times[6]
    else:
      print("Invalid input")
      main()

    print(
        "--------------------------------------------------------------------------------------------"
    )

    for i in range(1, len(self.trains)):
      print(i, self.trains[i])
    self.choice = int(input("\nEnter your choice:"))
    print(
        "--------------------------------------------------------------------------------------------"
    )

    for i in range(1, len(self.classes)):
      print(i, self.classes[i])
    class_temp = int(input("\nEnter your choice of class: "))
    class_name = "none"
    if (class_temp == 1):
      class_name = "General"
    elif (class_temp == 2):
      class_name = "AC-1st tier"
    elif (class_temp == 3):
      class_name = "AC-2nd tier"
    elif (class_temp == 4):
      class_name = "AC-3rd tier"
    elif (class_temp == 5):
      class_name = "Sleeper"
    else:
      print("Invalid input")
      main()

    print(
        "--------------------------------------------------------------------------------------------"
    )
    for i in range(1, len(self.trains)):
      if (self.choice == i and age > 12):
        train = self.trains[i]
        self.train_price = 1

      elif (self.choice == i and age < 12):
        train = self.trains[i]
        self.train_price = 0.7

      elif (self.choice > len(self.trains) - 1):
        #-1 because index starts from 0 aur length 1 se start hoga
        print("\nInvalid input")
        print("redirecting to main menu in 5 seconds")
        time.sleep(5)
        main()

    if (class_temp == 1):
      self.train_price = 500 * self.train_price
    elif (class_temp == 2):
      self.train_price = 1200 * self.train_price
    elif (class_temp == 3):
      self.train_price = 1500 * self.train_price
    elif (class_temp == 4):
      self.train_price = 2500 * self.train_price
    elif (class_temp == 5):
      self.train_price = 700 * self.train_price
    train_pricez=self.train_price
    bogi_no = self.bogi[random.randint(1, len(self.bogi) - 1)]
    seat_no = random.randint(1, 50)

    print("\nYour Ticket Price is", self.train_price)
    self.confirm = input(" \n Do you want to confirm the ticket(y/n): ")
    if (self.confirm.lower() == "y"):
      print("--------------------------------------------------------")
      print("\n Ticket booked successfully")
      train_no = random.randint(10000, 99999)
      id = random.randint(100000000, 999999999)
      ticket_id = id
      print("\n Your train ", train, "\n Train no: ", train_no, "\n Source: ",
            source, "\t Destination: ", destination, "\n Bogi No:", bogi_no,
            "\tSeat No:", seat_no, "\tClass:", class_name,
            "\n Time of Depature: ", timeslot)

      print("\n Your ticket id is: ", ticket_id)
      print("--------------------------------------------------------")

    elif (self.confirm.lower() == "n"):
      print("\n Ticket not booked")
    else:
      print("Invalid choice")

    print("\nRedirecting to main menu in 5 seconds")
    time.sleep(5)
    main()

  def cancel(self):
    global train_pricez
    print("\n----------------Cancelling Ticket----------------------\n")
    self.check_ticket_id = int(input("\n Enter your ticket id: "))
    print("After cancellation 70% of the ticket price will be refunded")
    self.confirm = input(" \n Do you want to confirm the ticket(y/n): ")

    if (self.check_ticket_id == ticket_id):
      if (self.confirm.lower() == "y"):
        print("\n Ticket cancelled successfully")
        print("Amount ", train_pricez * 0.7, "will be credited to your account")
        print("\n Redirecting to main menu in 5 seconds")
        time.sleep(5)
        main()
        

      elif (self.confirm.lower() == "n"):
        print("\n Ticket not cancelled")
      else:
        print("Invalid choice")
      
      

      print("--------------------------------------------------------")
    else:
      print("\n Invalid ticket id or train no")
      print("--------------------------------------------------------")

    print("\nRedirecting to main menu in 5 seconds")
    time.sleep(5)
    main()

  def pnr(self):
    print("\n------------------Printing PNR------------------------")
    self.check_ticket_id = int(input("Enter the ticket id to check PNR: "))
    if (self.check_ticket_id == ticket_id):
      print("\n Your train ", train, "\n Train no: ", train_no, "\n Source: ",
            source, "\t Destination: ", destination, "\n Bogi No:", bogi_no,
            "\tSeat No:", seat_no, "\tClass:", class_name,
            "\n Time of Depature: ", timeslot)

    else:
      print("\nInvalid ticket id")
    print("\nRedirection to main menu in 5 seconds")
    time.sleep(5)
    main()

  def train_status(self):
    print("\n----------------Train Status----------------------\n")
    self.status = int(input("Enter the train no to check status: "))
    if (self.status == train_no
        ):
      print("\nTrain no: ", train_no, "\t Boarding place: ",
            source)
      print("\nTravelling from ", source, " to ", destination)
      print("Boarding phase on", day)
      print("time of deparure: ", timeslot)

    else:
      print("\nInvalid train no. or boarding place")
    print("\nRedirection to main menu in 5 seconds")
    time.sleep(5)
    main()

  def restroom(self):
    print("\n----------------Restroom----------------------\n")
    self.check_ticket_id = int(
        input("Enter the ticket id to check restroom: "))
    if (self.check_ticket_id == ticket_id):
      print("\n Restroom is available\n")

      print("Available Time Slots\n")
      for i in range(1, len(self.times)):
        print(self.times[i], end="\t")
      check_time = input("\nEnter the time slot: ")
      restroom_slot = "00:00"
      if (check_time == "6:15"):
        restroom_slot = self.times[0]
      elif (check_time == "8:00"):
        restroom_slot = self.times[1]
      elif (check_time == "3:45"):
        restroom_slot = self.times[2]
      elif (check_time == "23:00"):
        restroom_slot = self.times[3]
      elif (check_time == "15:00"):
        restroom_slot = self.times[4]
      elif (check_time == "1:00"):
        restroom_slot = self.times[5]
      elif (check_time == "17:30"):
        restroom_slot = self.times[6]
      else:
        print("Invalid input")
        main()
      print("\nRestroom Booked Sucessfully")

    else:
      print("\nInvalid ticket id")
    print("\nRedirection to main menu in 5 seconds")
    time.sleep(5)
    main()

  def admin(self):

    global place
    global trains
    global train_price

    print("\n---------------------Admin Window---------------------------\n")
    self.admin_pass = input("Enter the admin password: ")
    if (self.admin_pass == "r"):
      print(
          "\n1.Add Train\n2.Delete Train\n3.List Trains\n4.Add Station \n5.Delete Station \n6.List stations \n7.Exit"
      )
      self.admin_choice = int(input("\nEnter your choice: "))
      if (self.admin_choice == 1):
        self.add_train = input("Enter the train name: ")
        self.trains.append(self.add_train)
        print("\nTrain added successfully")
        self.admin()

      elif (self.admin_choice == 2):
        for i in range(1, len(self.trains)):
          print(i, self.trains[i])
        self.delete_train = int(
            input("Enter the train no. you want to delete: "))
        self.trains.pop(self.delete_train)
        print("\nTrain deleted successfully")
        self.admin()

      elif (self.admin_choice == 3):
        print("\nList of trains: ")
        for i in range(1, len(self.trains)):
          print(self.trains[i])
        self.admin()

      elif (self.admin_choice == 4):
        self.add_station = input("Enter the station name: ")

        self.place.append(self.add_station)

        print("\nStation added successfully")

        self.admin()
      elif (self.admin_choice == 5):
        for i in range(1, len(self.place)):
          print(i, self.place[i])
        self.delete_station = int(
            input("Enter the Station no. you want to delete: "))
        self.place.pop(self.delete_station)
        print("\nTrain deleted successfully")
        self.admin()

      elif (self.admin_choice == 6):
        print("\nList of Stations: ")
        for i in range(1, len(self.place)):
          print(self.place[i])
        self.admin()
      elif (self.admin_choice == 7):
        main()

    else:
      print("\nInvalid password\n")
      main()


def main():
  print()
  print("\n------------------RAILWAY RESERVATION-------------------")
  print("\nSelect the operation you want to perform:\n")
  print("1. Book Ticket \t\t\t 2. Cancel Ticket")
  print("\n3. Check PNR status  \t 4. administration")
  print(" \n5. Check Train status \t 6. Book Restroom \n\n7. Exit")
  a = (input("\nEnter your choice: "))
  s1 = user()

  if (a == "7"):
    print()
    print(
        "===================Thank you for using our services==================\n Thala for a reason\n"
    )
    time.sleep(3)

  elif (a == "1"):

    s1.book()
  elif (a == "2"):
    s1.cancel()
  elif (a == "3"):
    s1.pnr()
  elif (a == "4"):
    s1.admin()
  elif (a == "5"):
    s1.train_status()
  elif (a == "6"):
    s1.restroom()
  else:
    print("\n\n ******* Invalid input *******\n\n\n\n")
    main()


main()
