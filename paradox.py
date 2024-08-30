import datetime,random
def getBirthdays(numberOfBirthdays):
    #returns a list of number random date objects for birthdays
    birthdays =[]
    for i in range(numberOfBirthdays):
        startOfYera=datetime.date(2000,1,1)
        randomNumberOfDays=datetime.timedelta(random.randint(0,364))
        birthday=startOfYera+randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    #returns dateobject that occurs more than once
    if len(birthdays)==len(set(birthdays)):
        return None #all birthdays are ubnique
    for a,birthdayA in enumerate(birthdays):
        for b,birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA ==birthdayB:
                return birthdayA
            
 # Display the intro:
 print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
 
  The birthday paradox shows us that in a group of N people, the odds
  that two of them have matching birthdays is surprisingly large.
  This program does a Monte Carlo simulation (that is, repeated random
  simulations) to explore this concept.
  
  (It's not actually a paradox, it's just a surprising result.)
  ''')

MONTHS=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall i generate  (max 100)')
    response =input('>')
    if response.isdecimal() and (0<int(response)<=100):
        numBDays=int(response)
        break
print()

#generate and display the bithdays
print('Here are',numBDays, 'bithdays')
birthdays=getBirthdays(numBDays)
for i ,birthday in enumerate(birthdays):
    if i!=0:
        print(', ',end=' ')
    monthName=MONTHS[birthday.month-1]
    dateText='{} {}'.format(monthName,birthday.day)
    print(dateText,end=' ')
print()
print()
match=getMatch(birthdays)
#display the results
print('In this simulation. ' ,end='')
if match != None:
    monthName=MONTHS[match.month-1]
    dateText='{} {} '.format(monthName,match.day)
    print('Multiple people have a birthday on',dateText)
else :
    print('there are no matching birthdays ')
print()

#run throuhg 100000simulation
print('Generating',numBDays, 'random birthdays 100000 times')
input('Press enter to begin')

print('Lets run another 100,000 simulation')
simMatch=0
for i in range (100000):
    if i%10000=0:
        print(i, ' similation run')
    birthdays=getBirthdays(numBDays)
    if getMatch(birthdays)!=None:
        simMatch=simMatch+1
print('1000000 sumulations run')


#dispaly simulation results
probability =round(simMatch/10000*100,2)
print('Out if 100000 simulation of ',numBDays, ' people there was a')
print('matching birtday in that group ', simMatch, ' times. This means')
print('that ',numBDays 'peiple have a ' probability, '% chance of')
print('having a matching birtday in their group')
print('THat is probably more than you would think')