print ('Welcome to the Height Converter\n\
----------------------------\n\
Here are your options:\n\
    (f)eet/Inches to meters\n\
    (m)eters to feet/inches\n\
----------------------------')
mode = input('What will it be?:  ')

if mode == 'f':
    print('Great! how tall are ya?')
    feet = int(input('Feet: '))
    inches = float(input('Inches: '))

    meters = 0.3048 * feet
    meters += round(0.0254 * inches)
    centimeters = round(meters*100,2)

    print(f'You are {meters} Meters tall!\n\
        or {centimeters} Centimeters')

elif mode == 'm':
    print('Great! how tall are ya?')
    meters = float(input('Meters: '))

    feet = 3.28084 * meters
    inches = int((feet - int(feet))*12)
    feet = int(feet)
    print(f'You are {feet} feet and {inches} inches tall!')
else:
        print('Try typing f or m next time.')