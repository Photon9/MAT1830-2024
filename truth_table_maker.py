import sympy

class node():
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

class truth_table():
    
    def __init__(self, variables):
        self.variables = variables
        self.sentence = None
        self.columns = []
    

    def parse_sentence(self, sentence: str) -> tuple[int, list]:
        clause_start = 0
        output = []
        while sentence[clause_start] != '(' and clause_start < len(sentence):
            clause_start += 1
                                        
        
