import argparse
from basic import Count


parser = argparse.ArgumentParser()

parser.add_argument('-f','--f_file_name', help="Output word frequencies")
parser.add_argument('-c','--c_file_name', help="Output character frequencies")
parser.add_argument('-p','--p_file_name', help="Output phrase frequencies")
parser.add_argument('-q','--q_file_name', help="Output PREPOSITION pair frequencies")

if(__name__ == '__main__'):
    args = parser.parse_args()
    if (args.f_file_name):
        fileName = args.f_file_name
        Count.CountLetters(fileName)
    if (args.c_file_name):
        fileName = args.c_file_name
        print(fileName)
    if (args.p_file_name):
        fileName = args.p_file_name
        print(fileName)
    if (args.q_file_name):
        fileName = args.q_file_name
        print(fileName)