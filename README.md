"# Fuzzy-Soft-Sets-Ideal-Solution" 
## Synopsis

This project contains all test cases for "A method for Fuzzy Soft Sets in Decision making Based on Ideal Solution".

## Environmental requirements

Programs can run under Windows, Linux, and Macs. </br>
Install Python2.7, download Address: https://www.python.org </br>
No additional libraries are required. Of course, if NumPy is used, the code will be more refined. </br>


## Code Example

  


Running programs, example: </br>

C:\Examples>e:\Python27\python.exe Example2_choice_value.py </br> 
[1.0, 1.0, 1.0, 1.0]</br> 
[1.0, 1.0, 1.0, 0.0]</br>
[1.0, 0.0, 1.0, 1.0]</br>
[1.0, 0.0, 1.0, 0.0]</br>
[1.0, 0.0, 0.0, 0.0]</br>
[1.0, 1.0, 1.0, 1.0]</br>
The choicevalue is:4.000 position is:0 </br>
The choicevalue is:4.000 position is:5 </br>
----------------------------------------------------------------------

C:\Examples>e:\python27\python.exe Example3_weighted_choice_value.py
[1.0, 1.0, 1.0, 1.0]
[1.0, 1.0, 1.0, 0.0]
[1.0, 0.0, 1.0, 1.0]
[1.0, 0.0, 1.0, 0.0]
[1.0, 0.0, 0.0, 0.0]
[1.0, 1.0, 1.0, 1.0]
[0.5, 0.25, 0.125, 0.0625]
The choicevalue is:0.9375 position is:0
The choicevalue is:0.9375 position is:5


The Programs for Example2, Example3. 
2017-10-09  19:20                54 example1.txt
2017-10-10  01:22             1,568 Example2_choice_value.py
2017-10-09  22:55             1,864 Example3_weighted_choice_value.py

C:\Examples>e:\python27\python.exe Example4_comparison_score.py
Soft Set =
[0.2, 0.4, 0.1, 0.5, 0.8, 0.1, 0.1]
[0.3, 0.2, 0.3, 0.6, 0.3, 0.9, 0.6]
[0.3, 0.1, 0.6, 0.7, 0.8, 0.8, 0.3]
[0.3, 0.7, 0.9, 0.9, 0.1, 0.4, 0.5]
[0.3, 0.9, 0.1, 0.3, 0.2, 0.2, 0.3]
[0.3, 0.9, 0.1, 0.3, 0.9, 0.7, 0.8]
[0.3, 0.9, 0.1, 0.3, 0.2, 0.8, 0.9]
[0.3, 0.9, 0.1, 0.3, 0.1, 0.4, 0.2]
Comparison Table =
[7, 2, 2, 1, 3, 2, 3, 3]
[5, 7, 4, 4, 6, 4, 5, 6]
[6, 4, 7, 3, 6, 4, 5, 6]
[6, 4, 5, 7, 5, 3, 3, 6]
[5, 2, 3, 3, 7, 4, 5, 6]
[6, 4, 4, 5, 7, 7, 5, 7]
[5, 3, 4, 5, 7, 6, 7, 7]
[5, 2, 2, 4, 5, 4, 4, 7]
row-sum: [23, 41, 41, 39, 35, 45, 44, 33]
col-sum: [45, 28, 31, 32, 46, 34, 37, 48]
Score Table=
23 & 45 & -22
41 & 28 & 13
41 & 31 & 10
39 & 32 & 7
35 & 46 & -11
45 & 34 & 11
44 & 37 & 7
33 & 48 & -15
[-22, 13, 10, 7, -11, 11, 7, -15]
The max score is:13 , pos is:1


The Programs for Example4. 
2017-10-09  22:06               232 example4.txt
2017-10-10  01:22             2,133 Example4_comparison_score.py

C:\Examples>e:\python27\python.exe Example5_cmpsco_rankrev.py
Soft Set =
[0.2, 0.3, 0.6, 0.3, 0.9, 0.6]
[0.9, 0.1, 0.3, 0.9, 0.7, 0.8]
[0.4, 0.1, 0.5, 0.8, 0.1, 0.1]
Comparison Table =
[6, 3, 4]
[3, 6, 5]
[2, 2, 6]
Score Table=
13 & 11 & 2
14 & 11 & 3
10 & 15 & -5
[2, 3, -5]
The max score is:3 , pos is:1
{0: 2, 1: 3, 2: -5}
[2, 0, 1]
2 > 0 > 1

The Programs for Example5. 
2017-10-09  22:39                75 example5.txt
2017-10-09  22:57             2,588 Example5_cmpsco_rankrev.py


C:\Examples>e:\python27\python.exe Example6_cmpsco_rankrev.py

------------------
Soft Set =
[0.2, 0.3, 0.6, 0.3, 0.9, 0.6]
[0.9, 0.1, 0.3, 0.9, 0.7, 0.8]
[0.4, 0.1, 0.5, 0.8, 0.1, 0.1]
[0.9, 0.3, 0.3, 0.2, 0.8, 0.9]
------------------
Comparison Table =
[6, 3, 4, 4]
[3, 6, 5, 3]
[2, 2, 6, 2]
[3, 5, 4, 6]
row-sum: [17, 17, 12, 18]
col-sum: [14, 16, 19, 15]
Score Table=
17 & 14 & 3
17 & 16 & 1
12 & 19 & -7
18 & 15 & 3
------------------
Score:
[3, 1, -7, 3]
The max score is:3 , pos is:0
The max score is:3 , pos is:3
{0: 3, 1: 1, 2: -7, 3: 3}
[2, 1, 0, 3]
2 > 1 > 0 > 3


