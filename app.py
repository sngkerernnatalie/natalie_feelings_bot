print("Title of program: Feelings Bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("It's a good day. Enjoy the rest of it.")
      counter += 1
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("This will pass with time, you are stronger than you think.")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("Seems like it's been a long day. Why don't you sleep?")
      counter += 1
      if each_word == "thirsty":
     feelings_list.append("thirsty")
      encouragement_list.append("you need to drink more water because its good and important for you")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
