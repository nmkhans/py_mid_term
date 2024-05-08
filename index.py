class Star_Cinema:
  hall_list = []

  def __init__(self):
    pass

  def entry_hall(self, hall):
    self.hall_list.append(hall)

class User:
  def __init__(self, name, password):
    self.name = name
    self.password = password


class Hall(Star_Cinema):
  def __init__(self, rows, cols, hall_no):
    super().__init__()
    self.__rows = rows
    self.__cols = cols
    self.__hall_no = hall_no
    self.__seats = {}
    self.__show_list = []
    self.users = []

    self.entry_hall(self)

  def add_user(self, name, password):
    user = User(name, password)
    self.users.append(user)
    return user

  def entry_show(self, id, movie_name, time):
    show = (id, movie_name, time)
    self.__show_list.append(show)

    self.__seats[id] = [['free' for i in range(self.__cols)] for i in range(self.__rows)]

    print("Show has been added!")

  def book_seats(self, show_id, seat_to_book):
    if show_id in self.__seats:
      for seat in seat_to_book:
        row, col = seat

        if 1 <= row <= self.__rows and 1 <= col <= self.__cols:
          if self.__seats[show_id][row - 1][col - 1] == 'free':
            self.__seats[show_id][row - 1][col - 1] = 'booked'
            
            print(f"Your seat {row}{chr(64 + col)} has been successfully booked.")
          else:
            print(f"seat {row}{chr(64 + col)} is already booked!")
        else:
          print(f"Invalid seat no {row} {chr(64 + col)} for show with id {show_id}.")
    else:
      print(f"No show available with id {show_id}")

  def view_show_list(self):
    print("List of running shows:")

    for show_info in self.__show_list:
      print(f"id: {show_info[0]}, movie: {show_info[1]}, time: {show_info[2]}")

  def view_available_seats(self, id):
    if id in self.__seats:
      print(f"Available seats for show with id {id}:")

      for row in range(self.__rows):
        for col in range(self.__cols):
          if self.__seats[id][row][col] == 'free':
            print(f"row {row + 1}, seat {chr(65 + col)}")
    else:
      print(f"show with id {id} does not exist.")

hall = Hall(10, 10, 1)
admin = hall.add_user("admin", "admin")
moin = hall.add_user("moin", "123")

current_user = None

while True:
  if current_user == None:
    print("\nNo user logged!")
    option = input("Login or Register (L/R): ")

    if option == "L":
      print("\nWelcome to login.")
      name = input("Enter your name: ")
      password = input("Enter your password: ")

      for user in hall.users:
        if user.name == name:
          if user.password == password:
            current_user = user
            print("Login successfull")
            break
          else:
            print("Invalid password!")

      if current_user == None:
        print(f"No user found named {name}")

    elif option == "R":
      print("\nWelcome to register.")
      name = input("Enter your name: ")
      password = input("Enter your password: ")
      
      user = hall.add_user(name, password)
      current_user = user
      print("Registration successfull")

  elif current_user.name == "admin":
    print(f"\nWelcome to hall dear {current_user.name}")
    print("Select a option from below: ")
    print("1. Entry show")
    print("2. Book seats")
    print("3. View show list")
    print("4. View available seats")
    print("5. Logout")

    option = int(input("Enter a option: "))

    if option == 1:
      id = input("Enter a id: ")
      movie_name = input("Enter movie name: ")
      time = input("Enter movie time: ")

      hall.entry_show(id, movie_name, time)
    elif option == 2:
      seats_to_book_list = []
      id = input("Enter a id: ")
      seats_to_book = int(input("Enter seats number to book: "))

      for i in range(seats_to_book):
        one = int(input("Enter seat one"))
        two = int(input("Enter seat two"))
        seats_to_book_list.append((one, two))
      
      hall.book_seats(id, seats_to_book_list)
    elif option == 3:
      hall.view_show_list()
    elif option == 4:
      id = input("Enter a show id: ")
      hall.view_available_seats(id)
    elif option == 5:
      current_user = None

  else:
    print(f"\nWelcome to hall dear {current_user.name}")
    print("Select a option from below: ")
    print("1. Book seats")
    print("2. View show list")
    print("3. View available seats")
    print("4. Logout")

    option = int(input("Enter a option: "))

    if option == 1:
      seats_to_book_list = []
      id = input("Enter a id: ")
      seats_to_book = int(input("Enter seats number to book: "))

      for i in range(seats_to_book):
        one = int(input("Enter seat one"))
        two = int(input("Enter seat two"))
        seats_to_book_list.append((one, two))
      
      hall.book_seats(id, seats_to_book_list)
    elif option == 2:
      hall.view_show_list()
    elif option == 3:
      id = input("Enter a show id: ")
      hall.view_available_seats(id)
    elif option == 4:
      current_user = None
