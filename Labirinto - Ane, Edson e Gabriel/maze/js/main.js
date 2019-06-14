//import GenerateMaze from './generate_mazess';

$(() => {
  const canvasEl = document.getElementsByTagName("canvas")[0];
  let width = 24;
  let height = 14;
  canvasEl.height = height * 10 + 30;
  canvasEl.width = width * 10 + 30;

  const clickName = [ "Dijkstra"];

  const disableAllBtns = () => {
    clickName.concat(["maze-regen"]).forEach(className => {
      $(`.${className}`).prop("disabled", true);
      $(`.${className}-recent`).unbind("mouseenter mouseleave");
    });
  };

  const enableAllBtns = () => {
    clickName.concat(["maze-regen"]).forEach(className => {
      $(`.${className}`).prop("disabled", false);
      $(`.${className}-recent`).mouseenter(() => {
        handleHover(`${className}`);
      }).mouseleave(() => {
        handleHover(lastAction);
      });
    });
  };

  const maze = new GenerateMaze(canvasEl, width, height, enableAllBtns);
  disableAllBtns();
  maze.generate(canvasEl);

  $(".prims").removeClass("hidden");
  let lastAction = null;

  const handleClick = searchType => {
    maze.quickRegen();
    maze.displayVisited(searchType);

    $(".info").addClass("hidden");
    $(`.${searchType}`).removeClass("hidden");
    $(`.${searchType}-recent`).removeClass("hidden");

    lastAction = searchType;
  };

  const handleHover = searchType => {
    maze.quickRegen();
    maze.quickDisplay(searchType);
    $(".info").addClass("hidden");
    $(`.${searchType}`).removeClass("hidden");
  };

  $(".maze-regen").on("click", () => {
    disableAllBtns();
    maze.generate(canvasEl);
    $(".info").addClass("hidden");
    $(".recenttrav").addClass("hidden");
    $(".prims").removeClass("hidden");
  });

  $(".search-btns").on("click", (event) => {
    if (clickName.includes(event.target.className)) {
      disableAllBtns();
      handleClick(event.target.className);
    }
  });
});
