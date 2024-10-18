import random

def password_generator(pw_lens):
    data_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@$^&**_"
    passwords_list = [] 
    for length in pw_lens:  # Iterate over the list of password lengths
        password = '' 
        for j in range(length):  # Use the length directly to generate password
            nxt_ind = random.randrange(len(data_string))
            password += data_string[nxt_ind]  # Concatenate using += for clarity
        passwords_list.append(password) 
    return passwords_list
 
n = int(input("Number of passwords to generate: "))
print('Generating', n, 'PASSWORDS')
password_lengths = []
for i in range(n):
    print('NOTE==> Minimum length of password is 6!')
    length = int(input('Enter the length of password ' + str(i + 1) + ': '))
    if length < 6:
        length = 6
        print('Length set to minimum of 6.')
    password_lengths.append(length)

# Generate passwords with the specified lengths
passwords = password_generator(password_lengths)
for i in range(n):
    print('Password', i + 1, '=', passwords[i])
