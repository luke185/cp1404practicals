import wikipedia

PROMPT = 'What page would you like to search for?'

print(PROMPT)
title = input('> ')
while title != '':
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(page.title)
        print(f"Summary: {page.summary}")
        print(f"Page link: {page.url}")
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
    except wikipedia.exceptions.DisambiguationError as e:
        print('Search term is too ambiguous, please choose an option from the following list instead: ')
        print(e.options)
    except wikipedia.exceptions.PageError:
        print('Page not found')

    print(PROMPT)
    title = input('> ')
