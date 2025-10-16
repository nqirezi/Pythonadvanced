
 try:
     result = 10 / 3
 except ZeroDivisionError:
     print("You can't divide by zero")





      fruits = {
          "apple": 10,
          "banana": 20,
          "orange": 30,
      }

     try:
         print(fruits["cherry"])
         except KeyError:
         print("You can't find prints something it doesn't exist")

         text = "this is a text "
         try:
             text_to_int = int(text)
     except Exception as e:
         print("An error will typecasting" e)

         def divide_numbers(a, b):
             try:
                 return a / b
             except ZeroDivisionError:
                 print("You can't divide by zero")
             except TypeError:
                 print("Invalide type of day")
             except Exception as e:
                 print("An error will typecasting" e)

divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "2")

