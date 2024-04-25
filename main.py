balance = 300.0
remaining_withdraws = 4
MAX_WITHDRAW_VALUE = 500.0
EXTRACT = []

## EXAMPLE USERS FOR TESTING
USERS = {
    '123': {'name': 'John', 'age': '18'},
    '987': {'name': 'Luck', 'age': '27'},
    '159': {'name': 'Lya', 'age': '38'}
}

## EXAMPLE ACCOUNTS FOR TESTING
ACCOUNTS = {
    '1': {'cpf': '123', 'agency': '0001'},
    '2': {'cpf': '987', 'agency': '0001'},
    '3': {'cpf': '123', 'agency': '0001'},
    '4': {'cpf': '159', 'agency': '0001'},
    '5': {'cpf': '987', 'agency': '0001'},
    '6': {'cpf': '123', 'agency': '0001'},
}

## MENU (MESSAGE AND CHOICES) PATTERN
## IT'S EASIER TO SEE WHAT THE CODE IS DOING
MAIN_MENU_MESSAGE = """
___________________

[1] Withdraw
[2] Deposit
[3] Extract

[4] Create User
[5] Create Account

[6] Find User

[0] Exit
___________________

Type here
"""

MAIN_MENU_CHOICES = {
    1:'withdraw', 
    2:'deposit',
    3:'extract', 
    4:'create_user',
    5:'create_account',
    6:'find_user',
    0:'exit'
}

## TO BETTER SEE RETURNED MESSAGES
def pressEnterToContinue():
    input('Press ENTER to continue.')
    
## SHOW MENU AND GETS USER INPUT
## CAN BE USED TO SHOW AND RETURN VALUES FOR DIFFERENT MENUS
## BY FOLLOWING THE MENU PATTERN ABOVE
def choose(menu_message, available_choices):
    user_choice = None

    while not user_choice:
        user_choice = int(input(menu_message).strip(' '))

        if user_choice not in available_choices:
            print('Type a valid choice...')
            pressEnterToContinue()
        else:
            return available_choices[user_choice]

def add_message_to_extract(message):
    EXTRACT.append(message)

## FUNCTION THAT ASK FOR VALUE INPUT FOR WITHDRAW
## THEN IT CHECK IF IS A VALID VALUE
## THEN IT RETURNS 2 VALUES
##   (BOOLEAN)
## AND
##   (DICT WITH THE KEY 'errors' THAT CONTAINS A ERROR LIST) [IF SOMETHING WENT WRONG]
##    OR
##   (DICT WITH THE KEY 'extract_message') [IF NO ERROR HAPPENED]
def withdraw():
    global balance
    value = float(input('How much do you want to withdraw? R$ ').strip(' '))

    errors = []

    if remaining_withdraws == 0:
        errors.append('You do not have any remaining withdraws. Try again later.')
    if value > MAX_WITHDRAW_VALUE:
        errors.append(f"You can't withdraw more than R$ {round(MAX_WITHDRAW_VALUE, 2)} at once.")
    if value > balance:
        errors.append(f'Your balance is R$ {round(balance, 2)}, you tried to withdraw a higher value.') 
    if value < 0:
        errors.append('Please, do not enter negative numbers') 

    if not errors:
        balance -= value
        return True, {'extract_message': f'- R$ {round(value, 2)} - Withdraw'}
    else:
        return False, {'errors': errors}

## SAME AS WITHDRAW
def deposit():
    global balance
    value = float(input('How much do you want to deposit? R$ ').strip(' '))

    errors = []

    if value <= 0:
        errors.append("You entered a value lower than 0, please enter a valid value.")

    if not errors: 
        balance += value
        return True, {'extract_message': f'+ R$ {round(value, 2)} - Deposit'}
    else:
        return False, {'errors': errors}

## IT SHOW A ERROR MESSAGE, IF IS NOT VALID
## OR ADDS THE EXTRACT_MESSAGE TO THE EXTRACT LIST
## THE ACTION_TYPE IS TO CUSTOMIZE THE RETURN MESSAGE
## USED THIS TO RETURN DEPOSIT AND WITHDRAW MESSAGE
def show_returned_action_info(is_valid, message, action_type):
    if is_valid:
        extract_message = message['extract_message']

        print(f"\nSuccess {extract_message}")
        add_message_to_extract(extract_message)
        pressEnterToContinue()
    else:
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'ERROR WHILE TRYING TO {action_type.upper()}')
        for error in message['errors']:
            print('=============================================')
            print(error)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        pressEnterToContinue()

