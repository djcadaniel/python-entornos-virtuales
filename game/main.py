import random
options = ('piedra','papel','tijera')


def choose_option():
  user = input('Usuario: ')
  user = user.lower()
  
  if not user in options:
    print('esa opcion no es valida')
    #continue
    return None, None

  computer = random.choice(options)
  print(f'Computadora: {computer}')
  return user, computer
  
def check_rules(user, computer, user_wins, conputer_wins):
  if user == computer:
    print('empate')
  elif user == 'piedra':
    if computer == 'papel':
      print('piedra gana a papel')
      print('Resultado: user gana')
      user_wins += 1
      print(f'Usuario ganó: {user_wins} veces')
      print(f'Computadora ganó: {conputer_wins} veces')
    elif computer == 'tijera':
      print('piedra gana a tijera')
      print('Resultado: user gana')
      user_wins += 1
      print(f'Usuario ganó: {user_wins} veces')
      print(f'Computadora ganó: {conputer_wins} veces')
  elif user == 'papel':
    if computer == 'piedra':
      print('piedra gana a papel')
      print('Resultado: computer gana')
      conputer_wins += 1
      print(f'Usuario ganó: {user_wins} veces')
      print(f'Computadora ganó: {conputer_wins} veces')
    elif computer == 'tijera':
      print('tijera gana a papel')
      print('Resultado: computer gana')
      conputer_wins += 1
      print(f'Usuario ganó: {user_wins} veces')
      print(f'Computadora ganó: {conputer_wins} veces')
  elif user == 'tijera':
    if computer == 'papel':
      print('tijera gana a papel')
      print('Resultado: user gana')
      user_wins += 1
      print(f'Usuario ganó: {user_wins} veces')
      print(f'Computadora ganó: {conputer_wins} veces')
    elif computer == 'piedra':
      print('piedra gana a tijera')
      print('Resultado: computer gana')
      conputer_wins += 1
      print(f'Usuario ganó: {user_wins} veces')
      print(f'Computadora ganó: {conputer_wins} veces')
  return user_wins, conputer_wins

def resultado_game(conputer_wins, user_wins):
    if conputer_wins == 2:
      print('El rotundo ganador es la computadora')
      return True
    elif user_wins == 2:
      print('El rotundo ganador es el usuario')
      return True
  
def run_game():
  conputer_wins = 0
  user_wins = 0
  rounds = 1

  while True:
    print('')
    print('')
    print('*' * 10)
    print('Ronda: ', rounds)
    print('*' * 10)

    user, computer = choose_option()
    user_wins, conputer_wins = check_rules(user, computer, user_wins, conputer_wins)
    rounds += 1
    if resultado_game(conputer_wins, user_wins):
      break
    
run_game()