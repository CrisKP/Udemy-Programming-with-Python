# Loop control statements

names = ['Zak', 'Joe', 'Sally', 'Mary', 'Fred']
name = input('Enter a name to find: ')
found = False
for i in range(len(names)):          # or for i in names:, or for i in range(5):
    if (names[i] == name):  # or if i == name:
        print('I found that name!')
        found = True
        break
    else:
        continue
if not(found): print('I could not find that name')  #if found == False:
