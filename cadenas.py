# Las cadenas de texto literales pueden contener múltiples líneas. Una forma es 
# usar triples comillas: """...""" o '''...'''. Los fin de línea son incluidos 
# automáticamente, pero es posible prevenir esto agregando una \ al final de la 
# línea. Por ejemplo:

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 3 times 'un', followed by 'ium'
print( 3 * 'un-' + 'ium' )
print( 'Py' 'thon' )

word = 'Python'
print( word[0] )  # character in position 0
print( word[5] )  # character in position 5
print( word[-1] )  # last character
print( word[-2] )  # second-last character
print( word[-6] )

print( word[0:2] )  # characters from position 0 (included) to 2 (excluded)
print( word[4:] )   # characters from position 4 (included) to the end
print( word[2:5] )  # characters from position 2 (included) to 5 (excluded)

print( word[:2] )  # character from the beginning to position 2 (excluded)
print( word[4:] )  # characters from position 4 (included) to the end
print( word[-2:] ) # characters from the second-last (included) to the end

print( word[:2] + word[2:] )
print( word[:4] + word[4:] )

s = 'supercalifragilisticexpialidocious'
print( len(s) )