## CREATE AN USER ACCOUNT BY PASSING IT'S CPF
def create_user():
    ## didn't add credential checks
    nuser_cpf = input('Enter your CPF here -> ').strip(' ')
    
    if nuser_cpf == '':
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('You typed an invalid CPF...')
        pressEnterToContinue()

    elif nuser_cpf in USERS:
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('This CPF is already registered')
        pressEnterToContinue()
        return
    
    else:
        nuser_name = input('Enter your name -> ')
        nuser_age = input('Enter your age -> ')

        if nuser_age != '' and nuser_name != '':
            USERS[nuser_cpf] = {'name': nuser_name.capitalize(), 'age': nuser_age}

            print('\nThe user was created successfully...')
            print('-----------------------------')
            print(f'CPF: {nuser_cpf}')
            print(f'Name: {nuser_name.capitalize()}')
            print(f'Age: {nuser_age}')
            print('-----------------------------')
            pressEnterToContinue()
        else:
            print('\n')
            if nuser_name == '':
                print('Type a valid name...')
            if nuser_age == '':
                print('Type a valid age...')
            
            pressEnterToContinue()

## CREATE AN BANK ACCOUNT FOR USERS THAT HAS ALREADY REGISTERED
## IT SIMPLE ADD A ACCOUNT NUMBER, AND SET THE ENTERED CPF TO THE ACCOUNT
## AGENCY IS 0001 TO ALL CREATED ACCOUNTS
def create_account():
    entered_cpf = input('Enter the user CPF here -> ').strip(' ')

    if entered_cpf not in USERS:
        print('\n')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('This user is not registered yet')
        print('Please, create an User Account...')
        print('After that, create the Bank Account.')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        pressEnterToContinue()
    else:
        account_number = 1

        while account_number in ACCOUNTS:
            account_number += 1

        ACCOUNTS[account_number] = {'cpf': entered_cpf, 'agency': '0001'}
        print('Account created successfully...')
        print('------------------------')
        print(f'Agency: {ACCOUNTS[account_number]['agency']}')
        print(f'Account: {account_number}')
        print('------------------------')
        pressEnterToContinue()

## SHOW SELECTED USER INFORMATION BY PASSING IT'S CPF
def find_user():     
    entered_cpf = input('Type the user CPF -> ').strip(' ')

    if entered_cpf not in USERS:
        print('\n')
        print('This CPF is not registed...')
        pressEnterToContinue()
    else:
        user_info = USERS[entered_cpf]

        print('\n')
        print('=========================')
        print(f'CPF: {entered_cpf}')
        print(f'Name: {user_info['name']}')
        print(f'Age: {user_info['age']}')
        print('=========================')
        print('ACCOUNTS')
        for account_number in ACCOUNTS:
            if ACCOUNTS[account_number]['cpf'] == entered_cpf:
                agency = ACCOUNTS[account_number]['agency']
                print(f' | Agency: {agency} - Account: {account_number}')
        print('=========================')
        pressEnterToContinue()

## APP FUNCTION ##
def bankApp():
    actual_choice = None

    while True:
        actual_choice = choose(MAIN_MENU_MESSAGE, MAIN_MENU_CHOICES)

        if not actual_choice:
            pass
        else:
            if actual_choice == 'exit':
                break

            elif actual_choice == 'withdraw':
                is_valid_withdraw, message = withdraw()

                show_returned_action_info(is_valid_withdraw, message, 'withdraw')

            elif actual_choice == 'deposit':
                is_valid_deposit, message = deposit()
                show_returned_action_info(is_valid_deposit, message, 'deposit')

            elif actual_choice == 'extract':
                print('\n============================')
                for message in EXTRACT:
                    print(message)
                print('\n============================')
                pressEnterToContinue()

            elif actual_choice == 'create_user':
                create_user()

            elif actual_choice == 'create_account':
                create_account()

            elif actual_choice == 'find_user':
                find_user()


## RUN APP ##
bankApp()