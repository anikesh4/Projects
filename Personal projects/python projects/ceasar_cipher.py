alphabet_list=['#','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

def Next_alphabet(num,key):
    new_num=(num+key)%26
    if new_num==0:
        new_num=26
    return new_num

def previous_alphabet(num,key):
    new_num=(num-key)
    if new_num==0:
        new_num=26
    if new_num<0:
        new_num+=26
    return new_num

while True:
	key=int(input('Please enter a key for the Cipher, between 1 and 25: '))
	string=list(input('Enter the message to be encrypted: ').lower())
	for letter in range(len(string)):
	    if string[letter] in 'qwertyuiopasdfghjklzxcvbnm':
	        string[letter]=alphabet_list[Next_alphabet(alphabet_dict[string[letter]],key)]
	new_string="".join(string)
	print(f'The message has been encrypted: {new_string}')

	print("\n\n")

	key=int(input('Please enter a key for the Cipher, between 1 and 25: '))
	string=list(input('Enter the message to be decrypted: ').lower())
	for letter in range(len(string)):
	    if string[letter] in 'qwertyuiopasdfghjklzxcvbnm':
	    	string[letter]=alphabet_list[previous_alphabet(alphabet_dict[string[letter]],key)]
	new_string="".join(string)
	print(f'The message has been decrypted: {new_string}')

	again=" "
	while again!='yes' and again !='no':
		again= input("Do you want to play again, 'yes' or 'no'??:  ").lower()

	if again=='no':
		print("See you next time!!!")
		break