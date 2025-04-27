### Python String Methods with Examples

# String capitalize()
text = "marium aftab"
print(text.capitalize())  # Output: 'Marium aftab'

# String casefold()
text = "MARIUM AFTAB"
print(text.casefold())  # Output: 'marium aftab'

# String center()
text = "Marium "
print(text.center(20, '-'))  # Output: '------Marium -------'

# String count()
text = "Marium aftab"
print(text.count("a"))  # Output: 3

# String encode()
text = "Marium"
print(text.encode())  # Output: b'Marium'

# String endswith()
text = "Marium Aftab"
print(text.endswith("Marium"))  # Output: False

# String expandtabs()
text = "Marium\tAftab"
print(text.expandtabs(10))  # Output: 'Marium    Aftab'

# String find()
text = "Marium Aftab"
print(text.find("Aftab"))  # Output: 7

# String format()
text = "My name is {}"
print(text.format("Marium Aftab"))  # Output: 'My name is Marium Aftab'

# String format_map()
data = {"name": "Marium"}
text = "My name is {name}"
print(text.format_map(data))  # Output: 'My name is Marium'

# String index()
text = "Marium Aftab"
print(text.index("Marium"))  # Output: 0

# String isalnum()
text = "Marium123"
print(text.isalnum())  # Output: True

# String isalpha()
text = "Marium"
print(text.isalpha())  # Output: True

# String isdecimal()
text = "12345"
print(text.isdecimal())  # Output: True

# String isdigit()
text = "12345"
print(text.isdigit())  # Output: True

# String isidentifier()
text = "Marium123"
print(text.isidentifier())  # Output: True

# String islower()
text = "marium"
print(text.islower())  # Output: True

# String isnumeric()
text = "12345"
print(text.isnumeric())  # Output: True

# String isprintable()
text = "Marium\n"
print(text.isprintable())  # Output: False

# String isspace()
text = "   "
print(text.isspace())  # Output: True

# String istitle()
text = "Marium Aftab"
print(text.istitle())  # Output: True

# String isupper()
text = "MARIUM"
print(text.isupper())  # Output: True

# String join()
text = ["Marium", "Aftab"]
print(" ".join(text))  # Output: 'Marium Aftab'

# String ljust()
text = "Marium"
print(text.ljust(10, '-'))  # Output: 'Marium----'

# String lower()
text = "MARIUM"
print(text.lower())  # Output: 'marium'

# String lstrip()
text = "   Marium"
print(text.lstrip())  # Output: 'Marium'

# String maketrans()
translation = str.maketrans("abc", "123")
text = "Marium"
print(text.translate(translation))  # Output: 'M1rium'

# String partition()
text = "Marium Aftab"
print(text.partition("Marium"))  # Output: ('', 'Marium', ' Aftab')

# String replace()
text = "Marium Aftab"
print(text.replace("Marium", "Aftab"))  # Output: 'Aftab Aftab'

# String rfind()
text = "Marium Aftab"
print(text.rfind("u"))  # Output: 4

# String rindex()
text = "Marium Aftab"
print(text.rindex("a"))  # Output: 10

# String rjust()
text = "Marium"
print(text.rjust(10, '-'))  # Output: '----Marium'

# String rpartition()
text = "Marium Aftab"
print(text.rpartition("Aftab"))  # Output: ('Marium ', 'Aftab', '')

# String rsplit()
text = "Marium Aftab"
print(text.rsplit(" ", 2))  # Output: ['Marium', 'Aftab']

# String rstrip()
text = "Marium   "
print(text.rstrip())  # Output: 'Marium'

# String split()
text = "Marium Aftab"
print(text.split())  # Output: ['Marium', 'Aftab']

# String splitlines()
text = "Marium\nAftab"
print(text.splitlines())  # Output: ['Marium', 'Aftab']

# String startswith()
text = "Marium Aftab"
print(text.startswith("Aftab"))  # Output: False

# String strip()
text = "   Marium   "
print(text.strip())  # Output: 'Marium'

# String swapcase()
text = "Marium Aftab"
print(text.swapcase())  # Output: 'mARIUM aFTAB'

# String title()
text = "marium aftab"
print(text.title())  # Output: 'Marium Aftab'

# String translate()
translation = str.maketrans("a", "@")
text = "aftab"
print(text.translate(translation))  # Output: '@ft@b'

# String upper()
text = "marium"
print(text.upper())  # Output: 'MARIUM'

# String zfill()
text = "123"
print(text.zfill(5))  # Output: '00123'