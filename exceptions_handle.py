try:
    text = raw_input('Enter something --> ')
except EOFError:
    print 'Why did you do an EOF for me?'
except KeyboardInterrupt:
    print 'You cancelled the operation.'
else:
    print 'You entered {}'.format(text)