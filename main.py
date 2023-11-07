# code by Lilith Richter-Stephenson 40288772

from typing import Dict, List

"""Evaluates a valid statement list containing boolean values and logical connectives"""
def evaluate(statement: List):

    #This will find and evaluate every set of brackets
    #The innermost bracket content will be evaluate first
    while "(" in statement:

        #finds the first closing bracket
        closing = statement.index(")")

        #Finds the matching opening bracket by iterating backwards from the closing bracket
        for i in range(closing,-1,-1):

            #sets opening bracket index and breaks out of the loop at the first opening bracket
            if statement[i]=="(":
                opening = i
                break

        #resets the statement, evaluating what is inside the brackets
        statement = statement[0:opening]+evaluate(statement[opening+1:closing])+statement[closing+1:]


    #evaluates all negations before evaluating other connectives
    while "not" in statement:

        #sets n to the first "not" within the statement
        n = statement.index("not")

        #In the case of multiple negations, this increments n until the last negation is found
        while statement[n+1]=="not":
            n+=1

        #sets start of statement to the statement up until the negation
        start_of_statement = statement[0:n]

        #appends the negated truth value to the start of statement
        '''This could also be done by setting statement[n] to negation(statement[n+1]) 
        and setting statement equal to statement[:n+1]+statement[:n+2]'''
        start_of_statement.append(negation(statement[n+1]))

        #Adds the end of the statement to appended start of statement
        statement = start_of_statement+statement[n+2:]


    """repeats the equivalent process for and, or, if, and iff in order"""

    while "and" in statement:
        a = statement.index("and")
        start_of_statement = statement[0:a-1]
        start_of_statement.append(conjunction(statement[a-1],statement[a+1]))
        statement = start_of_statement+statement[a+2:]

    while "or" in statement:
        o = statement.index("or")
        start_of_statement = statement[0:o-1]
        start_of_statement.append(disjunction(statement[o-1],statement[o+1]))
        statement = start_of_statement+statement[o+2:]

    while "if" in statement:
        i = statement.index("if")
        start_of_statement = statement[0:i-1]
        start_of_statement.append(implication(statement[i-1],statement[i+1]))
        statement = start_of_statement+statement[i+2:]
   
    while "iff" in statement:
        iff = statement.index("iff")
        start_of_statement = statement[0:iff-1]
        start_of_statement.append(implication(statement[iff-1],statement[iff+1]))
        statement = start_of_statement+statement[iff+2:]

    #returns the evaluated statement. The first statement to be evaluated will be the statement 
    #within the rightmost, innermost brackets
    return statement
   

#Logical not
def negation(arg: bool)->bool:
    return not arg

#Logical and
def conjunction(p: bool,q: bool)->bool:
    return p and q

#Logical or
def disjunction(p: bool,q: bool)->bool:
    return p or q

#Conditional    
def implication(hypothesis: bool, conclusion: bool)->bool:
    if hypothesis==False:
        return True
    if hypothesis==True and conclusion==True:
        return True
    else:
        return False

#Biconditional    
def biconditional(p: bool, q: bool)-> bool:
    if p==q:
        return True
    else:
        return False
   



