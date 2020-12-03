package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func xor(a bool, b bool) (bool) {
	return (a && !b) || (!a && b)
}

func validate(start int, end int, char string, password string) (bool) {
	count := 0
	for i := 0; i < len(password); i += 1 {
		if password[i:i+1] == char {
			count += 1
		}
	}
	return (start <= count && count <= end)
}

func validate2(start int, end int, char string, password string) (bool) {
	start, end = start-1, end-1
	if start >= len(password) || end >= len(password) {
		return false
	}
	return xor(password[start:start+1] == char, password[end:end+1] == char)
}

func main() {
	filename := "dec02_input.txt"

	content, err := ioutil.ReadFile(filename)
	check(err)
	lines := strings.Split(string(content), "\n")


	count := 0
	for i, line := range lines {
		if len(line) == 0 {
			continue
		}
		fmt.Printf("%d %s\n", i, line)

		line_arr := strings.Split(line, " ")
		span, char, password := line_arr[0], line_arr[1][0:1], line_arr[2]
		span_arr := strings.Split(span, "-")
		start, err := strconv.Atoi(span_arr[0])
		check(err)
		end, err := strconv.Atoi(span_arr[1])
		check(err)
		// fmt.Printf("%v\n", line_arr)
		// fmt.Printf("%v\n", span_arr)
		// fmt.Printf("%d, %d, %v, %v\n", start, end, char, password)

		if validate2(start, end, char, password) {
			fmt.Printf("Valid\n")
			count += 1
		} else {
			fmt.Printf("Invalid\n")
		}
	}

	fmt.Printf("Total Valid: %d\n", count)

}
