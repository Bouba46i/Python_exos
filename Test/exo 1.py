#TODO :
# bonus

#bonus pour après
dict_fizz_buzz = {'3': 'Fizz', '5':'Buzz'}


def output_numb():
    for i in range(1, 101):
        output = ''
        # pour le bonus, faire une fonction qui passe a travers le dico donné 
        # et ajouter la chaine quand c'est un dénominateur du nombre
        if i % 3 == 0: output += 'Fizz'
        if i % 5 == 0: output += 'Buzz'
        print(i if not output else output)

output_numb()