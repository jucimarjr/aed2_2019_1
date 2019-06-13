/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};

/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {

/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;

/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};

/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;

/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}


/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;

/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;

/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";

/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports, __webpack_require__) {

	module.exports = __webpack_require__(1);


/***/ },
/* 1 */
/***/ function(module, exports, __webpack_require__) {

	/* eslint-env browser */
	var algorithmFunc = __webpack_require__(2);
	var Maze = __webpack_require__(3).Maze;
	var GridMask = __webpack_require__(3).GridMask;
	var dirs = __webpack_require__(3).directions;

	if (!(algorithmFunc.features && algorithmFunc.features.mask)) {
	    document.getElementById('ifmask').style.display = 'none';
	}

	function makeRandom(seed) {
	    var randomjs = __webpack_require__(8);
	    var engine = randomjs.engines.mt19937().seed(seed);
	    var real = randomjs.real(0, 1);
	    return function() {
	        return real(engine);
	    };
	}

	function makeMask(width, height) {
	    var mask = new GridMask(width, height, {
	        interior: true
	    });
	    for (var x = 0 ; x < width; x += 10) {
	        for (var y = 0; y < height; y += 10) {
	            for (var xx = 0; xx < 5; xx ++) {
	                for (var yy = 0; yy < 5; yy ++) {
	                    mask.set(x + 5 + xx, y + 5 + yy, false);
	                }
	            }
	        }
	    }
	    return mask;
	}

	var go = document.getElementById('go');
	go.addEventListener('click', function() {
	    var width = +document.getElementById('width').value;
	    var height = +document.getElementById('height').value;
	    var seed = +document.getElementById('seed').value;
	    var mask = 0;
	    var zoom = 4;
	    if (!width || !height || width < 1 || height < 1)
	        return;

	    var options = {
	        random: seed ? makeRandom(seed) : Math.random
	    };
	    if (mask)
	        options.mask = makeMask(width, height);

	    var maze = new Maze(width, height);
	    algorithmFunc(maze, options);

	    var canvas = document.getElementById('result');
	    canvas.width = width * (1 + zoom) + 1;
	    canvas.height = height * (1 + zoom) + 1;
	    var context = canvas.getContext('2d');
	    context.fillStyle = 'white';
	    context.fillRect(0, 0, canvas.width, canvas.height);
	    context.fillStyle = 'black';
	    var cy, y;
	    for (y = 0; y < maze.height(); y ++) {
	        cy = y * (1 + zoom);
	        var cx, x;
	        for (x = 0; x < maze.width(); x ++) {
	            cx = x * (1 + zoom);
	            if (mask) {
	                if (!options.mask.get(x, y)) {
	                    context.fillRect(cx, cy, 1 + zoom, 1 + zoom);
	                    continue;
	                }
	            }
	            context.fillRect(cx, cy, 1, 1);
	            if (!maze.getPassage(x, y, dirs.NORTH))
	                context.fillRect(cx + 1, cy, zoom, 1);
	            if (!maze.getPassage(x, y, dirs.WEST))
	                context.fillRect(cx, cy + 1, 1, zoom);
	        }
	        cx = x * (1 + zoom);
	        context.fillRect(cx, cy, 1, 1 + zoom);
	    }
	    cy = y * (1 + zoom);
	    context.fillRect(0, cy, canvas.width, 1);
	});


/***/ },
/* 2 */
/***/ function(module, exports, __webpack_require__) {

	var core = __webpack_require__(3);
	var dirs = core.directions;
	var SetGrid = __webpack_require__(7);

	/**
	 * @typedef {Object} MGOptions
	 * @property {Function} random Returns a random float between 0 (inclusive) and 1 (exclusive)
	 */

	/**
	 * Chooses a random integer between 0 (inclusive) and max (exclusive)
	 *
	 * @param {MGOptions} options
	 * @param {integer} max
	 */
	function randomInt(options, max) {
	    return Math.floor(options.random() * max);
	}

	/**
	 * Shuffles an array
	 *
	 * @param {MGOptions} options
	 * @param {Array} array
	 */
	function randomShuffle(options, array) {
	    for (var i = array.length; i > 0; i --) {
	        var j = randomInt(options, i);
	        var temp = array[i - 1];
	        array[i - 1] = array[j];
	        array[j] = temp;
	    }
	}

	/**
	 * Returns an array of all possible passages in the grid.
	 *
	 * @param {MGOptions} options
	 * @param {integer} width
	 * @param {integer} height
	 */
	function allEdgesArray(options, width, height) {
	    var edges = [];
	    for (var x = 0; x < width; x ++) {
	        for (var y = 0; y < height; y ++) {
	            if (options.mask && !options.mask.get(x, y))
	                continue;
	            if (x > 0 && (!options.mask || options.mask.get(x - 1, y)))
	                edges.push([x, y, dirs.WEST]);
	            if (y > 0 && (!options.mask || options.mask.get(x, y - 1)))
	                edges.push([x, y, dirs.NORTH]);
	        }
	    }
	    return edges;
	}

	/**
	 * Kruskal's algorithm maze generator.
	 *
	 * @param {Maze} maze
	 * @param {MGOptions} options
	 */
	function kruskal(maze, options) {
	    var width = maze.width();
	    var height = maze.height();

	    // First generate a list of all the possible passages in the maze
	    var edges = allEdgesArray(options, width, height);

	    // Now shuffle that list of passages
	    randomShuffle(options, edges);

	    var setGrid = new SetGrid(width, height);

	    for (var i = 0; i < edges.length; i ++) {
	        var edge = edges[i];
	        if (edge[2] == dirs.WEST) {
	            if (setGrid.merge(edge[0], edge[1], edge[0] - 1, edge[1]))
	                maze.setPassage(edge[0], edge[1], edge[2], true);
	        } else {
	            if (setGrid.merge(edge[0], edge[1], edge[0], edge[1] - 1))
	                maze.setPassage(edge[0], edge[1], edge[2], true);
	        }
	    }
	}

	kruskal.id = 'kruskal';
	kruskal.name = 'Kruskal\'s algorithm';
	kruskal.features = {
	    mask: true
	};

	module.exports = kruskal;


/***/ },
/* 3 */
/***/ function(module, exports, __webpack_require__) {

	exports.GridMask = __webpack_require__(4);
	exports.Maze = __webpack_require__(5);
	exports.directions = __webpack_require__(6);


/***/ },
/* 4 */
/***/ function(module, exports) {

	/**
	 * @typedef {Object} GridMaskOptions
	 * @property {boolean} [interior] The value to intialize interior cells to
	 * @property {boolean} [exterior] The value to return for exterior cells
	 */

	/**
	 * A GridMask is a rectangular grid of boolean values.
	 *
	 * @constructor
	 * @param {integer} width
	 * @param {integer} height
	 * @param {GridMaskOptions} options
	 */
	function GridMask(width, height, options) {
	    if (width < 0 || height < 0)
	        throw new Error('invalid size: ' + width + 'x' + height);
	    options = options || {};
	    var interior = false;
	    if (options.interior != null)
	        interior = !!options.interior;
	    this._width = width;
	    this._height = height;
	    this._exterior = false;
	    if (options.exterior != null)
	        this._exterior = !!options.exterior;
	    this._blockWidth = (width+31) >> 5;
	    if (options._grid) {
	        this._grid = options._grid;
	        return;
	    }
	    this._grid = new Array(this._blockWidth * height);
	    var initBlock = interior ? ~0 : 0;
	    for (var i = 0; i < this._blockWidth * height; i ++) {
	        this._grid[i] = initBlock;
	    }
	}

	/**
	 * The width of the GridMask
	 *
	 * @return {integer}
	 */
	GridMask.prototype.width = function() {
	    return this._width;
	};

	/**
	 * The height of the GridMask
	 *
	 * @return {integer}
	 */
	GridMask.prototype.height = function() {
	    return this._height;
	};

	/**
	 * Returns a copy of the GridMask.
	 *
	 * @return {GridMask}
	 */
	GridMask.prototype.clone = function() {
	    return new GridMask(this.width(), this.height(), {
	        exterior: this._exterior,
	        _grid: this._grid.slice()
	    });
	};

	/**
	 * Returns the boolean value at the specified cell
	 *
	 * @param {integer} x
	 * @param {integer} y
	 */
	GridMask.prototype.get = function(x, y) {
	    if (x < 0 || x >= this._width || y < 0 || y >= this._height) {
	        return this._exterior;
	    }
	    var index = y * this._blockWidth + (x >> 5);
	    var mask = 1 << (x & 31);
	    return (this._grid[index] & mask) != 0;
	};

	/**
	 * Sets the boolean value at the specified cell.  Throws an
	 * error for coordinates that lie outside the grid.
	 *
	 * @param {integer} x
	 * @param {integer} y
	 * @param {boolean} [value=true]
	 */
	GridMask.prototype.set = function(x, y, value) {
	    if (value == null)
	        value = true;
	    if (x < 0 || x >= this._width || y < 0 || y >= this._height) {
	        throw new Error('cell out of bounds: ' + x + ',' + y);
	    }
	    var index = y * this._blockWidth + (x >> 5);
	    var mask = 1 << (x & 31);
	    if (value)
	        this._grid[index] |= mask;
	    else
	        this._grid[index] &= ~mask;
	    return this;
	};

	/**
	 * ...
	 *
	 * @param {integer} x
	 * @param {integer} y
	 * @param {boolean} [value=true]
	 */
	GridMask.prototype.testAndSet = function(x, y, value) {
	    if (value == null)
	        value = true;
	    if (x < 0 || x >= this._width || y < 0 || y >= this._height) {
	        if (this._exterior == value)
	            return false;
	        throw new Error('cell out of bounds: ' + x + ',' + y);
	    }
	    var index = y * this._blockWidth + (x >> 5);
	    var mask = 1 << (x & 31);
	    if (((this._grid[index] & mask) != 0) == value)
	        return false;
	    if (value)
	        this._grid[index] |= mask;
	    else
	        this._grid[index] &= ~mask;
	    return true;
	};

	module.exports = GridMask;


/***/ },
/* 5 */
/***/ function(module, exports, __webpack_require__) {

	var dirs = __webpack_require__(6);

	/**
	 * A Cell is a wrapper object that makes it easier to
	 * ask for passage information by name.
	 *
	 * @constructor
	 * @private
	 * @param {integer} width
	 * @param {integer} height
	 */
	function Cell(north, east, south, west) {
	    this._north = north;
	    this._east = east;
	    this._south = south;
	    this._west = west;
	}

	Cell.prototype.north = function() {
	    return this._north;
	};

	Cell.prototype.west = function() {
	    return this._west;
	};

	Cell.prototype.south = function() {
	    return this._south;
	};

	Cell.prototype.east = function() {
	    return this._east;
	};

	/**
	 * A Maze is a rectangular grid of cells, where each cell
	 * may have passages in each of the cardinal directions.
	 * The maze is initialized with each cell having no passages.
	 *
	 * @constructor
	 * @param {integer} width
	 * @param {integer} height
	 */
	function Maze(width, height) {
	    if (width < 0 || height < 0)
	        throw new Error('invalid size: ' + width + 'x' + height);
	    this._width = width;
	    this._height = height;
	    this._blockWidth = ((width+1)+15) >> 4;
	    this._grid = new Array(this._blockWidth * (height + 1));
	    for (var i = 0; i < this._blockWidth * (height + 1); i ++)
	        this._grid[i] = 0;
	}

	/**
	 * The width of the Maze
	 *
	 * @return {integer}
	 */
	Maze.prototype.width = function() {
	    return this._width;
	};

	/**
	 * The height of the Maze
	 *
	 * @return {integer}
	 */
	Maze.prototype.height = function() {
	    return this._height;
	};

	// function cellData(grid, blockWidth, x, y) {
	//     var index = y * blockWidth + (x >> 3);
	//     var shift = ((x & 7) * 4);
	//     return (grid[index] >> shift) & 15;
	// }
	//
	// function setCellPassage(grid, blockWidth, x, y, dir, value) {
	//     var index = y * blockWidth + (x >> 3);
	//     var shift = ((x & 7) * 4);
	//     var mask = dirs.bitmask(dir) << shift;
	//     if (value)
	//         grid[index] |= mask;
	//     else
	//         grid[index] &= ~mask;
	// }

	/**
	 * Returns the cell at the given position.
	 *
	 * @param {integer} x
	 * @param {integer} y
	 * @return {Cell}
	 */
	Maze.prototype.cell = function(x, y) {
	    if (x < 0 || y < 0 || x >= this._width || y >= this._height)
	        return new Cell(false, false, false, false);
	    var north, east, south, west;
	    var index = y * this._blockWidth + (x >> 4);
	    var mask = 1 << ((x & 15) * 2);
	    north = (this._grid[index] & mask) != 0;
	    west = (this._grid[index] & (mask << 1)) != 0;
	    south = (this._grid[index + this._blockWidth] & mask) != 0;
	    var x2 = x + 1;
	    var index2 = y * this._blockWidth + (x2 >> 4);
	    var mask2 = 1 << ((x2 & 15) * 2);
	    east = (this._grid[index2] & (mask2 << 1)) != 0;
	    return new Cell(north, east, south, west);
	};

	/**
	 * Returns whether there is a passage at the given position and
	 * direction
	 *
	 * @param {integer} x
	 * @param {integer} y
	 * @param {Direction} dir
	 */
	Maze.prototype.getPassage = function(x, y, dir) {
	    if (x < 0 || y < 0 || x >= this._width || y >= this._height)
	        return false;
	    var index, mask;
	    if (dir != dirs.EAST) {
	        index = y * this._blockWidth + (x >> 4);
	        mask = 1 << ((x & 15) * 2);
	        if (dir == dirs.NORTH)
	            /* pass through */;
	        else if (dir == dirs.WEST)
	            mask <<= 1;
	        else
	            index += this._blockWidth;
	    } else {
	        index = y * this._blockWidth + ((x + 1) >> 4);
	        mask = 1 << (((x + 1) & 15) * 2 + 1);
	    }
	    return (this._grid[index] & mask) != 0;
	};

	/**
	 * Creates or removes a passage at the given position and
	 * direction.  Note that this also creates the corresponding
	 * passage in the neighboring cell.
	 *
	 * @param {integer} x
	 * @param {integer} y
	 * @param {Direction} dir
	 * @param {boolean} value
	 */
	Maze.prototype.setPassage = function(x, y, dir, value) {
	    if (value == null)
	        value = true;
	    var index, mask;
	    if (dir != dirs.EAST) {
	        index = y * this._blockWidth + (x >> 4);
	        mask = 1 << ((x & 15) * 2);
	        if (dir == dirs.NORTH) {
	            if (x < 0 || y < 1 || x >= this._width || y >= this._height)
	                throw new Error('passage out of bounds: ' + x + ',' + y + ' dir=' + dir);
	        } else if (dir == dirs.WEST) {
	            if (x < 1 || y < 0 || x >= this._width || y >= this._height)
	                throw new Error('passage out of bounds: ' + x + ',' + y + ' dir=' + dir);
	            mask <<= 1;
	        } else {
	            if (x < 0 || y < 0 || x >= this._width || y >= this._height - 1)
	                throw new Error('passage out of bounds: ' + x + ',' + y + ' dir=' + dir);
	            index += this._blockWidth;
	        }
	    } else {
	        if (x < 0 || y < 0 || x >= this._width - 1 || y >= this._height)
	            throw new Error('passage out of bounds: ' + x + ',' + y + ' dir=' + dir);
	        index = y * this._blockWidth + ((x + 1) >> 4);
	        mask = 1 << (((x + 1) & 15) * 2 + 1);
	    }
	    if (value)
	        this._grid[index] |= mask;
	    else
	        this._grid[index] &= ~mask;
	};

	module.exports = Maze;


/***/ },
/* 6 */
/***/ function(module, exports) {

	var dirs = {};

	/**
	 * @typedef {integer} Direction
	 */

	dirs.NORTH = 0;
	dirs.EAST =  1;
	dirs.SOUTH = 2;
	dirs.WEST =  3;

	dirs.ALL = [dirs.NORTH, dirs.EAST, dirs.SOUTH, dirs.WEST];

	/**
	 * Returns the opposite direction
	 *
	 * @param {Direction} dir
	 * @return {Direction}
	 */
	dirs.opposite = function(dir) {
	    switch (dir) {
	        case 0/*dirs.NORTH*/: return 2;
	        case 1/*dirs.EAST*/: return 3;
	        case 2/*dirs.SOUTH*/: return 0;
	        case 3/*dirs.WEST*/: return 1;
	        default: throw new Error('bad direction: ' + dir);
	    }
	};

	/**
	 * Returns the x component of the direction vector
	 *
	 * @param {Direction} dir
	 * @return {integer}
	 */
	dirs.dx = function(dir) {
	    switch (dir) {
	        case 0/*dirs.NORTH*/: return 0;
	        case 1/*dirs.EAST*/: return 1;
	        case 2/*dirs.SOUTH*/: return 0;
	        case 3/*dirs.WEST*/: return -1;
	        default: throw new Error('bad direction: ' + dir);
	    }
	};

	/**
	 * Returns the y component of the direction vector
	 *
	 * @param {Direction} dir
	 * @return {integer}
	 */
	dirs.dy = function(dir) {
	    switch (dir) {
	        case 0/*dirs.NORTH*/: return -1;
	        case 1/*dirs.EAST*/: return 0;
	        case 2/*dirs.SOUTH*/: return 1;
	        case 3/*dirs.WEST*/: return 0;
	        default: throw new Error('bad direction: ' + dir);
	    }
	};

	/**
	 * Moves the coordinate in the given direction
	 *
	 * @param {integer} x
	 * @param {integer} y
	 * @param {Direction} dir
	 * @return {integer[]}
	 */
	dirs.move = function(x, y, dir) {
	    switch (dir) {
	        case 0/*dirs.NORTH*/: return [x, y-1];
	        case 1/*dirs.EAST*/: return [x+1, y];
	        case 2/*dirs.SOUTH*/: return [x, y+1];
	        case 3/*dirs.WEST*/: return [x-1, y];
	        default: throw new Error('bad direction: ' + dir);
	    }
	};

	/**
	 * Returns a bitmask for the direction, useful for
	 * storing a bunch of direction boolean values in
	 * a single integer.
	 *
	 * @param {Direction} dir
	 * @return {integer}
	 */
	dirs.bitmask = function(dir) {
	    return 1 << dir;
	};

	module.exports = dirs;


/***/ },
/* 7 */
/***/ function(module, exports) {

	/**
	 * A SetGrid is a rectangular grid, with the cells placed in sets (or partitions).
	 * The SetGrid can efficiently look up the set for a given cell, place a cell in
	 * a new set, and merge two sets.  The grid is initialized with every cell in
	 * its own set.
	 *
	 * @constructor
	 * @param {integer} width
	 * @param {integer} height
	 */
	function SetGrid(width, height, options) {
	    if (width < 0 || height < 0)
	        throw new Error('invalid size: ' + width + 'x' + height);
	    this._width = width;
	    this._height = height;
	    if (options && options._grid) {
	        this._grid = options._grid;
	        return;
	    }
	    this._grid = new Array(this._width * height * 2);
	    for (var i = 0; i < this._grid.length; i += 2) {
	        this._grid[i] = -1;
	        this._grid[i+1] = i;
	    }
	}

	SetGrid.EXTERIOR = -1;

	/**
	 * The width of the SetGrid
	 *
	 * @return {integer}
	 */
	SetGrid.prototype.width = function() {
	    return this._width;
	};

	/**
	 * The height of the SetGrid
	 *
	 * @return {integer}
	 */
	SetGrid.prototype.height = function() {
	    return this._height;
	};

	/**
	 * Returns a copy of the SetGrid.
	 *
	 * @return {SetGrid}
	 */
	SetGrid.prototype.clone = function() {
	    return new SetGrid(this.width(), this.height(), {
	        _grid: this._grid.slice()
	    });
	};

	/**
	 * Returns the set identifier at the specified cell.  Will return
	 * SetGrid.EXTERIOR for cells that haven't been placed into sets yet.
	 *
	 * @param {integer} x
	 * @param {integer} y
	 */
	SetGrid.prototype.get = function(x, y) {
	    if (x < 0 || x >= this._width || y < 0 || y >= this._height) {
	        return SetGrid.EXTERIOR;
	    }
	    for (;;) {
	        var index = (y * this._width + x) * 2;
	        x = this._grid[index];
	        y = this._grid[index+1];
	        if (x < 0)
	            return y;
	    }
	};

	// TODO path compression?
	/**
	 * If the two specified cells are in different sets, merges those
	 * sets and returns true.  Otherwise returns false.  Throws an
	 * error if either cell is out of bounds.
	 *
	 * @param {integer} x
	 * @param {integer} y
	 * @param {boolean} [value=true]
	 */
	SetGrid.prototype.merge = function(x1, y1, x2, y2) {
	    if (x1 < 0 || x1 >= this._width || y1 < 0 || y1 >= this._height) {
	        throw new Error('cell out of bounds: ' + x1 + ',' + y1);
	    }
	    if (x2 < 0 || x2 >= this._width || y2 < 0 || y2 >= this._height) {
	        throw new Error('cell out of bounds: ' + x2 + ',' + y2);
	    }
	    var index1, index2;
	    var depth1, depth2;
	    for (;;) {
	        index1 = (y1 * this._width + x1) * 2;
	        depth1 = this._grid[index1];
	        if (depth1 < 0) {
	            break;
	        }
	        x1 = depth1;
	        y1 = this._grid[index1+1];
	    }
	    for (;;) {
	        index2 = (y2 * this._width + x2) * 2;
	        depth2 = this._grid[index2];
	        if (depth2 < 0) {
	            break;
	        }
	        x2 = depth2;
	        y2 = this._grid[index2+1];
	    }
	    if (x1 == x2 && y1 == y2)
	        return false;
	    if (depth1 > depth2) {
	        this._grid[index1] = x2;
	        this._grid[index1+1] = y2;
	    } else if (depth1 < depth2) {
	        this._grid[index2] = x1;
	        this._grid[index2+1] = y1;
	    } else {
	        this._grid[index2] = x1;
	        this._grid[index2+1] = y1;
	        this._grid[index1] --;
	    }
	    return true;
	};

	module.exports = SetGrid;


/***/ },
/* 8 */
/***/ function(module, exports, __webpack_require__) {

	var __WEBPACK_AMD_DEFINE_RESULT__;/*jshint eqnull:true*/
	(function (root) {
	  "use strict";

	  var GLOBAL_KEY = "Random";

	  var imul = (typeof Math.imul !== "function" || Math.imul(0xffffffff, 5) !== -5 ?
	    function (a, b) {
	      var ah = (a >>> 16) & 0xffff;
	      var al = a & 0xffff;
	      var bh = (b >>> 16) & 0xffff;
	      var bl = b & 0xffff;
	      // the shift by 0 fixes the sign on the high part
	      // the final |0 converts the unsigned value into a signed value
	      return (al * bl) + (((ah * bl + al * bh) << 16) >>> 0) | 0;
	    } :
	    Math.imul);

	  var stringRepeat = (typeof String.prototype.repeat === "function" && "x".repeat(3) === "xxx" ?
	    function (x, y) {
	      return x.repeat(y);
	    } : function (pattern, count) {
	      var result = "";
	      while (count > 0) {
	        if (count & 1) {
	          result += pattern;
	        }
	        count >>= 1;
	        pattern += pattern;
	      }
	      return result;
	    });

	  function Random(engine) {
	    if (!(this instanceof Random)) {
	      return new Random(engine);
	    }

	    if (engine == null) {
	      engine = Random.engines.nativeMath;
	    } else if (typeof engine !== "function") {
	      throw new TypeError("Expected engine to be a function, got " + typeof engine);
	    }
	    this.engine = engine;
	  }
	  var proto = Random.prototype;

	  Random.engines = {
	    nativeMath: function () {
	      return (Math.random() * 0x100000000) | 0;
	    },
	    mt19937: (function (Int32Array) {
	      // http://en.wikipedia.org/wiki/Mersenne_twister
	      function refreshData(data) {
	        var k = 0;
	        var tmp = 0;
	        for (;
	          (k | 0) < 227; k = (k + 1) | 0) {
	          tmp = (data[k] & 0x80000000) | (data[(k + 1) | 0] & 0x7fffffff);
	          data[k] = data[(k + 397) | 0] ^ (tmp >>> 1) ^ ((tmp & 0x1) ? 0x9908b0df : 0);
	        }

	        for (;
	          (k | 0) < 623; k = (k + 1) | 0) {
	          tmp = (data[k] & 0x80000000) | (data[(k + 1) | 0] & 0x7fffffff);
	          data[k] = data[(k - 227) | 0] ^ (tmp >>> 1) ^ ((tmp & 0x1) ? 0x9908b0df : 0);
	        }

	        tmp = (data[623] & 0x80000000) | (data[0] & 0x7fffffff);
	        data[623] = data[396] ^ (tmp >>> 1) ^ ((tmp & 0x1) ? 0x9908b0df : 0);
	      }

	      function temper(value) {
	        value ^= value >>> 11;
	        value ^= (value << 7) & 0x9d2c5680;
	        value ^= (value << 15) & 0xefc60000;
	        return value ^ (value >>> 18);
	      }

	      function seedWithArray(data, source) {
	        var i = 1;
	        var j = 0;
	        var sourceLength = source.length;
	        var k = Math.max(sourceLength, 624) | 0;
	        var previous = data[0] | 0;
	        for (;
	          (k | 0) > 0; --k) {
	          data[i] = previous = ((data[i] ^ imul((previous ^ (previous >>> 30)), 0x0019660d)) + (source[j] | 0) + (j | 0)) | 0;
	          i = (i + 1) | 0;
	          ++j;
	          if ((i | 0) > 623) {
	            data[0] = data[623];
	            i = 1;
	          }
	          if (j >= sourceLength) {
	            j = 0;
	          }
	        }
	        for (k = 623;
	          (k | 0) > 0; --k) {
	          data[i] = previous = ((data[i] ^ imul((previous ^ (previous >>> 30)), 0x5d588b65)) - i) | 0;
	          i = (i + 1) | 0;
	          if ((i | 0) > 623) {
	            data[0] = data[623];
	            i = 1;
	          }
	        }
	        data[0] = 0x80000000;
	      }

	      function mt19937() {
	        var data = new Int32Array(624);
	        var index = 0;
	        var uses = 0;

	        function next() {
	          if ((index | 0) >= 624) {
	            refreshData(data);
	            index = 0;
	          }

	          var value = data[index];
	          index = (index + 1) | 0;
	          uses += 1;
	          return temper(value) | 0;
	        }
	        next.getUseCount = function() {
	          return uses;
	        };
	        next.discard = function (count) {
	          uses += count;
	          if ((index | 0) >= 624) {
	            refreshData(data);
	            index = 0;
	          }
	          while ((count - index) > 624) {
	            count -= 624 - index;
	            refreshData(data);
	            index = 0;
	          }
	          index = (index + count) | 0;
	          return next;
	        };
	        next.seed = function (initial) {
	          var previous = 0;
	          data[0] = previous = initial | 0;

	          for (var i = 1; i < 624; i = (i + 1) | 0) {
	            data[i] = previous = (imul((previous ^ (previous >>> 30)), 0x6c078965) + i) | 0;
	          }
	          index = 624;
	          uses = 0;
	          return next;
	        };
	        next.seedWithArray = function (source) {
	          next.seed(0x012bd6aa);
	          seedWithArray(data, source);
	          return next;
	        };
	        next.autoSeed = function () {
	          return next.seedWithArray(Random.generateEntropyArray());
	        };
	        return next;
	      }

	      return mt19937;
	    }(typeof Int32Array === "function" ? Int32Array : Array)),
	    browserCrypto: (typeof crypto !== "undefined" && typeof crypto.getRandomValues === "function" && typeof Int32Array === "function") ? (function () {
	      var data = null;
	      var index = 128;

	      return function () {
	        if (index >= 128) {
	          if (data === null) {
	            data = new Int32Array(128);
	          }
	          crypto.getRandomValues(data);
	          index = 0;
	        }

	        return data[index++] | 0;
	      };
	    }()) : null
	  };

	  Random.generateEntropyArray = function () {
	    var array = [];
	    var engine = Random.engines.nativeMath;
	    for (var i = 0; i < 16; ++i) {
	      array[i] = engine() | 0;
	    }
	    array.push(new Date().getTime() | 0);
	    return array;
	  };

	  function returnValue(value) {
	    return function () {
	      return value;
	    };
	  }

	  // [-0x80000000, 0x7fffffff]
	  Random.int32 = function (engine) {
	    return engine() | 0;
	  };
	  proto.int32 = function () {
	    return Random.int32(this.engine);
	  };

	  // [0, 0xffffffff]
	  Random.uint32 = function (engine) {
	    return engine() >>> 0;
	  };
	  proto.uint32 = function () {
	    return Random.uint32(this.engine);
	  };

	  // [0, 0x1fffffffffffff]
	  Random.uint53 = function (engine) {
	    var high = engine() & 0x1fffff;
	    var low = engine() >>> 0;
	    return (high * 0x100000000) + low;
	  };
	  proto.uint53 = function () {
	    return Random.uint53(this.engine);
	  };

	  // [0, 0x20000000000000]
	  Random.uint53Full = function (engine) {
	    while (true) {
	      var high = engine() | 0;
	      if (high & 0x200000) {
	        if ((high & 0x3fffff) === 0x200000 && (engine() | 0) === 0) {
	          return 0x20000000000000;
	        }
	      } else {
	        var low = engine() >>> 0;
	        return ((high & 0x1fffff) * 0x100000000) + low;
	      }
	    }
	  };
	  proto.uint53Full = function () {
	    return Random.uint53Full(this.engine);
	  };

	  // [-0x20000000000000, 0x1fffffffffffff]
	  Random.int53 = function (engine) {
	    var high = engine() | 0;
	    var low = engine() >>> 0;
	    return ((high & 0x1fffff) * 0x100000000) + low + (high & 0x200000 ? -0x20000000000000 : 0);
	  };
	  proto.int53 = function () {
	    return Random.int53(this.engine);
	  };

	  // [-0x20000000000000, 0x20000000000000]
	  Random.int53Full = function (engine) {
	    while (true) {
	      var high = engine() | 0;
	      if (high & 0x400000) {
	        if ((high & 0x7fffff) === 0x400000 && (engine() | 0) === 0) {
	          return 0x20000000000000;
	        }
	      } else {
	        var low = engine() >>> 0;
	        return ((high & 0x1fffff) * 0x100000000) + low + (high & 0x200000 ? -0x20000000000000 : 0);
	      }
	    }
	  };
	  proto.int53Full = function () {
	    return Random.int53Full(this.engine);
	  };

	  function add(generate, addend) {
	    if (addend === 0) {
	      return generate;
	    } else {
	      return function (engine) {
	        return generate(engine) + addend;
	      };
	    }
	  }

	  Random.integer = (function () {
	    function isPowerOfTwoMinusOne(value) {
	      return ((value + 1) & value) === 0;
	    }

	    function bitmask(masking) {
	      return function (engine) {
	        return engine() & masking;
	      };
	    }

	    function downscaleToLoopCheckedRange(range) {
	      var extendedRange = range + 1;
	      var maximum = extendedRange * Math.floor(0x100000000 / extendedRange);
	      return function (engine) {
	        var value = 0;
	        do {
	          value = engine() >>> 0;
	        } while (value >= maximum);
	        return value % extendedRange;
	      };
	    }

	    function downscaleToRange(range) {
	      if (isPowerOfTwoMinusOne(range)) {
	        return bitmask(range);
	      } else {
	        return downscaleToLoopCheckedRange(range);
	      }
	    }

	    function isEvenlyDivisibleByMaxInt32(value) {
	      return (value | 0) === 0;
	    }

	    function upscaleWithHighMasking(masking) {
	      return function (engine) {
	        var high = engine() & masking;
	        var low = engine() >>> 0;
	        return (high * 0x100000000) + low;
	      };
	    }

	    function upscaleToLoopCheckedRange(extendedRange) {
	      var maximum = extendedRange * Math.floor(0x20000000000000 / extendedRange);
	      return function (engine) {
	        var ret = 0;
	        do {
	          var high = engine() & 0x1fffff;
	          var low = engine() >>> 0;
	          ret = (high * 0x100000000) + low;
	        } while (ret >= maximum);
	        return ret % extendedRange;
	      };
	    }

	    function upscaleWithinU53(range) {
	      var extendedRange = range + 1;
	      if (isEvenlyDivisibleByMaxInt32(extendedRange)) {
	        var highRange = ((extendedRange / 0x100000000) | 0) - 1;
	        if (isPowerOfTwoMinusOne(highRange)) {
	          return upscaleWithHighMasking(highRange);
	        }
	      }
	      return upscaleToLoopCheckedRange(extendedRange);
	    }

	    function upscaleWithinI53AndLoopCheck(min, max) {
	      return function (engine) {
	        var ret = 0;
	        do {
	          var high = engine() | 0;
	          var low = engine() >>> 0;
	          ret = ((high & 0x1fffff) * 0x100000000) + low + (high & 0x200000 ? -0x20000000000000 : 0);
	        } while (ret < min || ret > max);
	        return ret;
	      };
	    }

	    return function (min, max) {
	      min = Math.floor(min);
	      max = Math.floor(max);
	      if (min < -0x20000000000000 || !isFinite(min)) {
	        throw new RangeError("Expected min to be at least " + (-0x20000000000000));
	      } else if (max > 0x20000000000000 || !isFinite(max)) {
	        throw new RangeError("Expected max to be at most " + 0x20000000000000);
	      }

	      var range = max - min;
	      if (range <= 0 || !isFinite(range)) {
	        return returnValue(min);
	      } else if (range === 0xffffffff) {
	        if (min === 0) {
	          return Random.uint32;
	        } else {
	          return add(Random.int32, min + 0x80000000);
	        }
	      } else if (range < 0xffffffff) {
	        return add(downscaleToRange(range), min);
	      } else if (range === 0x1fffffffffffff) {
	        return add(Random.uint53, min);
	      } else if (range < 0x1fffffffffffff) {
	        return add(upscaleWithinU53(range), min);
	      } else if (max - 1 - min === 0x1fffffffffffff) {
	        return add(Random.uint53Full, min);
	      } else if (min === -0x20000000000000 && max === 0x20000000000000) {
	        return Random.int53Full;
	      } else if (min === -0x20000000000000 && max === 0x1fffffffffffff) {
	        return Random.int53;
	      } else if (min === -0x1fffffffffffff && max === 0x20000000000000) {
	        return add(Random.int53, 1);
	      } else if (max === 0x20000000000000) {
	        return add(upscaleWithinI53AndLoopCheck(min - 1, max - 1), 1);
	      } else {
	        return upscaleWithinI53AndLoopCheck(min, max);
	      }
	    };
	  }());
	  proto.integer = function (min, max) {
	    return Random.integer(min, max)(this.engine);
	  };

	  // [0, 1] (floating point)
	  Random.realZeroToOneInclusive = function (engine) {
	    return Random.uint53Full(engine) / 0x20000000000000;
	  };
	  proto.realZeroToOneInclusive = function () {
	    return Random.realZeroToOneInclusive(this.engine);
	  };

	  // [0, 1) (floating point)
	  Random.realZeroToOneExclusive = function (engine) {
	    return Random.uint53(engine) / 0x20000000000000;
	  };
	  proto.realZeroToOneExclusive = function () {
	    return Random.realZeroToOneExclusive(this.engine);
	  };

	  Random.real = (function () {
	    function multiply(generate, multiplier) {
	      if (multiplier === 1) {
	        return generate;
	      } else if (multiplier === 0) {
	        return function () {
	          return 0;
	        };
	      } else {
	        return function (engine) {
	          return generate(engine) * multiplier;
	        };
	      }
	    }

	    return function (left, right, inclusive) {
	      if (!isFinite(left)) {
	        throw new RangeError("Expected left to be a finite number");
	      } else if (!isFinite(right)) {
	        throw new RangeError("Expected right to be a finite number");
	      }
	      return add(
	        multiply(
	          inclusive ? Random.realZeroToOneInclusive : Random.realZeroToOneExclusive,
	          right - left),
	        left);
	    };
	  }());
	  proto.real = function (min, max, inclusive) {
	    return Random.real(min, max, inclusive)(this.engine);
	  };

	  Random.bool = (function () {
	    function isLeastBitTrue(engine) {
	      return (engine() & 1) === 1;
	    }

	    function lessThan(generate, value) {
	      return function (engine) {
	        return generate(engine) < value;
	      };
	    }

	    function probability(percentage) {
	      if (percentage <= 0) {
	        return returnValue(false);
	      } else if (percentage >= 1) {
	        return returnValue(true);
	      } else {
	        var scaled = percentage * 0x100000000;
	        if (scaled % 1 === 0) {
	          return lessThan(Random.int32, (scaled - 0x80000000) | 0);
	        } else {
	          return lessThan(Random.uint53, Math.round(percentage * 0x20000000000000));
	        }
	      }
	    }

	    return function (numerator, denominator) {
	      if (denominator == null) {
	        if (numerator == null) {
	          return isLeastBitTrue;
	        }
	        return probability(numerator);
	      } else {
	        if (numerator <= 0) {
	          return returnValue(false);
	        } else if (numerator >= denominator) {
	          return returnValue(true);
	        }
	        return lessThan(Random.integer(0, denominator - 1), numerator);
	      }
	    };
	  }());
	  proto.bool = function (numerator, denominator) {
	    return Random.bool(numerator, denominator)(this.engine);
	  };

	  function toInteger(value) {
	    var number = +value;
	    if (number < 0) {
	      return Math.ceil(number);
	    } else {
	      return Math.floor(number);
	    }
	  }

	  function convertSliceArgument(value, length) {
	    if (value < 0) {
	      return Math.max(value + length, 0);
	    } else {
	      return Math.min(value, length);
	    }
	  }
	  Random.pick = function (engine, array, begin, end) {
	    var length = array.length;
	    var start = begin == null ? 0 : convertSliceArgument(toInteger(begin), length);
	    var finish = end === void 0 ? length : convertSliceArgument(toInteger(end), length);
	    if (start >= finish) {
	      return void 0;
	    }
	    var distribution = Random.integer(start, finish - 1);
	    return array[distribution(engine)];
	  };
	  proto.pick = function (array, begin, end) {
	    return Random.pick(this.engine, array, begin, end);
	  };

	  function returnUndefined() {
	    return void 0;
	  }
	  var slice = Array.prototype.slice;
	  Random.picker = function (array, begin, end) {
	    var clone = slice.call(array, begin, end);
	    if (!clone.length) {
	      return returnUndefined;
	    }
	    var distribution = Random.integer(0, clone.length - 1);
	    return function (engine) {
	      return clone[distribution(engine)];
	    };
	  };

	  Random.shuffle = function (engine, array, downTo) {
	    var length = array.length;
	    if (length) {
	      if (downTo == null) {
	        downTo = 0;
	      }
	      for (var i = (length - 1) >>> 0; i > downTo; --i) {
	        var distribution = Random.integer(0, i);
	        var j = distribution(engine);
	        if (i !== j) {
	          var tmp = array[i];
	          array[i] = array[j];
	          array[j] = tmp;
	        }
	      }
	    }
	    return array;
	  };
	  proto.shuffle = function (array) {
	    return Random.shuffle(this.engine, array);
	  };

	  Random.sample = function (engine, population, sampleSize) {
	    if (sampleSize < 0 || sampleSize > population.length || !isFinite(sampleSize)) {
	      throw new RangeError("Expected sampleSize to be within 0 and the length of the population");
	    }

	    if (sampleSize === 0) {
	      return [];
	    }

	    var clone = slice.call(population);
	    var length = clone.length;
	    if (length === sampleSize) {
	      return Random.shuffle(engine, clone, 0);
	    }
	    var tailLength = length - sampleSize;
	    return Random.shuffle(engine, clone, tailLength - 1).slice(tailLength);
	  };
	  proto.sample = function (population, sampleSize) {
	    return Random.sample(this.engine, population, sampleSize);
	  };

	  Random.die = function (sideCount) {
	    return Random.integer(1, sideCount);
	  };
	  proto.die = function (sideCount) {
	    return Random.die(sideCount)(this.engine);
	  };

	  Random.dice = function (sideCount, dieCount) {
	    var distribution = Random.die(sideCount);
	    return function (engine) {
	      var result = [];
	      result.length = dieCount;
	      for (var i = 0; i < dieCount; ++i) {
	        result[i] = distribution(engine);
	      }
	      return result;
	    };
	  };
	  proto.dice = function (sideCount, dieCount) {
	    return Random.dice(sideCount, dieCount)(this.engine);
	  };

	  // http://en.wikipedia.org/wiki/Universally_unique_identifier
	  Random.uuid4 = (function () {
	    function zeroPad(string, zeroCount) {
	      return stringRepeat("0", zeroCount - string.length) + string;
	    }

	    return function (engine) {
	      var a = engine() >>> 0;
	      var b = engine() | 0;
	      var c = engine() | 0;
	      var d = engine() >>> 0;

	      return (
	        zeroPad(a.toString(16), 8) +
	        "-" +
	        zeroPad((b & 0xffff).toString(16), 4) +
	        "-" +
	        zeroPad((((b >> 4) & 0x0fff) | 0x4000).toString(16), 4) +
	        "-" +
	        zeroPad(((c & 0x3fff) | 0x8000).toString(16), 4) +
	        "-" +
	        zeroPad(((c >> 4) & 0xffff).toString(16), 4) +
	        zeroPad(d.toString(16), 8));
	    };
	  }());
	  proto.uuid4 = function () {
	    return Random.uuid4(this.engine);
	  };

	  Random.string = (function () {
	    // has 2**x chars, for faster uniform distribution
	    var DEFAULT_STRING_POOL = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-";

	    return function (pool) {
	      if (pool == null) {
	        pool = DEFAULT_STRING_POOL;
	      }

	      var length = pool.length;
	      if (!length) {
	        throw new Error("Expected pool not to be an empty string");
	      }

	      var distribution = Random.integer(0, length - 1);
	      return function (engine, length) {
	        var result = "";
	        for (var i = 0; i < length; ++i) {
	          var j = distribution(engine);
	          result += pool.charAt(j);
	        }
	        return result;
	      };
	    };
	  }());
	  proto.string = function (length, pool) {
	    return Random.string(pool)(this.engine, length);
	  };

	  Random.hex = (function () {
	    var LOWER_HEX_POOL = "0123456789abcdef";
	    var lowerHex = Random.string(LOWER_HEX_POOL);
	    var upperHex = Random.string(LOWER_HEX_POOL.toUpperCase());

	    return function (upper) {
	      if (upper) {
	        return upperHex;
	      } else {
	        return lowerHex;
	      }
	    };
	  }());
	  proto.hex = function (length, upper) {
	    return Random.hex(upper)(this.engine, length);
	  };

	  Random.date = function (start, end) {
	    if (!(start instanceof Date)) {
	      throw new TypeError("Expected start to be a Date, got " + typeof start);
	    } else if (!(end instanceof Date)) {
	      throw new TypeError("Expected end to be a Date, got " + typeof end);
	    }
	    var distribution = Random.integer(start.getTime(), end.getTime());
	    return function (engine) {
	      return new Date(distribution(engine));
	    };
	  };
	  proto.date = function (start, end) {
	    return Random.date(start, end)(this.engine);
	  };

	  if (true) {
	    !(__WEBPACK_AMD_DEFINE_RESULT__ = function () {
	      return Random;
	    }.call(exports, __webpack_require__, exports, module), __WEBPACK_AMD_DEFINE_RESULT__ !== undefined && (module.exports = __WEBPACK_AMD_DEFINE_RESULT__));
	  } else if (typeof module !== "undefined" && typeof require === "function") {
	    module.exports = Random;
	  } else {
	    (function () {
	      var oldGlobal = root[GLOBAL_KEY];
	      Random.noConflict = function () {
	        root[GLOBAL_KEY] = oldGlobal;
	        return this;
	      };
	    }());
	    root[GLOBAL_KEY] = Random;
	  }
	}(this));

/***/ }
/******/ ]);
