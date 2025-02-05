if __name__ == "__main__":
    name = input("Hello What Is Your Name? ")

    year_now = int(input("What Year Is It Today? "))
    year_born = int(input("And What Year Were You Born? "))

    age = year_now - year_born

    print (f"Hello, {name}. It Is Good To Meet You. This Year, You Will Be {age} Years Old.")