# cisc3160lab2
Repository for Lab 2

## Part 2.1
```lab2_1.py``` takes a CSV file, in this case ```regional-global-daily-latest.csv```, this data set was downloaded from https://spotifycharts.com/regional. It then takes that data, multiplies the listens per day to get a 7 day projection.

### Execution
Execute ```lab2_1.py``` with ```python3 lab2_1.py```.

### Output
```
PROJECTED TOP 20 WEEKLY STREAMS


#    PROJECTED      SONG NAME                                ARTIST        
--------------------------------------------------------------------------------
1    41,949,047     WAP (feat. Megan Thee Stallion..         Cardi B 
2    37,400,580     Mood (feat. Iann Dior)                   24kGoldn
3    35,576,695     Hawái                                    Maluma  
4    28,573,650     Dynamite                                 BTS     
5    25,195,877     Blinding Lights                          The Weeknd
6    24,899,077     Watermelon Sugar                         Harry Styles
7    24,397,968     Savage Love (Laxed - Siren Bea..         Jawsh 685
8    23,638,048     Laugh Now Cry Later (feat. Lil..         Drake   
9    23,032,632     ROCKSTAR (feat. Roddy Ricch)             DaBaby  
10   19,169,073     For The Night (feat. Lil Baby ..         Pop Smoke
11   19,130,811     Ice Cream (with Selena Gomez)            BLACKPINK
12   18,767,847     Heather                                  Conan Gray
13   17,384,360     Mood Swings (feat. Lil Tjay)             Pop Smoke
14   17,276,805     Head & Heart (feat. MNEK)                Joel Corry
15   17,068,373     Breaking Me                              Topic   
16   16,913,855     Lemonade (feat. Gunna, Don Tol..         Internet Money
17   16,705,010     Roses - Imanbek Remix                    SAINt JHN
18   16,338,203     Ay, DiOs Mío!                            KAROL G 
19   15,547,385     POPSTAR (feat. Drake)                    DJ Khaled
20   15,048,460     UN DIA (ONE DAY) (Feat. Tainy)           J Balvin
```
## Part 2.2
```lab2_2.py``` takes a CSV file, in this case ```weatherdataset.csv``` then outputs and converts the tempuratures as suggested in the assignment example.

### Execution
Execute ```lab2_2.py``` with ```python3 lab2_2.py```

### Output
```
CONVERTED WEATHER DATA SET

DATE       TEMP (INPUT -> F)    TEMP (C)       TEMP (F)      
----------------------------------------------------------
01/01/01   18.3                 -7.61          18.3          
01/02/01   14.17                -9.91          14.17         
01/03/01   13.3                 -10.39         13.3          
01/04/01   19.7                 -6.83          19.7          
01/05/01   49.98                9.99           49.98         
01/06/01   78.65                25.92          78.65         
01/07/01   99.52                37.51          99.52         
01/08/01   100.78               38.21          100.78        
01/09/01   451.91               233.28         451.91        
01/10/01   44.81                7.12           44.81         
01/11/01   62.18                16.77          62.18         
01/12/01   14.5                 -9.72          14.5          
01/13/01   19.6                 -6.89          19.6          
01/14/01   51.3                 10.72          51.3          
01/15/01   49.11                9.51           49.11         
01/16/01   82.4                 28.0           82.4          
01/17/01   18.4                 -7.56          18.4          
01/18/01   19.2                 -7.11          19.2          
01/19/01   44.5                 6.94           44.5          
01/20/01   11.1                 -11.61         11.1          
01/21/01   33.65                0.92           33.65         
01/22/01   18.13                -7.71          18.13         
01/23/01   19.54                -6.92          19.54         
01/24/01   31.24                -0.42          31.24         
01/25/01   19.3                 -7.06          19.3          
01/26/01   14.5                 -9.72          14.5          
01/27/01   19.2                 -7.11          19.2          
```

## Part 2.3
```lab2_3.py``` is a simple request to a test API endpoint. If the request is successful (i.e. 200) then the returned JSON is printed to the terminal.

### Execution
Execute ```lab2_3.py``` with ```python3 lab2_3.py```

**Please note**: the ```requests``` library is a dependency and needed.

### Output
```
OK! - 200

RETURNED JSON:
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
```

# Reflection
## Which programming languages did you use for each of these problems?

I chose to use Python for all 3 of these exercises simple due to the simplicity and efficiency. Furthermore, the offered libraries such as csv and requests make the tasks 50 lines of code or less. If these exercises, namely 2.3, were to be done in a language such as Java the result may be something that would be more robust, secure, and easily scaled in a production case, but to do simple tasks Python works well. That being said there can be tremendous draw backs from using an interpreted language like Python mainly a reliance on external libraries and code that is resource intensive.

## Why did you choose a particular language? (There is no right or wrong answer here, choosing an implementation is an art form)

When approaching a problem it’s important to clearly rationalize the constraints of the problem and adhere to those bounds with a programming paradigm and language that meets and excels at those constraints. Python is an excellent extensive scripting language, and I selected it namely due to my somewhat familiarity with it, along with ability to easily solve all 3 of the exercises without a tremendous amount of forethought or headache.

## Was there any difficult or easy about using that language for solving the problem?

The hardest part of using Python for me is always retaining and remembering the syntax, however, for small excercises such as these it's extremely painless.

## If you had to solve the problem again, would you choose a different language?

With these specific exercises, absolutely not.
