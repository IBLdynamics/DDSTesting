<link rel="stylesheet" type="text/css" href="//jsxgraph.org/distrib/jsxgraph.css" />
<script type="text/javascript" src="//jsxgraph.org/distrib/jsxgraphcore.js"></script>
<div id="box" class="jxgbox" style="width:600px; height:600px;"></div>
<form><textarea id="input" rows=7 cols=35 wrap="off" >
function f(x) {
   return Math.cos(x)*p.Y();
}
c = plot(f);
// Derivative:
g = JXG.Math.Numerics.D(f);
plot(g,{strokecolor:'black', dash:1});
</textarea> <br>
<input type="button" value="plot" onClick="doIt()"> 
<input type="button" value="clear all" onClick="board=clearAll(board)"> 
</form>
var board = JXG.JSXGraph.initBoard('box', {boundingbox:[-5,8,8,-5], axis:true});

// Macro function plotter
function addCurve(board, func, atts) {
    var f = board.create('functiongraph', [func], atts);
    return f;
}
        
// Simplified plotting of function
function plot(func, atts) {
   if (atts==null) {
      return addCurve(board, func, {strokewidth:2});
   } else {
      return addCurve(board, func, atts);
   }    
}

// Free point
var p = board.create('point', [1,1], {style:6, name:'p'}); 

// Usage of the macro
function doIt() {
    eval(document.getElementById('input').value); 
}

function clearAll(board) {
    JXG.JSXGraph.freeBoard(board);
    board = JXG.JSXGraph.initBoard('box', {boundingbox:[-5,8,8,-5], axis:true});
    p = board.create('point', [3,-4], {style:6, name:'p'}); 
    return board;
}