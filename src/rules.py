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

    "NL": [["\n"]],

    "SLASH": [["/"]],
    "STAR": [["*"]],

    "START": [["STMT","START1"],["FCALL","START1"],["E","START1"],["COMNT","START"],["CURL1","BLK2"],["THR","E"],["IF","IF2"],["SWTC","SWTC2"],["TRY","TRY2"],["DCLR","V"],["FOR","FOR2"],["WHL","WHL2"],["FU1","FU2"],["AF1","AF2"],["AF3","AF10"],["V","AF10"],["V1","V2"],["A-Z"],["a-z"],["_"],["II1"],["0-9"],["IF1"],["S1S2"],["S5S6"],["true"],["false"],["null"],["E2","E3"],["O1","U2"],["P","U3"],["M","U4"],["V","U5"],["V","U6"],["E","B1"],["E","B2"],["E","B6"],["E","B13"],["E","T1"],["A5","E1"],["A7","A1"],["COMNT"],["NL","START"],["SCLN", "START"],["START","NL"],["START","SCLN"],["\n"],[";"]],

    "START1": [["COMNT","START1"],["NL","START"],["SCLN","START"]],

    "STARTSW": [["STMT","STARTSW1"],["FCALL","STARTSW1"],["E","STARTSW1"],["COMNT","STARTSW"],["CURL1","BLKSW2"],["THR","E"],["IF","IFSW2"],["SWTC","SWTC2"],["TRY","TRYSW2"],["VAR","V"],["VAR","A"],["LET","V"],["LET","A"],["CONST","V"],["CONST","A"],["FOR","FOR2"],["WHL","WHL2"],["break"],["FU1","FU2"],["AF1","AF2"],["AF3","AF10"],["V","AF10"],["V1","V2"],["A-Z"],["a-z"],["_"],["II1"],["0-9"],["IF1"],["S1S2"],["S5S6"],["true"],["false"],["null"],["E2","E3"],["O1","U2"],["P","U3"],["M","U4"],["V","U5"],["V","U6"],["E","B1"],["E","B2"],["E","B6"],["E","B13"],["E","T1"],["A5","E1"],["A7","A1"],["COMNT"],["NL","STARTSW"],["SCLN", "STARTSW"],["STARTSW","NL"],["STARTSW","SCLN"],["\n"],[";"]],

    "STARTSW1": [["COMNT","STARTSW1"],["NL","STARTSW"],["SCLN","STARTSW"]],

    "STARTL": [["STMT","STARTL1"],["FCALL","STARTL1"],["E","STARTL1"],["COMNT","STARTL"],["CURL1","BLKL2"],["THR","E"],["IF","IFL2"],["SWTCL","SWTCL2"],["TRY","TRYL2"],["VAR","V"],["VAR","A"],["LET","V"],["LET","A"],["CONST","V"],["CONST","A"],["FOR","FOR2"],["WHL","WHL2"],["break"],["continue"],["FU1","FU2"],["AF1","AF2"],["AF3","AF10"],["V","AF10"],["V1","V2"],["A-Z"],["a-z"],["_"],["II1"],["0-9"],["IF1"],["S1S2"],["S5S6"],["true"],["false"],["null"],["E2","E3"],["O1","U2"],["P","U3"],["M","U4"],["V","U5"],["V","U6"],["E","B1"],["E","B2"],["E","B6"],["E","B13"],["E","T1"],["A5","E1"],["A7","A1"],["COMNT"],["NL","STARTL"],["SCLN", "STARTL"],["STARTL","NL"],["STARTL","SCLN"],["\n"],[";"]],

    "STARTL1": [["COMNT","STARTL1"],["NL","STARTL"],["SCLN","STARTL"]],

    "COMNT": [["SLASH","COMNT1"],["SLASH","COMNT3"]],
    "COMNT1": [["SLASH","COMNT2"]],
    "COMNT2": [["S3","NL"]],
    "COMNT3": [["STAR","COMNT4"]],
    "COMNT4": [["S3","COMNT5"]],
    "COMNT5": [["STAR","SLASH"]],


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
    "U2": [["O1", "U2"],["V1", "V2"]]+uppercase+lowercase+integer+[['_'], ["I", "I1"], ["I", "F1"], ["S1", "S2"], ["S5", "S6"], ["true"], ["false"],
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
    "B7": [["B8", "B8"], ["B9", "B9"], ["B10", "B10"], ["B11", "B11"], ["B12", "B12"], ["B5", "B5"]],
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

    "CURL1": [["{"]],
    "CURL2": [["}"]],

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

    # Function Call
    "FCALL": [["FU1","FU2"],["AF1","AF2"],["AF3","AF10"],["V","AF10"]],

    # Extra symbols
    "CMA": [[","]],
    "CLN": [[":"]],
    "SCLN": [[";"]],
    "CURL1": [["{"]],
    "CURL2": [["}"]],

    # STATEMENT KEYWORDS
    "RTN": [["return"]],
    "BRK": [["break"]],
    "CNTN": [["continue"]],
    "THR": [["throw"]],
    "IF": [["if"]],
    "ELSE": [["else"]],
    "SWTC": [["switch"]],
    "CASE": [["case"]],
    "DFLT": [["default"]],
    "TRY": [["try"]],
    "CATCH": [["catch"]],
    "FNLY": [["finally"]],

    "VAR": [["var"]],
    "LET": [["let"]],
    "CONST": [["const"]],

    "WHL": [["while"]],
    "FOR": [["for"]],

    # Statement call    
    "STMT": [["CURL1","BLK2"],["THR","E"],["IF","IF2"],["SWTC","SWTC2"],["TRY","TRY2"],["VAR","V"],["VAR","A"],["LET","V"],["LET","A"],["CONST","V"],["CONST","A"],["FOR","FOR2"],["WHL","WHL2"]],

    "STMTSW": [["CURL1","BLKSW2"],["THR","E"],["IF","IFSW2"],["SWTC","SWTC2"],["TRY","TRYSW2"],["VAR","V"],["VAR","A"],["LET","V"],["LET","A"],["CONST","V"],["CONST","A"],["FOR","FOR2"],["WHL","WHL2"],["break"]],

    "STMTL": [["CURL1","BLKL2"],["THR","E"],["IF","IFL2"],["SWTCL","SWTCL2"],["TRY","TRYL2"],["VAR","V"],["VAR","A"],["LET","V"],["LET","A"],["CONST","V"],["CONST","A"],["FOR","FOR2"],["WHL","WHL2"],["break"],["continue"]],

    # Blocks
    "BLK": [["CURL1","BLK2"],["CURL1","CURL2"]],
    "BLK2": [["START","CURL2"]],

    "BLKSW": [["CURL1","BLKSW2"]],
    "BLKSW2": [["STARTSW","CURL2"]],

    "BLKL": [["CURL1","BLKL2"]],
    "BLKL2": [["STARTL","CURL2"]],

    # Throw
    "THR": [["THR","E"]],

    # If
    "IF1": [["IF","IF2"]],
    "IF2": [["E2","IF3"]],
    "IF3": [["E","IF4"]],
    "IF4": [["E4","IF5"],["E4","STMT"],["E4","E"],["E4","FCALL"]],
    "IF5": [["STMT","IF6"],["E","IF6"],["FCALL","IF6"]],
    "IF6": [["ELSE","STMT"],["ELSE","E"],["ELSE","FCALL"]],

    "IFSW1": [["IF","IFSW2"]],
    "IFSW2": [["E2","IFSW3"]],
    "IFSW3": [["E","IFSW4"]],
    "IFSW4": [["E4","IFSW5"],["E4","STMTSW"],["E4","E"],["E4","FCALL"]],
    "IFSW5": [["STMTSW","IFSW6"],["E","IFSW6"],["FCALL","IFSW6"]],
    "IFSW6": [["ELSE","STMTSW"],["ELSE","E"],["ELSE","FCALL"]],

    "IFL1": [["IF","IFL2"]],
    "IFL2": [["E2","IFL3"]],
    "IFL3": [["E","IFL4"]],
    "IFL4": [["E4","IFL5"],["E4","STMTL"],["E4","E"],["E4","FCALL"]],
    "IFL5": [["STMTL","IFL6"],["E","IFL6"],["FCALL","IFL6"]],
    "IFL6": [["ELSE","STMTL"],["ELSE","E"],["ELSE","FCALL"]],

    # Switch
    "SWTC1": [["SWTC","SWTC2"]],
    "SWTC2": [["E2","SWTC3"]],
    "SWTC3": [["E","SWTC4"]],
    "SWTC4": [["E4","SWTC5"],["CMA","SWTC3"]],
    "SWTC5": [["CURL1","SWTC6"]],
    "SWTC6": [["CASE","SWTC7"],["DEFAULT","SWTC11"]],
    "SWTC7": [["E","SWTC8"]],
    "SWTC8": [["CLN","SWTC9"]],
    "SWTC9": [["STARTSW","SWTC6"],["STARTSW","CURL2"]],
    "SWTC10": [["CASE","SWTC11"]],
    "SWTC11": [["E","SWTC12"]],
    "SWTC12": [["CLN","SWTC13"]],
    "SWTC13": [["STARTSW","SWTC10"],["STARTSW","CURL2"]],
    
    "SWTCL1": [["SWTCL","SWTCL2"]],
    "SWTCL2": [["E2","SWTCL3"]],
    "SWTCL3": [["E","SWTCL4"]],
    "SWTCL4": [["E4","SWTCL5"],["CMA","SWTCL3"]],
    "SWTCL5": [["CURL1","SWTCL6"]],
    "SWTCL6": [["CASE","SWTCL7"],["DEFAULT","SWTCL11"]],
    "SWTCL7": [["E","SWTCL8"]],
    "SWTCL8": [["CLN","SWTCL9"]],
    "SWTCL9": [["STARTL","SWTCL6"],["STARTL","CURL2"]],
    "SWTCL10": [["CASE","SWTCL11"]],
    "SWTCL11": [["E","SWTCL12"]],
    "SWTCL12": [["CLN","SWTCL13"]],
    "SWTCL13": [["STARTL","SWTCL10"],["STARTL","CURL2"]],

    # Try
    "TRY1": [["TRY","TRY2"]],
    "TRY2": [["BLK","TRY3"]],
    "TRY3": [["CATCH","BLK"],["CATCH","TRY4"],["CATCH","TRY8"],["FNLY","BLK"]],
    "TRY4": [["E2","TRY5"]],
    "TRY5": [["V","TRY6"]],
    "TRY7": [["E4","BLK"],["E4","TRY8"]],
    "TRY8": [["BLK","TRY9"]],
    "TRY9": [["FNLY","BLK"]],

    "TRYSW1": [["TRY","TRYSW2"]],
    "TRYSW2": [["BLKSW","TRYSW3"]],
    "TRYSW3": [["CATCH","BLKSW"],["CATCH","TRYSW4"],["CATCH","TRYSW8"],["FNLY","BLKSW"]],
    "TRYSW4": [["E2","TRYSW5"]],
    "TRYSW5": [["V","TRYSW6"]],
    "TRYSW7": [["E4","BLKSW"],["E4","TRYSW8"]],
    "TRYSW8": [["BLKSW","TRYSW9"]],
    "TRYSW9": [["FNLY","BLKSW"]],

    "TRYL1": [["TRY","TRYL2"]],
    "TRYL2": [["BLKL","TRYL3"]],
    "TRYL3": [["CATCH","BLKL"],["CATCH","TRYL4"],["CATCH","TRYL8"],["FNLY","BLKL"]],
    "TRYL4": [["E2","TRYL5"]],
    "TRYL5": [["V","TRYL6"]],
    "TRYL7": [["E4","BLKL"],["E4","TRYL8"]],
    "TRYL8": [["BLKL","TRYL9"]],
    "TRYL9": [["FNLY","BLKL"]],

    # Declarations
    "DCLR": [["VAR","V"],["VAR","A"],["LET","V"],["LET","A"],["CONST","V"],["CONST","A"]],

    # For loop
    "FOR1": [["FOR","FOR2"]],
    "FOR2": [["E2","FOR3"],["E2","FOR4"]],
    "FOR3": [["E","FOR4"]],
    "FOR4": [["SCLN","FOR5"],["SCLN","FOR6"]],
    "FOR5": [["E","FOR6"],["DCLR","FOR6"]],
    "FOR6": [["SCLN","FOR7"],["SCLN","FOR8"]],
    "FOR7": [["E","FOR8"]],
    "FOR8": [["E4","STMTL"],["E4","E"],["E4","FCALL"]],

    # While loop
    "WHL1": [["WHL","WHL2"]],
    "WHL2": [["E2","WHL3"]],
    "WHL3": [["E","WHL4"]],
    "WHL4": [["E4","STMTL"],["E4","E"],["E4","FCALL"]],

}