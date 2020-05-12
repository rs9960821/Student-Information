from menu import menu
from info import *
# from class import *
def main1():
    does = []
    while 1:
        menu()
        x = input('請選擇:')  
        if x == '1':
            does += main()
        elif x == '2':
            see(does)
        elif x == '3':
            amend(does)
        elif x == '4': 
            remove(does)
        elif x == '5': 
            L2 = sorted(does, key = lambda d : d['score'], reverse = True)
            see(L2)
        elif x == '6': 
            L2 = sorted(does, key = lambda d : d['score'], reverse = False)
            see(L2)
        elif x == '7': 
            L2 = sorted(does, key = lambda d : d['age'], reverse = True)
            see(L2)
        elif x == '8': 
            L2 = sorted(does, key = lambda d : d['age'], reverse = False)
            see(L2) 
        elif x == '9': 
            save_to_file(does)
        elif x == '10': 
            does = open_from_file()
        elif x == 'q':
            print('Bye')
            return
main1()