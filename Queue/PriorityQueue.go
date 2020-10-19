/*
Implementation of Priority Queue
*/

package main

import "fmt"

type QElement struct {
	data int
	priority int
}

type PriorityQueue struct {
	items []QElement
}

func (p *PriorityQueue) IsEmpty() bool {
	return len(p.items) == 0
}

func (p *PriorityQueue) EnQueue(d, p int) {
	element := QElement{data: d, priority: p,}
	l := len(p.items)
	contain := false
	for i := 0; i < l; i++ {
		if p.items[i].priority > element.priority {

			contain = true
		}
	}
	if !contain {
		p.items = append(q.items, element)
	}
}

func (p *PriorityQueue) DeQueue() {
	if p.IsEmpty() {
		fmt.Println("Underflow")
		return
	}


}

func (p *PriorityQueue) Front() {
	if p.IsEmpty() {
		fmt.Println("Underflow")
		return 
	}
	fmt.Println(p.items[0])
}

func (p *PriorityQueue) Rear() {
	if p.IsEmpty() {
		fmt.Println("Overflow")
		return
	}
	fmt.Println(p.items[len(items) - 1])
}

func main() {

}