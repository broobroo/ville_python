# from random import randint

# justPrice= randint(1,10)
# win=0
# while(win == 0):
#     while(1):
        
#         guessPrice=input("Quel est le prix ?")
#         try:
#             guessPrice= int(guessPrice)
#             if guessPrice>0 and guessPrice<11:
#                 print("Ce n'est pas dans l'interval !")
#                 break
#         except: print ("Ce n'est pas un entier !")    
        
#     if (guessPrice == justPrice):
#         print("Vous avez gagné !")
#         win=1
#     else: 
#         if(guessPrice>justPrice):
#             print("C'est moins !")
#         else:
#             print("C'est plus !")



from random import randint

price = randint(1, 10)
res = -1
print(type(res))
while price != res:
    print("Insérez un prix")
    try:
        res = int(input())
        if res > 11 or res < -1:
            raise Exception('Not interval')
        if res == price:
            print("You won !")
        elif res < price:
            print("Supérieur")
        elif res > price:
            print("Inférieur")
    except ValueError:
        print("Insert a numbers")
    except Exception as e:
        print(e)