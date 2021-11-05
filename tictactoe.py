
cells = '         '.upper()
print('---------')
print('| ' + cells[0] + ' ' + cells[1] + ' ' + cells[2] + ' |')
print('| ' + cells[3] + ' ' + cells[4] + ' ' + cells[5] + ' |')
print('| ' + cells[6] + ' ' + cells[7] + ' ' + cells[8] + ' |')
print('---------')


turn = 1
while True:
    if int(turn) % 2 != 0:
        turns = 'X'
    else:
        turns = 'O'
    cords = input('Enter coordinates:')
    new_cords = cords.replace(' ', '')
    if not new_cords.isnumeric():
        print('You should enter numbers!')
    else:
        act_cords = cords.split()
        for num in act_cords:
            if int(num) > 3:
                print('Coordinates should be from 1 to 3!')
                break
            elif act_cords == ['1', '1'] and (cells[0] == ' ' or cells[0] == '_'):
                cells = cells[:0] + turns + cells[0+1:]
                print('---------')
                print('| ' + cells[0] + ' ' + cells[1] + ' ' + cells[2] + ' |')
                print('| ' + cells[3] + ' ' + cells[4] + ' ' + cells[5] + ' |')
                print('| ' + cells[6] + ' ' + cells[7] + ' ' + cells[8] + ' |')
                print('---------')
                break
            elif act_cords == ['1', '2'] and (cells[1] == ' ' or cells[1] == '_'):
                cells = cells[:1] + turns + cells[1 + 1:]
                print('---------')
                print('| ' + cells[0] + ' ' + cells[1] + ' ' + cells[2] + ' |')
                print('| ' + cells[3] + ' ' + cells[4] + ' ' + cells[5] + ' |')
                print('| ' + cells[6] + ' ' + cells[7] + ' ' + cells[8] + ' |')
                print('---------')
                break
            elif act_cords == ['1', '3'] and (cells[2] == ' ' or cells[2] == '_'):
                cells = cells[:2] + turns + cells[2 + 1:]
                print('---------')
                print('| ' + cells[0] + ' ' + cells[1] + ' ' + cells[2] + ' |')
                print('| ' + cells[3] + ' ' + cells[4] + ' ' + cells[5] + ' |')
                print('| ' + cells[6] + ' ' + cells[7] + ' ' + cells[8] + ' |')
                print('---------')
                break
            elif act_cords == ['2', '1'] and (cells[3] == ' ' or cells[3] == '_'):
                cells = cells[:3] + turns + cells[3 + 1:]
                print('---------')
                print('| ' + cells[0] + ' ' + cells[1] + ' ' + cells[2] + ' |')
                print('| ' + cells[3] + ' ' + cells[4] + ' ' + cells[5] + ' |')
                print('| ' + cells[6] + ' ' + cells[7] + ' ' + cells[8] + ' |')
                print('---------')
                break
            elif act_cords == ['2', '2'] and (cells[4] == ' ' or cells[4] == '_'):
                cells = cells[:4] + turns + cells[4 + 1:]
                print('---------')
                print('| ' + cells[0] + ' ' + cells[1] + ' ' + cells[2] + ' |')
                print('| ' + cells[3] + ' ' + cells[4] + ' ' + cells[5] + ' |')
                print('| ' + cells[6] + ' ' + cells[7] + ' ' + cells[8] + ' |')
                print('---------')
                break
            elif act_cords == ['2', '3'] and (cells[5] == ' ' or cells[5] == '_'):
                cells = cells[:5] + turns + cells[5 + 1:]
                print('---------')
                print('| ' + cells[0] + ' ' + cells[1] + ' ' + cells[2] + ' |')
                print('| ' + cells[3] + ' ' + cells[4] + ' ' + cells[5] + ' |')
                print('| ' + cells[6] + ' ' + cells[7] + ' ' + cells[8] + ' |')
                print('---------')
                break
            elif act_cords == ['3', '1'] and (cells[6] == ' ' or cells[6] == '_'):
                cells = cells[:6] + turns + cells[6 + 1:]
                print('---------')
                print('| ' + cells[0] + ' ' + cells[1] + ' ' + cells[2] + ' |')
                print('| ' + cells[3] + ' ' + cells[4] + ' ' + cells[5] + ' |')
                print('| ' + cells[6] + ' ' + cells[7] + ' ' + cells[8] + ' |')
                print('---------')
                break
            elif act_cords == ['3', '2'] and (cells[7] == ' ' or cells[7] == '_'):
                cells = cells[:7] + turns + cells[7 + 1:]
                print('---------')
                print('| ' + cells[0] + ' ' + cells[1] + ' ' + cells[2] + ' |')
                print('| ' + cells[3] + ' ' + cells[4] + ' ' + cells[5] + ' |')
                print('| ' + cells[6] + ' ' + cells[7] + ' ' + cells[8] + ' |')
                print('---------')
                break
            elif act_cords == ['3', '3'] and (cells[8] == ' ' or cells[8] == '_'):
                cells = cells[:8] + turns + cells[8 + 1:]
                print('---------')
                print('| ' + cells[0] + ' ' + cells[1] + ' ' + cells[2] + ' |')
                print('| ' + cells[3] + ' ' + cells[4] + ' ' + cells[5] + ' |')
                print('| ' + cells[6] + ' ' + cells[7] + ' ' + cells[8] + ' |')
                print('---------')
                break
            else:
                print('This cell is occupied! Choose another one!')
                break
        matrix = [cells[0:3], cells[3:6], cells[6:9],
                  cells[0] + cells[3] + cells[6],
                  cells[1] + cells[4] + cells[7],
                  cells[2] + cells[5] + cells[8],
                  cells[0] + cells[4] + cells[8],
                  cells[6] + cells[4] + cells[2]]
        if " " not in cells and "XXX" not in matrix and "OOO" not in matrix:
            print("Draw")
            break
        elif "XXX" in matrix:
            print("X wins")
            break
        elif "OOO" in matrix:
            print("O wins")
            break
    turn += 1
