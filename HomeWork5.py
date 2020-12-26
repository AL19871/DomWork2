import os
board = """
 1 | 2 | 3 
----------
 4 | 5 | 6 
 ---------
 7 | 8 | 9 
"""
list_x_o = {'1':'1',
            '2':'2',
            '3':'3',
            '4':'4',
            '5':'5',
            '6':'6',
            '7':'7',
            '8':'8',
            '9':'9'}
while True:
    name_igrok = input('Выберите игрока "x" или "0":')
    if name_igrok == 'x' or name_igrok == '0':
        break
print(board)
while True:
    while True:
        cell = input('Выберите номер пустой ячейки для "' + name_igrok + '": ')
        if int(cell) > 0 and int(cell) < 10 and list_x_o[cell] == cell:
            list_x_o[cell] = name_igrok
            board = board.replace(cell, name_igrok)
            break
    os.system('cls' if os.name == 'nt' else 'clear')
    print(board)
    if ((list_x_o['1'] == list_x_o['2'] and list_x_o['2'] == list_x_o['3'])
            or (list_x_o['1'] == list_x_o['4'] and list_x_o['4'] == list_x_o['7'])
            or (list_x_o['1'] == list_x_o['5'] and list_x_o['5'] == list_x_o['9'])
            or (list_x_o['2'] == list_x_o['5'] and list_x_o['5'] == list_x_o['8'])
            or (list_x_o['3'] == list_x_o['6'] and list_x_o['6'] == list_x_o['9'])
            or (list_x_o['3'] == list_x_o['5'] and list_x_o['5'] == list_x_o['7'])
            or (list_x_o['7'] == list_x_o['8'] and list_x_o['8'] == list_x_o['9'])
            or (list_x_o['4'] == list_x_o['5'] and list_x_o['5'] == list_x_o['6'])):
        print('Выиграл игрок: ' + name_igrok)
        break
    elif (list_x_o['1'] == '1' or list_x_o['2'] == '2' or list_x_o['3'] == '3'
            or list_x_o['4'] == '4' or list_x_o['5'] == '5' or list_x_o['6'] == '6'
            or list_x_o['7'] == '7' or list_x_o['8'] == '8' or list_x_o['9'] == '9'):
        pass
    else:
        print('Ничья')
        break
    if name_igrok == 'x':
        name_igrok = '0'
    else:
        name_igrok = 'x'