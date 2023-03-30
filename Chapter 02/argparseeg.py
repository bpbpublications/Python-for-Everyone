# Eg1
# import argparse
# a_parser = argparse.ArgumentParser()
# a_parser.parse_args()

##########################positional args#########################################

# import argparse
# parser = argparse.ArgumentParser()
   
# parser.add_argument('Staff_Number')
# parser.add_argument('Name')
# parser.add_argument('Engineering_Branch')
# parser.add_argument('AIR')
# parser.add_argument('Age')

# args = parser.parse_args()

# print(f'My name is {args.Name} and I am {args.Age} years old')
# print(f'My Staff Number is {args.Staff_Number} and I had my BE in {args.Engineering_Branch} branch')
# print(f'My All India Rank is {args.AIR} ')

############################## positional args with default values#####################################

# import argparse
# parser = argparse.ArgumentParser()
   
# parser.add_argument('Staff_Number', nargs='?',default=567382)
# parser.add_argument('Name', nargs='?',default='Sohan')
# parser.add_argument('Engineering_Branch', nargs='?',default="EEE")
# parser.add_argument('AIR', nargs='?',default=12)
# parser.add_argument('Age', nargs='?',default=30)

# args = parser.parse_args()

# print(f'My name is {args.Name} and I am {args.Age} years old')
# print(f'My Staff Number is {args.Staff_Number} and I had my BE in {args.Engineering_Branch} branch')
# print(f'My All India Rank is {args.AIR} ')

##############################positional arguments with help#####################################
# import argparse
# parser = argparse.ArgumentParser()
   
# parser.add_argument('Staff_Number',help = "Enter the Staff Number",default=567382)
# parser.add_argument('Name',help = "Enter the Name",default='Sohan')
# parser.add_argument('Engineering_Branch',help = "Enter the Engg. Branch",default="EEE")
# parser.add_argument('AIR',help = "Enter the All India Rank",default=12)
# parser.add_argument('Age',help = "Enter the Age",default=30)

# args = parser.parse_args()

# print(f'My name is {args.Name} and I am {args.Age} years old')
# print(f'My Staff Number is {args.Staff_Number} and I had my BE in {args.Engineering_Branch} branch')
# print(f'My All India Rank is {args.AIR} ')

############################argparse string data type#######################################
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('num', help="Enter number to multiply by 2.")
# args = parser.parse_args()
# print(args.num*2)

############################argparse int data type#######################################
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('num', help="Enter number to multiply by 2.", type = int)
# args = parser.parse_args()
# print(args.num*2)

#############################argparse optional arguments######################################
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--title', help="Best title name here.")
# args = parser.parse_args()

# if args.title == 'optional':
#     print('Hey it is optional argument script')

#############################short names for optional arguments with arg parse######################################
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('-t', '--title', help="Best title name here")
# args = parser.parse_args()

# if args.title == 'optional':
#     print('Hey it is optional argument script')


###########################argparse with optional and positional arguments########################################
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('-t', '--title', help="Best title name here")
# parser.add_argument('name', help = 'The author name is: ')
# args = parser.parse_args()

# if args.title == 'optional':
#     print('Hey it is optional argument script')

# if args.name == 'ABC':
#     print('Hey you have successfully identified the author')

############################argparse with required#######################################
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--number', required=True)
# args = parser.parse_args()
# print(f'The number is {args.number}')

#############################argparse dest action######################################
# import argparse
# import datetime

# # dest gives a different name to a flag
# parser = argparse.ArgumentParser()
# parser.add_argument('-a', dest='animals', action='store_true', help="shows animals")
# args = parser.parse_args()

# # we can refer to the flag by a new name
# if args.animals:
#     animals = datetime.datetime.now()
#     print(f"Now: at zoo {animals}")

##############################argparse append action#####################################
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('-c', '--color', dest='colors', action='append', help="Different colors")
# args = parser.parse_args()
# colors = args.colors
# for name in colors:
#     print(f'The color is {name}!')

##############################allowing or disallowing abbreviations#####################################
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--number', action='store', type=int, required=True)
# parser.add_argument('--neg', action='store', type=int)
# args = parser.parse_args()
# print(args.number)

###############################allow_abbrev####################################
# import argparse
# parser = argparse.ArgumentParser(allow_abbrev=False)
# parser.add_argument('--number', action='store', type=int, required=True)
# parser.add_argument('--neg', action='store', type=int)
# args = parser.parse_args()
# print(args.number)

###################################################################

###################################################################

