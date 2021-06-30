import json
import sqlite3
import pandas as pd
from tabulate import tabulate
import requests
from flask import Flask, jsonify
import csv
cnx_lite = sqlite3.connect("TP3.0.db")
cursor_lite = cnx_lite.cursor()

# df = pd.read_csv("Menu.csv")
# df.rename(columns={"ID": "id", "Name":"name", "TYPE" : "type", "Total beef g" : "total_beef_grms",
# "Total ml": "total_ml","Topping1":"topping_1", "Topping2": "topping_2", "Topping3":"topping_3",
#  "Topping4":"topping_4", "Price" : "price"}, inplace=True)
# df.to_sql("Menu", cnx_lite, if_exists='append', index=False)

df = pd.read_sql('SELECT * FROM Menu', cnx_lite)
print(df.index)
df.drop(["id"], axis="columns", inplace=True)

elegir_ham = 100
elegir_ham_1 = 100
elegir_pollo = 100
elegir_pollo_1 = 100
elegir_tomar = 100
elegir_tomar_1 = 100
elegir_papas = 100
elegir_papas_1 = 100
elegir_extra = 100
elegir_extra_1 = 100
total_1 = 0
total_ham = 0
total_tom = 0
total_top = 0
total_chk = 0
total_sds = 0
subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
elegir_mas = 0

nombr = str(input("Insert name:\n"))
apellido = str(input("insert last name:\n"))
while True:
    try:
        age = int(input("how old are you?:\n"))
        break
    except ValueError:
        print("ingrese un valor valido")



food_typ = int(input("what type of food do you want? type: \n 1 for burgers \n 2 for fried chicken \n 3 for sides"
                       "\n 4 for beverages \n 5 for extra toppings\n"))
