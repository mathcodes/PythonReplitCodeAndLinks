# Create an empty list
users = []
# Add three-character elements
users.append('abc')
users.append('012')
users.append('112')
users.append('xyz')
users.append('lmn')
users.append('xzc')
users.append('jpc')
users.append('nol')
print(users) # ['abc', '012', '112', 'xyz']
# two by specifying their index
users.insert(3, 'thr')
print(users)
# deleting two
users.remove('012')
users.remove('112')
print(users)
# popping the third item in the list
third_pop = users.pop(2)
print(third_pop)
print(users)
# popping the third item in the list
last_pop = users.pop()
print(last_pop)
print(users)
# sorting the list permanently
users.sort()
print(users)
# reversing the list
users.reverse()
print(users)
# printing a message for each item on the list 
for user in users:
    print(f"Welcome, {user}!")
# include separate message afterwards.
print("Let's get rolling!")