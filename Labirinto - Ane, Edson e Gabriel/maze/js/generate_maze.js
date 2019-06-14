import Prims from './prims';
import Edge from './edge';
import Dijkstra from './dijkstra';


class GenerateMaze {
  constructor(canvasEl, width, height, enableAllBtns) {
    this.width = width * 20 + 10;
    this.height = height * 20 + 10;
    this.ctx = canvasEl.getContext("2d");
    this.setup(width, height);
    this.enableAllBtns = enableAllBtns;
  }

  setup(width, height) {
    this.grid = new Grid(width, height);
    this.startPos = this.grid.startPos;
    this.goalPos = this.grid.goalPos;
  }

  render(edges) {
    this.ctx.clearRect(10, 10, this.width, this.height);
    this.ctx.fillStyle = "rgb(35, 35, 35)";
    this.ctx.fillRect(10, 10, this.width, this.height);
    edges.forEach(edge => {
      edge.render(this.ctx, "grey");
    });
  }

  renderEndpoints() {
    this.ctx.fillStyle = "#3b721a";
    let startX = this.startPos[1] * 20 + 25;
    let startY = this.startPos[0] * 20 + 25;
    this.ctx.beginPath();
    this.ctx.arc(startX, startY, 10, 0, Math.PI*2, true);
    this.ctx.closePath();
    this.ctx.fill();

    this.ctx.fillStyle = "#871919";
    let goalX = this.goalPos[1] * 20 + 25;
    let goalY = this.goalPos[0] * 20 + 25;
    this.ctx.beginPath();
    this.ctx.arc(goalX, goalY, 10, 0, Math.PI*2, true);
    this.ctx.closePath();
    this.ctx.fill();
  }

  quickRegen() {
    this.render(this.allEdges);
    this.renderEndpoints(this.ctx);
  }

  generate() {
    this.setup(this.grid.width, this.grid.height);
    this.allEdges = new Prims(this.grid).generate();
    this.edges = [];
    let i = 0;

    const animateCallback = () => {
      if (i < this.allEdges.length) {
        this.edges.push(this.allEdges[i]);
        i++;
        this.render(this.edges);

        setTimeout(animateCallback, 1);
      } else {
        this.renderEndpoints(this.ctx);
        this.enableAllBtns();
      }
    };

    animateCallback();
  }

  nodesToEdges(path) {
    const pathEdges = [];
    for (let i = 1; i < path.length; i++) {
      pathEdges.push(new Edge(path[i-1], path[i], true));
    }

    return pathEdges;
  }

  quickDisplay(searchType) {
    let path; let visited;
    switch (searchType) {
      case "Dijkstra":
        path = this.nodesToEdges(this.pathDijkstra);
        visited = this.visitedDijkstra;
        break;
    }

    visited.forEach(edge => {
      edge.render(this.ctx, "#cc700e");
    });

    path.forEach(edge => {
      edge.render(this.ctx, "#1855a0");
    });

    this.renderEndpoints(this.ctx);
  }

  displayVisited(searchType) {
    let results;
    switch (searchType) {
      case "Dijkstra":
        this.search = new Dijkstra(this.grid, "M");
        results = this.search.solve();
        this.pathDijkstra = results[0];
        this.visitedDijkstra = results[1].slice();
        break;
    }
    this.path = results[0];
    this.visited = results[1];

    const visitedEdges = this.visited.slice();
    const renderedEdges = [];

    const animateCallback = () => {
      if (visitedEdges.length > 0) {
        renderedEdges.push(visitedEdges.shift());

        renderedEdges.forEach((edge, idx) => {
          edge.render(this.ctx, "#cc700e");
        });
        this.renderEndpoints(this.ctx);

        setTimeout(animateCallback, 1);
      } else {
        this.solve();
      }
    };

    animateCallback();
  }

  solve() {
    const pathEdges = this.nodesToEdges(this.path);
    const renderedEdges = [];

    const animateCallback = () => {
      if (pathEdges.length > 0) {
        renderedEdges.push(pathEdges.shift());

        renderedEdges.forEach(edge => {
          edge.render(this.ctx, "#1855a0");
        });
        this.renderEndpoints(this.ctx);

        setTimeout(animateCallback, 1);
      } else {
        this.enableAllBtns();
      }
    };

    animateCallback();
  }
}

export default GenerateMaze;
