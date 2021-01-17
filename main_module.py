import datetime
import time
import os
import msvcrt
import module_time
from random import randint

def stroka_cikla(n_s, cifra_spis):

    return module_time.STR_FINISH_CONST[cifra_spis][n_s]

def stroka_finish(t_list_f, nom_str_beg):
    razryv_m = 2 * ' '

    str_finish = ''
    for i in range(5):
        for r in range(2):
            for j in range(3):
                for p in range(2):
                    if len(t_list_f[j]) == 1 and p == 0:
                        str_finish = str_finish + stroka_cikla(i, '0')
                    elif len(t_list_f[j]) == 1 and p == 1:
                        str_finish = str_finish + stroka_cikla(i, t_list_f[j][0])
                    else:
                        str_finish = str_finish + stroka_cikla(i, t_list_f[j][p])
                    str_finish = str_finish + (razryv_m if p == 0 else '')
                str_finish = str_finish + module_time.begunok(i, nom_str_beg, j)
            str_finish = str_finish + ('\n' if r == 0 else '')
        str_finish = str_finish + '\n'
    return str_finish

def main_func():

    k = 0

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')

        time_sec = datetime.datetime.now().time()

        t_list = (str(time_sec.hour), str(time_sec.minute), str(time_sec.second))

        format = ';'.join([str(randint(0, 7)), str(randint(30, 37)), str(randint(40, 47))])

        str_kvad = '\x1b[%sm\u2b1b\x1b[0m' % (format)

        print(stroka_finish(t_list, k).replace('%', str_kvad))

        if k < 4:
            k += 1
        else:
            k = 0

        time.sleep(1)
        
        if msvcrt.kbhit():
            if ord(msvcrt.getch()) != None:
                break

if __name__ == '__main__':
    main_func()