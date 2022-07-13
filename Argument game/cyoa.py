#are you a daughter or a son? 1=daughter, 2=son
# type of personality for your character, 1=careful but preserve, 2=active but reckless
#Agrument
#Your parent go to work at 6am and come home at 5pm. You were playing video games, you slept really late so you woke up at 3pm and didn't come to class on time. 
#Your mom: "Didn't I tell u to sleep early? Why don't you listen to me?"
#choose the type of Personality to argue with your parent
#if chose 1, Your dad:"the kid is too stubborn and preserving , he/she will not listen to anyone"
#if == 2, Your dad: "the kid is to ignorant,he/she will never think anything straight!"
#Begining
#Choose your way of replying, 1 ==sorry, 2==it is not a big deal, 3==saying nothing and go to your room
#if 1, "Sorry isn't enough..."
input_msg =""
game_is_on = True
def check_answer(input):

  if "options" in input:
    print("")
  else:
      print("Do Whatever you wantt w/ your life, we just want the best for you")

def prompt_user():
       reply = input("What do you want to say?  >>  ")
       return reply

def start():
  name = input("What is your name? ")
  print ("Welcome, " + name)
  print ("You can type 'options' when struggling.")
  print ("Your parent go to work at 6am and come home at 5pm. You were playing video games last night, so you slept really late and woke up at 3pm and didn't go to class on time.")
  while game_is_on:
       check_answer(prompt_user())


start()