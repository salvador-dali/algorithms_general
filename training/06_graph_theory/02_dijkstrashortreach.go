package main
import (
	"bufio"
	"os"
	"strconv"
	"strings"
	"fmt"
	"container/heap"
)

// An Item is something we manage in a priority queue.
type Item struct {
	value    int
	priority int
	index int
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest, not lowest, priority so we use greater than here.
	return pq[i].priority < pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	item.index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

// update modifies the priority and value of an Item in the queue.
func (pq *PriorityQueue) update(item *Item, value int, priority int) {
	item.value = value
	item.priority = priority
	heap.Fix(pq, item.index)
}

func dijkstra(G map[int]map[int]int, N int, start int)[]int{
	MAX := 999999

	checked, distance := make([]bool, N + 1), make([]int, N + 1)
	for i := 0; i <= N; i++ { distance[i] = MAX }
	distance[start], checked[start] = 0, true

	frontier := make(PriorityQueue, 1)
	frontier[0] = &Item{value: start, priority: 0, index: 0}
	heap.Init(&frontier)

	for v, w := range(G[start]){
		heap.Push(&frontier, &Item{
			value: v,
			priority: w,
		})
	}

    
	for frontier.Len() > 0 {
		element := heap.Pop(&frontier).(*Item)
		vertex, cost := element.value, element.priority

		checked[vertex] = true
		if distance[vertex] > cost {
			distance[vertex] = cost
		}

		for vertexNew, costNew := range(G[vertex]){
			if !checked[vertexNew]{
				heap.Push(&frontier, &Item{
					value: vertexNew,
					priority: cost + costNew,
				})
			}
		}
	}

    res := []int{}
    for i := 1; i < len(distance); i++{
        if i != start{
            if distance[i] == MAX {
                res = append(res, -1)
            } else {
                res = append(res, distance[i])
            }
        }
    }
    return res
}

func main(){
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	T, _ := strconv.Atoi(scanner.Text())
	for T > 0 {
		T--
		scanner.Scan()
        arr := strings.Fields(scanner.Text()) // read N and M
        N, _ := strconv.Atoi(arr[0])
        M, _ := strconv.Atoi(arr[1])
		G := map[int]map[int]int{}
        maximum := 1
        for M > 0 {
			M--
			scanner.Scan()
			arr := strings.Fields(scanner.Text())
			num1, _ := strconv.Atoi(arr[0])
			num2, _ := strconv.Atoi(arr[1])
			weight, _ := strconv.Atoi(arr[2])
			if len(G[num1]) == 0 { G[num1] = map[int]int{} }
			if len(G[num2]) == 0 { G[num2] = map[int]int{} }
            
            val, ok := G[num2][num1]
            if ok {
                if weight < val{
                    G[num2][num1] = weight
                }
            } else {
                G[num2][num1] = weight
            }
            
            val, ok = G[num1][num2]
            if ok {
                if weight < val{
                    G[num1][num2] = weight
                }
            } else {
                G[num1][num2] = weight
            }
            maximum += weight
		}
		scanner.Scan() // read the starting node
		start, _ := strconv.Atoi(scanner.Text())
        r := dijkstra(G, N, start)
        fmt.Println(strings.Trim(fmt.Sprint(r), "[]"))
	}
}
