/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 3);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var Edge = function () {
  function Edge(vertex1, vertex2, search) {
    _classCallCheck(this, Edge);

    this.vertex1 = vertex1;
    this.vertex2 = vertex2;
    this.weight = Math.random();
    this.search = search;
  }

  _createClass(Edge, [{
    key: "render",
    value: function render(ctx, color) {
      var mult = 20;
      var lineWidth = this.search ? 6 : 10;
      var x1 = this.vertex1.pos[1] * mult + 25;
      var x2 = this.vertex2.pos[1] * mult + 25;
      var y1 = this.vertex1.pos[0] * mult + 25;
      var y2 = this.vertex2.pos[0] * mult + 25;

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
  }]);

  return Edge;
}();

exports.default = Edge;

/***/ }),
/* 1 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _slicedToArray = function () { function sliceIterator(arr, i) { var _arr = []; var _n = true; var _d = false; var _e = undefined; try { for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"]) _i["return"](); } finally { if (_d) throw _e; } } return _arr; } return function (arr, i) { if (Array.isArray(arr)) { return arr; } else if (Symbol.iterator in Object(arr)) { return sliceIterator(arr, i); } else { throw new TypeError("Invalid attempt to destructure non-iterable instance"); } }; }();

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var Node = function () {
  function Node(pos, value) {
    _classCallCheck(this, Node);

    this.pos = pos;
    this.value = value;
    this.edgeNeighbors = [];
  }

  _createClass(Node, [{
    key: "calcHeuristic",
    value: function calcHeuristic(fromNode, heuristic, dijkstra) {
      // This is the heuristic for A* and Dijkstra's
      // Setting this.weight to result to be compatible with binary heap
      this.costSoFar = fromNode.costSoFar + fromNode.costToPos(this.pos, heuristic);
      if (dijkstra) {
        this.weight = this.costSoFar;
      } else {
        this.goalPos = fromNode.goalPos;
        this.weight = this.costSoFar + this.costToPos(fromNode.goalPos, heuristic);
      }
      return this.weight;
    }
  }, {
    key: "costToPos",
    value: function costToPos(pos, heuristic) {
      var _pos = _slicedToArray(this.pos, 2),
          y1 = _pos[0],
          x1 = _pos[1];

      var _pos2 = _slicedToArray(pos, 2),
          y2 = _pos2[0],
          x2 = _pos2[1];

      if (heuristic === "SL") {
        // straight line distance
        var aSquared = Math.pow(x2 - x1, 2);
        var bSquared = Math.pow(y2 - y1, 2);
        return Math.pow(aSquared + bSquared, 0.5);
      } else if (heuristic === "M") {
        // manhattan distance
        return Math.abs(x2 - x1) + Math.abs(y2 - y1);
      }
    }
  }, {
    key: "neighbors",
    value: function neighbors() {
      var north = void 0;var east = void 0;var west = void 0;var south = void 0;

      var _pos3 = _slicedToArray(this.pos, 2),
          y = _pos3[0],
          x = _pos3[1];

      if (this.grid.array[y - 1]) {
        north = this.grid.array[y - 1][x];
      }
      if (this.grid.array[y + 1]) {
        south = this.grid.array[y + 1][x];
      }
      east = this.grid.array[y][x + 1];
      west = this.grid.array[y][x - 1];

      var possibleNeighbors = [north, east, south, west];
      return possibleNeighbors.filter(function (neighbor) {
        if (neighbor) {
          return neighbor;
        }
      });
    }
  }]);

  return Node;
}();

exports.default = Node;

/***/ }),
/* 2 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var BinaryMinHeap = function () {
  function BinaryMinHeap() {
    _classCallCheck(this, BinaryMinHeap);

    this.pq = [null];
  }

  _createClass(BinaryMinHeap, [{
    key: "length",
    value: function length() {
      return this.pq.length;
    }
  }, {
    key: "put",
    value: function put(edge) {
      this.pq.push(edge);
      if (this.pq.length > 2) {
        this.bubble();
      }
    }
  }, {
    key: "take",
    value: function take() {
      if (this.pq.length === 2) {
        return this.pq.pop();
      } else if (this.pq.length > 2) {
        var min = this.pq[1];
        this.pq[1] = this.pq.pop();
        this.sink();
        return min;
      }
    }
  }, {
    key: "bubble",
    value: function bubble() {
      var newIdx = this.pq.length - 1;
      var parentIdx = Math.floor(newIdx / 2);
      while (this.pq[newIdx].weight < this.pq[parentIdx].weight) {
        var _ref = [this.pq[parentIdx], this.pq[newIdx]];
        this.pq[newIdx] = _ref[0];
        this.pq[parentIdx] = _ref[1];

        newIdx = parentIdx;
        if (newIdx === 1) {
          break;
        }
        parentIdx = Math.floor(newIdx / 2);
      }
    }
  }, {
    key: "sink",
    value: function sink() {
      var idx = 1;
      var c1 = 2;
      var c2 = 3;

      while (this.pq[c1]) {
        if (this.pq[c2]) {
          if (this.pq[c2].weight < this.pq[c1].weight && this.pq[c2].weight < this.pq[idx].weight) {
            var _ref2 = [this.pq[idx], this.pq[c2]];
            this.pq[c2] = _ref2[0];
            this.pq[idx] = _ref2[1];

            idx = c2;
          } else if (this.pq[c1].weight < this.pq[idx].weight) {
            var _ref3 = [this.pq[idx], this.pq[c1]];
            this.pq[c1] = _ref3[0];
            this.pq[idx] = _ref3[1];

            idx = c1;
          } else {
            break;
          }
        } else if (this.pq[c1].weight < this.pq[idx].weight) {
          var _ref4 = [this.pq[idx], this.pq[c1]];
          this.pq[c1] = _ref4[0];
          this.pq[idx] = _ref4[1];

          idx = c1;
        } else {
          break;
        }

        c1 = idx * 2;
        c2 = idx * 2 + 1;
      }
    }
  }]);

  return BinaryMinHeap;
}();

exports.default = BinaryMinHeap;

/***/ }),
/* 3 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var _generate_maze = __webpack_require__(4);

var _generate_maze2 = _interopRequireDefault(_generate_maze);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

$(function () {
  var canvasEl = document.getElementsByTagName("canvas")[0];
  var width = 24;
  var height = 14;
  canvasEl.height = height * 20 + 40;
  canvasEl.width = width * 20 + 40;

  var clickNames = ["Dijkstra"];

  var disableAllBtns = function disableAllBtns() {
    clickNames.concat(["maze-regen"]).forEach(function (className) {
      $("." + className).prop("disabled", true);
      $("." + className + "-recent").unbind("mouseenter mouseleave");
    });
  };

  var enableAllBtns = function enableAllBtns() {
    clickNames.concat(["maze-regen"]).forEach(function (className) {
      $("." + className).prop("disabled", false);
      $("." + className + "-recent").mouseenter(function () {
        handleHover("" + className);
      }).mouseleave(function () {
        handleHover(lastAction);
      });
    });
  };

  var maze = new _generate_maze2.default(canvasEl, width, height, enableAllBtns);
  disableAllBtns();
  maze.generate(canvasEl);

  $(".prims").removeClass("hidden");
  var lastAction = null;

  var handleClick = function handleClick(searchType) {
    maze.quickRegen();
    maze.displayVisited(searchType);

    $(".info").addClass("hidden");
    $("." + searchType).removeClass("hidden");
    $("." + searchType + "-recent").removeClass("hidden");

    lastAction = searchType;
  };

  var handleHover = function handleHover(searchType) {
    maze.quickRegen();
    maze.quickDisplay(searchType);
    $(".info").addClass("hidden");
    $("." + searchType).removeClass("hidden");
  };

  $(".maze-regen").on("click", function () {
    disableAllBtns();
    maze.generate(canvasEl);
    $(".info").addClass("hidden");
    $(".recenttrav").addClass("hidden");
    $(".prims").removeClass("hidden");
  });

  $(".search-btns").on("click", function (event) {
    if (clickNames.includes(event.target.className)) {
      disableAllBtns();
      handleClick(event.target.className);
    }
  });
});

/***/ }),
/* 4 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _grid = __webpack_require__(5);

var _grid2 = _interopRequireDefault(_grid);

var _prims = __webpack_require__(6);

var _prims2 = _interopRequireDefault(_prims);

var _edge = __webpack_require__(0);

var _edge2 = _interopRequireDefault(_edge);

var _dijkstra = __webpack_require__(8);

var _dijkstra2 = _interopRequireDefault(_dijkstra);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var GenerateMaze = function () {
  function GenerateMaze(canvasEl, width, height, enableAllBtns) {
    _classCallCheck(this, GenerateMaze);

    this.width = width * 20 + 10;
    this.height = height * 20 + 10;
    this.ctx = canvasEl.getContext("2d");
    this.setup(width, height);
    this.enableAllBtns = enableAllBtns;
  }

  _createClass(GenerateMaze, [{
    key: 'setup',
    value: function setup(width, height) {
      this.grid = new _grid2.default(width, height);
      this.startPos = this.grid.startPos;
      this.goalPos = this.grid.goalPos;
    }
  }, {
    key: 'render',
    value: function render(edges) {
      var _this = this;

      this.ctx.clearRect(10, 10, this.width, this.height);
      this.ctx.fillStyle = "rgb(35, 35, 35)";
      this.ctx.fillRect(10, 10, this.width, this.height);
      edges.forEach(function (edge) {
        edge.render(_this.ctx, "grey");
      });
    }
  }, {
    key: 'renderEndpoints',
    //propriedade dos pontinhos
    value: function renderEndpoints() {
      this.ctx.fillStyle = "yellow";
      var startX = this.startPos[1] * 20 + 25;
      var startY = this.startPos[0] * 20 + 25;
      this.ctx.beginPath();
      this.ctx.arc(startX, startY, 10, 0, Math.PI * 2, true);
      this.ctx.closePath();
      this.ctx.fill();

      this.ctx.fillStyle = "green";
      var goalX = this.goalPos[1] * 20 + 25;
      var goalY = this.goalPos[0] * 20 + 25;
      this.ctx.beginPath();
      this.ctx.arc(goalX, goalY, 10, 0, Math.PI * 2, true);
      this.ctx.closePath();
      this.ctx.fill();
    }
  }, {
    key: 'quickRegen',
    value: function quickRegen() {
      this.render(this.allEdges);
      this.renderEndpoints(this.ctx);
    }
  }, {
    key: 'generate',
    value: function generate() {
      var _this2 = this;

      this.setup(this.grid.width, this.grid.height);
      this.allEdges = new _prims2.default(this.grid).generate();
      this.edges = [];
      var i = 0;

      var animateCallback = function animateCallback() {
        if (i < _this2.allEdges.length) {
          _this2.edges.push(_this2.allEdges[i]);
          i++;
          _this2.render(_this2.edges);

          setTimeout(animateCallback, 1);
        } else {
          _this2.renderEndpoints(_this2.ctx);
          _this2.enableAllBtns();
        }
      };

      animateCallback();
    }
  }, {
    key: 'nodesToEdges',
    value: function nodesToEdges(path) {
      var pathEdges = [];
      for (var i = 1; i < path.length; i++) {
        pathEdges.push(new _edge2.default(path[i - 1], path[i], true));
      }

      return pathEdges;
    }
  }, {
    key: 'quickDisplay',
    value: function quickDisplay(searchType) {
      var _this3 = this;

      var path = void 0;var visited = void 0;
      switch (searchType) {
        case "Dijkstra":
          path = this.nodesToEdges(this.pathDijkstra);
          visited = this.visitedDijkstra;
          break;
      }

      visited.forEach(function (edge) {
        edge.render(_this3.ctx, "#cc700e");
      });

      path.forEach(function (edge) {
        edge.render(_this3.ctx, "#1855a0");
      });

      this.renderEndpoints(this.ctx);
    }
  }, {
    key: 'displayVisited',
    value: function displayVisited(searchType) {
      var _this4 = this;

      var results = void 0;
      switch (searchType) {
        case "Dijkstra":
          this.search = new _dijkstra2.default(this.grid, "M");
          results = this.search.solve();
          this.pathDijkstra = results[0];
          this.visitedDijkstra = results[1].slice();
          break;
      }
      this.path = results[0];
      this.visited = results[1];

      var visitedEdges = this.visited.slice();
      var renderedEdges = [];

      var animateCallback = function animateCallback() {
        //arestas visitadas
        if (visitedEdges.length > 0) {
          renderedEdges.push(visitedEdges.shift());

          renderedEdges.forEach(function (edge, idx) {
            //cor das arestas visitadas
            edge.render(_this4.ctx, "white");
          });
          _this4.renderEndpoints(_this4.ctx);

          setTimeout(animateCallback, 1);
        } else {
          _this4.solve();
        }
      };

      animateCallback();
    }
  }, {
    key: 'solve',
    value: function solve() {
      var _this5 = this;

      var pathEdges = this.nodesToEdges(this.path);
      var renderedEdges = [];
      //arestas
      var animateCallback = function animateCallback() {
        if (pathEdges.length > 0) {
          renderedEdges.push(pathEdges.shift());

          renderedEdges.forEach(function (edge) {
            //pinta cor da aresta
            edge.render(_this5.ctx, "red");
          });
          _this5.renderEndpoints(_this5.ctx);

          setTimeout(animateCallback, 1);
        } else {
          _this5.enableAllBtns();
        }
      };

      animateCallback();
    }
  }]);

  return GenerateMaze;
}();

exports.default = GenerateMaze;

/***/ }),
/* 5 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _node = __webpack_require__(1);

var _node2 = _interopRequireDefault(_node);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var Grid = function Grid(width, height) {
  _classCallCheck(this, Grid);

  this.width = width;
  this.height = height;
  this.array = Grid.makeGrid(width, height);
  this.startPos = Grid.placeEndpoints(this);
  this.goalPos = Grid.placeEndpoints(this);
};

Grid.placeEndpoints = function (grid) {
  var i = Math.floor(Math.random() * grid.height);
  var j = Math.floor(Math.random() * grid.width);
  return [i, j];
};

Grid.makeGrid = function (width, height) {
  var grid = [];
  for (var i = 0; i < height; i++) {
    var row = [];
    for (var j = 0; j < width; j++) {
      row.push(new _node2.default([i, j], i * width + j));
    }
    grid.push(row);
  }
  console.log(grid);
  return grid;
};

exports.default = Grid;

/***/ }),
/* 6 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _binary_heap = __webpack_require__(2);

var _binary_heap2 = _interopRequireDefault(_binary_heap);

var _edge = __webpack_require__(0);

var _edge2 = _interopRequireDefault(_edge);

var _node = __webpack_require__(1);

var _node2 = _interopRequireDefault(_node);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var Prims = function () {
  function Prims(grid) {
    _classCallCheck(this, Prims);

    this.pq = new _binary_heap2.default();
    this.grid = grid;
    this.boolean = {
      length: 0,
      array: new Array(this.grid.width * this.grid.height).fill(false)
    };
    this.edges = [];
  }

  _createClass(Prims, [{
    key: 'generate',
    value: function generate() {
      var _this = this;

      var start = new _node2.default([0, 0], 0);
      start.grid = this.grid;
      this.boolean[start.value] = true;
      this.boolean.length++;
      start.neighbors().forEach(function (neighbor) {
        _this.pq.put(new _edge2.default(start, neighbor));
      });

      while (!this.treeFull()) {
        var cheapestEdge = this.pq.take();
        if (!this.boolean[cheapestEdge.vertex2.value]) {
          (function () {
            var vertex1 = cheapestEdge.vertex1;
            var vertex2 = cheapestEdge.vertex2;

            vertex2.grid = _this.grid;
            _this.boolean[vertex2.value] = true;
            _this.boolean.length++;

            // Whenever edge gets created, make 2 vertices neighbors
            if (!vertex1.edgeNeighbors.includes(vertex2)) {
              vertex1.edgeNeighbors.push(vertex2);
            }
            if (!vertex2.edgeNeighbors.includes(vertex1)) {
              vertex2.edgeNeighbors.push(vertex1);
            }

            _this.edges.push(cheapestEdge);
            vertex2.neighbors().forEach(function (neighbor) {
              _this.pq.put(new _edge2.default(vertex2, neighbor));
            });
          })();
        }
      }

      return this.edges;
    }
  }, {
    key: 'treeFull',
    value: function treeFull() {
      return this.boolean.length === this.boolean.array.length;
    }
  }]);

  return Prims;
}();

exports.default = Prims;

/***/ }),

