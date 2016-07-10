/*
all functions with bool return values calculate whether the first player wins
some helpful links
 - http://www.suhendry.net/blog/?p=1612
 - http://www.stat.berkeley.edu/~peres/gtlect.pdf
 - https://subtractiongames.files.wordpress.com/2012/02/subgames2.pdf
 - http://www.gabrielnivasch.org/fun/combinatorial-games/sprague-grundy
 - https://www.math.ucla.edu/~tom/Game_Theory/comb.pdf
 - https://www.math.ucsd.edu/~rjtobin/152/152_sol1.pdf
 - https://en.wikipedia.org/wiki/Octal_game
 - http://www.link.cs.cmu.edu/15859-s11/notes/Hackenbush.pdf
*/
package main

import (
	"fmt"
)

func nim(arr []int) bool {
	/* You have an array of stones. Each move players selects any number of elements (>= 1)
	from only one pile. A player who can't make a move loses
	*/
	res := 0
	for _, v := range arr {
		res ^= v
	}
	return res != 0
}

func nim_misere(arr []int) bool {
	// The same as nim, only the player who has done the last move loses
	res, max := 0, 0
	for _, v := range arr {
		if v > 0 {
			res ^= v
			if v > max {
				max = v
			}
		}
	}

	if max == 1 {
		return len(arr)%2 == 0
	}

	return !(res == 0 && max > 1)
}

func nim_poker(arr []int, k int) bool {
	/* the same as original nim, but each player can put some amount of stones in the pile.
	each player in the beginning has K stones at his possession. It is the same as nim and K is
	irrelevant, because whenever a player put K stones at some pile, another one can remove them
	*/
	return nim(arr)
}

func nimble(arr []int) bool {
	/* You have a line of squares labeled 0, 1, 2, ... In square i, there are arr[i] coins.
	Two players take turns. One move consists of taking any one coin and moving it to any square to
	the left of it. The person who can't move a coin loses

	This game is equivalent to Nim, where coin k-th square is equivalent to a pile of k elements.
	It is clear that if there is odd number of coins, it can be substituted with 1 coin, and
	even number of coins on a square can be ignored
	*/
	res := 0
	for k, v := range arr {
		if v%2 == 1 {
			res ^= k
		}
	}

	return res != 0
}

func subtraction(n int, arr []int){
	/** You have a pile of N stones. In one turn you can remove any number A of stones, where A is
	 a number from an Arr. Arr is basically a set, so make sure elements are unique.
	 A person who takes the last element wins.
	 */
}

func pn_table_subtraction(arr []int, n int){
	// make sure Arr is unique and sorted
	xor := 0
	for _, v := range arr {
		xor ^= v
	}
	fmt.Println(xor)


	table, smallest_p := make([]int, n), 0
	for smallest_p < n {
		for _, v := range arr {
			if smallest_p + v < n {
				table[smallest_p + v] = 1
			}
		}

		smallest_p++
		for smallest_p < n && table[smallest_p] == 1 {
			smallest_p++
		}
	}

	fmt.Println(table)
	for _, v := range table {
		if v == 1 {
			fmt.Print("N ")
		} else {
			fmt.Print("P ")
		}
	}
	fmt.Println()
}

func mex_arr(arr []int) int {
	// minimum excluded value. If you have a set of integers, Mex returns you the smallest integer
	// that does not exist in this set. mex({4, 5, 2, 0, 1, 8, 6}) = 3.
	// In this case it searches through the an array, not a set
	hash := map[int]bool{}
	for _, v := range arr {
		hash[v] = true
	}

	for i := 0; true; i++{
		if hash[i]{
			return i
		}
	}
	return -1
}

func mex_set(set map[int]bool) int {
	// minimum excluded value. If you have a set of integers, Mex returns you the smallest integer
	// that does not exist in this set. mex({4, 5, 2, 0, 1, 8, 6}) = 3; mex({}) = 0
	if len(set) == 0 {
		return 0
	}

	for i := 0; true; i++{
		if _, ok := set[i]; !ok {
			return i
		}
	}
	return -1
}

func nim_half(arr []int) bool {
	// Nim game, but at each move you should remove at least half of the stones in this pile.
	// calculate Sprague-Grundy values for each pile and xor all of them
	res := 0
	for _, v := range arr {
		i := 0
		for i = 0; v != 0; i++ {
			v /= 2
		}
		res ^= i
	}

	return res != 0
}

