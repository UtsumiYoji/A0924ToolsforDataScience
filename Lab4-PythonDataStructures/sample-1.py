from pprint import pprint

def main():
    # Exercise1
    students = {
        "Alice": [85, 78, 92],
        "Bob": [79, 74, 81],
        "Charlie": [91, 82, 85],
        "David": [76, 85, 83],
        "Eve": [88, 79, 92]
    }
    
    # 1. Calculate and print the average score for each student.
    for key, value in students.items():
        avg = sum(key) / len(value)
        print(key, avg)
    
    # 2. Find and print the name of the student with the highest average score.
    max_avg = 0
    for key, value in students.items():
        avg = sum(key) / len(value)
        if avg > max_avg:
            max_avg = avg
            max_student = key
    print('highest', max_student, max_avg)
    
    # 3. Find and print the name of the student with the lowest average score.
    min_avg = float('inf')
    for key, value in students.items():
        avg = sum(key) / len(value)
        if avg < min_avg:
            min_avg = avg
            min_student = key
    print('lowest', min_student, min_avg)
    
    # 4. Add a new student named Frank with the following scores: 80, 90, 85.
    students["Frank"] = [80, 90, 85]
    
    print(students)
    
    print()
    # Exercise2
    inventory = {
        "apple": (50, 0.5),
        "banana": (100, 0.2),
        "orange": (75, 0.3),
        "pear": (20, 0.4)
    }
    
    # 1. Print the inventory dictionary.
    pprint(inventory)
    
    # 2. Calculate and print the total value of the inventory.
    print("Total inventory value:")
    total = 0
    for value in inventory.values():
        total += (value[0] * value[1])
        # total = total + (value[0] * value[1])
    print(total)
    
    # 3. Update the quantity of "banana" to 120 and print the updated inventory.
    inventory["banana"] = (120, 0.2)
    pprint(inventory)
    
    # 4. Remove "pear" from the inventory and print the updated inventory.
    del inventory["pear"]
    inventory.pop("pear") # return (20, 0.4)
    pprint(inventory)
    
    print()
    # Exercise3
    employees = [
        ("John Doe", "Accounting", "john.doe@example.com"),
        ("Jane Smith", "Marketing", "jane.smith@example.com"),
        ("Emily Davis", "HR", "emily.davis@example.com"),
        ("Michael Brown", "IT", "michael.brown@example.com")
    ]
    
    # 1. Print the names and departments of all employees.
    for employee in employees:
        print(employee[0], employee[1])
        
    # 2. Print the email addresses of all employees in alphabetical order by their last names.
    new_employees = []
    for employee in employees:
        last_name = employee[0].split()[1]
        new_employees.append((last_name, employee[2]))
    # {
    #     ("Doe", "john.doe@example.com"),
    #     ("Smith", "jane.smith@example.com"),
    # }
    sorted_employees = sorted(new_employees)
    for employee in sorted_employees:
        print(employee[1])
    
    # 3. Add a new employee ("David Wilson", "Sales", "david.wilson@example.com")
    employees.append(("David Wilson", "Sales", "david.wilson@example.com"))
    
    # 4. Find and print the department of "Jane Smith".
    for employee in employees:
        if employee[0] == "Jane Smith":
            print(employee[1])
            break
    
    print()    
    # Exercise4
    library = {
        "978-3-16-148410-0": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
        "978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
        "978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
        "978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
    }
    
    # 1. Print the details of all books in a user-friendly format.
    for detail in library.values():
        pprint(detail)
        
    # 2. Find and print the details of the book with the ISBN "978-0-14-028329-7".
    print(library["978-0-14-028329-7"])
    
    # 3. Add a new book with ISBN "978-1-4028-9462-6", title "The Great Gatsby", author "F. Scott Fitzgerald", and year 1925.
    library["978-1-4028-9462-6"] = {
        "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
    
    # 4. Update the year of "To Kill a Mockingbird" to 1961
    for v in library.values():
        if v["title"] == "To Kill a Mockingbird":
            v["year"] = 1961
            break
    
    # 5. Remove the book with ISBN "978-0-452-28423-4"
    del library["978-0-452-28423-4"]
    print(library)

    print()
    # Exercise5
    cities = {
        "New York": 8419000,
        "Los Angeles": 3980000,
        "Chicago": 2716000,
        "Houston": 2328000,
        "Phoenix": 1690000
    }

    # 1. Print the population of each city in a user-friendly format.
    for v in cities.values():
        print(v)

    # 2. Find and print the city with the highest population.
    max_pop = 0
    for city, pop in cities.items():
        if pop > max_pop:
            max_pop = pop
            max_city = city
    print('highest', max_city, max_pop)

    # 3. Find and print the city with the lowest population.
    min_pop = float('inf')
    for city, pop in cities.items():
        if pop < min_pop:
            min_pop = pop
            min_city = city
    print('lowest', min_city, min_pop)

    # 4. Update the population of "Phoenix" to 1700000 and print the updated data.
    cities['Philadelphia'] = 1700000
    print(cities)

    # 5. Add a new city "San Francisco" with a population of 884000 and print the updated data.
    cities['San Francisco'] = 884000
    print(cities)
    
    print()
    # Exercise6
    movies = {
        "Inception": {"year": 2010, "rating": 8.8, "genre": "Sci-Fi"},
        "The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"},
        "The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"},
        "Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
        "Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}
    }

    # 1. Print the details of all movies in a user-friendly format.
    pprint(movies)

    # 2. Find and print the highest-rated movie.
    max_rate = 0
    for movie, detail in movies.items():
        if detail["rating"] > max_rate:
            max_rate = detail["rating"]
            max_movie = movie
    print('highest', max_movie, max_rate)

    # 3. Add a new movie "The Matrix" with year 1999, rating 8.7, and genre "Sci-Fi" to the database.
    movies["The Matrix"] = {"year": 1999, "rating": 8.7, "genre": "Sci-Fi"}

    # 4. Update the rating of "Inception" to 9.0 and print the updated details.
    movies["Inception"]["rating"] = 9.0
    print(movies)

    # 5. Remove "Pulp Fiction" from the database and print the updated list.
    del movies["Pulp Fiction"]
    print(movies)

    print()
    # Exercise7
    countries = {
        "USA": "Washington, D.C.",
        "Canada": "Ottawa",
        "France": "Paris",
        "Germany": "Berlin",
        "Japan": "Tokyo"
    }

    # 1. Print the names of all countries and their capitals.
    pprint(countries)

    # 2. Find and print the capital of Germany.
    print(countries["Germany"])

    # 3. Add a new country "Australia" with capital "Canberra" to the dictionary and print the updated dictionary.
    countries["Australia"] = "Canberra"
    print(countries)

    # 4. Update the capital of "USA" to "New Washington" and print the updated dictionary.
    countries["USA"] = "New Washington"
    print(countries)

    # 5. Remove "France" from the dictionary and print the updated dictionary.
    del countries["France"]
    print(countries)
    
    print()
    # Exercise8
    cart = [
        {"item": "apple", "quantity": 3, "price_per_unit": 0.5},
        {"item": "banana", "quantity": 6, "price_per_unit": 0.2},
        {"item": "orange", "quantity": 4, "price_per_unit": 0.3},
        {"item": "pear", "quantity": 2, "price_per_unit": 0.4}
    ]
    
    # 1. Print the details of all items in the cart.
    pprint(cart)

    # 2. Calculate and print the total cost of the cart.
    total = 0
    for item in cart:
        total += (item["quantity"] * item["price_per_unit"])

    # 3. Add a new item "grape" with quantity 5 and price per unit 0.6 to the cart.
    cart.append({"item": "grape", "quantity": 5, "price_per_unit": 0.6})

    # 4. Update the quantity of "banana" to 10 and print the updated cart.
    cart[1]["quantity"] = 10
    print(cart)

    # 5. Remove "pear" from the cart and print the updated cart.
    for item in cart:
        if item["item"] == "pear":
            cart.remove(item)
            break
    print(cart)
    
    print()
    # Exercise9
    weather = {
        "Monday": {"temperature": 20, "humidity": 60},
        "Tuesday": {"temperature": 22, "humidity": 55},
        "Wednesday": {"temperature": 19, "humidity": 65},
        "Thursday": {"temperature": 23, "humidity": 50},
        "Friday": {"temperature": 21, "humidity": 70}
    }

    # 1. Print the weather details for each day.
    for value in weather.values():
        print(value)

    # 2. Find and print the day with the highest temperature.
    max_temp = 0
    for day, detail in weather.items():
        if detail["temperature"] > max_temp:
            max_temp = detail["temperature"]
            max_day = day
    print('highest temperature', max_day, max_temp)

    # 3. Find and print the day with the lowest humidity.
    min_hum = float('inf')
    for day, detail in weather.items():
        if detail["humidity"] < min_hum:
            min_hum = detail["humidity"]
            min_day = day
    print('lowest humidity', min_day, min_hum)

    # 4. Update the temperature of "Wednesday" to 25 and print the updated weather data.
    weather["Wednesday"]['temperature'] = 25
    print(weather)

    # 5. Add weather data for "Saturday" with temperature 24 and humidity 60 to the dictionary
    weather["Sunday"] = {"temperature": 24, "humidity": 60}
    print(weather)

    print()
    # Exercise10
    members = [
        {"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
        {"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
        {"name": "Charlie", "age": 22, "books_borrowed": ["Brave New World", "1984"]},
        {"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]}
    ]
    
    # 1. Print the names and ages of all members.
    for member in members:
        print(member["name"], member["age"])
    
    # 2. Find and print the books borrowed by "Charlie".
    for member in members:
        if member["name"] == "Charlie":
            print(member["books_borrowed"])
            break
    
    # 3. Add a new member "Eve" with age 28 and books borrowed ["Pride and Prejudice"] to the list.
    members.append({"name": "Eve", "age": 28, "books_borrowed": ["Pride and Prejudice"]})
    
    # 4. Update the age of "Bob" to 31 and print the updated list.
    for member in members:
        if member["name"] == "Bob":
            member["age"] = 31
            break
    print(members)
    
    # 5. Remove "David" from the list and print the updated list.
    for member in members:
        if member["name"] == "David":
            members.remove(member)
            break
    print(members)


if __name__ == "__main__":
    main()