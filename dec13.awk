#!/usr/bin/awk -M -f
# awk arrays start at 1 instead of 0
BEGIN {
    print "$0"
}
NR==1{
    start=$0
    print "Starting point is",$0
    FS=","
}
NR==2{
    print "Entire line is",$0
    n=split($0, arr, ",")
    print "Array length is",n
}
END {
    max=0
    product=1
    j=1
    for (i=1; i<=n; i++) {
        if (arr[i] != "x") {
            print i, arr[i]
            times[j] = arr[i]
            product *= arr[i]
            j++
            if (max < arr[i]) {
                max = arr[i]
                max_i = i
            }

        }
    }
    print "---"
    print "max is:",max
    print "product is:",product

    print "---"
    min=max
    for (k=1; k<=j-1; k++) {
        print k, times[k]
        inc = times[k]
        diff = inc * (1 + int(start / inc)) - start
        if (min > diff) {
            min = diff
            best_bus = inc
        }
    }
    print "min is:",min
    print "best bus is:",best_bus
    print "answer to part 1 is:",min*best_bus


    # Move in increments of the largest value
    t = 1
    inc = 1
    i_cur = 1

    failure = 1
    while (failure) {
        t += inc
        failure = 0
        printf "Checking time %-14s increment %s\n", t, inc
        # Check to see if it's an increment of the current values in the list
        # If so, then update our increment
        for (i=i_cur; i<=n; i++) {
            freq = arr[i]
            if (freq == "x") {
                i_cur = i + 1
            } else {
                target = t + i - 1
                printf "t=%s, freq=%s, i=%s, diff=%-2s -- ", t, freq, i, diff
                if (target % freq == 0) {
                    i_cur = i + 1
                    inc *= freq
                    print "Changing increment! Now " inc
                } else {
                    failure = 1
                }
            }
            if (failure) break
        }
    }
    print "Success! answer to part 2 is",t
}