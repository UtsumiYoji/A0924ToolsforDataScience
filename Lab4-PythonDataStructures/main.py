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
    
    print('Average scores:')
    average_scores = {
        student: sum(scores) / len(scores)
        for student, scores in students.items()
    }
    print(average_scores)
        
    print("Highest average student:")
    key = max(average_scores, key=average_scores.get)
    print(key, average_scores[key])
    
    print("Lowest average student:")
    key = min(average_scores, key=average_scores.get)
    print(key, average_scores[key])
    
    students['Frank'] = [80, 90, 85]
    print(students)
    
    # Exercise2
    inventory = {
        "apple": (50, 0.5),
        "banana": (100, 0.2),
        "orange": (75, 0.3),
        "pear": (20, 0.4)
    }
    pprint(inventory)
    
    print("Total inventory value:")
    total_value = sum([quantity * price for quantity, price in inventory.values()])
    print(total_value)
    
    inventory['mango'] = (30, 0.6)
    inventory['banana'] = (120, 0.2)
    pprint(inventory)
    
    del inventory['pear']
    pprint(inventory)
    
    # Exercise3
    employees = [
        ("John Doe", "Accounting", "john.doe@example.com"),
        ("Jane Smith", "Marketing", "jane.smith@example.com"),
        ("Emily Davis", "HR", "emily.davis@example.com"),
        ("Michael Brown", "IT", "michael.brown@example.com")
    ]
    
    for employee in employees:
        print(employee[0], employee[1])
        
    sorted_employees = sorted(employees, key=lambda x: x[0].split()[-1])
    for employee in sorted_employees:
        print(employee[2])
        
    employees.append(("David Wilson", "Sales", "david.wilson@example.com"))
    
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
    
    for detail in library.values():
        pprint(detail)
        
    print(library["978-0-14-028329-7"])
    
    library["978-1-4028-9462-6"] = {
        "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
    
    library["978-0-7432-7356-5"]["year"] = 1961
    print(library["978-0-7432-7356-5"])
    
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

    for v in cities.values():
        print(v)

    highest_key = max(cities, key=cities.get)
    print('highest', highest_key, cities[highest_key])

    lowest_key = min(cities, key=cities.get)
    print('lowest', lowest_key, cities[lowest_key])

    cities['Philadelphia'] = 1700000
    print(cities)

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

    pprint(movies)

    highest_key = max(movies, key=lambda x: movies[x]["rating"])
    print('highest', highest_key)

    movies["The Matrix"] = {"year": 1999, "rating": 8.7, "genre": "Sci-Fi"}

    movies["Inception"]["rating"] = 9.0
    print(movies)

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

    pprint(countries)

    print(countries["Germany"])

    countries["Australia"] = "Canberra"
    print(countries)

    countries["USA"] = "New Washington"
    print(countries)

    del countries["France"]
    print(countries)
    
    # Exercise8
    cart = [
        {"item": "apple", "quantity": 3, "price_per_unit": 0.5},
        {"item": "banana", "quantity": 6, "price_per_unit": 0.2},
        {"item": "orange", "quantity": 4, "price_per_unit": 0.3},
        {"item": "pear", "quantity": 2, "price_per_unit": 0.4}
    ]
    
    pprint(cart)

    print('Total', sum([v["quantity"]*v["price_per_unit"] for v in cart]))

    cart.append({"item": "grape", "quantity": 5, "price_per_unit": 0.6})

    cart[1]["quantity"] = 10
    print(cart)

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

    for value in weather.values():
        print(value)

    highest_key = max(weather, key=lambda x: weather[x]["temperature"])
    print('highest temperature', highest_key)

    lowest_key = min(weather, key=lambda x: weather[x]["humidity"])
    print('lowest humidity', lowest_key)

    weather["Wednesday"]['temperature'] = 25
    print(weather)

    weather["Sunday"] = {"temperature": 24, "humidity": 60}
    print(weather)

    # Exercise10
    members = [
        {"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
        {"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
        {"name": "Charlie", "age": 22, "books_borrowed": ["Brave New World", "1984"]},
        {"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]}
    ]
    
    for member in members:
        print(member["name"], member["age"])
    
    for member in members:
        if member["name"] == "Charlie":
            print(member["books_borrowed"])
            break
    
    members.append({"name": "Eve", "age": 28, "books_borrowed": ["Pride and Prejudice"]})
    
    for member in members:
        if member["name"] == "Bob":
            member["age"] = 31
    print(members)
    
    for i, member in enumerate(members):
        if member["name"] == "David":
            del members[i]
            break
    print(members)


if __name__ == "__main__":
    main()