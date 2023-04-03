set output 'running_time.png'

set title 'Running Time of Brute-Force String Matching Algorithm'
set xlabel 'Input Size (n)'
set ylabel 'Running Time (s)'

plot 'output.txt' using 1:2 with linespoints
