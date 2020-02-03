def hometown_test(hometown):
    if hometown == "Hayward":
        return True
    else:
        return False


def full_name(firstName, lastName):
    fullName = firstName + " " + lastName
    return fullName


def greeting(firstName, lastName, homeTown):
    #case for matching hometown
    if homeTown == "Hayward":
        print("Hi " + firstName + " " + lastName + ", we're from the same place!")
    #case for non-matching hometown
    else:
        print("Hi " + firstName + " " + lastName + ", I'd like you to visit " + homeTown + "!")


def type_of_fruit(berry):
    if berry == "strawberry":
        return True
    elif berry == "raspberry":
        return True
    elif berry == "blackberry":
        return True
    elif berry == "currant":
        return True
    else:
        return False


def shipping_cost(item):
    if item == "berry":
        return 0
    else:
        return 5


def total_cost(price, state, tax):
    price = int(price)
    tax = float(tax/100)
    #case for CA
    if state == "CA":
        price = price + (price* tax)
        price = price + (price*0.03)
    #case for PA
    elif state == "PA":
        price = (price + (price* tax))+2
    #case for MA
    else:
        if price <= 100:
            price = (price + (price* tax)) + 1
        else:
            price = (price + (price* tax)) + 3
    return price


def arbitrary_args(myList, *args):
    #making a list out of the arbitrary amount of arguments
    listOfAddlArgs = [*args]
    for item in listOfAddlArgs:
        #appending all arbitrary arguments to myList
        myList.append(item)
    return myList


def create_tuple_word(word):
    #fucntion to triple the input word
    def triple_word(word):
        tripleWord = word+word+word
        return tripleWord
    #making the tuple
    tripleWordTuple = (word, triple_word(word))
    return tripleWordTuple
