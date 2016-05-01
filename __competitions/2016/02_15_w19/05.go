package main
import (
	"fmt"
	"time"
)

func minDistance(arr []int) int{
	minDist := len(arr) * 2
	for i := 0; i < len(arr) - 1; i++{
		v := arr[i] - arr[i + 1]
		if v < 0{
			v = -v
		}

		if v < minDist{
			minDist = v
		}
	}

	return minDist
}

func permutations(n int){
    s := make([]int, n)
    for i := range s {
        s[i] = i + 1
    }

    permute(s, func(arr []int) {
		m := minDistance(arr)
		if m == len(arr) / 2 {
            fmt.Println(arr)
		}
	})
}

func permute(s []int, emit func([]int)) {
    if len(s) == 0 {
        emit(s)
        return
    }

    var rc func(int)
    rc = func(np int) {
        if np == 1 {
            emit(s)
            return
        }
        np1 := np - 1
        pp := len(s) - np1
        rc(np1)
        for i := pp; i > 0; i-- {
            s[i], s[i-1] = s[i-1], s[i]
            rc(np1)
        }
        w := s[0]
        copy(s, s[1:pp+1])
        s[pp] = w
    }
    rc(len(s))
}

func main() {
	start := time.Now()
	permutations(15)
	fmt.Println(time.Since(start))
}


// After investigation: the number of permutations that we want:
// For n = 2k,		-> 2
// for n = 2k + 1	-> http://oeis.org/A078836

//2 2
//3 6
//4 2
//5 14
//6 2
//7 32
//8 2
//9 72
//10 2
//11 160
//12 2
//13 352
//14 2      took 1h50m39.803213687s
