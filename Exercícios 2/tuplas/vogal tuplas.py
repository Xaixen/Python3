palavras = ('marco', 'pedro', 'mamao', 'momochiki', 'livro', 'palmito', 'carne', 'urso')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos:', end='')
    for vogal in p:
        if vogal in 'aeiou':
            print(vogal.lower(), end='->')
    print('FIM')