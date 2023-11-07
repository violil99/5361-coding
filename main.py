from typing import Dict, List

def evaluate(statement: List):
    while "(" in statement:
        closing = statement.index(")")
        for i in range(closing,-1,-1):
            if statement[i]=="(":
                opening = i
                break

        statement = statement[0:opening]+evaluate(statement[opening+1:closing])+statement[closing+1:]


    while "not" in statement:
        n = statement.index("not")
        start_of_statement = statement[0:n]
        start_of_statement.append(negation(statement[n+1]))
        statement = start_of_statement+statement[n+2:]

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

    expression_list = statement.split()
   
    for i,s in enumerate(expression_list):
        s.strip()
        if s in propositional_variables:
            expression_list[i] = propositional_variables[s]
        else:
            expression_list[i] = s.lower()


    new_exp=evaluate(expression_list)
    return new_exp[0]
   
    ##DEAL WITH NOTS BEFORE PROPOSITIONS. MAYBE JUST MAKE THIS PART OF YOUR TREE

    ##SEPARATE OUT EXPRESSIONS BASED ON BRACKETS (TREE OR STACK)

    ##EVALUATE BRACKETS IN CORRECT ORDER NOT, AND, OR, IF, IFF
       





    # you can add helper methods if you want and use them here to improve your code readabilty
   
def make_combos(n: int, combos: str)->str:
    if (n==0):
        return combos
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


    n=len(propositional_variables)
    combos= make_combos(n," ")
    combos_list = combos.split()

    propositional_values = {}

    to_print = ""
    for prop in propositional_variables:
        to_print+=prop+"        "
    print("\n"+to_print)
    print("_____________________________________\n")


    for combo in combos_list:
        to_print=""
        for index, prop in enumerate(propositional_variables):
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
        
    n=len(propositional_variables)
    combos= make_combos(n," ")
    combos_list = combos.split()

    propositional_values = {}

    outcomes = []

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
    print(evaluate_statement("p1 and not not p2",{"p1":True,"p2":True}))
    '''print(evaluate_statement('P1 IF P2', {'P1': True, 'P2': False}))
    print(evaluate_statement('P1 IF ( P2 OR NOT P3 )', {'P1': True, 'P2': False, 'P3': True}))
    print(evaluate_statement('( NOT P1 AND ( P1 OR P2 ) ) IF P2', {'P1': False, 'P2': False}))
    print(evaluate_statement('( NOT P1 AND ( P1 OR P2 ) ) IF P2', {'P1': False, 'P2': True}))
    print(evaluate_statement('( NOT P1 AND ( P1 OR P2 ) ) IF P2', {'P1': True, 'P2': False}))
    print(evaluate_statement('( NOT P1 AND ( P1 OR P2 ) ) IF P2', {'P1': True, 'P2': True}))
    print(evaluate_statement('P2 AND ( P1 IF NOT P2 ) AND ( NOT P1 IF NOT P2 )', {'P1': True, 'P2': True}))
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
    print(evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': False, 'P2': False, 'P3': False}))'''

if __name__ == "__main__":
    print(main())


###################### Helper Methods ######################

# If you want to add helper methods, you can define them here
# and reuse them in the methods above.

# def helper_method():
#     something_else = does_something()
#     return something_else


###################### Helper Methods ######################



