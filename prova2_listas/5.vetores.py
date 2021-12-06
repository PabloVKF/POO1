
def musical_loop():  # FALTA TERMINAR
    '''
    se a diferença entre o input3 e o input2 for de mesmo sinal que a
    diferença entre input1 e input2, significa que nao houve um peak,
    caso sim, houve peak
    '''
    # t = int(input())
    # vet_list = list(map(int, input().strip().split()))
    

    # for i, v in enumerate(vet_list):
    #     if vet_list[i+1] > v:
    #         sentido = up
    #     elif vet_list[i+1] < v:
    #         sentido = down
    #     else:
    #         continue

        
    #     if sentido == 0:
    #         pass
    
    
    # for i, v in enumerate(vet_list):
    #     if v == vet_list[1] or v == vet_list[-1]:
    #         print(v)
    #         continue
    #     else:
    #         dif = vet_list[i+1] - v


def optical_reader():  # OK
    resps = []
    while True:
        total_answers = int(input())
        if total_answers == 0:
            break
        alternatives = ['A', 'B', 'C', 'D', 'E']
        
        for i in range(0, total_answers):
            answer = list(map(int, input().strip().split()))
            s = 0
            
            for i, color in enumerate(answer):
                if color <= 127:
                    alt = alternatives[i]
                    s += 1
            resps.append(alt) if s == 1 else resps.append('*')

    for r in resps:
        print(r)


def lowest_number_and_position():  # OK
    int(input())
    numbers = list(map(int, input().strip().split()))
    r = min(numbers)
    i = numbers.index(r)
    print(f'Menor valor: {r}\nPosicao: {i}')
    

def fake_tickets():  # FALTA TERMINAR
    while True:
        # MÉTODO 1 (NAO ROLA)
        # o, p = input().strip().split()
        # original_tickets, persons_attending = int(o), int(p)
        
        a = input().split()
        if '0' in a:
            break
        ticket_numbers = list(map(int, input().strip().split()))
        st = set(ticket_numbers)
        s = 0
        for v in ticket_numbers:
            if v in st:
                s += 1
        print(s - len(st))


def head_or_tail():  # OK
    while True:
        flag = int(input())
        
        if flag == 0:
            break
        else:
            games = list(map(int, input().strip().split()))
            sum0 = sum1 = 0
            for result in games:
                if result == 0:
                    sum0 += 1
                else:
                    sum1 += 1
            
            print(f'Mary won {sum0} times and John won {sum1} times')


def sticks_game():  # ERRO
    '''
    sticks with variable sizes;
    draw rectangles with these sticks;
    each stick can be used in only one rectangle;
    two kids with one set of sticks each;
    wins who draw the most rectangles.
    '''
    resps = []
    while True:
        number_of_sets = int(input())
        if number_of_sets == 0:
            break
        else:
            four_sides = []
            two_sides = []

            for set in range(0, number_of_sets):
                size, amount = map(int, input().strip().split())
                if amount >= 4:
                    full = amount // 4
                    four_sides.append(full)
                elif amount >= 2:
                    half = amount // 2
                    two_sides.append(half)
                
            total_rectangles = sum(four_sides) + sum(two_sides)//2
            resps.append(total_rectangles)
    
    for r in resps:
        print(r)


def dangerous_dive():  # ERRO. OTIMIZAR TEMPO DO CODIGO
    while True:
        resps = []
        try:
            # went, returned = map(int, input().strip().split())
            # returned_list = list(map(int, input().strip().split()))
            went, returned = input().strip().split()
            went = int(went)
            returned_string = input().strip().split()
            returned_list = []
            for ret in returned_string:
                ret = int(ret)
                returned_list.append(ret)
            
            went_list = []
            for i in range(1, went+1):
                went_list.append(i)
            
            not_returned_list = []
            for volunteer in went_list:
                if volunteer not in returned_list:
                    not_returned_list.append(volunteer)
            
            if not_returned_list == []:
                # print('*')
                resps.append('*')
            else:    
                for v in not_returned_list:
                    # print(v) if v == not_returned_list[-1] else print(v, end=' ')
                    a = f'{v} '
                    resps.append(v) if v == not_returned_list[-1] else resps.append(a)
            
        except EOFError:
            # break
            for r in resps:
                print(r)


def biochemical_digital_circuit():  # ERRO
    while True:
        nodes, measures, min_length = map(int, input().strip().split())
        if nodes == 0 and measures == 0 and min_length == 0:
            break
        else:
            s = 0
            for m in range(0, measures):
                binary = list(map(int, input().strip().split()))
                if sum(binary) >= min_length:
                    s += 1
            print(s)


