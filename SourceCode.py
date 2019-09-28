winner_list = []
winner_year = []
winner_dict = {}

def list():
    # The winners_file command will use the file titled 'WorldSeriesWinners.txt' so make sure to replace the variable 
    # titled 'FILEPATH' in the following command with the filepath of where the file is on your computer.
    winners_file = open(r'FILEPATH', 'r')

    winner = winners_file.readline()
    year = 1903

    while winner != '':
        winner = winner.rstrip('\n')
        winner_list.append(winner)
        winner = winners_file.readline()
        if (year == 1904)or(year == 1994):
            year += 1
            winner_year.append(year)
            year += 1
        else:
            winner_year.append(year)
            year += 1

    winners_file.close()

    index = 0
    while index < len(winner_list):
        winner_dict[winner_year[index]] = winner_list[index]
        index += 1

    return winner_dict

def search():
    search_year = int(input('This program will search for the winning team of the world series by year. What year would you like to search for? '))

    while (search_year == 1904)or(search_year == 1994):
        print('\nThe world series was not played during', search_year, 'try again.')
        search_year = int(input('What year would you like to search for? '))
    search_winner = winner_dict[search_year]
    print('\nWinning team in', search_year, ':', winner_dict[search_year])

    index = 0
    winner_count = 0
    for index in range(len(winner_dict)):
        if winner_list[index] == search_winner:
            winner_count += 1
        else:
            winner_count += 0
    if winner_count == 1:
        print('The', search_winner, "won the world series", winner_count, "time.")
    else:
        print('The', search_winner, "won the world series", winner_count, "times.")

list()
search()
