import copy

def simplify(c):  # if p and !P are in a clause, removes both
    clause = list(c)
    for l in clause:
        negated = '!'+l
        if negated in clause:
            clause.remove(l)
            clause.remove(negated)
    return tuple(clause)

def DPLL_Satisfiable(s):
    # input s is an array of clauses, where each clause is an array of the literals
    clauses = set()
    symbols = set()
    for x in s:
        clauses.add(tuple(sorted(x)))   #sorts the literals so that equal clauses can be removed
    new_clauses = set()
    for clause in clauses:
        simplfied = simplify(clause)
        if len(simplfied) != 0:
            new_clauses.add(simplfied)
    for c in new_clauses:   #adds unique symbols to a set
        for l in c:
            if len(l) == 2:
                symbols.add(l[1])
            else:
                symbols.add(l)
    DPLL(new_clauses, symbols, {})

def Find_Pure_Symbol(symbols, clauses, model):  #if p is in a clause and !p is not in any clause, then p is a pure symbol
    for x in symbols:
        if x[0] == '!':
            search = x[1]
        elif x[0] != '!':
            search = '!'+x[0]
        pure = True
        if search not in model:
            for clause in clauses:
                if search not in clause:
                    pure = True
                else:
                    pure = False
                    break
        if pure:
            return x, True
    return None, None

def Find_Unit_Clause(clauses, model):   #if only 1 literal is in a clause, assign truth value to that literal to make the clause
    new_subs = set()
    for clause in clauses:
        new_clause = set()
        for x in clause:
            if x in model:
                if model[x] == True:
                    new_clause = ()
                    break
            else:
                new_clause.add(x)
        if new_clause != ():
            new_subs.add(tuple(new_clause))
    for clause in new_subs:
        if len(clause) == 1:
            if len(clause[0]) == 1 and clause[0] not in model:
                return clause[0], True
            elif len(clause[0]) == 2 and clause[0][1] not in model:
                return clause[0], False
    return None, None

def substitute(clauses, model): #assigns the values specified in the model to the literals
    substitution=set()
    for x in clauses:
        subs = set()
        for literal in x:
            if len(literal) == 2:
                if literal[1] in model:
                    subs.add(not(model[literal[1]]))
                else:
                    subs.add(literal)
            else:
                if literal in model:
                    subs.add(model[literal[0]])
                else:
                    subs.add(literal)
        substitution.add(tuple(subs))
    true_clauses=0
    for x in substitution:
        if len(x)==1 and x[0]==False:
            return -1   # there exists 1 false clause so entirely false
        elif True in x:
            true_clauses+=1 # all clauses are true so satisfiable
    if true_clauses==len(substitution):
        return 1
    return 0

sat=-1
def DPLL(clauses, symbols, model):
    global sat
    if len(model)==0:#first iteration
        sat=-1
    substitution = set()
    every_clause_true = -1
    value=substitute(clauses,model)
    if (value == 1):
        print('Satisfiable')
        print('Assignment: ',model)
        sat=1
        return True
    elif value==-1:
        return False
    P, value = Find_Pure_Symbol(symbols, clauses, model)
    if P:
        symbols.remove(P)
        model[P] = value
        return DPLL(clauses, symbols, model)
    P, value = Find_Unit_Clause(clauses, model)
    if P:
        if P[0] == '!' :
            if P[1] in symbols:
                symbols.remove(P[1])
            model[P[1]] = value
        else:
            if P in symbols:
                symbols.remove(P)
            model[P] = value
        return DPLL(clauses, symbols, model)
    P = symbols.pop()
    rest = symbols
    new_model_1 = copy.deepcopy(model)
    new_model_2 = copy.deepcopy(model)
    new_model_1[P] = True
    new_model_2[P] = False
    return DPLL(clauses, rest, new_model_1) or DPLL(clauses, rest, new_model_2)

sentences=[[{'!a'},{'a'}],[{'a','!b'},{'a','b'}],[{'p','p','!p','q'},{'!q','r'}]]
for sentence in sentences:
    print('\nSentence: ',sentence)
    DPLL_Satisfiable(sentence)
    if sat==-1:
        print('Unsatisfiable')
            

"""
OUTPUT

Sentence:  [{'!a'}, {'a'}]
Unsatisfiable

Sentence:  [{'!b', 'a'}, {'b', 'a'}]
Satisfiable
Assignment:  {'a': True}

Sentence:  [{'q', '!p', 'p'}, {'r', '!q'}]
Satisfiable
Assignment:  {'r': True, 'q': True}
"""