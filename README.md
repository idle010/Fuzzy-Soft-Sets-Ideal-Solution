"# Fuzzy-Soft-Sets-Ideal-Solution" 

http://www.mdpi.com/2073-8994/9/10/246
Liu, Z.; Qin, K.; Pei, Z.	A Method for Fuzzy Soft Sets in Decision-Making Based on an Ideal Solution. Symmetry 2017, 9, 246.


## Synopsis

This project contains all test cases for "A method for Fuzzy Soft Sets in Decision making Based on Ideal Solution".

## Environmental requirements

Programs can run under Windows, Linux, and Macs. </br>
Install Python2.7, download Address: https://www.python.org </br>
No additional libraries are required. Of course, if NumPy is used, the code will be more refined. </br>


## Code Example


Running the examples: <br />
To run the first example, change directory to the example you want to run then issue the following command:
### Example2, Example3:&nbsp;<br />
C:\Examples&gt;e:\Python27\python.exe Example2_choice_value.py <br />
[1.0, 1.0, 1.0, 1.0]<br />
[1.0, 1.0, 1.0, 0.0]<br />
[1.0, 0.0, 1.0, 1.0]<br />
[1.0, 0.0, 1.0, 0.0]<br />
[1.0, 0.0, 0.0, 0.0]<br />
[1.0, 1.0, 1.0, 1.0]<br />
The choicevalue is:4.000 position is:0 <br />
The choicevalue is:4.000 position is:5 <br />

C:\Examples&gt;e:\python27\python.exe Example3_weighted_choice_value.py<br />
[1.0, 1.0, 1.0, 1.0]<br />
[1.0, 1.0, 1.0, 0.0]<br />
[1.0, 0.0, 1.0, 1.0]<br />
[1.0, 0.0, 1.0, 0.0]<br />
[1.0, 0.0, 0.0, 0.0]<br />
[1.0, 1.0, 1.0, 1.0]<br />
[0.5, 0.25, 0.125, 0.0625]<br />
The choicevalue is:0.9375 position is:0<br />
The choicevalue is:0.9375 position is:5<br />
<br />
<br />

2017-10-09&nbsp; 19:20&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 54 example1.txt<br />
2017-10-10&nbsp; 01:22&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1,568 Example2_choice_value.py<br />
2017-10-09&nbsp; 22:55&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1,864 Example3_weighted_choice_value.py<br />
<br />


### Example4:&nbsp;<br />
C:\Examples&gt;e:\python27\python.exe Example4_comparison_score.py<br />
Soft Set =<br />
[0.2, 0.4, 0.1, 0.5, 0.8, 0.1, 0.1]<br />
[0.3, 0.2, 0.3, 0.6, 0.3, 0.9, 0.6]<br />
[0.3, 0.1, 0.6, 0.7, 0.8, 0.8, 0.3]<br />
[0.3, 0.7, 0.9, 0.9, 0.1, 0.4, 0.5]<br />
[0.3, 0.9, 0.1, 0.3, 0.2, 0.2, 0.3]<br />
[0.3, 0.9, 0.1, 0.3, 0.9, 0.7, 0.8]<br />
[0.3, 0.9, 0.1, 0.3, 0.2, 0.8, 0.9]<br />
[0.3, 0.9, 0.1, 0.3, 0.1, 0.4, 0.2]<br />
Comparison Table =<br />
[7, 2, 2, 1, 3, 2, 3, 3]<br />
[5, 7, 4, 4, 6, 4, 5, 6]<br />
[6, 4, 7, 3, 6, 4, 5, 6]<br />
[6, 4, 5, 7, 5, 3, 3, 6]<br />
[5, 2, 3, 3, 7, 4, 5, 6]<br />
[6, 4, 4, 5, 7, 7, 5, 7]<br />
[5, 3, 4, 5, 7, 6, 7, 7]<br />
[5, 2, 2, 4, 5, 4, 4, 7]<br />
row-sum: [23, 41, 41, 39, 35, 45, 44, 33]<br />
col-sum: [45, 28, 31, 32, 46, 34, 37, 48]<br />
Score Table=<br />
23 &amp; 45 &amp; -22<br />
41 &amp; 28 &amp; 13<br />
41 &amp; 31 &amp; 10<br />
39 &amp; 32 &amp; 7<br />
35 &amp; 46 &amp; -11<br />
45 &amp; 34 &amp; 11<br />
44 &amp; 37 &amp; 7<br />
33 &amp; 48 &amp; -15<br />
[-22, 13, 10, 7, -11, 11, 7, -15]<br />
The max score is:13 , pos is:1<br />
<br />
<br />
2017-10-09&nbsp; 22:06&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;232 example4.txt<br />
2017-10-10&nbsp; 01:22&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;2,133 Example4_comparison_score.py<br />
<br />

