#!/usr/bin/python

number=23
guess=int(raw_input('Enter an integer:'))
if guess==number:
	print 'you guessed it.'
	print "but you don't win any prizes!)"
elif guess < number:
	print 'No, it is a little lower than that'
else:
	print 'No, it is a little higher than that'
	print 'Done'
