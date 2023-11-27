"""
Estimate: 25 minutes 00 seconds
Actual:   74 minutes 13 seconds
"""


def main():
    """take data from wimbledon winners wikipedia and format it"""
    file = 'wimbledon.csv'
    years = format_csv_file(file)

    year_to_info = {year[0]: year[1:] for year in years}

    player_winners = count_items_in_list([year_to_info[year][1] for year in year_to_info])

    print('Wimbledon Champions: ')
    for player, win_count in player_winners.items():
        print(f"{player} {win_count}")

    country_winners = convert_dictionary_to_set(year_to_info, 0)
    country_winners = list(country_winners)
    country_winners.sort()
    print(f'\nThese {len(country_winners)} countries have won Wimbledon: ')
    print(', '.join(country_winners))


def format_csv_file(file):
    """take a csv file and return of list of lists for each line"""
    with open(file, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip headers
        return [line.strip().split(',') for line in in_file]


def count_items_in_list(input_list):
    """take a list and return a dictionary with each unique item and it's count"""
    item_to_count = {}
    for item in input_list:
        try:
            item_to_count[item] += 1
        except KeyError:
            item_to_count[item] = 1
    return item_to_count


def convert_dictionary_to_set(dictionary, index):
    """take an index for a dictionary and create a set of that data"""
    return set([item[index] for item in dictionary.values()])


main()
