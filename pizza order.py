import pyautogui as pt
import time


def pizza_order():
    order = pt.confirm(title="Pizza order", text="Do you want to place a pizza order?", buttons=["Yes", "No"])
    if order == "Yes":
        topping = pt.confirm(title="Pizza order", text="What pizza toppings do you want?", buttons=["Pepperoni",
                                                                                                    "Mushrooms",
                                                                                                    "Green Peppers"])
        if topping == [0] or [1] or [2]:
            crust = pt.confirm(title="Pizza order", text="What pizza crust do you want?", buttons=["Thin Crust",
                                                                                                   "Thick Crust",
                                                                                                   "Stuffed Crust"])
            if crust == [0] or [1] or [2]:
                size = pt.confirm(title="Pizza order", text="What size of pizza do you want?", buttons=["Small",
                                                                                                        "Medium",
                                                                                                        "Large"])
                if size == [0] or [1] or [2]:
                    pt.prompt(title="Pizza order", text="Put the address you want the pizza to be delivered")
                    pt.alert(title="Pizza order", text="Your order was successful")
    if order == "No":
        pt.alert(title="Pizza order", text="You didn't order :(")


pizza_order()
