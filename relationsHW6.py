# Universidad del Valle de Guatemala
# Matematica Discreta - seccion 10
# Gustavo Mendez - 18500
# Archivo: relationsHW6.py
# Fecha: 30/09/2019
# Desc: Modulo que se encarga de realizar operaciones de relaciones, con una matriz inicial

#For all matrix operations, we need Numpy
import numpy as np;

#IO UTILS
def validateNumber(variable):
    try:
        #Try cast
        int(variable)
        return True
    except ValueError:
        return False


def isOptionInRange(x, a, b):
    #Validates range
    if(x >= a and x <= b) or (x <= a and x >= b):
        return True
    return False


#MATRIX RELATION PROPERTIES UTILS
def isReflexive(binaryMatrix):
	identityBinary = BinaryRelationMatrix(identityMatrix)
	return(identityBinary.precedence(binaryMatrix.matrix))

#Returns True if A = A**T (transposed)
def isSymmetric(binaryMatrix):
	return(binaryMatrix.equals(binaryMatrix.transposed()))

#Retuns True if	A (intersection) A**T (transposed) <= I												
def isAntisymmetric(binaryMatrix):
    # Calculate Identity Matrix
    identityMatrix = []
    return((binaryMatrix.intersection(binaryMatrix.transposed())).precedence(identityMatrix))

# Returns True if A**2 <= A
def isTransitive(binaryMatrix):
		return((binaryMatrix.multiplication(binaryMatrix.matrix)).precedence(binaryMatrix.matrix))



#Class for relation matrix management
class BinaryRelationMatrix(object):

	def __init__(self, matrix):
        #Numpy matrix
		self.matrix = matrix

	def multiplication(self, inputMatrix):
		dotMatrix = np.dot(self.matrix, inputMatrix)
		return BinaryRelationMatrix(dotMatrix)
        
    def intersection(self, inputMatrix):
        a = np.array(self.matrix, dtype=bool)
        b = np.array(inputMatrix, dtype=bool)
        return BinaryRelationMatrix(1*np.dot(a,b))

	def precedence(self, inputMatrix):
		#Not implemented yet
		return True

	def transposed(self):
		return self.matrix.transpose()

	def equals(self, inputMatrix):
		return np.array_equal(self.matrix, inputMatrix)


print("WELCOME!\n")
option = 1

while(option != 2):
    print("""
    ***********************
    Choose an option:
    1. Show relation matrix properties
    2. Exit
    ***********************
    """)
    option = input("> ")
    if(validateNumber(option)):
        option = int(option)
        #Check if option is in range
        validRange = isOptionInRange(option, 1, 2)
        if(validRange):
            if(option == 1): #Check Matrix properties
                print("""
                    ______                          _   _           
                    | ___ \                        | | (_)          
                    | |_/ / __ ___  _ __   ___ _ __| |_ _  ___  ___ 
                    |  __/ '__/ _ \| '_ \ / _ \ '__| __| |/ _ \/ __|
                    | |  | | | (_) | |_) |  __/ |  | |_| |  __/\__ \\
                    \_|  |_|  \___/| .__/ \___|_|   \__|_|\___||___/
                                | |                              
                                |_|                              

                    Please, enter a relation matrix. 
                    Type 'end' to get properties.

                    > 1 0 1
                    > 1 1 1
                    > 1 0 0
                    > end
                """)

                myRelationMatrix = []
                matrixLine = input("> ")
                while(matrixLine != 'end'):
                    newRow = matrixLine.split(' ')
                    myRelationMatrix.append(newRow)
                    matrixLine = input("> ")
                
                matrix = BinaryRelationMatrix(myRelationMatrix)

                print("*****************************")
                if(isReflexive(matrix)):
                    print("* Is reflexivity")
                if(isSymmetric(matrix)):
                    print("* Is symmetry")
                if(isAntisymmetric(matrix)):
                    print("* Is antisymmetry")
                if (isTransitive(matrix)):
                    print("* Is ransitivity")
                print("******************************")
                
                
            elif(option == 2): #Exit
                print("Exit...")
        else:
            print('Value out of range, try again...')
    else:
        print("Value is not a valid number, try again...")
