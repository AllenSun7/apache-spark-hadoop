import PathList

if __name__ == "__main__":
    names2 = ["123", "12321", "231213"]
    stop_point = 2
    folder_count = stop_point
    while (stop_point <= len(names2)):
        print(names2[stop_point-1])
        stop_point += 1
    
    parent_path = "in/maildir/dasovich-j"

    stop_point = 0
    folder_count = stop_point
    """    
    with open('out/spark-palindrome/40_watson-k.json') as f:
        dic_palindrome = json.load(f)
    with open('out/spark-palindrome/40_watson-k.json') as f:
        dic_anagram = json.load(f)
    """
    names = PathList.get_immediate_subdirectories(parent_path)
    print(names)
    