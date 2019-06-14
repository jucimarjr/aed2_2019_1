import BinaryMinHeap from './binary_heap';
import Edge from './edge';
import Node from './node';

class Prims {
  constructor(grid) {
    this.pq = new BinaryMinHeap();
    this.grid = grid;
    this.boolean = {
      length: 0,
      array: new Array(this.grid.width * this.grid.height).fill(false)
    };
    this.edges = [];
  }

  generate() {
    let start = new Node([0, 0], 0);
    start.grid = this.grid;
    this.boolean[start.value] = true;
    this.boolean.length++;
    start.neighbors().forEach(neighbor => {
      this.pq.put(new Edge(start, neighbor));
    });

    while (!this.treeFull()) {
      let cheapestEdge = this.pq.take();
      if (!this.boolean[cheapestEdge.vertex2.value]) {
        let vertex1 = cheapestEdge.vertex1;
        let vertex2 = cheapestEdge.vertex2;

        vertex2.grid = this.grid;
        this.boolean[vertex2.value] = true;
        this.boolean.length++;

        // Whenever edge gets created, make 2 vertices neighbors
        if (!vertex1.edgeNeighbors.includes(vertex2)) {
          vertex1.edgeNeighbors.push(vertex2);
        }
        if (!vertex2.edgeNeighbors.includes(vertex1)) {
          vertex2.edgeNeighbors.push(vertex1);
        }

        this.edges.push(cheapestEdge);
        vertex2.neighbors().forEach(neighbor => {
          this.pq.put(new Edge(vertex2, neighbor));
        });
      }
    }

    return this.edges;
  }

  treeFull() {
    return (this.boolean.length === this.boolean.array.length);
  }
}

export default Prims;
