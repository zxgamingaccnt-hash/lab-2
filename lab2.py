def calculate_bmi(height,weight):
    print("value of height is :",height,"cm")
    print(f"value of weight is: {weight}kg")
    bmi=weight/(height**2)
    print("weight of bmi is",bmi)
    if bmi <18.5:
            print("bmi is underweight")
    elif bmi >=18.5 and bmi<24.9:
            print("BMI is normal")
    else:
            print("bmi is overweight")
    return bmi

def display_main_menu():
    print()
def get_user_input():
    print()

def main():
    display_main_menu()
    num_list = get_user_input()


if __name__=="__main__":
      main()



