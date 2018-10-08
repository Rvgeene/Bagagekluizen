import os.path

kluisnummers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']


def kluismenu():

    print('\u001b[33mWelkom bij onze kluizen: Kies een nummer uit het menu ')
    print('1 : Ik wil weten hoeveel kluizen nog vrij zijn')
    print('2 : Ik wil een nieuwe kluis')
    print('3 : Ik wil even iets uit mijn kluis halen')
    print('4 : Ik geef mijn kluis terug')
    print('5 : Verlaat dit menu\u001b[0m')

    keuze = int((input('Geef een nummer op : ')))

    if keuze == 1:
        beschikbaar()

    if keuze == 2:
        nieuwekluis()

    if keuze == 3:
        openkluis()

    if keuze == 4:
        verwijderkluis()

    if keuze == 5:
        print('Bedankt voor uw bezoek en tot ziens!')
        exit()


def beschikbaar():

        if os.path.exists('kluizen.txt'):
            readsafe = open('kluizen.txt', 'r')

        readLine = readsafe.readlines()

        for line in readLine:
            splitNumber = line.split()[0]

            if splitNumber in kluisnummers:
             kluisnummers.remove(splitNumber)

        print(len(kluisnummers), 'zijn beschikbaar')

def nieuwekluis():

    if os.path.exists('kluizen.txt'):

        readFile = open('kluizen.txt', 'r')
        writeFile = open('kluizen.txt', 'a')
        readLine = readFile.readlines()

        for line in readLine:

            splitNumber = line.split()[0]

            if splitNumber in kluisnummers:
                kluisnummers.remove(splitNumber)

        print('De volgende kluizen zijn beschikbaar: ', kluisnummers)

        inputNumber = int(input('Geef een kluisnummer op: '))

        if str(inputNumber) in kluisnummers:
            inputpassword = input('Voer een wachtwoord in met minstens 4 karakters: ')

            if len(inputpassword) < 4:
                print('Wachtwoord moet minimaal 4 karakters lang zijn')

                nieuwekluis()

            else:
                writeFile.write(str(inputNumber))
                writeFile.write(' : ')

                writeFile.write(str(inputpassword))
                writeFile.write('\n')

                print('Je hebt nu kluis', inputNumber)

        else:
            print('Deze kluis is niet beschikbaar!')

            nieuwekluis()

    else:
        print('De volgende kluizen zijn beschikbaar: ', kluisnummers)

        writeFile = open('kluizen.txt', 'w')
        inputNumber = int(input('Voer een kluisnummer in : '))

        if str(inputNumber) in kluisnummers:

            inputPassword = input('Voer een wachtwoord in met minstens 4 karakters: ')

            if len(inputPassword) < 4:
                print('Wachtwoord moet minstens 4 karakters bevatten')

                nieuwekluis()

            else:
                writeFile.write(str(inputNumber))
                writeFile.write(' : ')

                writeFile.write(str(inputPassword))
                writeFile.write('\n')

                print('Je hebt nu kluis #', inputNumber)

        else:
            print('Deze kluis is niet beschikbaar')

            nieuwekluis()

def openkluis():

    print('Geef je kluis informatie op\n')
    inputNumber = int(input('Nummer : '))
    inputPassword = input('Wachtwoord : ')


    if os.path.exists('kluizen.txt'):
        readtxt = open('kluizen.txt', 'r')
        readlne = readtxt.readlines()

        for line in readlne:

            if str(inputNumber) in line:

                if inputPassword in line:

                    print('Kluis is geopent')

                else:
                    print('Het wachtwoord is onjuist')



    else:

        print('Er is geen kluis gevonden')


def verwijderkluis():


    if os.path.exists('kluizen.txt'):


        inputNumber = int(input('Voer je kluisnummer in: '))
        inputPassword = input('Voer je wachtwoord in: ')

        complete = str(inputNumber) + ' : ' + str(inputPassword) + '\n'


        f = open('kluizen.txt', 'r')

        lines = f.readlines()

        f.close()

        f = open('kluizen.txt', 'w')

        for line in lines:

            if line not in complete:

                f.write(line)

        print('Jouw kluis is weer beschikbaar gestelt')

        f.close()

    else:

        print('Deze kluis is niet van iemand.')


kluismenu()