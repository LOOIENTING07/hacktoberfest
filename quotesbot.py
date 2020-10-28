# hacktoberfest
print("Title of program: Quotes Bot")
print()
while True:
  description = input("Hi! How do you feel now?")

  list_of_words = description.split()

  feelings_list = []
  quotes_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      quotes_list.append("Learning to let go is the key to happiness")
      counter += 1
    if each_word in ["happy","cheerful","joyful"]:
      feelings_list.append(each_word)
      quotes_list.append("Stay positive~ Be kind whenever possible")
      counter += 1
    if each_word in ["tired","exhausted","drained"]:
      feelings_list.append(each_word)
      quotes_list.append("Tough times don't last but tough people do")
      counter += 1
    if each_word == "indecisive":
      quotes_list.append("indecisive")
      encouragement_list.append("Sometimes the heart sees what invisible to the eye")
      counter += 1
    if each_word == "bored":
      feelings_list.append("bored")
      quotes_list.append("Life is never boring unless someone chooses to be bored")
      counter += 1
    if each_word == "regretful":
      feelings_list.append("regretful")
      quotes_list.append("Don't regret from the past. Learn from it")
      counter += 1   
    if each_word == "angry":
      feelings_list.append("angry")
      quotes_list.append("Calm down. Never make impulsive decisions out of anger")
      counter += 1
    if each_word == "ambitious":
      feelings_list.append("ambitious")
      quotes_list.append("Set your goals high and never stop until you get there")
      counter += 1
    if each_word in ["afraid","scared","frightened"]:
      feelings_list.append(each_word)
      quotes_list.append("Never let your fear decide your future")
      counter += 1
    if each_word == "anxious":
      feelings_list.append("anxious")
      quotes_list.append("Trust yourself. You have survived a lot of obstacles and you will brave through what's coming")
      counter += 1
    if each_word in ["sick","queasy","unwell"]:
      feelings_list.append(each_word)
      quotes_list.append("There are some days when you need to rest. Stay strong")
      counter += 1
    if each_word == "jealous":
      feelings_list.append("jealous")
      quotes_list.append("Jealousy is counting other's blessings instead of your own. Don't be jealous of others")
      counter += 1  
    if each_word in ["lost","confused","unsure", "unclear"] :
      feelings_list.append(each_word)
      quotes_list.append("It's normal to be confused, take time to think things through, I believe in you!")
      counter += 1 
    if each_word in ["satisfied","content"] :
      feelings_list.append(each_word)
      quotes_list.append("A blissful state of the heart, the seed of which gives rise to peace. I'm happy for you :)")
      counter += 1 
    if each_word in ["peaceful","at peace","tranquil", "calm"] :
      feelings_list.append(each_word)
      quotes_list.append("Peace comes from within, do not seek it without. Inner peace heals the soul ")
      counter += 1
      
      
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+quotes_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(quotes_list)-1):
      encouragement += quotes_list[i] + ", "
    encouragement += "and " + quotes_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
