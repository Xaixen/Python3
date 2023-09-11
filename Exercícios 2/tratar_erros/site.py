from urllib import request
try:
    site = request.urlopen('http://pudim.com.br')
except:
    print('Deu erro!')
else:
    print('Tudo ok')
    print(site.read())