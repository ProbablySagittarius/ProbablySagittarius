##This was a Python code on Genorating random license plates, it isn't the most accurate at the moment and I'm still tweaking it

import random

##California License plate

plate_california = []


def ran_num():
    number1 = random.randint(7, 8)
    plate_california.append(number1)


def ran_numb():
    numb = random.randint(1, 9)
    plate_california.append(numb)


list1 = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

list2 = ['First of all! type exactly one of the options and it should be simple as that','Type one of the options to get a result!','What']

def ran_let():
    random_letter = random.choice(list1)
    plate_california.append(random_letter)


ran_num()
ran_let()
ran_let()
ran_let()
ran_numb()
ran_numb()
ran_numb()

##Nevada License Plate.

plate_Nevada = []


def ran_num1():
    number2 = random.randint(0, 9)
    plate_Nevada.append(number2)


def ran_let1():
    random_letter = random.choice(list1)
    plate_Nevada.append(random_letter)


ran_num1()
ran_num1()
ran_num1()
plate_Nevada.append('-')
ran_let1()
ran_num1()
ran_num1()

##Oregon License plate

plate_Oregon = []


def ran_num2():
    number3 = random.randint(0, 9)
    plate_Oregon.append(number3)


def ran_let2():
    random_letter = random.choice(list1)
    plate_Oregon.append(random_letter)


ran_num2()
ran_num2()
ran_num2()
ran_let2()
ran_let2()
ran_let2()

##New York License Plates

plate_Newyork = []


def ran_num3():
    number4 = random.randint(0, 9)
    plate_Newyork.append(number4)


def ran_let3():
    random_letter = random.choice(list1)
    plate_Newyork.append(random_letter)


ran_let3()
ran_let3()
ran_let3()
plate_Newyork.append('-')
ran_num3()
ran_num3()
ran_num3()
ran_num3()

##Options are
print('Type HELP for info')
print('California')
print('Nevada')
print('Oregon')
print('New York')

what_about = (random.choice(list2))

struct = {'instructions':what_about}

def asking_1():
  question_1 = input('Which License Plate..?')
  if question_1 == 'California':
    print(plate_california)
  if question_1 == 'New York':
    print(plate_Newyork)
  if question_1 == 'Oregon':
    print(plate_Oregon)
  if question_1 == 'Nevada':
    print(plate_Nevada)
  if question_1 == 'HELP':
    print('Huh whats that?',struct['instructions'])

asking_1()

if asking_1() == 'California':
    print(plate_california)
    print('Here you go!')
    asking_1()
elif asking_1() == 'Nevada':
    print(plate_Nevada)
    print('Sure thing!')
    asking_1()
elif asking_1() == 'Oregon':
    print(plate_Oregon)
    print('As you wish!')
    asking_1()
elif asking_1() == 'New York':
    print(plate_Newyork)
    print('Totally!')
    asking_1()
elif asking_1() == 'Done':
    print('Finished!')
else:
  print('Error no Plate matched by that name')
