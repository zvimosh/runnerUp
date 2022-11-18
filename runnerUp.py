scores = [] # create empty list 
#scores = [4,6,23,1,4,37,7] # Example list if you don't want to enter your own

def calcRunnerup(scores): # calculate runner up with list sort
    scores.sort()
    print ("Number of items in the list = {0}".format(len(scores)))
    print("Runner up nubmer is: {0}".format(scores[-2]))

def validateInput(scores): # validate input
    if isinstance(scores, list):
        if len(scores) < 2:
            print("Please enter at least two numbers")
        else:
            calcRunnerup(scores)
    else:
        print("Invalid input")

if __name__ == '__main__':
    if len(scores) == 0: # check if the list is empty, if so, ask for input
        try:
            while True:
                scores.append(int(input("Please enter a number, enter any other key to stop: ")))
        except:
            print("The Scores entered are: {0}".format(scores))
    validateInput(scores)