### Example5:&nbsp;<br />
C:\Examples&gt;e:\python27\python.exe Example5_cmpsco_rankrev.py<br />
Soft Set =<br />
[0.2, 0.3, 0.6, 0.3, 0.9, 0.6]<br />
[0.9, 0.1, 0.3, 0.9, 0.7, 0.8]<br />
[0.4, 0.1, 0.5, 0.8, 0.1, 0.1]<br />
Comparison Table =<br />
[6, 3, 4]<br />
[3, 6, 5]<br />
[2, 2, 6]<br />
Score Table=<br />
13 &amp; 11 &amp; 2<br />
14 &amp; 11 &amp; 3<br />
10 &amp; 15 &amp; -5<br />
[2, 3, -5]<br />
The max score is:3 , pos is:1<br />
{0: 2, 1: 3, 2: -5}<br />
[2, 0, 1]<br />
2 &gt; 0 &gt; 1<br />
<br />
2017-10-09&nbsp; 22:39&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 75 example5.txt<br />
2017-10-09&nbsp; 22:57&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;2,588 Example5_cmpsco_rankrev.py<br />
<br />

### Example6:&nbsp;<br />
C:\Examples&gt;e:\python27\python.exe Example6_cmpsco_rankrev.py<br />
<br />
------------------<br />
Soft Set =<br />
[0.2, 0.3, 0.6, 0.3, 0.9, 0.6]<br />
[0.9, 0.1, 0.3, 0.9, 0.7, 0.8]<br />
[0.4, 0.1, 0.5, 0.8, 0.1, 0.1]<br />
[0.9, 0.3, 0.3, 0.2, 0.8, 0.9]<br />
------------------<br />
Comparison Table =<br />
[6, 3, 4, 4]<br />
[3, 6, 5, 3]<br />
[2, 2, 6, 2]<br />
[3, 5, 4, 6]<br />
row-sum: [17, 17, 12, 18]<br />
col-sum: [14, 16, 19, 15]<br />
Score Table=<br />
17 &amp; 14 &amp; 3<br />
17 &amp; 16 &amp; 1<br />
12 &amp; 19 &amp; -7<br />
18 &amp; 15 &amp; 3<br />
------------------<br />
Score:<br />
[3, 1, -7, 3]<br />
The max score is:3 , pos is:0<br />
The max score is:3 , pos is:3<br />
{0: 3, 1: 1, 2: -7, 3: 3}<br />
[2, 1, 0, 3]<br />
2 &gt; 1 &gt; 0 &gt; 3<br />
<br />
2017-10-09&nbsp; 22:50&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;100 example6.txt<br />
2017-10-12&nbsp; 23:43&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;2,662 Example6_cmpsco_rankrev.py<br />
<br />

### Example7:&nbsp;<br />
C:\Examples&gt;e:\python27\python.exe Example7_fss_idealsolution.py<br />
[1.0, 1.0, 1.0, 0.0, 1.0, 1.0]<br />
[0.741, 0.182, 0.5, 0.924, 0.5, 1.0]<br />
[0.891, 0.891, 0.269, 0.971, 0.0, 0.5]<br />
[0.652, 0.5, 0.622, 0.818, 0.75, 0.75]<br />
[0.813, 0.354, 0.5, 0.881, 0.5, 0.5]<br />
[0.5, 0.0625, 0.0625, 0, 0.25, 0.125]<br />
The weighted Hamming distance is [0.33687500000000004, 0.4195, 0.322625, 0.35262<br />
5]<br />
The min distance is:0.3226 The choice is:h2<br />
{0: 0.33687500000000004, 1: 0.4195, 2: 0.322625, 3: 0.352625}<br />
3 &lt; 1 &lt; 4 &lt; 2<br />
<br />
The Programs for Example7.&nbsp;<br />
2017-10-10&nbsp; 00:55&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;148 example7.txt<br />
2017-10-12&nbsp; 23:51&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;2,900 Example7_fss_idealsolution.py<br />
<br />

