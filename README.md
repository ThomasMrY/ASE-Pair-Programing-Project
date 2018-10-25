---
title: The ASE Pair Project (MSRA)
---

# Step-0:Output the character frenquency
How is the 26-letter frequency of English distributed in a novel? What are the words that often appear in a type of article? What is the most commonly used term for a writer? What is the most commonly used phrase in Harry Potter, and so on. We will write some procedures to solve this problem and satisfy our curiosity.

Let's Count the occurrences of 26 characters(a,b,c,...) in a text file.
##Usage:
The Arguements

	usage: main.py [-h] [-f F_FILE_NAME] [-c C_FILE_NAME] [-p P_FILE_NAME]
	               [-q Q_FILE_NAME]
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -f F_FILE_NAME, --f_file_name F_FILE_NAME
	                        Output word frequencies
	  -c C_FILE_NAME, --c_file_name C_FILE_NAME
	                        Output character frequencies
	  -p P_FILE_NAME, --p_file_name P_FILE_NAME
	                        Output phrase frequencies
	  -q Q_FILE_NAME, --q_file_name Q_FILE_NAME
	                        Output PREPOSITION pair frequencies
 Count the occurrences of 26 characters(a,b,c,...) in <file name\>

```
python mian.py -c <file name>
```

The output example:
here we use 'gone with the wind' as an exmaple:
```
python mian.py -c gone_with_the_wind.txt
``` 

Then we can get:

	--------------------------
	|     The rank list      |
	|   Letter   | Frequency |
	|          e | 0.13      |
	|          t | 0.09      |
	|          a | 0.08      |
	|          o | 0.07      |
	|          n | 0.07      |
	|          h | 0.07      |
	|          s | 0.06      |
	|          r | 0.06      |
	|          i | 0.06      |
	|          d | 0.05      |
	|          l | 0.04      |
	|          u | 0.03      |
	|          w | 0.02      |
	|          m | 0.02      |
	|          g | 0.02      |
	|          y | 0.02      |
	|          c | 0.02      |
	|          f | 0.02      |
	|          b | 0.01      |
	|          p | 0.01      |
	|          k | 0.01      |
	|          v | 0.01      |
	|          I | 0.00      |
	|          S | 0.00      |
	|          A | 0.00      |
	|          T | 0.00      |
	|          M | 0.00      |
	|          H | 0.00      |
	|          W | 0.00      |
	|          B | 0.00      |
	|          Y | 0.00      |
	|          C | 0.00      |
	|          x | 0.00      |
	|          P | 0.00      |
	|          O | 0.00      |
	|          G | 0.00      |
	|          j | 0.00      |
	|          R | 0.00      |
	|          N | 0.00      |
	|          q | 0.00      |
	|          E | 0.00      |
	|          D | 0.00      |
	|          F | 0.00      |
	|          z | 0.00      |
	|          L | 0.00      |
	|          J | 0.00      |
	|          U | 0.00      |
	|          K | 0.00      |
	|          V | 0.00      |
	|          X | 0.00      |
	|          Q | 0.00      |
	|          Z | 0.00      |
	--------------------------