package main

import (
	"testing"
)

func create_arr_1(n int) []int {
	arr := []int{}
	for i := 0; i < n; i++ {
		arr = append(arr, i)
	}
	return arr
}

func create_arr_2(n int) []int {
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		arr[i] = i
	}
	return arr
}

func BenchmarkArr1_tiny(b *testing.B) {
	n := 10
	for i := 0; i < b.N; i++ {
		create_arr_1(n)
	}
}

func BenchmarkArr2_tiny(b *testing.B) {
	n := 10
	for i := 0; i < b.N; i++ {
		create_arr_2(n)
	}
}

func BenchmarkArr1_small(b *testing.B) {
	n := 100
	for i := 0; i < b.N; i++ {
		create_arr_1(n)
	}
}

func BenchmarkArr2_small(b *testing.B) {
	n := 100
	for i := 0; i < b.N; i++ {
		create_arr_2(n)
	}
}

func BenchmarkArr1_medium(b *testing.B) {
	n := 10000
	for i := 0; i < b.N; i++ {
		create_arr_1(n)
	}
}

func BenchmarkArr2_medium(b *testing.B) {
	n := 10000
	for i := 0; i < b.N; i++ {
		create_arr_2(n)
	}
}

func BenchmarkArr1_huge(b *testing.B) {
	n := 100000
	for i := 0; i < b.N; i++ {
		create_arr_1(n)
	}
}

func BenchmarkArr2_huge(b *testing.B) {
	n := 100000
	for i := 0; i < b.N; i++ {
		create_arr_2(n)
	}
}

func BenchmarkArr1_enormous(b *testing.B) {
	n := 1000000
	for i := 0; i < b.N; i++ {
		create_arr_1(n)
	}
}

func BenchmarkArr2_enormous(b *testing.B) {
	n := 1000000
	for i := 0; i < b.N; i++ {
		create_arr_2(n)
	}
}