func grundy_inf(arr []int) bool {
	// You have piles of stones, people alternate turns, person who can't make a move loses.
	// During the move, a player can select any one of the piles divide the stones in it into
	// any number of unequal piles such that no two of the newly created piles have
	// the same number of stones.
	// http://math.stackexchange.com/q/1796335/50804
	first_grundy, res := []int{0, 0, 0, 1, 0, 2, 3, 4, 0}, 0
	for _, v := range arr {
		if v < len(first_grundy){
			res ^= first_grundy[v]
		} else {
			res ^= v - 4
		}
	}
	return res != 0
}

func silver_dollar_game(arr []int) bool {
	// This game is played on a line of squares labeled 0, 1, 2, ... with several coins are
	// placed in some square such that no two coins are placed in a same square. One move
	// consists of moving one coin to its left onto any empty square and not passing any other coin.
	// The game ends when a player cannot make any legal moves, since all the coins
	// are jammed at the left-end of the strip.
	// http://www.suhendry.net/blog/?p=1612
	//
	// Also it is similar game to nim, where all the piles are non-decreasing and during each move
	// the non-decreasing property should remain
	res := 0
	for i := len(arr) - 1; i > 0; i-- {
		res ^= arr[i] - arr[i - 1] - 1
	}

	return res ^ (arr[0] - 1) != 0
}

func divide_tower(arr []int, k int) bool {
	// you have many piles of stones. During each move, one can take a pile and divide it into
	// any number of non empty piles from 2 to K. First person who can't divide a pile (because
	// all the piles have 1 stone loses.
	// https://www.hackerrank.com/contests/w20/challenges/simple-game
	//
	// after the analysis, I found that SG values are the following. If
	// k = 2, SG = 1 if k is even, 0 if odd
	// k = 3, a big sequence, for which I was not able to find a period
	// k >=4, n - 1
	res := 0
	if k == 2 {
		for _, v := range arr {
			res ^= (v + 1) % 2
		}
	} else if k == 3 {
		sg_values := []int{0, 0, 1, 2, 3, 1, 4, 3, 2, 4, 5, 6, 7, 8, 9, 7, 6, 9, 8, 11, 10, 12, 13, 10, 11, 13, 12, 15, 14, 16, 17, 5, 15, 17, 16, 19, 18, 20, 21, 18, 19, 21, 20, 23, 22, 25, 24, 22, 23, 24, 25, 26, 27, 29, 28, 27, 26, 28, 29, 30, 31, 14, 32, 31, 30, 32, 33, 34, 35, 37, 36, 35, 34, 36, 37, 38, 39, 40, 41, 39, 38, 41, 40, 43, 42, 44, 45, 42, 43, 45, 44, 47, 46, 48, 49, 46, 47, 49, 48, 51, 50, 52, 53, 50, 51, 53, 52, 55, 54, 57, 56, 54, 55, 56, 57, 58, 59, 61, 60, 59, 58, 60, 61, 62, 63, 64, 65, 63, 62, 65, 64, 67, 66, 68, 69, 66, 67, 69, 68, 71, 70, 73, 72, 70, 71, 72, 73, 74, 75, 77, 76, 75, 74, 76, 77, 78, 79, 81, 80, 79, 78, 80, 81, 82, 83, 85, 84, 83, 82, 84, 85, 86, 87, 88, 89, 87, 86, 89, 88, 91, 90, 92, 93, 90, 91, 93, 92, 95, 94, 96, 97, 94, 95, 97, 96, 99, 98, 100, 101, 33, 99, 101, 100, 103, 102, 105, 104, 102, 103, 104, 105, 106, 107, 109, 108, 107, 106, 108, 109, 110, 111, 113, 112, 111, 110, 112, 113, 114, 115, 117, 116, 115, 114, 116, 117, 118, 119, 120, 121, 119, 118, 121, 120, 123, 122, 124, 125, 122, 123, 125, 124, 127, 126, 128, 129, 126, 127, 129, 128, 131, 130, 132, 133, 130, 131, 133, 132, 135, 134, 137, 136, 134, 135, 136, 137, 138, 139, 141, 140, 139, 138, 140, 141, 142, 143, 145, 144, 143, 142, 144, 145, 146, 147, 149, 148, 147, 146, 148, 149, 150, 151, 152, 153, 151, 150, 153, 152, 155, 154, 156, 157, 154, 155, 157, 156, 159, 158, 160, 161, 158, 159, 161, 160, 163, 162, 164, 165, 162, 163, 165, 164, 167, 166, 169, 168, 166, 167, 168, 169, 170, 171, 98, 172, 171, 170, 172, 173, 174, 175, 177, 176, 175, 174, 176, 177, 178, 179, 181, 180, 179, 178, 180, 181, 182, 183, 184, 185, 183, 182, 185, 184, 187, 186, 188, 189, 186, 187, 189, 188, 191, 190, 193, 192, 190, 191, 192, 193, 194, 195, 197, 196, 195, 194, 196, 197, 198, 199, 200, 201, 199, 198, 201, 200, 203, 202, 204, 205, 202, 203, 205, 204, 207, 206, 208, 209, 206, 207, 209, 208, 211, 210, 212, 213, 210, 211, 213, 212, 215, 214, 217, 216, 214, 215, 216, 217, 218, 219, 221, 220, 219, 218, 220, 221, 222, 223, 225, 224, 223, 222, 224, 225, 226, 227, 229, 228, 227, 226, 228, 229, 230, 231, 232, 233, 231, 230, 233, 232, 235, 234, 236, 237, 234, 235, 237, 236, 239, 238, 240, 241, 238, 239, 241, 240, 243, 242, 244, 245, 242, 243, 245, 244, 247, 246, 249, 248, 246, 247, 248, 249, 250, 251, 253, 252, 251, 250, 252, 253, 254, 255, 256, 257, 173, 254, 257, 256, 259, 258, 260, 261, 258, 259, 261, 260, 263, 262, 265, 264, 262, 263, 264, 265, 266, 267, 269, 268, 267, 266, 268, 269, 270, 271, 273, 272, 271, 270, 272, 273, 274, 275, 277, 276, 275, 274, 276, 277, 278, 279, 280, 281, 279, 278, 281, 280, 283, 282, 284, 285, 282, 283, 285, 284, 287, 286, 288, 289, 286, 287, 289, 288, 291, 290, 292, 293, 290, 291, 293, 292, 295, 294, 297, 296, 294, 295, 296, 297, 298, 299, 301, 300, 299, 298, 300, 301, 302, 303, 305, 304, 303, 302, 304}
		for _, v := range arr {
			res ^= sg_values[v]
		}
	} else {
		for _, v := range arr {
			res ^= v - 1
		}
	}

	return res != 0
}

