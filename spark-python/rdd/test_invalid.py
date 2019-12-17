import os
import timeit
import PathList
import json
from os import listdir
from os.path import isfile, join

#@pysnooper.snoop()
def word_count():
    '''count words of palindrome and anagram respectively'''
    parent_path = "in/maildir"
    invalid_folders = []
    names = PathList.get_immediate_subdirectories(parent_path)
    stop_point = 40
    folder_count = stop_point
    while (stop_point < len(names)):
        folder_count += 1
        stop_point += 1
        print("Number of name: %d, at number: %d" % (len(names), folder_count))
        name = names[folder_count-1]
        sub_lines_path = parent_path + "/" + name             
        path_list = PathList.get_all_path(sub_lines_path)
        
        sub_names = PathList.get_immediate_subdirectories(sub_lines_path)
        for sub_name in sub_names:
            mypath = sub_lines_path + "/" + sub_name
            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            if len(onlyfiles) < 5000:
                pass
            else:
                invalid_folders.append(mypath)
                file_invaid = open("out/invalid_folder.txt","w")#write mode 
                for invalid_folder in invalid_folders:
                    file_invaid.write(invalid_folder + "\n") 
                file_invaid.close() 


def main():
    '''cauculate runtime'''
    start = timeit.default_timer()
    word_count()
    stop = timeit.default_timer()
    time = stop - start
    print('Runtime: ', time)  

if __name__ == "__main__":
    main()



