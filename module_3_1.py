calls = 0

def count_calls() :
    global calls
    calls += 1

def string_info(string) :
    global calls
    count_calls()
    string = len(string), string.upper(), string.lower()
    print(string)

def is_contains(string,list) :
    global calls
    count_calls()
    string = string.lower()
    list = [list.lower() for list in list]  # Пришлось погуглить. Не совсем понимаю , как выражение читается, но оно работает
    while string in list :
        print(True)
        break
    else:
        print(False)

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban',['ban','BaNaN','urBAN'])
is_contains('cycle',['recycling','cyclic'])
print(calls)

