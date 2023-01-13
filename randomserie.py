# Name: Nathália Pimentel de Assis

series = [['breaking bad', 'drama', ] 
         ['prison break', 'action']
         ['greys anatomy','medical'] 
         ['how i met your mother', 'comedy']
         ['game of thrones', 'adventure']]
print('Choose the gender of your serie:  ')
gender = input()
for item in series:
  if item[1] == gender:
    print(gender + 'serie:' + item[0])
