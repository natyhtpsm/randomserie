# Name: Nathália Pimentel de Assis

# Version one: completely random choice, not based in genre
# from random import choice
# series = ['breaking bad', 'prison break', 'greys anatomy', 'how i met your mother', 'game of thrones'] ]
# print (choice(series))


#Version two below: 

series = [['breaking bad', 'drama', ] 
         ['prison break', 'action']
         ['greys anatomy','medical'] 
         ['how i met your mother', 'comedy']
         ['game of thrones', 'adventure']]
print('Choose the genre of your serie:  ')
genre = input()
for item in series:
  if item[1] == genre:
    print(gender + 'serie:' + item[0])
