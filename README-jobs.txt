Dataroc VM

At jar path:
type
hadoop jar <Enther jar name> <main java class> [input path] [output path]

<Example> 
-Hadoop
*AnagramCheck:
hadoop jar anagram.jar AnagramCheck gs://apache-dataset-all/test-data/hadoop/* gs://apache-dataset-all/out/hadoop-anagram

*PalindromCheck
hadoop jar palindrome.jar PalindromeCheck gs://apache-dataset-all/test-data/hadoop/* gs://apache-dataset-all/out/hadoop-palindrome
#useful data (1) (5)
--------------------------------------------------
-Spark
spark-submit words_gcp_list.py

======================================================

Jobs
<Submit Job>
****Hadoop****
*1. AnagramCheck
-Region:
us-west1

-Job type:
Hadoop

-Main class or jar:
AnagramCheck

-Arguement:
--input source path:
gs://apache-dataset-all/test-data/words.txt
--output source path:
gs://apache-dataset-all/out/hadoop-anagram

-Jar files:
gs://apache-dataset-all/jar-files/anagram.jar

*2. PalindromeCheck
-Region:
us-west1

-Job type:
Hadoop

-Main class or jar:
PalindromeCheck

-Arguement:
--input source path:
gs://apache-dataset-all/test-data/hadoop/*
--output source path:
gs://apache-dataset-all/out/hadoop-palindrome

-Jar files:
gs://apache-dataset-all/jar-files/palindrome.jar

-----------------------------------------------
****Spark****
*1. SpAnagram
-Region:
us-west1

-Job type:
Spark

-Main class or jar:
SpAnagram

-Arguement:
--min lenth:
3
--input source path:
gs://apache-dataset-all/test-data/spark/*
--output source path:
gs://apache-dataset-all/out/spark-anagram

-Jar files:
gs://apache-dataset-all/jar-files/spanagram.jar


*2. SpPalindrome
-Region:
us-west1

-Job type:
Spark

-Main class or jar:
SpPalindrome

-Arguement:
--input source path:
gs://apache-dataset-all/test-data/hadoop/*
--output source path:
gs://apache-dataset-all/out/spark-palindrome

-Jar files:
gs://apache-dataset-all/jar-files/sppalindrome.jar
