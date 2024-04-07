10
10+10
5%2
9//2
2**2
3**3
3^3
_+5
9//2
_+1

result = 3*5
result

type(result)
 
nome = 'bruno'
type(nome)

nome == 'Bruno'

'a'+'b' *4 -"b"
"a"-"b" 

"teste"
'it\'s a scape quote'

"""can I do a 
... break line"""

"""can I do a 
break line"""

nome.count('o')
nome.capitalize()
nome.upper()
nome.isalnum()
nome.__len__()
len(nome)
'hello,world'.split()

string = "Hello world"
string.replace('world', 'users')
nome[3]
enumerate(nome)

nome[0]
string[::-1]
string.replace('world', 'students').upper()
my_age= 40
f'My age is {my_age}'
f'{nome} , {my_age}'
print(f'{nome}', f'{my_age}')

print('texto \n com quebra')
print('texto com \t tab')

fechado = False

if fechado:
  print('porta fechada!')
else:
  print('vamos lá!')
  
  
for l in 'Hello':
  print(l)
  
my_list = [1, 'a', 'Hello']

for item in my_list:
  print(item) 

my_list[1]

i=1
while i < 4:
  print(i)
  i=i+1
  
def say_hi():
  print('Hi!')

say_hi()

def say_hi(name):
    print('Hi, ' + name)

print("Let's greet the entire world")
say_hi('world')


def add(a, b):
  return(a+b)

add(1,2)

def optional_greeter(name):
    if name.startswith('X'):
        # We don't greet people with weird names :p
        return
    
    print('Hi there, ', name)

optional_greeter('Bander')


def say_hi(name):
    if name == '':
        print("You didn't enter your name!")
    else:
        print("Hi there...")
        for letter in name:
            print(letter)

name = input("Your name: ")

say_hi(name)

say_hi('')

#########
'a' + str(1)

int('2') + 2

class Vehicle:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed
    def start(self):
        self.started = True
        print("Started, let's ride!")
    def stop(self):
        self.speed = 0
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vrooooom!")
        else:
            print("You need to start me first")


class Car(Vehicle):
    trunk_open = False
    def open_trunk(self):
        self.trunk_open = True
    def close_trunk(self):
        self.trunk_open = False
        
        
car0=Car()

########

check = 'hamburguer'
if check == False:
  print("It is False")
elif check == 'hamburguer':
  print("yhammm!!")
else:
  print("It is not False")



