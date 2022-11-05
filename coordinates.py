coord = 1, 1
commands = ['down', 'down', 'up', 'left', 'stop', 'right']

moves = {'down': (0, -1), 'up': (0, 1), 'left': (-1 , 0), 'right': (1, 0)}
coord_x, coord_y = coord

for command in commands:
    if command == 'stop':
        break
    else:
        coord_x += moves[command][0]
        coord_y += moves[command][1]

new_coord = coord_x, coord_y
print(new_coord)
