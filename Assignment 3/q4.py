#define my variables

#receiving input command which is argument in functions
command = input("")

#if command is avg
if 'avg' in command:

#opening file
    file = open('C:\\Users\\vicky\\OneDrive\\SFU\\CMPT120\\Assignment 3\\grades.txt', 'r') 
    for line in file:
        line = line.rstrip()
        line_list = line.split(' ')
        print(line)


    # print("{:.2f}".format(average))

# #if command is gpa
# elif 'gpa' in command:
# #if command is fails
# elif 'fails' in command:
# #if command is quit
# else:
#     exit()