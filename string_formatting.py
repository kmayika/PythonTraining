
name = 'kwezi'
#old style
text = 'Hello, %s' % name
print(text)

#new style

text = 'Hello, {name} you have a {errno} error'.format(name=name, errno='0xbadc0ffee')
print(text)

#literal string format
a,b = 1,2
text = f'Hello, {name} the answer is {a + b}'
print(text)

def greet(name, question):
    return f'Hello, {name} how is it {question}?'

print(greet(name, 'going'))

import dis

dis.dis(greet)

#Template Strings
from string import Template

t = Template('Hello, $name')
print(t.substitute(name=name))

#Security vulnerabilities is using f-strings
SECRET = 'Secret-Code'
class Error:
    def __init__(self):
        pass

err = Error()
user_input = '{error.__init__.__globals__[SECRET]}'

print(user_input.format(error=err))


