 # string showcase
from pyscript import display, document

def stringshowcase(e):
    name = document.getElementById('name').value
    age = float(document.getElementById('age').value)
    school = document.getElementById('school').value


    message = f"""
        my student profile
        Name   : {name}
        Age    : {age}
        School : {school}

        your message:
        hii, my name is {name} and i am {age} years old. i study at {school}, and
        this message was made for our drill #2
    """

    display(message, target="output")
