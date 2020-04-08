settings = ['ug', 'ie','if', 'uf']
a=''
for i in settings:
    a += f'<div class="w3-bar-item w3-button w3-hover-theme"><input class="w3-check" type="checkbox" name="{i}"><label class="w3-margin">{i}</label></div> '
# print(a)

a = {'AlphaAvr', 'dU/dt', 'yVoltCnl', 'Usyn', 'Pg', 'Alpha', 'Hz', 'If', 'Fsyn', 'Fg', 'yManCnl', 'MaxSetUgV/Hz', 'yPSS', 'dIf/dt', 'Qg', 'Ig', 'yAvr', 'SetUg', 'Ie', 'Ie(A-C)', 'yTest', 'xCmnCnl', 'Ie(A-B)', 'gr', 'Uf', 'Ie(B-C)', 'SetIe', 'Ug', 'BiasCmn'}
b = {'Pg', 'Ie', 'Ug', 'If', 'Ig'}

c = a-b
# print(c)

d = {'AlphaAvr':'dU/dt',
     'yVoltCnl':'Usyn',
     'Pg':'Alpha',
     'Hz':'If',
     'Fsyn':'Fg',
     'yManCnl':'MaxSetUgV/Hz',
     'yPSS':'dIf/dt',
     'Qg':'Ig',
     'yAvr':'SetUg',
     'Ie':'Ie(A-C)',
     'yTest':'xCmnCnl',
     'Ie(A-B)':'gr',
     'Uf':'Ie(B-C)',
     'SetIe':'Ug'}
e = set(d)

print(b&e)