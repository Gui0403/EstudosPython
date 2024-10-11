from PySimpleGUI import Window, Button, Image, Input, Text

layout =[
    [Image(filename= 'avatar.png')]
    [Text('E-mail: '),Input('')],
    [Text('Senha: '),Input('')],
    [Button('Login!'),Button('Esqueci a senha!')]
]

Window = Window(
    'Interface',
    layout=layout
)
Window.read()






Window.close()