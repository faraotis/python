nome = input('Digite um nome: ')
print(f'''Tipo primitivo: {type(nome)}
So tem espacos? {nome.isspace()}
E um numero? {nome.isnumeric()}
E alfabetico? {nome.isalpha()}
Esta maiusculo? {nome.isupper()}
Esta minusculo? {nome.islower()}
E alfanumerico? {nome.isalnum()}
''')
