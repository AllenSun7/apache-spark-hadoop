import os
import timeit
def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def main():
        #cauculate runtime
    start = timeit.default_timer()
    stop = timeit.default_timer()
    print('Time: ', stop - start) 

if __name__ == "__main__":
    main()