def evaluate_statement(statement: str, propositional_variables: Dict[str, bool]) -> bool:
    """
    Evaluates a statement and returns a boolean value.
    The statement can be a simple statement or a compound statement.
    Valid operators are: IF, IFF, AND, OR, NOT, (, ).
    Valid operands are: true, false, and any variable names such as p1, p2, p3, etc.

    Note1: You are not allowed to use eval() while you are allowed to use simpler
    functions such as split().

    To make your life easier, you might separate operators and operands by spaces.

    Parameters:
    statement (str): a statement to evaluate
    propositional_variables (dict): a dictionary of propositional variables and their values
        - key (str): a propositional variable name
        - value (bool): a boolean value

    Returns:
    bool: a boolean value as the result of the statement

    Examples:
    >>> evaluate_statement('true', {})
    True

    >>> evaluate_statement('false AND p1', {'p1': True})
    False

    >>> evaluate_statement('p1 AND p2', {'p1': True, 'p2': False})
    False

    >>> evaluate_statement('( p1 IF p2 )', {'p1': False, 'p2': True})
    True
    """
    # write your code here

    #Turns the space separated statement into a list
    expression_list = statement.split()
   
    #Sets propositional variables to their truth values and sets all logical connectives to lower case
    for i,s in enumerate(expression_list):
        s.strip()
        if s in propositional_variables:
            expression_list[i] = propositional_variables[s]
        else:
            expression_list[i] = s.lower()


    #evaluates the expression list 
    new_exp=evaluate(expression_list)

    #given valid input, this conditional branch will always be taken
    if len(new_exp)==1:
        return new_exp[0]
    else:
        print("uh oh, looks like your expression was not solvable")
   

    # you can add helper methods if you want and use them here to improve your code readabilty
   
"""Takes a number and an empty string and returns a string of all possible truth value 
combinations for n variables. This will be returned in the form: "TT TF FT FF" """
def make_combos(n: int, combos: str)->str:
    #does not recurse when n==0
    if (n==0):
        return combos
    
    #otherwise calls itself twice, decrementing n and adding "T" to one branch and "F" to the other
    else:
        return make_combos(n-1,combos+"T")+make_combos(n-1,combos+"F")
       

def generate_truth_table(statement: str, propositional_variables: List[str]):
    """
    This method generates a truth table for a given statement and prints it to the console.
    Also, it does not necessarily return anything. But the truth table must be printed by calling
    this function and passing in the statement.

    Note that you are not allowed to use eval() while you are allowed to use simpler
    functions such as split().

    To make your life easier, you might separate operators and operands by spaces.

    Parameters:
    statement (str): a statement to evaluate
    propositional_variables (List[str]): a list of propositional variables.

    Examples:
    >>> generate_truth_table('false AND p1', ['p1'])
    True  =>  False
    False =>  False

    >>> generate_truth_table('p1 IF p2', ['p1', 'p2'])
    True    |  False =>  False
    False   |  True  =>  True
    False   |  False =>  True
    True    |  True  =>  True
    """
    # write your code here
    # this part of the code will be evaluated manually
    # print the truth table to the console
    # print(truth_table)
    # you can add helper methods if you want and use them here to improve your code readabilty


    #makes a list of all possible truth values based on the number of propositional variables
    #example n==2, combos_list = ["TT","TF","FT","FF"]
    n=len(propositional_variables)
    combos= make_combos(n," ")
    combos_list = combos.split()


    #prints a header with the names of variables and a divider
    to_print = ""
    for prop in propositional_variables:
        to_print+=prop+"        "
    print("\n"+to_print)
    print("_____________________________________\n")

    #creates a dictionary to store the truth values of each combination of truth values
    propositional_values = {}


    #This will print a line (for each combination of truth values) with the truth values 
    # of each propositional variable and the truth values of the evaluated statement
    for combo in combos_list:

        #resets this value for each line
        to_print=""

        #iterates through each truth value within the given combination
        for index, prop in enumerate(propositional_variables):

            #sets boolean value for each propositional variable and appends this value to to_print with formatting
            if combo[index]=="T":
                propositional_values[prop] = True
                if index == len(propositional_variables)-1:
                    to_print += str(propositional_values[prop]) +"   =>  "
                else:
                    to_print += str(propositional_values[prop]) +"   |  "
            else:
                propositional_values[prop] = False
                if index == len(propositional_variables)-1:
                    to_print += str(propositional_values[prop]) +"  =>  "
                else:
                    to_print += str(propositional_values[prop]) +"  |  "

        # prints the formatted list of propositional truth values along with the result of the statement 
        # (evalueted with the current truth values)
        print(to_print, evaluate_statement(statement,propositional_values))
                
            
   


