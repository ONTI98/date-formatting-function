#function to format a date to user specifics
#needs perimiters(This will be used instead of user input)
#accepts a date from input(if not in a function)
#prints in a whatever specified format format
#user can change function arguments

#condence this code into a function and use the input values  in the place of perimeters
import datetime

def format_date(day,formatted_date):

    date=datetime.datetime.strptime(day,"%Y/%m/%d")
    print(date)
    print(date.strftime(f"Your formatted date is  {formatted_date}"))
    return 
format_date(day= "2024/12/22",formatted_date="%Y %b %d ")