The Programs for Example6. 
2017-10-09  22:50               100 example6.txt
2017-10-12  23:43             2,662 Example6_cmpsco_rankrev.py

C:\Examples>e:\python27\python.exe Example7_fss_idealsolution.py
[1.0, 1.0, 1.0, 0.0, 1.0, 1.0]
[0.741, 0.182, 0.5, 0.924, 0.5, 1.0]
[0.891, 0.891, 0.269, 0.971, 0.0, 0.5]
[0.652, 0.5, 0.622, 0.818, 0.75, 0.75]
[0.813, 0.354, 0.5, 0.881, 0.5, 0.5]
[0.5, 0.0625, 0.0625, 0, 0.25, 0.125]
The weighted Hamming distance is [0.33687500000000004, 0.4195, 0.322625, 0.35262
5]
The min distance is:0.3226 The choice is:h2
{0: 0.33687500000000004, 1: 0.4195, 2: 0.322625, 3: 0.352625}
3 < 1 < 4 < 2



The Programs for Example7. 
2017-10-10  00:55               148 example7.txt
2017-10-12  23:51             2,900 Example7_fss_idealsolution.py

C:\Examples>e:\python27\python.exe Example8_fss_idealsolution.py
[1.0, 1.0, 1.0, 0.881, 1.0, 1.0]
[0.741, 0.182, 0.5, 0.924, 0.5, 1.0]
[0.891, 0.891, 0.269, 0.971, 0.0, 0.5]
[0.652, 0.5, 0.622, 0.818, 0.75, 0.75]
[0.813, 0.354, 0.5, 0.881, 0.5, 0.5]
The weighted Hamming distance is [0.31196666666666667, 0.4225333333333333, 0.269
8333333333333, 0.3610666666666667]
The min distance is:0.2698 The choice is:h2
{0: 0.31196666666666667, 1: 0.4225333333333333, 2: 0.2698333333333333, 3: 0.3610
666666666667}
3 < 1 < 4 < 2

The Programs for Example8. 
2017-10-10  01:08               152 example8.txt
2017-10-12  23:51             2,893 Example8_fss_idealsolution.py

C:\Examples>e:\python27\python.exe Example9_fss_idealsolution.py
[1.0, 1.0, 1.0, 0.0, 1.0, 1.0]
[0.741, 0.182, 0.5, 0.924, 0.5, 1.0]
[0.891, 0.891, 0.269, 0.971, 0.0, 0.5]
[0.652, 0.5, 0.622, 0.818, 0.75, 0.75]
[0.813, 0.354, 0.5, 0.881, 0.5, 0.5]
The weighted Hamming distance is [0.5849333333333333, 0.6502, 0.5027999999999999
, 0.6047333333333333]
The min distance is:0.5028 The choice is:h2
{0: 0.5849333333333333, 1: 0.6502, 2: 0.5027999999999999, 3: 0.6047333333333333}

3 < 1 < 4 < 2


The Programs for Example9. 
2017-10-10  01:12               148 example9.txt
2017-10-12  23:51             2,890 Example9_fss_idealsolution.py

C:\Examples>e:\python27\python.exe Example_fss_idealsolution.py
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
[0.2, 0.4, 0.1, 0.5, 0.8, 0.1, 0.1]
[0.3, 0.2, 0.3, 0.6, 0.3, 0.9, 0.6]
[0.3, 0.1, 0.6, 0.7, 0.8, 0.8, 0.3]
[0.3, 0.7, 0.9, 0.9, 0.1, 0.4, 0.5]
[0.3, 0.9, 0.1, 0.3, 0.2, 0.2, 0.3]
[0.3, 0.9, 0.1, 0.3, 0.9, 0.7, 0.8]
[0.3, 0.9, 0.1, 0.3, 0.2, 0.8, 0.9]
[0.3, 0.9, 0.1, 0.3, 0.1, 0.4, 0.2]
The normalized Hamming distance is: [0.6857142857142857, 0.5428571428571428, 0.4
8571428571428577, 0.4571428571428572, 0.6714285714285715, 0.42857142857142855, 0
.5000000000000001, 0.6714285714285715]
The min distance is:0.4286 The choice is:h5
[0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0]
The weighted Hamming distance is [0.7140625, 0.6859375000000001, 0.6531250000000
001, 0.48125, 0.56875, 0.5390625, 0.5593750000000001, 0.56875]
The min distance is:0.4813 The choice is:h3

The Programs for Example9. 
2017-10-10  00:08               247 examplefssis.txt
2017-10-12  23:48             2,626 Example_fss_idealsolution.py



The Programs for Example9. 
2017-10-09  23:12               566 randgen_softset.py
2017-10-11  22:33            24,341 randsoftset.txt


----------------------------------------------------------------------
README.md





## License

This project is licensed under the MIT License.
