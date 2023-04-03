set title "Sorting Algorithms Analysis"
set xlabel "Number of Elements"
set ylabel "Time (seconds)"
set key left top
plot "output1.txt" using 1:2 with lines title "KMP", \
