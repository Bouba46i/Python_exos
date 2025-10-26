#TODO :
# done

dict_fizz_buzz = {'3': 'Fizz', '5':'Buzz'}
dict_fizz_buzz_lazz_dezz = {'3': 'Fizz', '5':'Buzz', '9':'Lazz', '15': 'Dezz'}



def get_processed_output(numb, dict):
        output = ''
        for key, val in dict.items():
            if key.isdigit() and numb % int(key) == 0: output += val
        return output

    
def output_numb(dict):
    for i in range(1, 101):
        output = get_processed_output(i, dict)
        print(i if not output else output)


print("#### first dict ####")
output_numb(dict_fizz_buzz)
print("\n#### second dict ####")
output_numb(dict_fizz_buzz_lazz_dezz)