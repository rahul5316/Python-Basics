msg = "Hello World"

print(msg.lower()) #prints lower casr
print(msg.upper()) #print the entire message in upper case

print(msg[2]) #prints the chrcter a idx 2

print(len(msg)) #prints the length of the string

print(msg[0:5]) #prints the msg from 0 inclusive to 5 exclusive

print(msg.count('l')); #prints the number of l present in string

print(msg.find("World")) #finds the first index of the string that is passed otherwise -1 is printed

print(msg.find("l")) # prints the first index of l


new_msg = msg.replace("World", "Universe") # takes 2 arguments and returns a new string replaced with the second argument of replace. it returns so we need a new variable

print(new_msg) #prints the new message with the replaced word

#concatination of string using place holders for formatted strings

greeting = 'hello'
name = 'michael'

message = '{}, {}. Welcome'.format(greeting,name)

print(message) 
