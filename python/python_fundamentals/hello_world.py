# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"

# using comma
print("Hello", name)

# using +
print("Hello " + name)

# 3. print "Hello 42!" with the number in a variable
num = 42

# using comma
print("Hello", num)

# using + (this gives error ❌)
# print("Hello " + num)

# ✅ NINJA BONUS (حل الخطأ بدون comma)
print("Hello " + str(num))

# 4. print "I love to eat sushi and pizza." with variables
fave_food1 = "sushi"
fave_food2 = "pizza"

# using .format()
print("I love to eat {} and {}.".format(fave_food1, fave_food2))

# using f-string
print(f"I love to eat {fave_food1} and {fave_food2}.")