class Node {
  constructor(pos, value) {
    this.pos = pos;
    this.value = value;
    this.edgeNeighbors = [];
  }

  calcHeuristic(fromNode, heuristic, dijkstra) {
    // This is the heuristic for A* and Dijkstra's
    // Setting this.weight to result to be compatible with binary heap
    this.costSoFar = fromNode.costSoFar + fromNode.costToPos(
      this.pos, heuristic
    );
    if (dijkstra) {
      this.weight = this.costSoFar;
    } else {
      this.goalPos = fromNode.goalPos;
      this.weight = this.costSoFar + this.costToPos(
        fromNode.goalPos, heuristic
      );
    }
    return this.weight;
  }

  costToPos(pos, heuristic) {
    let [y1, x1] = this.pos;
    let [y2, x2] = pos;

    if (heuristic === "SL") {
      // straight line distance
      let aSquared = Math.pow(x2 - x1, 2);
      let bSquared = Math.pow(y2 - y1, 2);
      return Math.pow(aSquared + bSquared, 0.5);
    } else if (heuristic === "M") {
      // manhattan distance
      return Math.abs(x2 - x1) + Math.abs(y2 - y1);
    }
  }

  neighbors() {
    let north; let east; let west; let south;
    let [y, x] = this.pos;
    if (this.grid.array[y - 1]) {
      north = this.grid.array[y - 1][x];
    }
    if (this.grid.array[y + 1]) {
      south = this.grid.array[y + 1][x];
    }
    east = this.grid.array[y][x + 1];
    west = this.grid.array[y][x - 1];

    let possibleNeighbors = [north, east, south, west];
    return possibleNeighbors.filter(neighbor => {
      if (neighbor) { return neighbor; }
    });
  }
}

export default Node;
