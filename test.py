articles = [
    {'id': 1, 'title': '"How to foo?"', 'author': 'F. BarBaz'},
    {'id': 2, 'title': '"Force 101"', 'author': 'O-W. Kenobi'},
    {'id': 3, 'title': '"Top 10 skyscrapers"', 'author': 'K. Kong'},
    {'id': 4, 'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla'},
    {'id': 5, 'title': '"5 min recepies"', 'author': 'H. Lector'},
]

id = 5
print(list(filter(lambda x: x.get('id') == id, articles))[0])
