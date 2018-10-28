import argparse
from basic import Count


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-f','--countWords', help="Output word frequencies",action = "store_true")
group.add_argument('-c','--countChar', help="Output character frequencies",action = "store_true")
parser.add_argument('-d','--dirFlag', help="Treat the <file name> as an directory",action = "store_true")
parser.add_argument('-s','--reFlag', help="Verb file to normalize the veb tenses",action = "store_true")
parser.add_argument('-n','--num',type = int, help="Output only the top <num> iterms",default=10)
parser.add_argument('path', help="The file/directory to be operated with")


if(__name__ == '__main__'):
    args = parser.parse_args()
    if (args.countWords):
        if(args.dirFlag):
            Count.OperateInDir(Count.CountWords,args.path, int(args.num), None, None,args.reFlag)
        else:
            Count.CountWords(args.path, int(args.num), None, None)
    elif (args.countChar):
        if (args.dirFlag):
            Count.OperateInDir(Count.CountLetters, args.path, int(args.num), None, None, args.reFlag)
        else:
            Count.CountLetters(args.path, int(args.num), None, None)
    else:
        print("Error: Please input the operation type (-f|-q|-p|-c)")