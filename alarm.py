import winsound

code = 1234

user = int(input('Enter the code: '))

if user == code:
    print('Welcome')
else:
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 5000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)