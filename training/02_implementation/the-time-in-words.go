// https://www.hackerrank.com/challenges/the-time-in-words
package main
import (
	"fmt"
)

func findTime(h, m int)string{
	time := []string{"pass", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
		"ten", "eleven", "twelve", "thirteen", "fourteen", "pass", "sixteen", "seventeen",
		"eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four",
		"twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine", "pass",
	}
	if m == 0{
		return time[h] + " o' clock"
	}
	if m == 15{
		return "quarter past " + time[h]
	}
	if m == 30{
		return "half past " + time[h]
	}
	if m == 45{
		return "quarter to " + time[(h + 1) % 12]
	}

	isS := ""
	if m < 30{
		if m != 1 && m != 21{
			isS = "s"
		}
		return time[m] + " minute" + isS + " past " + time[h]
	}

	if m > 30{
		m = 60 - m
		if m != 1 && m != 21{
			isS = "s"
		}
		return time[m] + " minute" + isS + " to " + time[(h + 1) % 12]
	}
	return ""
}

func main(){
    h, m := 0, 0
    fmt.Scanf("%d %d", &h, &m)
	answer := findTime(h, m)
	fmt.Println(answer)
}
