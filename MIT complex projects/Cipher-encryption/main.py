'''
The Caesar Cipher

The idea of the Caesar Cipher is to pick an integer and shift every letter of your message by that integer. In other words, suppose the shift is k . Then, all instances of the i-th letter of the alphabet that appear in the plaintext should become the (i+k)-th letter of the alphabet in the ciphertext. You will need to be careful with the case in which i + k > 26 (the length of the alphabet). Here is what the whole alphabet looks like shifted three spots to the right:

Original:  a b c d e f g h i j k l m n o p q r s t u v w x y z
 3-shift:  d e f g h i j k l m n o p q r s t u v w x y z a b c
'''

def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

#### 1st PROBLEM ####

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        slist=[]
        list1=list('abcdefghijklmnopqrstuvwxyz')
        slist1=(list1[shift:])
        slist2=(list1[:shift])
        slist=slist1+slist2

        dict1={}
        for i in range(26):
            dict1[list1[i]]=slist[i]

        uslist=[]
        ulist1=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        uslist1=(ulist1[shift:])
        uslist2=(ulist1[:shift])
        uslist=uslist1+uslist2

        for i in range(26):
          dict1[ulist1[i]]=uslist[i]
        return dict1


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        slist=[]
        list1=list('abcdefghijklmnopqrstuvwxyz')
        slist1=(list1[shift:])
        slist2=(list1[:shift])
        slist=slist1+slist2

        dict1={}
        for i in range(26):
            dict1[list1[i]]=slist[i]

        uslist=[]
        ulist1=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        uslist1=(ulist1[shift:])
        uslist2=(ulist1[:shift])
        uslist=uslist1+uslist2
        total=list1+ulist1

        for i in range(26):
          dict1[ulist1[i]]=uslist[i]  
        
        
        listedm=list(self.message_text)

        a=""

        for i in range(len(listedm)):
          if list(listedm)[i] in total:
            a+=(dict1[listedm[i]])
          else:
            a+=(listedm[i])
        return a


#### 2nd PROBLEM ####


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self,shift)
        self.message_text_encrypted = Message.apply_shift(self,shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift=shift
        self.encrypting_dict = Message.build_shift_dict(self,shift)
        self.message_text_encrypted = Message.apply_shift(self,shift)


#### 3rd PROBLEM ####


class CiphertextMessage(Message):
    def __init__(self, text):
        Message.__init__(self, text)
        self.best_shift = ()

    def decrypt_message(self):
        most_real_words = 0

        for shift in range(26):
            real_words = 0
            test_cipher = self.apply_shift(shift).split()
            for word in test_cipher:
                if word in self.valid_words:
                    real_words += 1

            if not self.best_shift:
                self.best_shift = (shift, self.apply_shift(shift))

            if real_words > most_real_words:
                self.best_shift = (shift, self.apply_shift(shift))
                most_real_words = real_words

        return self.best_shift


#### 4th PROBLEM ####


def decrypt_story():
    print(CiphertextMessage(get_story_string()).decrypt_message())

decrypt_story()
#output(the shift number, the encrypted or decrypted message)