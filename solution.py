"""Case-study #4 Parsing web-pages
Developer:
Balabanov M.A.

"""

import urllib.request

with open('input.txt', 'r') as f_in:
    lines = f_in.readlines()

with open('output.txt', 'w') as f_out:
    col = '{:<20}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}\n'.format('Full Name', 'COMP', 'ATT', 'YDS', 'TD', 'INT', 'RATE')
    f_out.write(col)
    for url in lines:
        f = urllib.request.urlopen(url)
        s = f.read()
        text = str(s)
        part_name = text.find("player-name")
        name = text[text.find('>', part_name) + 1:text.find('&', part_name)]

        player_total = text.find("player-totals")
        line = text[text.find('>', player_total) + 1:text.find('</tr>', player_total)]
        lst = ['n', 't', 'd', 'TOTAL', '\\', '<', '>', '/']
        for i in lst:
            line = line.replace(i, ' ')
            line = line.replace('  ', ' ')

        _lst = line.split()
        COMP = _lst[0].replace(',', '')
        ATT = _lst[1].replace(',', '')
        YDS = _lst[3].replace(',', '')
        TD = _lst[5].replace(',', '')
        INT = _lst[6].replace(',', '')
        RATE = _lst[9].replace(',', '')

        res = '{:<20}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}\n'.format(name, COMP, ATT, YDS, TD, INT, RATE)
        f_out.write(res)
