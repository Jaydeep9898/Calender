import Calendar as calendar

# ----------------------------------------------------------------------------
# Functions dealing with the user. This is the calendar application.
# Please do use input and print as needed in order to provide a
# nice and meaningful user interaction with your application.
# ----------------------------------------------------------------------------


def user_interface():
    '''
    Load calendar.txt and then interact with the user. The user interface
    operates as follows, the text after command: is the command entered by the
    user.
    calendar loaded
    command: add 2017-10-21 budget meeting
    added
    command: add 2017-10-22 go to the gym
    added
    command: add 2017-10-23 go to the gym
    added
    command: fadd 2017-11-01 Make sure to submit csc108 assignment 2
    added
    command: add 2017-12-02 Make sure to submit csc108 assignment 3
    added
    command: add 2017-11-06 Term test 2
    added
    command: add 2017-10-29 Get salad stuff,lettuce, red peppers, green peppers
    added
    command: add 2017-11-06 Sid's birthday
    added
    command: show
        2017-10-21:
            0: budget meeting
        2017-10-22:
            0: go to the gym
        2017-10-23:
            0: go to the gym
        2017-10-29:
            0: Get salad stuff, leuttice, red peppers, green peppers
        2017-11-01:
            0: Make sure to submit csc108 assignment 2
        2017-11-06:
            0: Term test 2
            1: Sid's birthday
        2017-12-02:
            0: Make sure to submit csc108 assignment 3
    command: delete 2017-10-29 0
    deleted
    command: delete 2015-12-03 0
    2015-12-03 is not a date in the calendar
    command: delete 2017-12-02 0
    deleted
    command: show
        2017-10-21:
            0: budget meeting
        2017-10-22:
            0: go to the gym
        2017-10-23:
            0: go to the gym
        2017-11-01:
            0: Make sure to submit csc108 assignment 2
        2017-11-06:
            0: Term test 2
            1: Sid's birthday
    command: quit
    calendar saved

    :return: None
    '''
    custom_calendar = calendar.load_calendar()
    print('Calendar loaded.')
    command = input('command: ')
    while not command == 'quit':
        input_command = calendar.parse_command(command)
        if len(input_command) > 2 and input_command[0] == 'add' or input_command[0] == 'delete' :
            if input_command[0] == 'add':
                if calendar.is_calendar_date(input_command[1]):
                    date = input_command[1]
                else:
                    print('Enter correct date.')
                    continue
                res = calendar.command_add(date, input_command[2], custom_calendar)
                if res == '':
                    print('added')
            if input_command[0] == 'delete':
                if calendar.is_natural_number(input_command[2]):
                    entry_num = input_command[2]
                else:
                    print('Enter correct entry number.')
                    continue
                res = calendar.command_delete(input_command[1], int(entry_num), custom_calendar)
                if res == '':
                    print('deleted')
                else:
                    print(res)
        elif input_command[0] == 'show' or input_command[0] == 'help':
            if input_command[0] == 'show':
                print(calendar.command_show(custom_calendar))
            if input_command[0] == 'help':
                print(calendar.command_help())
        else:
            print(input_command[0]+input_command[1])
        command = input('command: ')
    if calendar.save_calendar(custom_calendar):
            print('calendar saved.')


if __name__ == "__main__":
    user_interface()