/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };

var _slicedToArray = function () { function sliceIterator(arr, i) { var _arr = []; var _n = true; var _d = false; var _e = undefined; try { for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"]) _i["return"](); } finally { if (_d) throw _e; } } return _arr; } return function (arr, i) { if (Array.isArray(arr)) { return arr; } else if (Symbol.iterator in Object(arr)) { return sliceIterator(arr, i); } else { throw new TypeError("Invalid attempt to destructure non-iterable instance"); } }; }();

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _binary_heap = __webpack_require__(2);

var _binary_heap2 = _interopRequireDefault(_binary_heap);

var _edge = __webpack_require__(0);

var _edge2 = _interopRequireDefault(_edge);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var Dijkstra = function () {
  function Dijkstra(grid, heuristic) {
    _classCallCheck(this, Dijkstra);

    this.pq = new _binary_heap2.default();
    this.grid = grid;
    this.visited = {
      bool: new Array(grid.width * grid.height).fill(false),
      pq: new _binary_heap2.default(),
      save: []
    };
    this.heuristic = heuristic;
    this.goalValue = grid.goalPos[0] * grid.width + grid.goalPos[1];
    this.setupPriorityQueue();
  }

  _createClass(Dijkstra, [{
    key: 'setupPriorityQueue',
    value: function setupPriorityQueue() {
      var _grid$startPos = _slicedToArray(this.grid.startPos, 2),
          startY = _grid$startPos[0],
          startX = _grid$startPos[1];

      var startNode = this.grid.array[startY][startX];
      startNode.costSoFar = 0;
      startNode.calcHeuristic(startNode, this.heuristic, true);
      startNode.parent = null;
      this.visited.bool[startNode.value] = true;
      this.pq.put(startNode);
    }
  }, {
    key: 'traverseGrid',
    value: function traverseGrid() {
      var _this = this;

      var _loop = function _loop() {
        var current = _this.pq.take();

        _this.visited.save.push(_this.visited.pq.take());

        if (current.value === _this.goalValue) {
          return {
            v: current
          };
        }

        current.edgeNeighbors.forEach(function (neighbor) {
          var newCost = neighbor.calcHeuristic(current, _this.heuristic, true);

          if (!_this.visited.bool[neighbor.value] || newCost < neighbor.weight) {
            _this.visited.bool[neighbor.value] = true;
            neighbor.weight = newCost;
            neighbor.parent = current;
            _this.pq.put(neighbor);

            var edge = new _edge2.default(current, neighbor, true);
            edge.weight = neighbor.weight;
            _this.visited.pq.put(edge);
          }
        });
      };

      while (this.pq.length() > 1) {
        var _ret = _loop();

        if ((typeof _ret === 'undefined' ? 'undefined' : _typeof(_ret)) === "object") return _ret.v;
      }
    }
  }, {
    key: 'traversePath',
    value: function traversePath() {
      var path = [this.traverseGrid()];

      while (path.slice(-1)[0].parent) {
        path.push(path.slice(-1)[0].parent);
      }

      return [path, this.visited.save.slice(1)];
    }
  }, {
    key: 'solve',
    value: function solve() {
      return this.traversePath();
    }
  }]);

  return Dijkstra;
}();

exports.default = Dijkstra;

/***/ }),
/* 9 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _node = __webpack_require__(1);

var _node2 = _interopRequireDefault(_node);

var _edge = __webpack_require__(0);

var _edge2 = _interopRequireDefault(_edge);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var BreadthOrDepthFirstSearch = function () {
  function BreadthOrDepthFirstSearch(grid, searchType) {
    _classCallCheck(this, BreadthOrDepthFirstSearch);

    this.queue = [grid.array[grid.startPos[0]][grid.startPos[1]]];
    this.visited = {
      bool: new Array(grid.width * grid.height).fill(false),
      all: [],
      save: []
    };
    this.goalValue = grid.goalPos[0] * grid.width + grid.goalPos[1];
    this.searchType = searchType;
  }

  _createClass(BreadthOrDepthFirstSearch, [{
    key: 'traverseGrid',
    value: function traverseGrid() {
      var _this = this;

      var _loop = function _loop() {
        var current = void 0;
        if (_this.searchType === "DFS") {
          current = _this.queue.pop();
          _this.visited.save.push(_this.visited.all.pop());
        } else {
          current = _this.queue.shift();
          _this.visited.save.push(_this.visited.all.shift());
        }
        _this.visited.bool[current.value] = true;
        if (current.value === _this.goalValue) {
          return {
            v: current
          };
        }

        current.edgeNeighbors.forEach(function (neighbor) {
          if (!_this.queue.includes(neighbor) && !_this.visited.bool[neighbor.value]) {

            _this.visited.all.push(new _edge2.default(current, neighbor, true));

            neighbor.parent = current;
            _this.queue.push(neighbor);
          }
        });
      };

      while (this.queue.length > 0) {
        var _ret = _loop();

        if ((typeof _ret === 'undefined' ? 'undefined' : _typeof(_ret)) === "object") return _ret.v;
      }
    }
  }, {
    key: 'traversePath',
    value: function traversePath() {
      var path = [this.traverseGrid()];

      while (path.slice(-1)[0].parent) {
        path.push(path.slice(-1)[0].parent);
      }

      return [path, this.visited.save.slice(1)];
    }
  }, {
    key: 'solve',
    value: function solve() {
      return this.traversePath();
    }
  }]);

  return BreadthOrDepthFirstSearch;
}();

exports.default = BreadthOrDepthFirstSearch;

/***/ })
/******/ ]);
//# sourceMappingURL=bundle.js.map