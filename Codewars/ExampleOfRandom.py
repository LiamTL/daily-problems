# Not an actual problem, but you COULD make it one... But Just credit me, K?
import random

foods = {"Soda": 3.50, "Fries": 5.75, "Chicken Sandwich": 25.50, "Corn Nuggets": 7.50, "Super Spicy Chicken Sandwich": 35.50, "Super Chicken Sandwich": 45.25, "Family Lime": 99.99, "10 Tenders": 45.99, "5 Piece": 63.50, "8 Piece": 75.99, "Kids Meal": 25.50}
ask_for_random = input("What would be your order Sir or Madame?")
print("\n".join(foods))
order = []
bill = 0
while True:
    where_muh_food = input("")
    for food in range(len(foods)):
        if where_muh_food == "That is all I would like please!" or where_muh_food == "Thanks, that is all!":
            break
        if where_muh_food in foods.keys():
            bill += foods[where_muh_food]
            order.append(f"{foods.keys()}\n")
            

    

