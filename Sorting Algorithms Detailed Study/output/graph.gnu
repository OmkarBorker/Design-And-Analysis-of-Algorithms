
set title "Sorting Algorithms Analysis"
set xlabel "Number of Elements"
set ylabel "Time (seconds)"
set key left top
plot "insertion.txt" using 1:2 with lines title "Insertion Sort", \
     "bubble.txt" using 1:2 with lines title "Bubble Sort", \
     "selection.txt" using 1:2 with lines title "Selection Sort", \
     "merge.txt" using 1:2 with lines title "Merge Sort", \
     "quick.txt" using 1:2 with lines title "Quick Sort", \
     "heap.txt" using 1:2 with lines title "Heap Sort"
