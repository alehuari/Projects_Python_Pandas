import numpy as np  

def main():
    try:
        input_str = input("Write exactly 9 numbers separated by spaces: ")  
        nums_str = input_str.split()        
        if len(nums_str) != 9:
            raise ValueError("List must conatin nine numbers")
        else:        
            lst = [int(num_str) for num_str in nums_str]
            result = calculate(lst)
            return result      
    except ValueError as e:
        print(e)
        return None
        
def calculate(lst):
    result_dict = {}
    lst = np.array(lst).reshape(3, 3)
    result_dict['mean'] = round(np.mean(lst), 2)
    result_dict['variance'] = round(np.var(lst), 2)
    result_dict['standard_deviation'] = round(np.std(lst), 2) 
    result_dict['max'] = round(np.max(lst), 2)
    result_dict['min'] = round(np.min(lst), 2)
    result_dict['sum'] = round(np.sum(lst), 2)

    print(result_dict)
    return result_dict

if __name__ == "__main__":
    main()
