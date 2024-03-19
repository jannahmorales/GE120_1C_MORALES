"""
1. Differentiate Procedural Programming from Functional Programming
Functional Programming emphasizes being concise and this is done through the use of functions, modules, 
and packages. It is advised to avoid the 'WET' principle, which means to 'Write Everything Twice', to be more efficient
and intentional with your code. Why rewrite a lines of code repeatedly when you are able to define a function that
could perform the same functions with a single line? Similarly, why go through the hassle of writing code that would convert
a value to radians when you could use the existing function from the math module. Procedural Programming, on the other hand, 
allows us to create a code that will perform a task for varying conditions. Under procedural programming, the sequence in which
you begin to write your code is discussed. From writing an algorithm, creating a pseudocode, a flowchart, and then the actual program.
It helps visualize the sequence of actions that your code is supposed to perform, the use of loops, such as for and while loops,
are introduced in procedural programming as well.

repeating your code through the use of functions.Procedural programming loops 

2. How does Git help in the Collaborative Development and Version Control environment of programming?
Git helps with collaborative development as users are able to work on a program separately through different branches,
users are able to create different versions of a code without having to worry about potentially ruining the main code.
Through Git, since individual users can work on the same code, there are more eyes combing through the code to test and
solve different parts of a problem which means that users are able to learn from one another. Git also helps with
version control as prior to uploading to a repository, users are prompted to write messages describing the changes made
to a program, who made certain changes are tracked through Git as well.

3. When should one use a while loop and when should one use a for loop? Give examples in the field of geomatics.
A while loop is used if there is a fixed condition necessary to repeat a task, it could also be used with boolean logic. 
For example, if you needed to write program that computes for the REC of a closed-loop traverse, there is a standard 
that you are required to follow. As such, 'while' the value is not (!=) equal to the required REC, the program has to
repeatedly compute for the REC until the standard is reached. On the other hand, a for loop is used in situations
where a task is repeated for existing objects within a range of values. An example is in computing for the elevation
of different turning points in a vertical control survey. The program has to repeat the task of computing for the elevation
'for' every turning point.

- while loop: necessary to repeat a task with a fixed condition
- for loop: repetition but for existing objects within a range of values 

4. Discuss the Divide and COnquer paradigm in programming
The Divide and Conquer paradigm in programming intends to break down a primary or bigger task into sub-problems. Upon
creating an algorithm, the different tasks that could be solved with smaller sets of code and turned into functions
be seen. As such, the length of a code is minimized and the overall program is more efficient. By breaking down the
main task or problem to be solved, mas lilitaw yung mga cases where an error occur na ma-mimiss if we attempt to
solve the task with one big code. The divide and conquer paradigm will help ensure the functionality as well as thoroughness
of a code, we can work on a sub-problem and create solutions for different test cases and thus, avoid minor errors in coming 
up as the different solutions for each sub-task are put together.
- break down a bigger problem into subproblems, create a program that solves individual problems and minimize length of code by creating functions throughout the process

5. Give an example of a task related to geomatics that is done manually and can be optimized using programming? WHat would be your plan of attack for this solution?
An example of a task related to geomatics that is usually done manually is the computation of the Northings and Eastings
of a traverse. The task makes use of codes we have created for prior machine exercises such as coverting azimuth to bearing
and computing for the latitude and departure of a line. A possible plan-of-attack for this solution would be to use the existing
code for latitude and departure, and build on it by creating a function that computes for the correction of each latitude and departure,
and the adjusted values using algebraic functions and a for loop. The next task would be to ask for the user to input
the Northing and Easting of the first point and create a code that would add the adjusted latitude and departure values
to the Northing and Easting for each point.
"""