def detective_watson():  # OK
    '''
    its never the most suspicious,
    but the second most suspicious. - Sherlock Holmes
    '''
    while True:
        suspects = int(input())
        if suspects == 0:
            break
        jw_opinions = list(map(int, input().strip().split()))
        killer = sorted(jw_opinions)[-2]
        i = jw_opinions.index(killer) + 1
        print(i)


def automated_checking_machine():  # OK
    first_connector = list(map(int, input().strip().split()))
    second_connector = list(map(int, input().strip().split()))
    # 0 = outlet; 1 = plug
    not_compatible = False
    for i in range(0, 5):
        if first_connector[i] == second_connector[i]:
            not_compatible = True
            break
    print('N') if not_compatible else print('Y')


def brazilian_economy():  # OK
    citizens = int(input())
    opinions = list(map(int, input().strip().split()))
    # is_ok = 0; not_ok = 1
    not_ok = sum(opinions)
    majority = citizens // 2 + 1
    print('N') if not_ok >= majority or not_ok == citizens/2 else print('Y')


def sansas_snow_castle():  # FALTA TERMINAR
    towers, peaks = map(int, input().strip().split())
    beautiful = towers[1] > towers[0]


def jumping_frog():  # OK
    frog_jump_height, total_pipes = map(int, input().strip().split())
    pipes_height = list(map(int, input().strip().split()))
    
    toohigh_or_toolow = False
    for i, pipe_height in enumerate(pipes_height):
        base = pipe_height if i == 0 else pipes_height[i-1]
        if abs(base - pipe_height) > frog_jump_height:
            toohigh_or_toolow = True
            break

    print('YOU WIN') if not toohigh_or_toolow else print('GAME OVER')


def airport():  # ERRO
    c = 1
    while True:
        keys = []
        airports, flights = map(int, input().strip().split())
        if airports == flights == 0:
            break
        
        total_list = []
        for f in range(0, flights):
            airport1, airport2 = map(int, input().strip().split())
            # total_list.append(airport1)
            # total_list.append(airport2)
            total_list.append(airport1)
            total_list.append(airport2)
        
        total_list = sorted(total_list)
        print(total_list)

        sums = []
        indices = []
        sum = 0
        ini = min(total_list)
        for i, v in enumerate(total_list):
            if v == ini:
                sum += 1
            else:
                sums.append(sum)
                ind = i - 1
                indices.append(ind)
                sum = 1
                ini = v
        print(sums)
        print(indices)
        result = []
        for i, s in enumerate(sums):
            if s == max(sums):
                result.append(total_list[indices[i]])
        print(result)

        # 2 3
        # 7 4
        # 6 5
        # 5 6
        # 7 3
        # 2 1
        # 6 8
        # 9 3

        # from typing import Counter
        # count = Counter(total_list)
        # max = [0]
        # for value in count.values():
        #     if value > max[0]:
        #         max.clear()
        #         max.append(value)
        #     elif value == max[0]:
        #         max.append(value)
        
        # temp_keys = []
        # for key in count:
        #     if count[key] == max[0]:
        #         temp_keys.append(key)
        # keys.append(temp_keys)
        # keys = sorted(keys)

        # print(f'Teste {c}')
        # for k in keys:
        #     for v in k:
        #         print(v) if v == k[-1] else print(v, end=' ')
        # print()


def maratona():  # AVALIAR
    entry = input().strip().split()
    dist_interm_max = int(entry[1])  # metros
    pos_postos_agua = list(map(int, input().strip().split()))  # metros
    # dist_maratona = 42195  # metros
    dif = 0
    for posto in pos_postos_agua:
        dif = posto - dif
        consegue_terminar = True if dist_interm_max >= dif else False
    print('S') if consegue_terminar else print('N')


def pulo_do_sapo():  # AVALIAR
    num_pedras, num_sapos = map(int, input().strip().split())
    pedras_lista = []
    for pedra in range(1, num_pedras+1):
        pedras_lista.append(pedra)
    possibs = []
    for sapo in range(0, num_sapos):
        pos_inicial, dist_fixa = map(int, input().strip().split())
        possibs.append(pos_inicial)
        possib_pedra = pos_inicial
        while True:
            possib_pedra -= dist_fixa
            if possib_pedra >= 1:
                possibs.append(possib_pedra)
            else:
                break
        possib_pedra = pos_inicial
        while True:
            possib_pedra += dist_fixa
            if possib_pedra <= num_pedras + 1:
                possibs.append(possib_pedra)
            else:
                break
    possibs = sorted(possibs)
    for i in range(0, num_pedras):
        print('1') if pedras_lista[i] in possibs else print('0')


def campo_minado():
    pass





pulo_do_sapo()

# PARA MEDIR A PERFORMANCE DO CODIGO:
    # from time import perf_counter
    # def start_code_time():
    #     return perf_counter()
        
    # def end_code_time(start_code_time):
    #     end_code = perf_counter()
    #     time_code = end_code - start_code_time
    #     return time_code
