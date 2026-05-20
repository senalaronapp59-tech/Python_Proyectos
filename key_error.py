dictionary = {"fruta": "mango",
              "color": "rosa",
              "pajaro": "gorrion"}

try:
    print(dictionary["verdura"])
except KeyError:
    print("no esta en el diccionario esa palabra")