### Example8:&nbsp;<br />
C:\Examples&gt;e:\python27\python.exe Example8_fss_idealsolution.py<br />
[1.0, 1.0, 1.0, 0.881, 1.0, 1.0]<br />
[0.741, 0.182, 0.5, 0.924, 0.5, 1.0]<br />
[0.891, 0.891, 0.269, 0.971, 0.0, 0.5]<br />
[0.652, 0.5, 0.622, 0.818, 0.75, 0.75]<br />
[0.813, 0.354, 0.5, 0.881, 0.5, 0.5]<br />
The weighted Hamming distance is [0.31196666666666667, 0.4225333333333333, 0.269<br />
8333333333333, 0.3610666666666667]<br />
The min distance is:0.2698 The choice is:h2<br />
{0: 0.31196666666666667, 1: 0.4225333333333333, 2: 0.2698333333333333, 3: 0.3610<br />
666666666667}<br />
3 &lt; 1 &lt; 4 &lt; 2<br />
<br />
2017-10-10&nbsp; 01:08&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;152 example8.txt<br />
2017-10-12&nbsp; 23:51&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;2,893 Example8_fss_idealsolution.py<br />
<br />

### Example9:&nbsp;<br />
C:\Examples&gt;e:\python27\python.exe Example9_fss_idealsolution.py<br />
[1.0, 1.0, 1.0, 0.0, 1.0, 1.0]<br />
[0.741, 0.182, 0.5, 0.924, 0.5, 1.0]<br />
[0.891, 0.891, 0.269, 0.971, 0.0, 0.5]<br />
[0.652, 0.5, 0.622, 0.818, 0.75, 0.75]<br />
[0.813, 0.354, 0.5, 0.881, 0.5, 0.5]<br />
The weighted Hamming distance is [0.5849333333333333, 0.6502, 0.5027999999999999<br />
, 0.6047333333333333]<br />
The min distance is:0.5028 The choice is:h2<br />
{0: 0.5849333333333333, 1: 0.6502, 2: 0.5027999999999999, 3: 0.6047333333333333}<br />
<br />
3 &lt; 1 &lt; 4 &lt; 2<br />
<br />
2017-10-10&nbsp; 01:12&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;148 example9.txt<br />
2017-10-12&nbsp; 23:51&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;2,890 Example9_fss_idealsolution.py<br />
<br />

### Example10:&nbsp;<br />
C:\Examples&gt;e:\python27\python.exe Example_fss_idealsolution.py<br />
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]<br />
[0.2, 0.4, 0.1, 0.5, 0.8, 0.1, 0.1]<br />
[0.3, 0.2, 0.3, 0.6, 0.3, 0.9, 0.6]<br />
[0.3, 0.1, 0.6, 0.7, 0.8, 0.8, 0.3]<br />
[0.3, 0.7, 0.9, 0.9, 0.1, 0.4, 0.5]<br />
[0.3, 0.9, 0.1, 0.3, 0.2, 0.2, 0.3]<br />
[0.3, 0.9, 0.1, 0.3, 0.9, 0.7, 0.8]<br />
[0.3, 0.9, 0.1, 0.3, 0.2, 0.8, 0.9]<br />
[0.3, 0.9, 0.1, 0.3, 0.1, 0.4, 0.2]<br />
The normalized Hamming distance is: [0.6857142857142857, 0.5428571428571428, 0.4<br />
8571428571428577, 0.4571428571428572, 0.6714285714285715, 0.42857142857142855, 0<br />
.5000000000000001, 0.6714285714285715]<br />
The min distance is:0.4286 The choice is:h5<br />
[0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0]<br />
The weighted Hamming distance is [0.7140625, 0.6859375000000001, 0.6531250000000<br />
001, 0.48125, 0.56875, 0.5390625, 0.5593750000000001, 0.56875]<br />
The min distance is:0.4813 The choice is:h3<br />
<br />
2017-10-10&nbsp; 00:08&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;247 examplefssis.txt<br />
2017-10-12&nbsp; 23:48&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;2,626 Example_fss_idealsolution.py<br />
<br />
### Random generate SoftSet:&nbsp;<br />
In some cases, we need large dataset to test the program.<br />
This program automatically generates fuzzy soft sets randomly.<br />
This is especially useful for testing the rank reversal.<br />


2017-10-09&nbsp; 23:12&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;566 randgen_softset.py<br />
2017-10-11&nbsp; 22:33&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 24,341 randsoftset.txt<br />
<br />

----------------------------------------------------------------------
README.md





## License

This project is licensed under the MIT License.
