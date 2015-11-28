/**
  Binary Indexed Tree (Fenwick tree) is a data structure that supports two operations:
  - update(index, value):	arr[i] += value										O(log(n))
  - prefix(index):			arr[1] + ... + arr[index]							O(log(n))
  - summation(s, e):		arr[i] + arr[i + 1] + ... + arr[j]					O(log(n))
  - initialize(arr)			create a Fenwick tree. Array should start with 0.	O(n)
  - scale(c)				multiply all values in an array by C				O(n)
  - readSingle(idx)			find the value from the single index				O(log(n))
  - findIndexOfFrequency(f)	find the index of the element with some frequency	o(log(n))

  The best way to understand the tree is to realize that there can be a compromise between two
  potential ways to solve the problem:
  - updates in O(1) and prefix in O(n)
  - updates in O(n) and prefix in O(1) if we convert an array to a prefix array

  But what if we will not convert all array into a prefix array and have some nodes there
  that are responsible for some regions. If there will be overlapping regions, we would be able
  to calculate a sum by somehow combining these regions.

  And here is an example of overlapping regions:
  http://community.topcoder.com/i/education/binaryIndexedTrees/BITimg.gif
  As you see each point is responsible for regions. The region stop at this point and starts with
  point - number of 2^k where k is the maximum possible that point is divisible by 2^k

  For example the point 12 is responsible for region [8-12], because the maximum 2^k which divides 12
  is 4. So starting point is 12 - 4 = 8.

  So how can we find the sum of the prefix? We need to add the all intervals that will cover this
  region. For example for 11 it will be 11, 10 and 8. Note that the size of these elements will be
  less than log(n).

  important thing is that we can find the largest power of 2 that divides x as:
  x & -x

  https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/
 */

package main
import (
	"fmt"
)

func update(arr []int, index, value int){
	for ; index < len(arr); index += index & -index{
		arr[index] += value
	}
}

func prefix(arr []int, index int)int{
	s := 0
	for ; index > 0; index -= index & -index {
		s += arr[index]
	}
	return s
}

func summation(arr []int, s, e int)int{
	return prefix(arr, e) - prefix(arr, s - 1)
}

func scale(arr []int, c int){
    for i := 1; i < len(arr); i++ {
		arr[i] *= c
	}
}

func readSingle(arr []int, idx int)int{
	// if you need super fast readSingle, you can just maintain additional array with
	// all frequencies and modify it on every update. Then use it to readSingle in O(1)
	// also you can do it by calling summation and it will be 2 * O(log(n))

	// the following readSingle has complexity c * log(n) where c < 1
	sum := arr[idx]
	if idx > 0{
    	z := idx - (idx & -idx)
    	idx--
    	for idx != z {
        	sum -= arr[idx];
        	idx -= idx & -idx
    	}
	}
	return sum
}

func findIndexOfFrequency(arr []int, f int)int{
	// find the index for a given frequency. The naive way is to get all the values
	// and find if any of them is equal to the one we are looking for. Naive way is
	// the best one if we have some negative values in our original array (cumulative sum
	// is not always increasing). But if all the values are non-negative, we can do better with
	// binary search.
	// returns the greatest index
	idx := 0
	bitMask := 0
	for n := len(arr); n > 0; n /= 2 {
    	bitMask++;
	}

    for bitMask != 0 && idx < len(arr){
        tIdx := idx + bitMask;
        if f >= arr[tIdx]{
            idx = tIdx;
            f -= arr[tIdx];
        }
        bitMask /= 2;
    }
    if f != 0{
		return -1
	}

    return idx
}

func initialize(arr []int)[]int{
	// the array has to have additional starting 0 at the beginning
	// http://stackoverflow.com/q/31068521/1090562
	n := len(arr)
	for i := 1; i < n; i++{
		j := i + (i & -i)
		if j < n {
			arr[j] += arr[i]
		}
	}
	return arr
}



func main(){
	queries := [][]int{[]int{1, 3}, []int{2, -2}, []int{3, 4}, []int{4, 9}, []int{5, 12}, []int{6, -7}, []int{7, 3}, []int{8, 8}, []int{9, 12}, []int{10, 6}, []int{11, -8}}
	arr := make([]int, 12)
	for _, v := range(queries){
		update(arr, v[0], v[1])
	}

	fmt.Println(readSingle(arr, 9))
	fmt.Println(summation(arr, 9, 9))
}
