from typing import List, Dict

class Solution:

    def __init__(self) -> None:
        pass

    def twoSum(self, inputs: List[int], target:int) -> List[int]:
        # to store indices 
        solution_list = []
        # observed values
        noticed_values = set()
        # for index in inputs:
        for index, input in enumerate(inputs):
            # remaining value required to meet target
            remaining = target - input
            print(f"index --> {index}, input --> {input}, remaining --> {remaining}")
            if remaining in inputs[index+1:]: # check if remaining value exist as a value in next upcoming list values
                solution_list.append(index)
                # remaining_value_index = inputs.index(remaining) return first occured single index
                # find all indexs where remaining value exists in inputs
                remaining_value_found_indexs = [i for i in range(0, len(inputs)) if inputs[i] == remaining and i > index]
                # print(f"    >> remaining_value_found_indexs --> {remaining_value_found_indexs}")
                # find remaining value index i.e., after current index
                remaining_value_index = remaining_value_found_indexs[0] if len(remaining_value_found_indexs) == 1 else remaining_value_found_indexs[index+1:][0]
                solution_list.append(remaining_value_index)
                break
            noticed_values.add(input)
        if len(solution_list) == 0: # if there is no values exists that makes target value
            solution_list = [0,0]
        return solution_list

if __name__ == "__main__":

    # input_list = [2,5,5,11]
    # input_list = [2,7,11,15]
    input_list = [1,2,4]
    # input_list = [3,3]
    print(f"input_list --> {input_list}")
    # target_value = #10 
    # target_value = #9
    target_value = 6
    s = Solution()
    solution_list = s.twoSum(inputs=input_list, target=target_value)
    print(f"solution_list indices --> {solution_list} to match target value --> {target_value}")

