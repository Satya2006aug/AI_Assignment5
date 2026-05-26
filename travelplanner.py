# simple knowledge base

travel_data = {

    "Paris": {

        "places": [
            "Eiffel Tower",
            "Louvre Museum",
            "Notre Dame"
        ],

        "food": [
            "Croissant",
            "Macarons",
            "French Onion Soup"
        ],

        "budget": 150
    },

    "Tokyo": {

        "places": [
            "Tokyo Tower",
            "Shibuya",
            "Sensoji Temple"
        ],

        "food": [
            "Sushi",
            "Ramen",
            "Tempura"
        ],

        "budget": 120
    },

    "Delhi": {

        "places": [
            "India Gate",
            "Red Fort",
            "Qutub Minar"
        ],

        "food": [
            "Biryani",
            "Butter Chicken",
            "Chole Bhature"
        ],

        "budget": 70
    }
}


# function for plan

def generate_plan(city, days):

    if city not in travel_data:

        print("city not found")
        return

    data = travel_data[city]

    total = data["budget"] * days

    print("\nTravel Plan for", city)

    print("\nTourist Places:")

    for p in data["places"]:
        print("-", p)

    print("\nFood Recommendations:")

    for f in data["food"]:
        print("-", f)

    print("\nEstimated Cost =", total)


city = input("enter city: ")
days = int(input("enter days: "))

generate_plan(city, days)
