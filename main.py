from maybe_boolean import MaybeBoolean as Maybe

maybe = Maybe()

print("I cant decide what to do.")

answer = int(input("Your boolean:"))

if maybe.maybe():
    print("True")
else:
    print("False")

 