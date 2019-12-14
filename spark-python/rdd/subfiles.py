import os
import timeit
def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def mergeDict(dict1, dict2):
   ''' Merge dictionaries and keep values of common keys in list'''
   dict3 = {**dict1, **dict2}
   for key, value in dict3.items():
       if key in dict1 and key in dict2:
               dict3[key] = [value , dict1[key]]
 
   return dict3
 
# Merge dictionaries and add values of common keys in a list

def main():
        #cauculate runtime
    start = timeit.default_timer()
    stop = timeit.default_timer()
    dict3 = mergeDict(dict1, dict2)
    print('Dictionary 3 :')
    print(dict3)
    print('Time: ', stop - start) 

if __name__ == "__main__":
    main()