Dataroc VM

At jar path:
type
hadoop jar <Enther jar name> <main java class> [input path] [output path]

<Example> 
*AnagramCheck:
hadoop jar anagram.jar AnagramCheck gs://apache-dataset-all/test-data/* gs://apache-dataset-all/out_anagram

PalindromCheck
hadoop jar palindrome.jar PalindromeCheck gs://apache-dataset-all/test-data/* gs://apache-dataset-all/out_palindrome

===========================================
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
gs://apache-dataset-all/test-data/hadoop/*
--output source path:
gs://apache-dataset-all/out_hadoop-anagram

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
gs://apache-dataset-all/out_hadoop-palindrome

-Jar files:
gs://apache-dataset-all/jar-files/palindrome.jar

-----------------------------------------------
****Spark****
*1. AnagramCheck
-Region:
us-west1

-Job type:
Spark

-Main class or jar:
PalindromeCheck

-Arguement:
--input source path:
gs://apache-dataset-all/test-data/spark/*
--output source path:
gs://apache-dataset-all/out_spark-palindrome

-Jar files:
gs://apache-dataset-all/jar-files/spanagram.jar


*2. PalindromeCheck
-Region:
us-west1

-Job type:
Spark

-Main class or jar:
PalindromeCheck

-Arguement:
--input source path:
gs://apache-dataset-all/test-data/hadoop/*
--output source path:
gs://apache-dataset-all/out_spark-palindrome

-Jar files:
gs://apache-dataset-all/jar-files/sppalindrome.jar
