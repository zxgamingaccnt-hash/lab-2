import statistics as stat
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
    numlist = input()
    floatlist=numlist.split(',')
    floatlist=list(map(float,floatlist))
    return floatlist



def calc_average_temperature(temperature):
        
   avg=sum(temperature)/len(temperature)
   print(avg)

def find_min_max(temp_list):
    min_max_list = [min(temp_list),max(temp_list)]
    print(min_max_list)
    return min_max_list

def sort_temperature(temp_list):
    print(temp_list.sort())

def calc_median_temperature(temp_list):
    print(stat.median(temp_list))


def main():
    print("helloworld")
    display_main_menu()
    value=get_user_input()
    calc_average_temperature(value) 
    find_min_max(value)
    sort_temperature(value)
    calc_median_temperature(value)
    


if __name__ == "__main__" :
  main()  