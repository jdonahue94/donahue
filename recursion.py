# define the recursive function
def recursive_function(name:str, current:int):
    single_letter = name[current]
    # base case
    if current < len(name) -1 :
        # recursive case
        return f'{single_letter}\n' + recursive_function(name, current+1)
    else:
        return name[current]

# wrapper function
def call_recursive(name:str):
    if name:
        print(recursive_function(name,0))
    else:
        print('Please enter a name with at least one character.')

# call the recursive function
name = 'pluto'
call_recursive(name)
