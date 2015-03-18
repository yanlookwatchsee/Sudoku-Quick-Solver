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

<table>
<tr> <td>8  </td> <td>   </td> <td>   </td> <td>   </td> <td>   </td> <td>   </td> <td>   </td> <td>   </td> <td>   </td> </tr>
<tr> <td>   </td> <td>   </td> <td>3  </td> <td>6  </td> <td>   </td> <td>   </td> <td>   </td> <td>   </td> <td>   </td> </tr>
<tr> <td>   </td> <td>7  </td> <td>   </td> <td>   </td> <td>9  </td> <td>   </td> <td>2  </td> <td>   </td> <td>   </td> </tr>
<tr> <td>   </td> <td>5  </td> <td>   </td> <td>   </td> <td>   </td> <td>7  </td> <td>   </td> <td>   </td> <td>   </td> </tr>
<tr> <td>   </td> <td>   </td> <td>   </td> <td>   </td> <td>4  </td> <td>5  </td> <td>7  </td> <td>   </td> <td>   </td> </tr>
<tr> <td>   </td> <td>   </td> <td>   </td> <td>1  </td> <td>   </td> <td>   </td> <td>   </td> <td>3  </td> <td>   </td> </tr>
<tr> <td>   </td> <td>   </td> <td>1  </td> <td>   </td> <td>   </td> <td>   </td> <td>   </td> <td>6  </td> <td>8  </td> </tr>
<tr> <td>   </td> <td>   </td> <td>8  </td> <td>5  </td> <td>   </td> <td>   </td> <td>   </td> <td>1  </td> <td>   </td> </tr>
<tr> <td>   </td> <td>9  </td> <td>   </td> <td>   </td> <td>   </td> <td>   </td> <td>4  </td> <td>   </td> <td>   </td> </tr>
</table>


<p>The solutin is ...</p>

<p>0 units unsolved...</p>



<table>
<tr> <td>8    </td> <td>1	</td> <td>2	</td> <td>7	</td> <td>5	</td> <td>3	</td> <td>6	</td> <td>4	</td> <td>9	</td> </tr>
<tr> <td>9	</td> <td>4	</td> <td>3	</td> <td>6	</td> <td>8	</td> <td>2	</td> <td>1	</td> <td>7	</td> <td>5	</td> </tr>
<tr> <td>6	</td> <td>7	</td> <td>5	</td> <td>4	</td> <td>9	</td> <td>1	</td> <td>2	</td> <td>8	</td> <td>3	</td> </tr>
<tr> <td>1	</td> <td>5	</td> <td>4	</td> <td>2	</td> <td>3	</td> <td>7	</td> <td>8	</td> <td>9	</td> <td>6	</td> </tr>
<tr> <td>3	</td> <td>6	</td> <td>9	</td> <td>8	</td> <td>4	</td> <td>5	</td> <td>7	</td> <td>2	</td> <td>1	</td> </tr>
<tr> <td>2	</td> <td>8	</td> <td>7	</td> <td>1	</td> <td>6	</td> <td>9	</td> <td>5	</td> <td>3	</td> <td>4	</td> </tr>
<tr> <td>5	</td> <td>2	</td> <td>1	</td> <td>9	</td> <td>7	</td> <td>4	</td> <td>3	</td> <td>6	</td> <td>8	</td> </tr>
<tr> <td>4	</td> <td>3	</td> <td>8	</td> <td>5	</td> <td>2	</td> <td>6	</td> <td>9	</td> <td>1	</td> <td>7	</td> </tr>
<tr> <td>7	</td> <td>9	</td> <td>6	</td> <td>3	</td> <td>1	</td> <td>8	</td> <td>4	</td> <td>5	</td> <td>2	</td> </tr>
</table>

<p>********* SOLVE DONE*********</p>

<p>Total Cost:  185.254096986 Mili Seconds</p>
-----------------

3. Efficiency:
---------------
<p>On OSX platform, @2.3GHz.</p>
<p>To solve "simple" sudoku, less than 5 ms;</p>
<p>To solve "hard" sudoku, 20-50 ms;</p>
<p>To solve "world hardest" sudoku, 330 ms.</p>

