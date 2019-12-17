import os
import timeit

def get_all_path(parent_path):
    '''return all direstoray paths'''
    names = get_immediate_subdirectories(parent_path)
    path_list = []
    for sub_name in names:
        sub_sub_path, sub_sub_names = get_sub_directory(parent_path, sub_name)
        if sub_sub_names:
            for sub_sub_name in sub_sub_names:
                sub_sub_sub_path, sub_sub_sub_names = get_sub_directory(sub_sub_path, sub_sub_name)
                if sub_sub_sub_names:
                    for sub_sub_sub_name in sub_sub_sub_names:
                        sub_sub_sub_sub_path, sub_sub_sub_sub_names = get_sub_directory(sub_sub_sub_path, sub_sub_sub_name)
                        if sub_sub_sub_sub_names:
                            for sub_sub_sub_sub_name in sub_sub_sub_sub_names:
                                sub_sub_sub_sub_sub_path, sub_sub_sub_sub_sub_names = get_sub_directory(sub_sub_sub_sub_path, sub_sub_sub_sub_name)
                                if sub_sub_sub_sub_sub_names:
                                    for sub_sub_sub_sub_sub_name in sub_sub_sub_sub_sub_names:
                                        sub_sub_sub_sub_sub_sub_path, sub_sub_sub_sub_sub_sub_names = get_sub_directory(sub_sub_sub_sub_path, sub_sub_sub_sub_name)                                        
                                        if sub_sub_sub_sub_sub_sub_names:
                                            for sub_sub_sub_sub_sub_sub_name in sub_sub_sub_sub_sub_sub_names:
                                                sub_sub_sub_sub_sub_sub_sub_path, sub_sub_sub_sub_sub_sub_sub_names = get_sub_directory(sub_sub_sub_sub_sub_path, sub_sub_sub_sub_sub_name)                                        
                                                if sub_sub_sub_sub_sub_sub_sub_names:
                                                    for sub_sub_sub_sub_sub_sub_sub_name in sub_sub_sub_sub_sub_sub_sub_names:
                                                        path_list.append(sub_sub_sub_sub_sub_sub_sub_path  + "/" + sub_sub_sub_sub_sub_sub_sub_name + "/*")
                                            
                                                else:
                                                    path_list.append(sub_sub_sub_sub_sub_sub_path  + "/" + sub_sub_sub_sub_sub_sub_name + "/*")

                                        else:
                                            path_list.append(sub_sub_sub_sub_sub_path  + "/" + sub_sub_sub_sub_sub_name + "/*")

                                else:    
                                    path_list.append(sub_sub_sub_sub_path  + "/" + sub_sub_sub_sub_name + "/*")
                                
                        else:
                            path_list.append(sub_sub_sub_path + "/" + sub_sub_sub_name + "/*")
                
                else:
                    path_list.append(sub_sub_path + "/" + sub_sub_name + "/*")

        else:
            path_list.append(parent_path + "/" + sub_name + "/*")
    return path_list

def get_sub_directory(path, names):
    '''sub sub path'''
    sublines_path = path + "/" + names
    return (sublines_path, get_immediate_subdirectories(sublines_path))      

def get_immediate_subdirectories(a_dir):
    '''get subdiretory of dataset'''
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def folder_path(path):

    folders = []

    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for folder in d:
            folders.append(os.path.join(r, folder))
    return folders  

def main():
    '''
    start = timeit.default_timer()
    path_list = get_all_path("in/maildir")
    #print(path_list)
    print("Number of paths: ", len(path_list))
    stop = timeit.default_timer()
    print('Runtime: ', stop - start)  
    
    start = timeit.default_timer()
    path = folder_path("in/maildir")
    #print(path)
    print("Number of paths: ", len(path))
    stop = timeit.default_timer()
    print('Runtime: ', stop - start)  
    '''
    path_list_all = get_immediate_subdirectories("in/maildir")
    count = 0
    for path in path_list_all:
        count += 1
        print(str(count) + "_" + path)
    print("path_list_all: ", len(path_list_all))

if __name__ == "__main__":
    main()