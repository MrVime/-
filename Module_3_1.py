calls = 0
def count_calls():
    global calls
    calls += 1
    return
def string_info(s):
    count_calls()
    string = []
    string.append(len(s))
    string.append(s.upper())
    string.append(s.lower())
    print(tuple(string))
    return
def is_contains(line,list):
    count_calls()
    for i in range(len(list)):
        if list[i].lower() == line.lower():
            list.append(True)
        else:
            continue
    if list[-1] == True:
        print(True)
    else:
        print(False)
string_info('Capybara')
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)