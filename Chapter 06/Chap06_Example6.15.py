# Eg1 -----------------------------
# def outside_func():
#     def inner_func():
#         print("Inside Inner Function")
#     print("Inside Outer Function")
#     inner_func()

# Eg2 -----------------------------
def outside_func(str1):
    def inner_func():
        print(str1 + "Inner Function")
    print("Inside Outer Function")
    inner_func()

outside_func("Hello ")

