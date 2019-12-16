from pyspark import SparkContext, SparkConf
import enchant
import timeit
import pysnooper
import os


def word_count():
    stop0 = timeit.default_timer()
    conf = SparkConf().setAppName("word count").setMaster("local[5]")
    sc = SparkContext(conf = conf)
    parent_path = "in/maildir/kaminski-v/c/mangmt"
    names = get_immediate_subdirectories(parent_path)
    stop1 = timeit.default_timer()
    stop2 = timeit.default_timer()
    stop3 = timeit.default_timer()  
    stop4 = timeit.default_timer()  
    stop5 = timeit.default_timer()  
    for sub_names in names:
        sublines_path = parent_path + "/" + sub_names
        sub_sub_names = get_immediate_subdirectories(sublines_path)      
        for name in sub_sub_names:
            #print("It is the %dth number of %d" % (count,len(names)))
            #count += 1
            lines_path = sublines_path + "/" + name + "/*"
            stop1 += timeit.default_timer()
            lines = sc.textFile(lines_path) 
            stop2 += timeit.default_timer()
            lines_filter = lines.filter(get_palindrome)
            stop3 += timeit.default_timer()   
            words = lines_filter.flatMap(lambda line: line.split(" "))
            stop4 += timeit.default_timer()   
            wordCounts = words.countByValue()
            stop5 += timeit.default_timer()
            print(wordCounts)
    stop6 = timeit.default_timer()

    
 
    print('Runtime1: ', (stop2 - stop1)) 
    print('Runtime2: ', (stop3 - stop2)) 
    print('Runtime3: ', (stop4 - stop3)) 
    print('Runtime4: ', (stop5 - stop4)) 
    print('Wordcounts Runtime: ', (stop6 - stop0)) 
    
    '''
    wordCounts = words.countByValue()
    
    for word, count in wordCounts.items():
        if word == word[::-1]:
            print("True")
        print("{} : {}".format(word, count))
    '''

def get_immediate_subdirectories(a_dir):
    '''get subdiretory of dataset'''
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def get_palindrome(word):
    '''palindrome'''
    #not same characters: "AAA","BBB"...
    return (len(word) > 2 and \
            word == word[::-1] and \
            not all(c == word[0] for c in word[1:]))  


def main():
    '''cauculate runtime'''
    start = timeit.default_timer()
    word_count()
    stop = timeit.default_timer()
    print('Runtime: ', stop - start) 

if __name__ == "__main__":
    main()