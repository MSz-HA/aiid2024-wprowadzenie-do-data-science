#z https://pyformat.info/ NEW:

print('{:>10}'.format('test'))
print('{:_<10}'.format('test'))
print('{:^10}'.format('test'))
print('{:.5}'.format('xylophone'))
print('{:10.5}'.format('xylophone'))

# f-string:

print(f'{'test':>10}')
print(f'{'test':_<10}')
print(f'{'test':^10}')
print(f'{'xylophone':.5}')
print(f'{'xylophone':10.5}')