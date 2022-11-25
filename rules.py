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

    ### Class
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