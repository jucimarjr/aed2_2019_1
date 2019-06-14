class BinaryMinHeap {
  constructor() {
    this.pq = [null];
  }

  length() {
    return this.pq.length;
  }

  put(edge) {
    this.pq.push(edge);
    if (this.pq.length > 2) {
      this.bubble();
    }
  }

  take() {
    if (this.pq.length === 2) {
      return this.pq.pop();
    }
    else if (this.pq.length > 2) {
      let min = this.pq[1];
      this.pq[1] = this.pq.pop();
      this.sink();
      return min;
    }
  }

  bubble() {
    let newIdx = this.pq.length - 1;
    let parentIdx = Math.floor(newIdx/2);
    while (this.pq[newIdx].weight < this.pq[parentIdx].weight) {
      [this.pq[newIdx], this.pq[parentIdx]] =
        [this.pq[parentIdx], this.pq[newIdx]];
      newIdx = parentIdx;
      if (newIdx === 1) { break; }
      parentIdx = Math.floor(newIdx/2);
    }
  }

  sink() {
    let idx = 1;
    let c1 = 2;
    let c2 = 3;

    while (this.pq[c1]) {
      if (this.pq[c2]) {
        if (this.pq[c2].weight < this.pq[c1].weight &&
            this.pq[c2].weight < this.pq[idx].weight) {
          [this.pq[c2], this.pq[idx]] = [this.pq[idx], this.pq[c2]];
          idx = c2;
        } else if (this.pq[c1].weight < this.pq[idx].weight) {
          [this.pq[c1], this.pq[idx]] = [this.pq[idx], this.pq[c1]];
          idx = c1;
        } else {
          break;
        }
      } else if (this.pq[c1].weight < this.pq[idx].weight) {
        [this.pq[c1], this.pq[idx]] = [this.pq[idx], this.pq[c1]];
        idx = c1;
      } else {
        break;
      }

      c1 = idx * 2;
      c2 = idx * 2 + 1;
    }
  }
}

export default BinaryMinHeap;
