# Print all the names of states in a list that starts with M.

def MSEARCH(states):
    for state in states:
        if state[0] == 'M':
            print(state)

if __name__ == '__main__':
    print("Enter the states: \t\t\tTo exit, press enter...")
    states = []
    while(True):
        state = input("Enter a state: ")
        if state == '':
            break
        states.append(state)
    MSEARCH(states)
