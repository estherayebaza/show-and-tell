a=["kotlin","python","javascript","html"]
b=["ux_research","internet_of_things","backend","frontedweb development","frontendmobile development"]

print(a!=b)
print(a==b)
print(type(b))

c=a+b
print(c)
print(len(a))
print(len(b))
print (b[2])


for course in b:
    print(course.upper())
course=[d.upper()for d in b]
print(course)

name="Esther"
introduction="my name is"+" "+name
print(introduction)
programming_language="Python,kotlin,javascript"
passion="coding"

print(f"Hi {introduction} ,I am passionate about {passion} in {programming_language.upper()}" )

print("Hello \t{}\n, am  passionate about {} in {} " .format(introduction,passion,programming_language))
print(b[0:3])
b.append("ux design")
print(b)