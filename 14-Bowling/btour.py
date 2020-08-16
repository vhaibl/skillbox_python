from collections import defaultdict
from bowling import get_score, get_score2

game, result_list = None, []
winnor_name = None
winnor_count, total_games = defaultdict(lambda: 0), defaultdict(lambda: 0)
tableoffame, tableoffame_line = [], []
version = None


def calc_tour(version, input_file, output_file):
    if version == 'new':
        calc = get_score2
        print('running NEW')

    else:
        calc = get_score
        print('running OLD')

    winner, result_line = 0, []
    with open(output_file, 'w', encoding='utf-8') as out:
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip('\n')
                if '###' in line:
                    out.write('{}\n'.format(line))
                    gamenumber = line.strip('### Tour')
                if '	' in line:
                    result_line = line.split('	')

                    try:
                        result_line.append(calc(result_line[1]))
                        out.write('{}	{}\n'.format(line, calc(result_line[1])))
                    except Exception as esc:
                        result_line.append('0')
                        out.write('{}	0 - {}\n'.format(line, esc))
                    if int(result_line[2]) > winner:
                        winner = int(result_line[2])
                        winner_name = result_line[0]

                    result_line.append(gamenumber)
                    result_list.append(result_line)
                if 'winner' in line:
                    out.write('winner is {}\n\n'.format(winner_name))
                    winnor_count[result_line[0]] += 1
                    winner_name = None
                    winner = 0

    for i, k, v, z in result_list:
        total_games[i] += 1
    for k in total_games.keys():
        tableoffame_line = [k, total_games[k], winnor_count[k]]
        tableoffame.append(tableoffame_line)

    tableoffame.sort(key=lambda i: i[1], reverse=True)

    print('+----------+------------------+--------------+')
    print('| Игрок    |  сыграно матчей  |  всего побед |')
    print('+----------+------------------+--------------+')
    for i, k, v in tableoffame:
        print(f'| {i:10}|{k:^17}|{v:^14}|')
    print('+----------+------------------+--------------+')
