def pyhelp(met):
    s = help(met)
    return s


while True:
    lib = input('Função ou Biblioteca: ')
    print(pyhelp(lib))
    if lib in 'FimFIMfim':
        break
