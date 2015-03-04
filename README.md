Sudoku-Quick-Solver
===================


1. Description: 
----------------
This is a python programe to solve sudoku problem.

----------------

2. Example:
----------------
To solve the world "hardest" Sudoku:

./sudokuSlove.py 800000000 003600000 070090200 050007000 000045700 000100030 001000068 008500010 090000400


<p>********* SOLVE BEGIN *********</p>


<p>60 units unsolved...</p>

|8  |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |3  |6  |   |   |   |   |   |
|   |7  |   |   |9  |   |2  |   |   |
|   |5  |   |   |   |7  |   |   |   |
|   |   |   |   |4  |5  |7  |   |   |
|   |   |   |1  |   |   |   |3  |   |
|   |   |1  |   |   |   |   |6  |8  |
|   |   |8  |5  |   |   |   |1  |   |
|   |9  |   |   |   |   |4  |   |   |

<p>The solutin is ...</p>

<p>0 units unsolved...</p>



|8    |1	|2	|7	|5	|3	|6	|4	|9	|
|---|---|---|---|---|---|---|---|---|
|9	|4	|3	|6	|8	|2	|1	|7	|5	|
|6	|7	|5	|4	|9	|1	|2	|8	|3	|
|1	|5	|4	|2	|3	|7	|8	|9	|6	|
|3	|6	|9	|8	|4	|5	|7	|2	|1	|
|2	|8	|7	|1	|6	|9	|5	|3	|4	|
|5	|2	|1	|9	|7	|4	|3	|6	|8	|
|4	|3	|8	|5	|2	|6	|9	|1	|7	|
|7	|9	|6	|3	|1	|8	|4	|5	|2	|


<p>********* SOLVE DONE*********</p>

<p>Total Cost:  185.254096986 Mili Seconds</p>
-----------------

3. Efficiency:
---------------
<p>On OSX platform, @2.3GHz.</p>
<p>To solve "simple" sudoku, less than 5 ms;</p>
<p>To solve "hard" sudoku, 20-50 ms;</p>
<p>To solve "world hardest" sudoku, 330 ms.</p>

