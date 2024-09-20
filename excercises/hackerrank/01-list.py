if __name__ == '__main__':
    N = int(input())

list = []
def perform_command(command_string):
    commands = {
        'append': lambda x, value: x.append(value),
        'print': lambda x: print(x),
        'insert': lambda x, index, value: x.insert(index, value),
        'pop': lambda x: x.pop(),
        'sort': lambda x: x.sort(),
        'remove': lambda x, value: x.remove(value),
        'reverse': lambda x: x.reverse()
    }
    cmd = command_string[0]
    if cmd in commands:
        if cmd == 'insert':
            index = int(command_string[1])
            value = int(command_string[2])
            commands[cmd](list, index, value)
        elif cmd == 'remove' or cmd == 'append':
            value = int(command_string[1])
            commands[cmd](list, value)
        else:
            commands[cmd](list)

for raw in range(1, N+1):
    command_string = input().split(' ')
    perform_command(command_string)
