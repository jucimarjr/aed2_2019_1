class Edge {
  constructor(vertex1, vertex2, search) {
    this.vertex1 = vertex1;
    this.vertex2 = vertex2;
    this.weight = Math.random();
    this.search = search;
  }

  render(ctx, color) {
    const mult = 20;
    const lineWidth = this.search ? 6 : 10;
    let x1 = this.vertex1.pos[1] * mult + 25;
    let x2 = this.vertex2.pos[1] * mult + 25;
    let y1 = this.vertex1.pos[0] * mult + 25;
    let y2 = this.vertex2.pos[0] * mult + 25;

    if (x1 === x2 && y1 < y2) {
      y1 -= lineWidth / 2;
      y2 += lineWidth / 2;
    } else if (x1 === x2 && y1 > y2) {
      y2 -= lineWidth / 2;
      y1 += lineWidth / 2;
    } else if (y1 === y2 && x1 < x2) {
      x1 -= lineWidth / 2;
      x2 += lineWidth / 2;
    } else {
      x2 -= lineWidth / 2;
      x1 += lineWidth / 2;
    }

    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.strokeStyle = color;
    ctx.lineWidth = lineWidth;
    ctx.stroke();
  }
}

export default Edge;
