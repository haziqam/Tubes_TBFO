# Terminals
uppercase=[[chr(ord('A')+i)] for i in range(26)]
lowercase=[[chr(ord('a')+i)] for i in range(26)]
integer=[[chr(ord('0')+i)] for i in range(10)]
nonzero=[[chr(ord('1')+i)] for i in range(9)]
binary=[["+"],["-"],["*"],["/"],["%"],["|"],["^"],["&"]]
boolop=[["and"],["or"],["is"],["in"],["<"],[">"]]
unary=[["Not"],["+"],["-"],["~"]]
boolean=[["True"],["False"],["None"]]

# Rules of the grammar
R = {
    # Variables
    "V": [["V1","V2"]]+uppercase+lowercase+[['_']],
    "V1": uppercase+lowercase+[['_']],
    "V2": [["V2","V2"]]+uppercase+lowercase+integer+[['_']],

    # Integers
    "I": [["I", "I1"]]+integer,
    "I1": integer,

    # Floats (numeric)
    "F": [["I", "F1"], ["F2", "I"]],
    "F1": [["F2", "I"]],
    "F2": [["."]],

    # Booleans
    "B": [["true"], ["false"]],

    # Null
    "N": [["null"]],

    # Strings/char
    "S": [["S1", "S2"], ["S4", "S5"]],
    "S1": [['"']],
    "S2": [["S3", "S1"], ['"']],
    "S3": [["S3", "S3"], [["V2","V2"]]]+uppercase+lowercase+integer+[['_']],     # harusnya ASCII
    "S4": [["'"]],
    "S5": [["S3", "S4"], ["'"]],

    # Operators
    # Unary operators (prefix)
    "O1": [["+"], ["-"], ["~"], ["!"], ["delete"]],

    # Binary operators
    "O2": [["+"], ["-"], ["/"], ["*"], ["%"], ["<"], [">"], ["&"], ["|"], ["^"]],

    # Ternary operators
    "O3": [["?"]],

    # Expressions
    "E": [["V1", "V2"]]+uppercase+lowercase+integer+[['_'], ["I", "I1"], ["I", "F1"], ["S1", "S2"], ["S5", "S6"], ["true"], ["false"],
        ["null"], ["E2", "E3"], ["O1", "U2"], ["P", "U3"], ["M", "U4"], ["V", "U5"], ["V", "U6"], ["E", "B1"], ["E", "B2"], ["E", "B6"],
        ["E", "B13"], ["E", "T1"], ["A5", "E1"], ["A7", "A1"]],

    # Expression: variable / int / float / string / bool (literal) 
    # E: V1 V2 | A-Z | a-z | _ | II1 | 0-9 | IF1 | S1S2 | S5S6 | true | false | null  
    "E1": [["V1", "V2"]]+uppercase+lowercase+integer+[['_'], ["I", "I1"], ["I", "F1"], ["S1", "S2"], ["S5", "S6"], ["true"], ["false"], ["null"]],

    # Expression: (Expression)
    # E: E2 E3
    "E2": [["("]],
    "E3": [["E", "E4"], [[")"]]],
    "E4": [[")"]],

    # Expressions: (semua operasi yg ada di bawah)
    # E: O1 U2 | P U3 | M U4 | V U5 | V U6 | E B1 | E B2 | E B6 | E B13 | E T1 | A5 E1 | A7 A1

    # Unary
    "U": [["O1", "U2"], ["P", "U3"], ["M", "U4"], ["V", "U5"], ["V", "U6"]],

    # Unary: Operator + Operator + ... + Operand (expression)
    # U: O1 U2
    "U2": [["O1", "U2"]["V1", "V2"]]+uppercase+lowercase+integer+[['_'], ["I", "I1"], ["I", "F1"], ["S1", "S2"], ["S5", "S6"], ["true"], ["false"],
        ["null"], ["E2", "E3"], ["O1", "U2"], ["P", "U3"], ["M", "U4"], ["V", "U5"], ["V", "U6"], ["E", "B1"], ["E", "B2"], ["E", "B6"], ["E", "B13"],
        ["E", "T1"], ["A5", "E1"], ["A7", "A1"]],

    # Special case; increment and decrement (e.g. var++, --var)
    # U: P U3 | M U4 | V U5 | V U6
    "U3": [["P", "V"]],
    "P": [["+"]],
    "U4": ["M", "V"],
    "M": [["-"]],
    "U5": [["P", "P"]],
    "U5": [["M", "M"]],

    # Binary 
    "B": [["E", "B1"], ["E", "B2"], ["E", "B6"], ["E", "B13"]],

    # Binary: Operand + Operator + Operand + Operator + ... + Operand 
    # B: E B1
    "B1": [["O2", "B"], ["O2", "E"]],

    # >=, <=
    # B: E B2
    "B2": [["B3", "B4"]],
    "B3": [[">"], ["<"]], 
    "B4": [["B5", "E"]],
    "B5": [["="]],

    # ||, &&, >>, <<, **, ==
    # B: E B6
    "B6": [["B7", "E"]],
    "B7": [["B8", "B8"], ["B9", "B9"], ["B10", "B10"], ["B11", "B11"], ["B12", "B12"]],
    "B8": [["|"]],
    "B9": [["&"]],
    "B10": [[">"]],
    "B11": [["<"]],
    "B12": [["*"]],

    #  ===
    # B: E B13
    "B13": [["B5", "B14"]],
    "B14": [["B5", "B4"]],

    # Ternary: condition ? exprIfTrue : exprIfFalse
    "T": [["E", "T1"]],
    "T1": [["O3", "T2"]],
    "T2": [["E", "T3"]],
    "T3": [["T4", "E"]],
    "T4": [[":"]],

    # Assignment 
    "A": [["A5", "E1"], ["A7", "A1"]],

    # Assignment: X = Y = Z = ... (variable) = literal
    # A: A5 E1
    "A5": [["A5", "A5"], ["V", "A6"]],
    "A6": [["="]],

    # +=, -=, *=, /=, %=, |=, &=, ^=, >>=, <<=, ||=, &&=, **=
    # A: A7 A1
    "A7": [["A7", "A7"], ["V", "A8"]],
    "A8": [["A9", "A6"]],
    "A9": [["+"], ["-"], ["/"], ["*"], ["%"], ["&"], ["|"], ["^"], ["B8", "B8"], ["B9", "B9"], ["B10", "B10"], ["B11", "B11"], ["B12", "B12"]],

    # basic function
    "FU": [["FU1", "FU2"]],
    "FU1": [["function"]],
    "FU2": [["FU3", "FU4"]],
    "FU3": [["V1","V2"]]+uppercase+lowercase+[['_']],
    "FU4": [["FU5", "FU6"]],
    "FU5": [["("]],
    "FU6": [["FU7", "FU10"], ["FU7", "FU11"]],
    "FU7": [["empty"], ["V", "FU8"], ["V1", "V2"], ["DP", "FU8"], ["DP1", "V"], ["DP1", "I"], ["DP1", "S"]]+uppercase+lowercase+[['_']],
    "FU8": ["FU9", "FU7"],
    "FU9": [[","]],
    "FU10": [["RP", "FU11"]],
    "FU11": [["FU12", "STMTSW"]],
    "FU12": [[")"]],

    # Arrow function
    "AF": [["AF1", "AF2"], ["AF3", "AF10"], ["V", "AF10"]],
    "AF1": [["async"]],
    "AF2": [["AF3", "AF10"], ["V", "AF10"]],
    "AF3": [["AF4", "AF5"]],
    "AF4": [["("]],
    "AF5": [["AF6", "AF9"]],
    "AF6": [["empty"], ["V", "AF7"], ["V1", "V2"], ["DP", "AF7"], ["DP1", "V"], ["DP1", "I"], ["DP1", "S"]]+uppercase+lowercase+[['_']],
    "AF7": [["AF8", "AF6"]],
    "AF8": [[","]],
    "AF9": [[")"]],
    "AF10": [["AF11", "E"], ["AF11", "STMTSW"]],
    "AF11": [["=>"]],

    # default params
    "DP": [["DP1", "V"]],
    "DP1": [["V", "B5"]],

    # Rest params
    "RP": [["RP1", "V"]],
    "RP1": [["..."]],

    # const function
    "CF": [["CF1", "CF2"]],
    "CF1": [["const"]],
    "CF2": [["CF3", "AF"]],
    "CF3": [["V", "B5"]],

    # Getter
    "GE": [["GE1", "GE2"], ["GE1", "GE3"]],
    "GE1": [["get"]],
    "GE2": [["V", "GE3"], ["E", "GE3"]],
    "GE3": [["GE4", "STMTSW"]],
    "GE4": [["GE5", "GE6"]],
    "GE5": [["("]],
    "GE6": [[")"]],

    # Setter
    "SE": [["SE1", "SE2"], ["SE1", "SE3"]],
    "SE1": [["set"]],
    "SE2": [["V", "SE3"], ["E", "SE3"]],
    "SE3": [["SE4", "STMTSW"]],
    "SE4": [["SE5", "SE6"]],
    "SE5":  [["SE7", "V"]],
    "SE6": [[")"]],
    "SE7": [["("]],

    # function usage
    "FUS": [["FUS1", "FUS2"]],
    "FUS1": [["V1","V2"]]+uppercase+lowercase+[['_']],
    "FUS2": [["FUS3", "FUS4"]],
    "FUS3": [["("]],
    "FUS4": [["FUS5", "FUS8"], ["FUS5", "FUS9"]],
    "FUS5": [["empty"], ["V", "FUS6"], ["V1", "V2"], ["DP", "FUS6"], ["DP1", "V"], ["DP1", "I"], ["DP1", "S"]]+uppercase+lowercase+[['_']],
    "FUS6": [["FUS7", "FUS5"]],
    "FUS7": [[","]],
    "FUS8": [["RP", "FUS9"]],
    "FUS9": [[")"]],

    # Class: class variable {expression}
    "CL": [["CL1", "CL2"]],
    "CL1": [["class"]],
    "CL2": [["V", "STMTSW"]],

    # Constructor: CO1CO2 tambahin ke DLCR
    "CO": [["CO1", "CO2"]],
    "CO1": [["construtor"]],
    "CO2": [["CO3", "CO4"]],
    "CO3": [["("]],
    "CO4": [["CO5", "CO8"]],
    "CO5": [["empty"], ["V", "CO6"], ["V1", "V2"], ["DP", "CO6"], ["DP1", "V"], ["DP1", "I"], ["DP1", "S"]]+uppercase+lowercase+[['_']],
    "CO6": [["CO7", "CO5"]],
    "CO7": [[","]],
    "CO8": [["CO9", "STMTSW"]],
    "CO9": [[")"]],
}