try:
    class Hamburguesa:
        def __init__(self, name, total_beef_g, topping1, topping2, topping3, topping4):
            self.name = name
            self.total_beef_g = total_beef_g
            self.topping1 = topping1
            self.topping2 = topping2
            self.topping3 = topping3
            self.topping4 = topping4

        def __str__(self):
            return 'Your burger is a {}, its weight is {} g, and it has, topping 1 = {}, topping 2 = {}, topping 3 = {}, topping 4 = {}'.format(
                self.name, self.total_beef_g, self.topping1, self.topping2, self.topping3, self.topping4)


    # POO CHICKEN
    class Chicken:
        def __init__(self, name, amount):
            self.name = name
            self.amount = amount

        def __str__(self):
            return 'You chose {}, whith {} pices'.format(self.name, self.amount)


    # POO PAPAS
    class Papas_comunes:
        __tipoPapas = 'Papas solas con sal'

        def queTienePapas(self):
            return self.__tipoPapas
    tusPapas = Papas_comunes()


    class Papas_cheddar:
        __tipoPapas = 'Papas con cheddar y sal'

        def queTienePapas(self):
            return self.__tipoPapas
    tusPapas1 = Papas_cheddar()


    class Papas_chebacon:
        __tipoPapas = 'Papas con cheddar, bacon y sal'
        def queTienePapas(self):
            return self.__tipoPapas
    tusPapas2 = Papas_chebacon()


    # POO BEBIDAS
    class Bebidas:
        def __init__(self, name, total_ml):
            self.name = name
            self.total_ml = total_ml

        def __str__(self):
            return 'Your drink is a {}, and has {} ml'.format(self.name, self.total_ml)

        def abrir(self):
            print('Open your drink')


    class Lata(Bebidas):
        def __init__(self, name, total_ml, azucar):
            super().__init__(name, total_ml)
            self.azucar = azucar

        def __str__(self):
            agrego = ', it has {} of sugar'.format(self.azucar)
            return super().__str__() + agrego

        def abrir(self):
            print('Must pull the metal ring on the top part of the can, to open')


    class Plastico(Bebidas):
        def __init__(self, name, total_ml, gas, tamano):
            super().__init__(name, total_ml)
            self.gas = gas
            self.tamano = tamano
        def __str__(self):
            agrego = ', {}, and is {} size'.format(self.gas, self.tamano)
            return super().__str__() + agrego
        def abrir(self):
            print('Must turn right, the plastic cap on the top part of the bottle, to open')


    # POO EXTRAS
    class Extras:
        def __init__(self, name, forwhat):
            self.name = name
            self.forwhat = forwhat
        def __str__(self):
            return 'The extra you choose is {}, it is for the {}'.format(self.name, self.forwhat)


    class Vegan(Extras):
        def __init__(self, name, forwhat, type):
            super().__init__(name, forwhat)
            self.type = type
        def __str__(self):
            agrego = ', it comes from {}'.format(self.type)
            return super().__str__() + agrego

    class Vegetarian(Extras):
        def __init__(self, name, forwhat, whatanimal):
            super().__init__(name, forwhat)
            self.whatanimal = whatanimal
        def __str__(self):
            agrego = ', as not being vegan it comes from animal, but is not meat, it is from {}'.format(self.whatanimal)
            return super().__str__() + agrego

    class Meat(Extras):
        def __init__(self, name, forwhat, typeofmeat):
            super().__init__(name, forwhat)
            self.typeofmeat = typeofmeat
        def __str__(self):
            agrego = ', this extra comes from {} type of meat'.format(self.typeofmeat)
            return super().__str__() + agrego

    if food_typ == 1:
        headers = ["nro", "name", "type", "total_beef_grms", "topping1", "topping2", "topping3", "topping4",
                   "price"]
        df.drop(["total_ml"], axis="columns", inplace=True)
        print(tabulate(df.iloc[0:10], headers, tablefmt="fancy_grid"))
        elegir_ham = float(input("which burger do you want? type nro: \n"))

        if elegir_ham == 0:
            cantidad_ham = float(input("how many do you want?\n"))
            tuHamburguesa0 = Hamburguesa('plain cheeseburger', 250, 'cheese', 'onion', 'none', 'none')
            print(str(tuHamburguesa0))
            elegir_mas = str(input("ger, do you want anything else? "
                                   "(type yes or no)\n"))
            total_1 = df.iloc[0, 7] * cantidad_ham
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":

                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham == 1:
            cantidad_ham = float(input("how many do you want?\n"))
            tuHamburguesa1 = Hamburguesa('plain bacon cheeseburger', 250, 'bacon', 'cheese', 'onion', 'none')
            print(str(tuHamburguesa1))
            elegir_mas = str(input("eseburger, do you want anything else? "
                                   "(type yes or no)\n"))

            total_1 = df.iloc[1, 7] * cantidad_ham
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham == 2:
            cantidad_ham = float(input("how many do you want?\n"))
            tuHamburguesa2 = Hamburguesa('plain veggie', 250, 'lettuce', 'tomato', 'onion', 'pickles')
            print(str(tuHamburguesa2))
            elegir_mas = str(input("o you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[2, 7] * cantidad_ham
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham == 3:
            cantidad_ham = float(input("how many do you want?\n"))
            tuHamburguesa3 = Hamburguesa('double cheeseburger', 350, 'cheese', 'onion', 'none', 'none')
            print(str(tuHamburguesa3))
            elegir_mas = str(input("rger, do you want anything else? "
                                   "(type yes or no)\n"))
            total_1 = df.iloc[3, 7] * cantidad_ham
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham == 4:
            cantidad_ham = float(input("how many do you want?\n"))
            tuHamburguesa4 = Hamburguesa('double bacon cheeseburger', 350, 'bacon', 'cheese', 'onion', 'none')
            print(str(tuHamburguesa4))
            elegir_mas = str(input("eeseburger, do you want anything else? "
                                   "(type yes or no)\n"))
            total_1 = df.iloc[4, 7] * cantidad_ham
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham == 5:
            cantidad_ham = float(input("how many do you want?\n"))
            tuHamburguesa5 = Hamburguesa('double veggie', 350, 'lettuce', 'tomato', 'onion', 'pickles')
            print(str(tuHamburguesa5))
            elegir_mas = str(input("do you want anything else? "
                                   "(type yes or no)\n"))
            total_1 = df.iloc[5, 7] * cantidad_ham
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham == 6:
            cantidad_ham = float(input("how many do you want?\n"))
            tuHamburguesa6 = Hamburguesa('triple cheeseburger', 450, 'cheese', 'onion', 'none', 'none')
            print(str(tuHamburguesa6))
            elegir_mas = str(input("rger, do you want anything else? "
                                   "(type yes or no)\n"))
            total_1 = df.iloc[6, 7] * cantidad_ham
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham == 7:
            cantidad_ham = float(input("how many do you want?\n"))
            tuHamburguesa7 = Hamburguesa('triple bacon cheeseburger', 450, 'bacon', 'cheese', 'onion', 'none')
            print(str(tuHamburguesa7))
            elegir_mas = str(input("eeseburger, do you want anything else? "
                                   "(type yes or no)\n"))
            total_1 = df.iloc[7, 7] * cantidad_ham
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham == 8:
            cantidad_ham = float(input("how many do you want?\n"))
            tuHamburguesa8 = Hamburguesa('triple bacon-egg cheese burger', 450, 'egg', 'bacon', 'cheese', 'onion')
            print(str(tuHamburguesa8))
            elegir_mas = str(input("g cheeseburger, do you want anything else? "
                                   "(type yes or no)\n"))
            total_1 = df.iloc[8, 7] * cantidad_ham
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham == 9:
            cantidad_ham = float(input("how many do you want?\n"))
            tuHamburguesa9 = Hamburguesa('5.0 bacon cheese burger', 600, 'bacon', 'cheese', 'onion', 'none')
            print(str(tuHamburguesa9))
            elegir_mas = str(input("you chose the 5.0 bacon cheeseburger, do you want anything else?(type yes or no)\n"))
            total_1 = df.iloc[9, 7] * cantidad_ham
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        else:
            elegir_mas = print("por favor siga las intrucciones")
            print("please type a valid number")
    elif food_typ == 2:
        headers_2 = ["nro", "name", "type", "price"]
        df.drop(["total_beef_grms", "total_ml", "topping_1", "topping_2", "topping_3", "topping_4"],
                axis="columns", inplace=True)
        print(tabulate(df.iloc[31:34], headers_2, tablefmt="fancy_grid"))
        elegir_pollo = float(input("which chicken do you want? type nro: \n"))
        if elegir_pollo == 31:
            cantidad_pollo = float(input("how many do you want?\n"))
            tuChicken = Chicken('fried chicken', '4')
            print(str(tuChicken))
            elegir_mas = str(input("you chose 4 pieces of fried chicken, do you want anything else? "
                                   "(type yes or no)\n"))
            total_1 = df.iloc[31, 2] * cantidad_pollo
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_pollo == 32:
            cantidad_pollo = float(input("how many do you want?\n"))
            tuChicken1 = Chicken('fried chicken', '3')
            print(str(tuChicken1))
            elegir_mas = str(input("you chose 3 pieces of fried chicken, do you want anything else? ("
                                   "type yes or no)\n"))
            total_1 = df.iloc[32, 2] * cantidad_pollo
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_pollo == 33:
            cantidad_pollo = float(input("how many do you want?\n"))
            tuChicken2 = Chicken('fried chicken', '2')
            print(str(tuChicken2))
            elegir_mas = str(input("you chose 2 pieces of fried chicken, do you want anything else? "
                                   "(type yes or no)\n"))
            total_1 = df.iloc[33, 2] * cantidad_pollo
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        else:
            elegir_mas = print("por favor siga las instrucciones")
            print("please type a valid number")
    elif food_typ == 3:
        headers_3 = ["nro", "name", "type", "price"]
        df.drop(["total_beef_grms", "total_ml", "topping_1", "topping_2", "topping_3", "topping_4"],
                axis="columns", inplace=True)
        print(tabulate(df.iloc[28:31], headers_3, tablefmt="fancy_grid"))
        elegir_papas = float(input("which french fires do you want? type nro: \n"))
        if elegir_papas == 28:
            cantidad_papas = float(input("how many do you want?\n"))
            print('Tus papas son: ', tusPapas.queTienePapas())
            elegir_mas = str(input("you chose un cono de papas, do you want anything else? (type yes or no)\n"))
            if elegir_mas == "yes":
                total_1 = df.iloc[28, 2] * cantidad_papas
                print("current total:", total_1)
            elif elegir_mas == "no":
                total_1 = df.iloc[28, 2] * cantidad_papas
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_papas == 29:
            cantidad_papas = float(input("how many do you want?\n"))
            print('Tus papas son: ', tusPapas1.queTienePapas())
            elegir_mas = str(input("you chose un cono de papas con cheddar, do you want anything else? "
                                   "(type yes or no)\n"))
            if elegir_mas == "yes":
                total_1 = df.iloc[29, 2] * cantidad_papas
                print("current total:", total_1)
            elif elegir_mas == "no":
                total_1 = df.iloc[29, 2] * cantidad_papas
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_papas == 30:
            cantidad_papas = float(input("how many do you want?\n"))
            print('Tus papas son: ', tusPapas2.queTienePapas())
            elegir_mas = str(input("you chose un cono de papas con panceta y cheddar, do you want anything else? "
                                   "(type yes or no)\n"))
            if elegir_mas == "yes":
                total_1 = df.iloc[30, 2] * cantidad_papas
                print("current total:", total_1)
            elif elegir_mas == "no":
                total_1 = df.iloc[30, 2] * cantidad_papas
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        else:
            elegir_mas = print("por favor siga las instrucciones")
            print("please type a valid number")
    elif food_typ == 4:
        headers_4 = ["nro", "name", "type", "total_ml", "price"]
        df.drop(["total_beef_grms", "topping_1", "topping_2", "topping_3", "topping_4"],
                axis="columns", inplace=True)
        print(tabulate(df.iloc[10:28], headers_4, tablefmt="fancy_grid"))
        elegir_tomar = float(input("which beverage do you want? type nro: \n"))
        if elegir_tomar == 10:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuLata = Lata('coca', 500, 'lots')
            print(str(tuLata))
            tuLata.abrir()
            elegir_mas = str(input("nt anything else? (type yes or no)\n"))
            total_1 = df.iloc[10, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 11:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuLata1 = Lata('coca zero', 500, 'none')
            print(str(tuLata1))
            tuLata1.abrir()
            elegir_mas = str(input("do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[11, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 12:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuLata2 = Lata('coca light', 500, 'very little')
            print(str(tuLata2))
            tuLata2.abrir()
            elegir_mas = str(
                input("do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[12, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 13:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuLata3 = Lata('sprite', 500, 'lots')
            print(str(tuLata3))
            tuLata3.abrir()
            elegir_mas = str(
                input("do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[13, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 14:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuLata4 = Lata('sprite zero', 500, 'none')
            print(str(tuLata4))
            tuLata4.abrir()
            elegir_mas = str(
                input(" you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[14, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 15:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuLata5 = Lata('fanta', 500, 'lots')
            print(str(tuLata5))
            tuLata5.abrir()
            elegir_mas = str(
                input("ant anything else? (type yes or no)\n"))
            total_1 = df.iloc[15, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 16:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuLata6 = Lata('fanta zero', 500, 'none')
            print(str(tuLata6))
            tuLata6.abrir()
            elegir_mas = str(
                input("you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[16, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 17:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuPlastico = Plastico('agua', 500, 'none gas', 'small')
            print(str(tuPlastico))
            tuPlastico.abrir()
            elegir_mas = str(
                input("you chose un agua, do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[17, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 18:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuPlastico1 = Plastico('agua con gas', 500, 'it has gas', 'small')
            print(str(tuPlastico1))
            tuPlastico1.abrir()
            elegir_mas = str(
                input("you chose un agua con gas, do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[18, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 19:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuLata7 = Lata('cerveza heineken', 500, 'some')
            print(str(tuLata7))
            tuLata7.abrir()
            elegir_mas = str(
                input("n, do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[19, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 20:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuPlastico2 = Plastico('coca grande', 2250, 'it has gas', 'big')
            print(str(tuPlastico2))
            tuPlastico2.abrir()
            elegir_mas = str(
                input(" you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[20, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 21:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuPlastico3 = Plastico('coca zero grande', 2250, 'it has gas', 'big')
            print(str(tuPlastico3))
            tuPlastico3.abrir()
            elegir_mas = str(
                input("e, do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[21, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 22:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuPlastico4 = Plastico('sprite grande', 2250, 'it has gas', 'big')
            print(str(tuPlastico4))
            tuPlastico4.abrir()
            elegir_mas = str(
                input("do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[22, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 23:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuPlastico5 = Plastico('sprite zero grande', 2250, 'it has gas', 'big')
            print(str(tuPlastico5))
            tuPlastico5.abrir()
            elegir_mas = str(
                input("nde, do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[23, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 24:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuPlastico6 = Plastico('fanta zero grande', 2250, 'it has gas', 'big')
            print(str(tuPlastico6))
            tuPlastico6.abrir()
            elegir_mas = str(
                input("de, do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[24, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 25:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuPlastico7 = Plastico('fanta grande', 2250, 'it has gas', 'big')
            print(str(tuPlastico7))
            tuPlastico7.abrir()
            elegir_mas = str(
                input("o you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[25, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 26:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuPlastico8 = Plastico('agua con gas grande', 2000, 'it has no gas', 'big')
            print(str(tuPlastico8))
            tuPlastico8.abrir()
            elegir_mas = str(
                input("you chose un agua con gas grande, do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[26, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar == 27:
            cantidad_tomar = float(input("how many do you want?\n"))
            tuPlastico9 = Plastico('agua grande', 2000, 'it has no gas', 'big')
            print(str(tuPlastico9))
            tuPlastico9.abrir()
            elegir_mas = str(input("you chose un agua grande, do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[27, 3] * cantidad_tomar
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        else:
            elegir_mas = print("por favor siga las instrucciones")
            print("please type a valid number")
    elif food_typ == 5:
        headers_5 = ["nro", "name", "type", "price"]
        df.drop(["total_beef_grms", "total_ml", "topping_1", "topping_2", "topping_3", "topping_4"],
                axis="columns", inplace=True)
        print(tabulate(df.iloc[34:42], headers_5, tablefmt="fancy_grid"))
        elegir_extra = float(input("which extra do you want? type nro: \n"))
        if elegir_extra == 34:
            cantidad_extra = float(input("how many do you want?\n"))
            tuExtraVege = Vegetarian('extra cheese', 'burger', 'cow milk')
            print(str(tuExtraVege))
            elegir_mas = str(input("you chose extra cheese, do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[34, 2] * cantidad_extra
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_extra == 35:
            cantidad_extra = float(input("how many do you want?\n"))
            tuExtraMeat = Meat('extra bacon', 'burger', 'pig meat')
            print(str(tuExtraMeat))
            elegir_mas = str(input("you chose extra bacon, do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[35, 2] * cantidad_extra
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_extra == 36:
            cantidad_extra = float(input("how many do you want?\n"))
            tuExtraVeget = Vegetarian('extra egg', 'burger', 'chickens')
            print(str(tuExtraVeget))
            elegir_mas = str(input("you chose extra egg , do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[36, 2] * cantidad_extra
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_extra == 37:
            cantidad_extra = float(input("how many do you want?\n"))
            tuExtraMea = Meat('extra patty', 'burger', 'cow meat')
            print(str(tuExtraMea))
            elegir_mas = str(input("you chose extra patty , do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[37, 2] * cantidad_extra
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_extra == 38:
            cantidad_extra = float(input("how many do you want?\n"))
            tuExtraVega = Vegan('extra onion', 'burger', 'our super quality fields')
            print(str(tuExtraVega))
            elegir_mas = str(input("you chose extra onion, do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[38, 2] * cantidad_extra
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_extra == 39:
            cantidad_extra = float(input("how many do you want?\n"))
            tuExtraVegan = Vegan('extra tomato', 'burger', 'our super quality fields')
            print(str(tuExtraVegan))
            elegir_mas = str(input("you chose extra tomato, do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[39, 2] * cantidad_extra
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_extra == 40:
            cantidad_extra = float(input("how many do you want?\n"))
            tuExtraVegaan = Vegan('extra lettuce', 'burger', 'our super quality fields')
            print(str(tuExtraVegaan))
            elegir_mas = str(input("you chose extra lettuce, do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[40, 2] * cantidad_extra
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_extra == 41:
            cantidad_extra = float(input("how many do you want?\n"))
            tuExtraVe = Vegan('extra pickles', 'burger', 'our super quality fields')
            print(str(tuExtraVe))
            elegir_mas = str(input("you chose extra pickles, do you want anything else? (type yes or no)\n"))
            total_1 = df.iloc[41, 2] * cantidad_extra
            subtotal = total_ham + total_sds + total_top + total_chk + total_tom + total_1
            if elegir_mas == "yes":
                print("current total:", total_1)
            elif elegir_mas == "no":
                print(total_1)
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        else:
            elegir_mas = print("por favor siga las instrucciones")
            print("please type a valid number")
    else:
        print("remember to type a valid number, try again")
        food_typ = float(input("what type of food do you want? (type 1 for burgers, 2 for fried chicken, 3 for sides,"
                               "4 for beverages or 5 for extra toppings):\n"))
except ValueError:
    print("ingrese un valor valido")

while elegir_mas == "yes":
    df = pd.read_sql('SELECT * FROM Menu', cnx_lite)
    print(df.index)
    df.drop(["id"], axis="columns", inplace=True)
    subtotal = total_1
    add = float(input("what type of food do you want? type: \n 1 for burgers \n 2 for fried chicken \n 3 for sides"
                       "\n 4 for beverages \n 5 for extra toppings\n"))

    if add == 1:
        headers = ["nro", "name", "type", "total_beef_grms", "topping1", "topping2", "topping3", "topping4", "price"]
        df.drop(["total_ml"], axis="columns", inplace=True)
        print(tabulate(df.iloc[0:10], headers, tablefmt="fancy_grid"))
        elegir_ham_1 = float(input("which burger do you want? type nro: \n"))
        if elegir_ham_1 == 0:
            cantidad_ham = float(input("how many do you want?\n"))
            elegir_mas = str(input("ger, do you want anything else? (type yes or no)\n"))

            if elegir_mas == "yes":
                total_ham = df.iloc[0, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print("current total:", subtotal)
            elif elegir_mas == "no":
                total_ham = df.iloc[0, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham_1 == 1:
            cantidad_ham = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("eseburger, do you want anything else? (type yes or no)\n"))
            if elegir_mas == "yes":
                total_ham = df.iloc[1, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                total_ham = df.iloc[1, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham_1 == 2:
            cantidad_ham = float(input("how many do you want?\n"))
            elegir_mas = str(input("o you want anything else? (type yes or no)\n"))
            if elegir_mas == "yes":
                total_ham = df.iloc[2, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                total_ham = df.iloc[2, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham_1 == 3:
            cantidad_ham = float(input("how many do you want?\n"))
            elegir_mas = str(input("rger, do you want anything else? (type yes or no)\n"))
            if elegir_mas == "yes":
                total_ham = df.iloc[3, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                total_ham = df.iloc[3, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham_1 == 4:
            cantidad_ham = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("eeseburger, do you want anything else? (type yes or no)\n"))
            if elegir_mas == "yes":
                total_ham = df.iloc[4, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                total_ham = df.iloc[4, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham_1 == 5:
            cantidad_ham = float(input("how many do you want?\n"))
            elegir_mas = str(input("do you want anything else? (type yes or no)\n"))
            if elegir_mas == "yes":
                total_ham = df.iloc[5, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                total_ham = df.iloc[5, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham_1 == 6:
            cantidad_ham = float(input("how many do you want?\n"))
            elegir_mas = str(input("rger, do you want anything else? (type yes or no)\n"))

            if elegir_mas == "yes":
                total_ham = df.iloc[6, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                total_ham = df.iloc[6, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham_1 == 7:
            cantidad_ham = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("eeseburger, do you want anything else? (type yes or no)\n"))
            if elegir_mas == "yes":
                total_ham = df.iloc[7, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                total_ham = df.iloc[7, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham_1 == 8:
            cantidad_ham = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("g cheeseburger, do you want anything else? (type yes or no)\n"))
            if elegir_mas == "yes":
                total_ham = df.iloc[8, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                total_ham = df.iloc[8, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_ham_1 == 9:
            cantidad_ham = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("you chose the 5.0 bacon cheeseburger, do you want anything else? (type yes or no)\n"))
            if elegir_mas == "yes":
                total_ham = df.iloc[9, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                total_ham = df.iloc[9, 7] * cantidad_ham
                subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        else:
            print("please type a valid number")
    elif add == 2:
        headers_2 = ["nro", "name", "type", "price"]
        df.drop(["total_beef_grms", "total_ml", "topping_1", "topping_2", "topping_3", "topping_4"], axis="columns",
                inplace=True)
        print(tabulate(df.iloc[31:34], headers_2, tablefmt="fancy_grid"))
        elegir_pollo_1 = int(input("which chicken do you want? type nro: \n"))
        if elegir_pollo_1 == 31:
            cantidad_pollo = int(input("how many do you want?\n"))
            elegir_mas = str(
                input("you chose 4 pieces of fried chicken, do you want anything else? (type yes or no)\n"))
            total_chk = df.iloc[31, 2] * cantidad_pollo
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_pollo_1 == 32:
            cantidad_pollo = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("you chose 3 pieces of fried chicken, do you want anything else? (type yes or no)\n"))
            total_chk = df.iloc[32, 2] * cantidad_pollo
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_pollo_1 == 33:
            cantidad_pollo = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("you chose 2 pieces of fried chicken, do you want anything else? (type yes or no)\n"))
            total_chk = df.iloc[33, 2] * cantidad_pollo
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        else:
            print("please type a valid number")
    elif add == 3:
        headers_3 = ["nro", "name", "type", "price"]
        df.drop(["total_beef_grms", "total_ml", "topping_1", "topping_2", "topping_3", "topping_4"], axis="columns",
                inplace=True)
        print(tabulate(df.iloc[28:31], headers_3, tablefmt="fancy_grid"))
        elegir_papas_1 = int(input("which french fires do you want? type nro: \n"))

        if elegir_papas_1 == 28:
            cantidad_papas = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("you chose un cono de papas, do you want anything else? (type yes or no)\n"))
            total_sds = df.iloc[28, 2] * cantidad_papas
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_papas_1 == 29:
            cantidad_papas = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("you chose un cono de papas con cheddar, do you want anything else? (type yes or no)\n"))
            total_sds = df.iloc[29, 2] * cantidad_papas
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_papas_1 == 30:
            cantidad_papas = float(input("how many do you want?\n"))
            elegir_mas = str(input(
                "you chose un cono de papas con panceta y cheddar, do you want anything else? (type yes or no)\n"))
            total_sds = df.iloc[30, 2] * cantidad_papas
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        else:
            print("please type a valid number")
    elif add == 4:
        headers_4 = ["nro", "name", "type", "total_ml", "price"]
        df.drop(["total_beef_grms", "topping_1", "topping_2", "topping_3", "topping_4"], axis="columns",
                inplace=True)
        print(tabulate(df.iloc[10:28], headers_4, tablefmt="fancy_grid"))
        elegir_tomar_1 = float(input("which beverage do you want? type nro: \n"))
        if elegir_tomar_1 == 10:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(input("nt anything else? (type yes or no)\n"))
            total_tom = df.iloc[10, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 11:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(input("ou want anything else? (type yes or no)\n"))
            total_tom = df.iloc[11, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 12:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("you want anything else? (type yes or no)\n"))
            total_tom = df.iloc[12, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 13:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("want anything else? (type yes or no)\n"))
            total_tom = df.iloc[13, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 14:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(
                input(" you want anything else? (type yes or no)\n"))
            total_tom = df.iloc[14, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 15:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("ant anything else? (type yes or no)\n"))
            total_tom = df.iloc[15, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 16:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("you want anything else? (type yes or no)\n"))
            total_tom = df.iloc[16, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 17:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("you chose un agua, do you want anything else? (type yes or no)\n"))
            total_tom = df.iloc[17, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 18:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("you chose un agua con gas, do you want anything else? (type yes or no)\n"))
            total_tom = df.iloc[18, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 19:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("do you want anything else? (type yes or no)\n"))
            total_tom = df.iloc[19, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 20:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("do you want anything else? (type yes or no)\n"))
            total_tom = df.iloc[20, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 21:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("do you want anything else? (type yes or no)\n"))
            total_tom = df.iloc[21, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 22:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("do you want anything else? (type yes or no)\n"))
            total_tom = df.iloc[22, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 23:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("do you want anything else? (type yes or no)\n"))
            total_tom = df.iloc[23, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 24:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("do you want anything else? (type yes or no)\n"))
            total_tom = df.iloc[24, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 25:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(input("do you want anything else? (type yes or no)\n"))
            total_tom = df.iloc[25, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 26:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("you chose un agua con gas grande, do you want anything else? (type yes or no)\n"))
            total_tom = df.iloc[26, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_tomar_1 == 27:
            cantidad_tomar = float(input("how many do you want?\n"))
            elegir_mas = str(
                input("you chose un agua grande, do you want anything else? (type yes or no)\n"))
            total_tom = df.iloc[27, 3] * cantidad_tomar
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        else:
            print("please type a valid number")
    elif add == 5:
        headers_5 = ["nro", "name", "type", "price"]
        df.drop(["total_beef_grms", "total_ml", "topping_1", "topping_2", "topping_3", "topping_4"], axis="columns",
                inplace=True)
        print(tabulate(df.iloc[34:42], headers_5, tablefmt="fancy_grid"))
        elegir_extra_1 = float(input("which extra do you want? type nro: \n"))
        subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
        if elegir_extra_1 == 34:
            cantidad_extra = float(input("how many do you want?\n"))
            elegir_mas = str(input("you chose extra cheese, do you want anything else? (type yes or no)\n"))
            total_top = df.iloc[34, 2] * cantidad_extra
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_extra_1 == 35:
            cantidad_extra = float(input("how many do you want?\n"))
            elegir_mas = str(input("you chose extra bacon, do you want anything else? (type yes or no)\n"))
            total_top = df.iloc[35, 2] * cantidad_extra
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_extra_1 == 36:
            cantidad_extra = float(input("how many do you want?\n"))
            elegir_mas = str(input("you chose extra egg , do you want anything else? (type yes or no)\n"))
            total_top = df.iloc[36, 2] * cantidad_extra
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_extra_1 == 37:
            cantidad_extra = float(input("how many do you want?\n"))
            elegir_mas = str(input("you chose extra patty , do you want anything else? (type yes or no)\n"))
            total_top = df.iloc[37, 2] * cantidad_extra
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_extra_1 == 38:
            cantidad_extra = float(input("how many do you want?\n"))
            elegir_mas = str(input("you chose extra onion, do you want anything else? (type yes or no)\n"))
            total_top = df.iloc[38, 2] * cantidad_extra
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_extra_1 == 39:
            cantidad_extra = float(input("how many do you want?\n"))
            elegir_mas = str(input("you chose extra tomato, do you want anything else? (type yes or no)\n"))
            total_top = df.iloc[39, 2] * cantidad_extra
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_extra_1 == 40:
            cantidad_extra = float(input("how many do you want?\n"))
            elegir_mas = str(input("you chose extra lettuce, do you want anything else? (type yes or no)\n"))
            total_top = df.iloc[40, 2] * cantidad_extra
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        elif elegir_extra_1 == 41:
            cantidad_extra = float(input("how many do you want?\n"))
            elegir_mas = str(input("you chose extra pickles, do you want anything else? (type yes or no)\n"))
            total_top = df.iloc[41, 2] * cantidad_extra
            subtotal = total_1 + total_chk + total_sds + total_ham + total_top + total_tom
            if elegir_mas == "yes":
                print("current total:$", subtotal)
            elif elegir_mas == "no":
                print(subtotal, "$")
                print("thank you, to show you how much we apriciate you,  we are more than welcome to gift you"
                      "a random drink, come back later")
            else:
                print("please try again and type valid words")
        else:
            print("please type a valid number")
    else:
        print("remember to type a valid number, try again")
else:
    pass

try:
    if elegir_ham == 0:
        elegir_ham = "plain cheeseburger"
    elif elegir_ham == 1:
        elegir_ham = "plain bacon cheeseburger"
    elif elegir_ham == 2:
        elegir_ham = "plain veggie"
    elif elegir_ham == 3:
        elegir_ham = "double cheeseburger"
    elif elegir_ham == 4:
        elegir_ham = "double bacon cheeseburger"
    elif elegir_ham == 5:
        elegir_ham = "double veggie"
    elif elegir_ham == 6:
        elegir_ham = "triple cheeseburger"
    elif elegir_ham == 7:
        elegir_ham = "triple bacon cheeseburger"
    elif elegir_ham == 8:
        elegir_ham = "triple bacon-egg cheese burger"
    elif elegir_ham == 9:
        elegir_ham = "5.0 bacon cheese burger"
    else:
        elegir_ham =""
except ValueError:
    print("invalid number please try again")
try:
    if elegir_ham_1 == 0:
        elegir_ham_1 = "plain cheeseburger"
    elif elegir_ham_1 == 1:
        elegir_ham_1 = "plain bacon cheeseburger"
    elif elegir_ham_1 == 2:
        elegir_ham_1 = "plain veggie"
    elif elegir_ham_1 == 3:
        elegir_ham_1 = "double cheeseburger"
    elif elegir_ham_1 == 4:
        elegir_ham_1 = "double bacon cheeseburger"
    elif elegir_ham_1 == 5:
        elegir_ham_1 = "double veggie"
    elif elegir_ham_1 == 6:
        elegir_ham_1 = "triple cheeseburger"
    elif elegir_ham_1 == 7:
        elegir_ham_1 = "triple bacon cheeseburger"
    elif elegir_ham_1 == 8:
        elegir_ham_1 = "triple bacon-egg cheese burger"
    elif elegir_ham_1 == 9:
        elegir_ham_1 = "5.0 bacon cheese burger"
    else:
        elegir_ham_1 = ""
except ValueError:
    print("invalid number please try again")

try:
    if elegir_pollo == 31:
        elegir_pollo = "4 piezas de pollo frito"
    elif elegir_pollo == 32:
        elegir_pollo = "3 piezas de pollo frito"
    elif elegir_pollo == 33:
        elegir_pollo = "2 piezas de pollo frito"
    else:
        elegir_pollo = ""
except ValueError:
    print("invalid number please try again")
try:
    if elegir_pollo_1 == 31:
        elegir_pollo_1 = "4 piezas de pollo frito"
    elif elegir_pollo_1 == 32:
        elegir_pollo_1 = "3 piezas de pollo frito"
    elif elegir_pollo_1 == 33:
        elegir_pollo_1 = "2 piezas de pollo frito"
    else:
        elegir_pollo_1 = " "
except ValueError:
    print("invalid number please try again")

try:
    if elegir_papas == 28:
        elegir_papas = "cono de papas"
    elif elegir_papas == 29:
        elegir_papas = "cono de papas cheddar"
    elif elegir_papas == 30:
        elegir_papas = "cono de papas bacon cheddar"
    else:
        elegir_papas = ""
except ValueError:
    print("invalid number please try again")
try:
    if elegir_papas_1 == 28:
        elegir_papas_1 = "cono de papas"
    elif elegir_papas_1 == 29:
        elegir_papas_1 = "cono de papas cheddar"
    elif elegir_papas_1 == 30:
        elegir_papas_1 = "cono de papas bacon cheddar"
    else:
        elegir_papas_1 = ""
except ValueError:
    print("invalid number please try again")

try:
    if elegir_tomar == 10:
        elegir_tomar = "coca"
    elif elegir_tomar == 11:
        elegir_tomar = "coca zero"
    elif elegir_tomar == 12:
        elegir_tomar = "coca light"
    elif elegir_tomar == 13:
        elegir_tomar = "sprite"
    elif elegir_tomar == 14:
        elegir_tomar = "sprite zero"
    elif elegir_tomar == 15:
        elegir_tomar = "fanta"
    elif elegir_tomar == 16:
        elegir_tomar = "fanta zero"
    elif elegir_tomar == 17:
        elegir_tomar = "agua"
    elif elegir_tomar == 18:
        elegir_tomar = "agua con gas"
    elif elegir_tomar == 19:
        elegir_tomar = "cerveza heineken"
    elif elegir_tomar == 20:
        elegir_tomar = "coca grande"
    elif elegir_tomar == 21:
        elegir_tomar = "coca zero grande"
    elif elegir_tomar == 22:
        elegir_tomar = "sprite  grande"
    elif elegir_tomar == 23:
        elegir_tomar = "sprite zero grande"
    elif elegir_tomar == 24:
        elegir_tomar = "fanta zero grande"
    elif elegir_tomar == 25:
        elegir_tomar = "fanta grande"
    elif elegir_tomar == 26:
        elegir_tomar = "agua con gas grande"
    elif elegir_tomar == 27:
        elegir_tomar = "agua grande"
    else:
        elegir_tomar = ""
except ValueError:
    print("invalid number please try again")
try:
    if elegir_tomar_1 == 10:
        elegir_tomar_1 = "coca"
    elif elegir_tomar_1 == 11:
        elegir_tomar_1 = "coca zero"
    elif elegir_tomar_1 == 12:
        elegir_tomar_1 = "coca light"
    elif elegir_tomar_1 == 13:
        elegir_tomar_1 = "sprite"
    elif elegir_tomar_1 == 14:
        elegir_tomar_1 = "sprite zero"
    elif elegir_tomar_1 == 15:
        elegir_tomar_1 = "fanta"
    elif elegir_tomar_1 == 16:
        elegir_tomar_1 = "fanta zero"
    elif elegir_tomar_1 == 17:
        elegir_tomar_1 = "agua"
    elif elegir_tomar_1 == 18:
        elegir_tomar_1 = "agua con gas"
    elif elegir_tomar_1 == 19:
        elegir_tomar_1 = "cerveza heineken"
    elif elegir_tomar_1 == 20:
        elegir_tomar_1 = "coca grande"
    elif elegir_tomar_1 == 21:
        elegir_tomar_1 = "coca zero grande"
    elif elegir_tomar_1 == 22:
        elegir_tomar_1 = "sprite  grande"
    elif elegir_tomar_1 == 23:
        elegir_tomar_1 = "sprite zero grande"
    elif elegir_tomar_1 == 24:
        elegir_tomar_1 = "fanta zero grande"
    elif elegir_tomar_1 == 25:
        elegir_tomar_1 = "fanta grande"
    elif elegir_tomar_1 == 26:
        elegir_tomar_1 = "agua con gas grande"
    elif elegir_tomar_1 == 27:
        elegir_tomar_1 = "agua grande"
    else:
        elegir_tomar_1 = ""
except ValueError:
    print("invalid number please try again")

try:
    if elegir_extra == 34:
        elegir_extra = "xtra chees"
    elif elegir_extra == 35:
        elegir_extra = "xtra bacon"
    elif elegir_extra == 36:
        elegir_extra = "xtra egg"
    elif elegir_extra == 37:
        elegir_extra = "xtra paty"
    elif elegir_extra == 38:
        elegir_extra = "xtra onion"
    elif elegir_extra == 39:
        elegir_extra = "xtra tomato"
    elif elegir_extra == 40:
        elegir_extra = "xtra lettuce"
    elif elegir_extra == 41:
        elegir_extra = "xtra pickles"
    else:
        elegir_extra = ""
except ValueError:
    print("invalid number please try again")

try:
    if elegir_extra_1 == 34:
        elegir_extra_1 = "xtra chees"
    elif elegir_extra_1 == 35:
        elegir_extra_1 = "xtra bacon"
    elif elegir_extra_1 == 36:
        elegir_extra_1 = "xtra egg"
    elif elegir_extra_1 == 37:
        elegir_extra_1 = "xtra paty"
    elif elegir_extra_1 == 38:
        elegir_extra_1 = "xtra onion"
    elif elegir_extra_1 == 39:
        elegir_extra_1 = "xtra tomato"
    elif elegir_extra_1 == 40:
        elegir_extra_1 = "xtra lettuce"
    elif elegir_extra_1 == 41:
        elegir_extra_1 = "xtra pickles"
    else:
        elegir_extra_1 = ""
except ValueError:
    print("invalid number please try again")

try:
    conectar = sqlite3.connect('TP3.0.db')
    sql_clientes_insert = """INSERT INTO CLIENTES(nombre, apellido, edad, burger, chicken, beverage, side, extra_topping
    , price)
    VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');"""\
    .format(nombr, apellido, age, elegir_ham + " "+ elegir_ham_1, elegir_pollo +" "+ elegir_pollo_1,
    elegir_tomar + " " + elegir_tomar_1, elegir_papas +" "+ elegir_papas_1, elegir_extra + " " + elegir_extra_1, subtotal)

    cursor = conectar.cursor()
    cursor.execute(sql_clientes_insert)
    conectar.commit()
    print("insert operation successful")
    cursor.close()
except sqlite3.Error as e:
    print("error while inserting", e)
finally:
    if (conectar):
        conectar.close()
        print("connection closed")
    else:
        pass

url2 = 'http://www.thecocktaildb.com/api/json/v1/1/random.php'  #Cocktails api terceros

def get_api_response(url2):
    response = requests.get(url2)
    if response.status_code == 200:
        print('Recibiendo datos correctamente: {}'.format(response))
        response_json = response.json()
        json_data = response_json['drinks']
        for data in json_data:
            iden_num = data['idDrink']
            titulo = data['strDrink']
            recipe_en = data['strInstructions']
            recipe_es = data['strInstructionsES']
            url2 = data['strDrinkThumb']
            ingrediente_1 = data["strIngredient1"]
            ingrediente_2 = data["strIngredient2"]
            ingrediente_3 = data["strIngredient3"]
            ingrediente_4 = data["strIngredient4"]
            ingrediente_5 = data["strIngredient5"]
            ingrediente_6 = data["strIngredient6"]
            ingrediente_7 = data["strIngredient7"]
            ingrediente_8 = data["strIngredient8"]
            ingrediente_9 = data["strIngredient9"]
            ingrediente_10 = data["strIngredient10"]
            ingrediente_11 = data["strIngredient11"]
            ingrediente_12 = data["strIngredient12"]
            ingrediente_13 = data["strIngredient13"]
            ingrediente_14 = data["strIngredient14"]
            ingrediente_15 = data["strIngredient15"]

            print('Usted a obtenido el siguiente trago:\n', titulo)
            print('su numero de identificacion es: \n', iden_num)
            print('Podra reclamar el trago a traves del siguiente link:\n', url2)
            print('si quiere crear este trago en su casa le dejamos los pasos a continuacion:\n', recipe_en, recipe_es)
            print('necesitara los siguientes ingredientes:\n', ingrediente_1, ingrediente_2, ingrediente_3,
                  ingrediente_4, ingrediente_5, ingrediente_6, ingrediente_7, ingrediente_8, ingrediente_9,
                  ingrediente_10, ingrediente_11, ingrediente_12, ingrediente_13, ingrediente_14, ingrediente_15)
    else:
        print('Error en recivir datos, respone_status_code: {}'.format(response))
    return
get_api_response(url2=url2)

with open("Menu.csv", "r") as f:
    reader = csv.reader(f)

    next(reader)
    data = {"Menu":[]}
    for row in reader:
        data["Menu"].append({"name": row[1], "type": row[2], "total beef g": row[3], "total ml": row[4],
                            "Topping1": row[5], "Topping2": row[6], "Topping3": row[7], "Topping4": row[8],	"Price": row[9]})
       # print(data)
        with open("Menu.json", "w") as f:
            json.dump(data, f, indent=4)

with open('stock.csv',"w", newline='') as s:
    encabezados = ['name', 'type', 'price', 'quantity']
    write = csv.DictWriter(s, fieldnames=encabezados)
    write.writeheader()
    write.writerow({'name': 'plain cheeseburger', "type": "burger", "price": 200, 'quantity':900})
    write.writerow({'name': 'plain bacon cheeseburger', "type": "burger", "price": 240, 'quantity':900})
    write.writerow({'name': 'plain veggie', "type": "burger", "price": 100, 'quantity':900})
    write.writerow({'name': 'double cheeseburger', "type": "burger", "price": 300, 'quantity':900})
    write.writerow({'name': 'double bacon cheeseburger', "type": "burger", "price": 320, 'quantity':900})
    write.writerow({'name': 'double veggie', "type": "burger", "price": 200, 'quantity':900})
    write.writerow({'name': 'triple cheeseburger', "type": "burger", "price": 300, 'quantity':900})
    write.writerow({'name': 'triple bacon cheeseburger', "type": "burger", "price": 390, 'quantity':900})
    write.writerow({'name': 'triple bacon-egg cheese burger', "type": "burger", "price": 400, 'quantity':900})
    write.writerow({'name': ' 5.0 bacon cheese burger', "type": "burger", "price": 410, 'quantity':900})
    write.writerow({'name': 'coca', "type": "beverage", "price": 20, 'quantity':1000})
    write.writerow({'name': 'coca zero', "type": "beverage", "price": 20, 'quantity':1000})
    write.writerow({'name': 'coca light', "type": "beverage", "price": 20, 'quantity':1000})
    write.writerow({'name': 'sprite', "type": "beverage", "price": 20, 'quantity':1000})
    write.writerow({'name': 'sprite zero', "type": "beverage", "price": 20, 'quantity':1000})
    write.writerow({'name': 'fanta', "type": "beverage", "price": 20, 'quantity':1000})
    write.writerow({'name': 'fanta zero', "type": "beverage", "price": 20, 'quantity':1000})
    write.writerow({'name': 'agua', "type": "beverage", "price": 15, 'quantity':1000})
    write.writerow({'name': 'agua con gas', "type": "beverage", "price": 15, 'quantity':1000})
    write.writerow({'name': 'cerveza heineken', "type": "beverage", "price": 30, 'quantity':1000})
    write.writerow({'name': 'coca grande', "type": "beverage", "price": 50, 'quantity':1000})
    write.writerow({'name': 'coca zero grande', "type": "beverage", "price": 50, 'quantity':1000})
    write.writerow({'name': 'sprite grande', "type": "beverage", "price": 50, 'quantity':1000})
    write.writerow({'name': 'sprite zero grande', "type": "beverage", "price": 50, 'quantity':1000})
    write.writerow({'name': 'fanta zero grande', "type": "beverage", "price": 50, 'quantity':1000})
    write.writerow({'name': 'fanta grande', "type": "beverage", "price": 50, 'quantity':1000})
    write.writerow({'name': 'agua con gas grande', "type": "beverage", "price": 30, 'quantity':1000})
    write.writerow({'name': 'agua grande', "type": "beverage", "price": 30, 'quantity':1000})
    write.writerow({'name': 'cono de papas', "type": "sides", "price": 60, 'quantity':1000})
    write.writerow({'name': 'cono de papas cheddar', "type": "sides", "price": 70, 'quantity':600})
    write.writerow({'name': 'cono de papas bacon cheddar', "type": "sides", "price": 100, 'quantity': 500})
    write.writerow({'name': '4 piezas de pollo frito', "type": "fried chicken", "price": 200, 'quantity':800})
    write.writerow({'name': '3 piezas de pollo frito', "type": "fried chicken", "price": 150, 'quantity':700})
    write.writerow({'name': '2 piezas de pollo frito', "type": "fried chicken", "price": 100, 'quantity':600})
    write.writerow({'name': 'xtra cheese', "type": "extra topping", "price": 10, 'quantity':1200})
    write.writerow({'name': 'xtra bacon', "type": "extra topping", "price": 15, 'quantity':1200})
    write.writerow({'name': 'xtra egg', "type": "extra topping", "price": 15, 'quantity':1200})
    write.writerow({'name': 'xtra paty', "type": "extra topping", "price": 20, 'quantity':1200})
    write.writerow({'name': 'xtra onion', "type": "extra topping", "price": 7, 'quantity':1200})
    write.writerow({'name': 'xtra tomato', "type": "extra topping", "price": 5, 'quantity':1200})
    write.writerow({'name': 'xtra lettuce', "type": "extra topping", "price": 5, 'quantity':1200})
    write.writerow({'name': 'xtra pickles', "type": "extra topping", "price": 6, 'quantity':1200})
with open('stock.csv', "r") as f:
    read = csv.reader(f)
    next(read)
    stocks = {'stock': []}
    for row in read:
        stocks["stock"].append({"name": row[0], "type": row[1], "price": row[2], "quantity": row[3]})
        with open("stock.json", "w") as f:
            json.dump(data, f, indent=4)

with open('stock.csv', "r") as f:
    read = csv.reader(f)
    next(read)
    stocks = {'stock':[]}
    for row in read:
        stocks['stock'].append({"name": row[0], "type": row[1], "price": row[2], "quantity": row[3]})
with open("stock.json", "w") as f:
     json.dump(stocks, f, indent=4)

app = Flask(__name__)
@app.route('/stock', methods=["GET"])
def productos():
        return jsonify({"nuestro almacenamiento contiene: ": stocks})

@app.route('/stock/<string:producto_name>')
def getproducto(producto_name):
    producto_en = [producto for producto in stocks if producto ['name'] == producto_name]
    return jsonify({"producto": producto_en[0]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)


# hacer api que los demas puedan hacer pedidos a nuestro api, ej pedidos ya muestre mis productos en un lugar especia
# usar api que venda recetas
# en un csv que muestre el inventario de stock
# programacion de objetos con la hamburguesa herencia encapsulamiento
# gramos en la mhamburguesa pero no en salcichas o pollo,