def statement_type(statement: str, propositional_variables: List[str]) -> str:
    """
    This method determines the type of a statement and returns it as a string.
    Valid return types are: tautology, contradiction, contingency.

    Note that the returned string must be one of the valid return types.

    Parameters:
    statement (str): a statement to evaluate
    propositional_variables (List[str]): a list of propositional variables.

    Returns:
    str: a string representing the type of the statement

    Examples:
    >>> statement_type('true', {})
    'tautology'

    >>> statement_type('false AND p1', ['p1'])
    'contradiction'

    >>> statement_type('p1 IF p2', ['p1', 'p2'])
    'contingency'
    """
    # write your code here
    # you can add helper methods if you want and use them here to improve your code readabilty

    #makes a list of all possible truth values based on the number of propositional variables
    #example n==2, combos_list = ["TT","TF","FT","FF"]    
    n=len(propositional_variables)
    combos= make_combos(n," ")
    combos_list = combos.split()

    #creates a dictionary to store the truth values of each combination of truth values
    propositional_values = {}

    #creates a list to hold the outcomes of the evaluated statement
    outcomes = []


    #sets proposional variables and evaluates the expression
    for combo in combos_list:
        for index, prop in enumerate(propositional_variables):
            if combo[index]=="T":
                propositional_values[prop] = True
            else:
                propositional_values[prop] = False

        outcomes.append(evaluate_statement(statement,propositional_values))


    if False not in outcomes:
        return "tautology"
    if True not in outcomes:
        return "contradiction"
    return "contingency"





def main():
    """
    In the main method, if you wish to receive the code from user and show the results
    to the user, you can do so. But this is not required.
    """


    # write your code here
    #print(evaluate_statement("p1 and not not p2",{"p1":True,"p2":True}))
    #generate_truth_table("p1 and not not not not not p2",["p1","p2"])
    print(evaluate_statement('P1 IFF P2', {'P1': True, 'P2': False}))
    print(evaluate_statement('P1 IF ( P2 OR NOT P3 )', {'P1': True, 'P2': False, 'P3': True}))
    print(evaluate_statement('( NOT P1 AND ( P1 OR P2 ) ) IF P2', {'P1': False, 'P2': False}))
    print(evaluate_statement('( NOT P1 AND ( P1 OR P2 ) ) IF P2', {'P1': False, 'P2': True}))
    print(evaluate_statement('( NOT P1 AND ( P1 OR P2 ) ) IF P2', {'P1': True, 'P2': False}))
    print(evaluate_statement('( NOT P1 AND ( P1 OR P2 ) ) IF P2', {'P1': True, 'P2': True}))
    print(evaluate_statement('P2 AND ( ( P1 AND P1 ) IF NOT ( P2 ) ) AND ( NOT P1 IF NOT P2 )', {'P1': True, 'P2': True}))

    print(evaluate_statement('P2 AND ( P1 IF NOT P2 ) AND ( NOT P1 IF NOT P2 )', {'P1': True, 'P2': False}))
    print(evaluate_statement('P2 AND ( P1 IF NOT P2 ) AND ( NOT P1 IF NOT P2 )', {'P1': False, 'P2': True}))
    print(evaluate_statement('P2 AND ( P1 IF NOT P2 ) AND ( NOT P1 IF NOT P2 )', {'P1': False, 'P2': False}))
    print(evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': True, 'P2': True, 'P3': True}))
    print(evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': True, 'P2': True, 'P3': False}))
    print(evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': False, 'P2': True, 'P3': False}))
    print(evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': True, 'P2': False, 'P3': False}))
    print(evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': True, 'P2': False, 'P3': True}))
    print(evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': False, 'P2': False, 'P3': True}))
    print(evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': False, 'P2': True, 'P3': True}))
    print(evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': False, 'P2': False, 'P3': False}))

if __name__ == "__main__":
    print(main())


###################### Helper Methods ######################

# If you want to add helper methods, you can define them here
# and reuse them in the methods above.

# def helper_method():
#     something_else = does_something()
#     return something_else


###################### Helper Methods ######################



