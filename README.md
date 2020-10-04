# Strassen-Matrix-Multiplication

- Implementation

For the implementation of the algorithm we use the python programming language, since it is very performative when it comes to mathematical operations.
We use the resources of the numpy library to carry out the base operations with the matrices, such as addition, subtraction, separation into 4 groups and their union.

- Experimentation

For experimenting with the efficiency of the Strassen algorithm we consider generating pairs of random matrices of sizes that are power of 2, and for each we execute each algorithm 30 times, however, for the larger matrices of size 512 and 1024 we execute 5 and 3 times respectively, since the processing time for these entries is considerably longer than the others, which makes the 30 repetitions unfeasible.

- Results

After performing the experimentation tests, the results were as expected, the Strassen algorithm has a noticeably better performance than the classic algorithm for larger matrices.
From the graph below, it is possible to visualize the performance of the strassen algorithm compared to the usual implementation of matrix multiplication demonstrated by the red line.
The raw data of an experimentation simulation run is contained here: [Results](https://github.com/yandiaszup/Strassen-Matrix-Multiplication/blob/main/Results.txt)

![alt text](https://github.com/yandiaszup/Strassen-Matrix-Multiplication/blob/main/StrassenBenchmark.png)
