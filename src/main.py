import argparse

parser = argparse.ArgumentParser()
parser.add_argument('namafile', type=str)
args = parser.parse_args()

print(f"Nama file: {args.namafile}")