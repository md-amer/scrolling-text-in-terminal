# Animated banner in terminal
# By Amer

from pyfiglet import Figlet
import os
from time import sleep

f = Figlet(font='slant')
text = f.renderText('AMER')

main_content1 = '        _____    ____ _    ___________'
main_content2 = '       / /   |  / __ \ |  / /  _/ ___/'
main_content3 = '  __  / / /| | / /_/ / | / // / \__ \ '
main_content4 = ' / /_/ / ___ |/ _, _/| |/ // / ___/ / '
main_content5 = ' \____/_/  |_/_/ |_| |___/___//____/ '
main_content6 = ''


def print_content():
	i=0
	j=70
	for k in range(71):
		i+=1
		j-=1
		clear_screen()
		print('* '*70)
		print('*'+' '*i+main_content1+' '*(70-len(main_content1)-2)+' '*j+'*')
		print('*'+' '*i+main_content2+' '*(70-len(main_content2)-2)+' '*j+'*')
		print('*'+' '*i+main_content3+' '*(70-len(main_content3)-2)+' '*j+'*')
		print('*'+' '*i+main_content4+' '*(70-len(main_content4)-2)+' '*j+'*')
		print('*'+' '*i+main_content5+' '*(70-len(main_content5)-2)+' '*j+'*')
		print('* '*70)
		sleep(0.1)
		
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')
		
print_content()
