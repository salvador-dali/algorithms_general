/**
 https://www.hackerrank.com/challenges/dfsprobreach
 stupid hackerrank has a wrong solution
 basically reverse a graph. And after this use DFS from starting point.
 Then we will have all reachable vertices.

 Then for each non zero probability we check whether this vertex was reachable.
 */

package main
import (
    "fmt"
    "os"
    "bufio"
    "strings"
    "strconv"
)

func dfs(G map[int]map[int]bool, N int)map[int]bool{
    frontier := []int{N}
    seen := map[int]bool{N: true}
    
    for len(frontier) > 0 {
        el := frontier[len(frontier) - 1]
        frontier = frontier[:len(frontier) - 1]
        for node := range(G[el]){
            if !seen[node]{
                seen[node] = true
                frontier = append(frontier, node)
            }
        }
    }
    
    delete(seen, N)
    return seen
}

func answer(seen map[int]bool, probabilities []float64)int{
    for k, v := range(probabilities){
        if v > 0 {
            if !seen[k + 1] {
                return 0
            }
        }
    }
    return 1
}

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    T, _ := strconv.Atoi(scanner.Text())
    for T > 0 {
        T--
        scanner.Scan()
        N, _ := strconv.Atoi(scanner.Text())
        G := map[int]map[int]bool{}
        for n := 1; n <= N + 1; n++ {
            G[n] = map[int]bool{}
        }
        
        for n := 1; n <= N + 1; n++ {
            scanner.Scan()
            arr := strings.Fields(scanner.Text())
            for i := 1; i < len(arr); i++ {
                v, _ := strconv.Atoi(arr[i])
                G[v][n] = true
            }
        }
        scanner.Scan()
        probabilities := []float64{}
        for _, v := range(strings.Fields(scanner.Text())) {
            num, _ := strconv.ParseFloat(v, 64)
            probabilities = append(probabilities, num)
        }
        
        r := answer(dfs(G, N + 1), probabilities)
        fmt.Println(r)
    }
}
