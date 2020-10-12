import random

class sorting: # We initalise the class
    def swap(self, lst, x, y): # Used to swap two numbers in a list
        temp = lst[x] # We need a temp value otherwise the swap will not work
        lst[x] = lst[y] # Swap the values
        lst[y] = temp
        return lst # Retuen the swapped list

    def shuffle(self, lst):
        for i in range(len(lst)): # Loop over the indexes of the list
            lst = self.swap(lst, i, random.randint(0, len(lst)-1)) # Swap the current index nd a radom one
            yield lst # Yield the current state of the list

    def bubble(self, lst):
        checks = 0 # Check is used to count how many times we ran an if statement
        for y in range(len(lst), -1, -1): # We iterate backwords over the length of the list
            for x in range(y): # Loop over the indexs remaining to be sorted
                try:
                    if lst[x] > lst[x+1]: # Check if the numbers are larger than eachother
                        lst = self.swap(lst, x, x+1) # Swap them
                except IndexError: # Too lazy to do stuff so this indxust catches the error
                    pass

                checks += 1 # We have 1 if here so we inceace the number by one

                yield lst, checks # We yield the current state and the result becomes a genarator obindxect

    def selection(self, lst):
        checks = 0 # Check is used to count how many times we ran an if statement
        for i in range(len(lst)): #loop over the indexes of the list
            indxMin = i # We start the loop from where our indexer is

            for x in range(i+1, len(lst)): # We loop over the values remaning
                if lst[indxMin] > lst[x]: # Check if the value is smaller than the current smallest index
                    indxMin = x # Update the minimum index variable

                checks += 1 # We did another check here so incerace it by one

            lst = self.swap(lst, i, indxMin) # Swap the current index and the minimum index variables

            yield lst, checks

    def insert(self, lst):
        checks = 0 # Check is used to count how many times we ran an if statement
        for i in range(1, len(lst)): # Loop over the indexes of the list

            key = lst[i] # Set the key variable for verifying later

            indx = i-1 # Keep track of the items index we are working with
            while indx >= 0 and key < lst[indx]: # Only stop moving it back when we know its been moved correctly
                lst[indx + 1] = lst[indx] # Update and move the index
                indx -= 1 # Decreace the index variable by one

                checks += 1 # We did a check in the form of the while loop so same here

                yield lst, checks# Return the list for displaying

            lst[indx + 1] = key # Uppdate the list finally to match up
