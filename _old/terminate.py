def terminate():
    term = input('Do you want to exit? (Y/n) ')
    term = term.lower()

    if term != 'n' and term != 'y':
        while term != 'n' and term != 'y':
            term = input('Do you want to exit? (Y/n) ')
            term = term.lower()

    return term