func divide_numbers(arr []int) bool {
	// you have an array of integers. On each turn you can divide the number by any of it's divisors
	// the person who can't make a move loses
	// It is equivalent to Nim after calculating the number of prime factors of the number
	// implementation here:
	// https://www.hackerrank.com/contests/5-days-of-game-theory/challenges/tower-breakers-2/submissions/code/5964006
	return true
}

func divide_numbers_2(arr []int) bool {
	// you have array of integers. On each turn you can divide an integer into any number of its divisors
	// thus increasing the size of an array. The person who can't make a move loses.
	// https://www.hackerrank.com/contests/5-days-of-game-theory/challenges/tower-breakers-3/submissions/code/5965816
	return true
}

func half_knight_on_board(n int, coordinates [][2]int) bool {
	// A chess board of size N has a lot of knights at the location of Coordinates.
	// each knight can move to (x - 2, y + 1), (x - 2, y - 1), (x + 1, y - 2), (x - 1, y - 2)
	// Knights can't go outside the board. A person who can't move loses
	// https://www.hackerrank.com/contests/5-days-of-game-theory/challenges/a-chessboard-game/submissions/code/5966140
	return true
}

// unimplemented

func chomp(){
	// page 7 https://www.math.ucla.edu/~tom/Game_Theory/comb.pdf
	// a move is taking a square and removing everything on the right and above
	// the player who takes the lowest right square loses
}

func fibNim(){
	// page 7 https://www.math.ucla.edu/~tom/Game_Theory/comb.pdf
	// the same as nim, but you can take at most twice the number of stones, you opponent previously took
}

func turningTurtles(){
	// page 12 https://www.math.ucla.edu/~tom/Game_Theory/comb.pdf
	// horizontal line is filled with coins, some of them showing Head/Tails. With one move you can
	// turn a coin from head to tail. In addition to this if needed, you can turn over one coin on
	// the left of it.
}

func staircaseNim(){
	// page 13 https://www.math.ucla.edu/~tom/Game_Theory/comb.pdf
	// you have stairs. On each stair there are some stones. You can move any number of stones
	// from stair J to J - 1. Last to move wins
}

func mooreNim(){
	// page 13 https://www.math.ucla.edu/~tom/Game_Theory/comb.pdf
	// generalization of nim, where on each step you can remove any number of stones from any K piles
}

func wythoff(){
	// page 19 https://www.math.ucla.edu/~tom/Game_Theory/comb.pdf
	// you have a queen on the chessboard that can move down/left/diagonally as a normal queen

}

func some2(){
	// https://www.math.ucla.edu/~tom/Game_Theory/comb.pdf
}

func some3(){
	// https://www.math.ucla.edu/~tom/Game_Theory/comb.pdf
}

func some4(){
	// https://www.math.ucla.edu/~tom/Game_Theory/comb.pdf
}
