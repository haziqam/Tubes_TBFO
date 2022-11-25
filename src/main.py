import argparse
import i_o
import CYKParser as CYK

parser = argparse.ArgumentParser()
parser.add_argument('namafile', type=str)
args = parser.parse_args()

filename = args.namafile

L = i_o.fileToList(filename)

print(L)

if(isinstance(L, list)):
    verdict = 'START' in CYK.CYKParse(L)
else:
    verdict = L

if(verdict):
    print("Accepted")
else:
    print("Syntax Error")
