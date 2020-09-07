import re

print("Welcome to \"Not So SoftBank!\" Type \"quit\" to exit.")
# sentence = "wow fs 434s!!1 balance?"
#Tokenizing input sentence and removing all punctuation.

def tokenize(sentence):
    sentence = " ".join(re.findall(r"[a-zA-Z0-9]+", sentence))
    sentence = sentence.split()
    # print(sentence)
    return sentence

#To scale up the use of this chatbot, I can move all keywords below to another file and then build my dictonary after lemmatizing and adding all synonyms.

#Balance Function
balance = r"\b[bB]a?la?nce?\b|\b[sS]tatus\b|\b[mM]oney\b|\b[lL]eft\b"
balance_response = "Your account balance is $342,869.90"

#Transaction Function
transaction = (r"\b[tT]ransact(ion)?\b|\b[sS]pent?d?(ing)?\b|\b[pP]urchase?(ing)?\b|\b[lL]ast\b|\b[rR]emov(e|al)\b|\b[lL]ast\b|\b[bB]uy\b|\b[bB]ought\b|\b[eE]xpenses?\b")
deb_response = "Last Debit transaction: 19/09/20 TACO BELL Amt: $18.00"

#Function to identify inputs and respond to different keyword matches
def debit_respond(sentence):
    sentence = tokenize(sentence)
    output = ""
    bot = "Bot: "
    for token in sentence:
        if re.search(balance, token):
            output = balance_response
            print(bot + output)
            break
        elif re.search(transaction, token):
            output = deb_response
            print(bot + output)
            break
        else:
            continue

    if output == "":
        print("I can’t answer that. Please contact the branch.")

#Credit Function 
outstanding = (r"\b[oO]utsta?n?d(ing)?|\b[lL]imits?\b|\b[cC]redit\b")
credit_response = "You've $12458.70 remaining left of your credit card spending limit."

#Payment Function
credit_payment_inputs = (r"[pP]ay(ment)?|[dD]ue|\b[bB]ill(ing)?\b|\b[rR]eceipts?\b")
payment_response = "Your credit card bill is $1895.30 and is due on 23/10/2020"

cred_response = "Last Credit transaction: 21/09/20 STARK INDUSTRIES Amt: $2400.00"

def credit_respond(sentence):
    sentence = tokenize(sentence)
    output = ""
    bot = "Bot: "
    for token in sentence:
        if re.search(balance, token):
            output = balance_response
            print(bot + output)
            break
        elif re.search(outstanding, token):
            output = credit_response
            print(bot + output)
            break
        elif re.search(credit_payment_inputs, token):
            output = payment_response
            print(bot + output)
            break
        elif re.search(transaction, token):
            output = cred_response
            print(bot + output)
            break
        else:
            continue

    if output == "":
        print("I can’t answer that. Please contact the branch.")

#Function to continuously run and accept inputs
def credit_bot():
    run = True
    while run == True:
        sentence = input("You: ")
        if sentence == "quit":
            run = False
            print("Thank You for visiting!")
        else:
            credit_respond(sentence)

def debit_bot():
    run = True
    while run == True:
        sentence = input("You: ")
        if sentence == "quit":
            run = False
            print("Thank You for visiting!")
        else:
            debit_respond(sentence)

#Validating the User's Account Number. It'll only authenticate if the input is a 7-digit numeric value.
def validation():
    validate = False
    answer = False
    account = r"^\d{7}$"
    while validate == False:
        number = input("Bot: Please Enter Your 7-digit account number: ")
        if re.search(account, number):
            print("Authentication Successful! Welcome Mr. Stark!")
            validate = True
            print("What would you like to check today?")
            while answer == False:
                selection = input("Credit or Debit?: ")
                if re.search( r"\b[cC]redit\b" , selection):
                    print("Welcome to the Credit Section! How can I help you?")
                    answer = True
                    credit_bot()
                elif re.search( r"\b[dD]ebit\b" , selection):
                    print("Welcome to the Debit Section! How can I help you?")
                    answer = True
                    debit_bot()
                elif selection == "quit":
                    return
                else:
                    print("Bot: Invalid Response! Please enter a Valid Input!")
        elif number == "quit":
            return
        else:
            print("Bot: Invalid Response! Please enter a Valid Input!")

validation()
# tokenize(sentence)