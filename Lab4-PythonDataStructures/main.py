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
    print('Average scores:')
    average_scores = {
        student: sum(scores) / len(scores)
        for student, scores in students.items()
    }
    print(average_scores)
    
    # 2. Find and print the name of the student with the highest average score.
    print("Highest average student:")
    key = max(average_scores, key=average_scores.get)
    print(key, average_scores[key])
    
    # 3. Find and print the name of the student with the lowest average score.
    print("Lowest average student:")
    key = min(average_scores, key=average_scores.get)
    print(key, average_scores[key])
    
    # 4. Add a new student named Frank with the following scores: 80, 90, 85.
    students['Frank'] = [80, 90, 85]
    print(students)
    
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
    total_value = sum([quantity * price for quantity, price in inventory.values()])
    print(total_value)
    
    # 3. Update the quantity of "banana" to 120 and print the updated inventory.
    inventory['mango'] = (30, 0.6)
    inventory['banana'] = (120, 0.2)
    pprint(inventory)
    
    # 4. Remove "pear" from the inventory and print the updated inventory.
    del inventory['pear']
    pprint(inventory)
    
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
    sorted_employees = sorted(employees, key=lambda x: x[0].split()[-1])
    for employee in sorted_employees:
        print(employee[2])
        
    # 3. Add a new employee ("David Wilson", "Sales", "david.wilson@example.com")
    employees.append(("David Wilson", "Sales", "david.wilson@example.com"))
    
    # 4. Find and print the department of "Jane Smith".
    for employee in employees:
        if employee[0] == "Jane Smith":
            print(employee[1])
            
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
    library["978-0-7432-7356-5"]["year"] = 1961
    print(library["978-0-7432-7356-5"])
    
    # 5. Remove the book with ISBN "978-0-452-28423-4"
    del library["978-0-452-28423-4"]
    print(library)

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
    highest_key = max(cities, key=cities.get)
    print('highest', highest_key, cities[highest_key])

    # 3. Find and print the city with the lowest population.
    lowest_key = min(cities, key=cities.get)
    print('lowest', lowest_key, cities[lowest_key])

    # 4. Update the population of "Phoenix" to 1700000 and print the updated data.
    cities['Philadelphia'] = 1700000
    print(cities)

    # 5. Add a new city "San Francisco" with a population of 884000 and print the updated data.
    cities['San Francisco'] = 884000
    print(cities)
    
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
    highest_key = max(movies, key=lambda x: movies[x]["rating"])
    print('highest', highest_key)

    # 3. Add a new movie "The Matrix" with year 1999, rating 8.7, and genre "Sci-Fi" to the database.
    movies["The Matrix"] = {"year": 1999, "rating": 8.7, "genre": "Sci-Fi"}

    # 4. Update the rating of "Inception" to 9.0 and print the updated details.
    movies["Inception"]["rating"] = 9.0
    print(movies)

    # 5. Remove "Pulp Fiction" from the database and print the updated list.
    del movies["Pulp Fiction"]
    print(movies)

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
    print('Total', sum([v["quantity"]*v["price_per_unit"] for v in cart]))

    # 3. Add a new item "grape" with quantity 5 and price per unit 0.6 to the cart.
    cart.append({"item": "grape", "quantity": 5, "price_per_unit": 0.6})

    # 4. Update the quantity of "banana" to 10 and print the updated cart.
    cart[1]["quantity"] = 10
    print(cart)

    # 5. Remove "pear" from the cart and print the updated cart.
    for i, detail in enumerate(cart):
        if detail["item"] == "pear":
            break
    del cart[i]
    print(cart)
    
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
    highest_key = max(weather, key=lambda x: weather[x]["temperature"])
    print('highest temperature', highest_key)

    # 3. Find and print the day with the lowest humidity.
    lowest_key = min(weather, key=lambda x: weather[x]["humidity"])
    print('lowest humidity', lowest_key)

    # 4. Update the temperature of "Wednesday" to 25 and print the updated weather data.
    weather["Wednesday"]['temperature'] = 25
    print(weather)

    # 5. Add weather data for "Saturday" with temperature 24 and humidity 60 to the dictionary
    weather["Sunday"] = {"temperature": 24, "humidity": 60}
    print(weather)

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
    print(members)
    
    # 5. Remove "David" from the list and print the updated list.
    for i, member in enumerate(members):
        if member["name"] == "David":
            del members[i]
            break
    print(members)


if __name__ == "__main__":
    main()