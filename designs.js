


// When size is submitted by the user, call makeGrid()
// select submission button
const submissionButton = document.getElementById('submitButton');


submissionButton.addEventListener('click', preventDefault);
submissionButton.addEventListener('click', makeGrid);
//create rows + cols
var tr = document.createElement('tr');
var td = document.createElement('td');
// Select color input
var cellColor = document.getElementById('colorPicker');
// Select table
const gridContainer = document.getElementById('pixelCanvas');

function preventDefault(action){
	action.preventDefault();
}

function makeGrid() {
	//reset 
	gridContainer.innerHTML ='';
	// Select size input
	var rows = document.getElementById('inputHeight').value;
	var cols = document.getElementById('inputWidth').value;
	console.log('1');
   	console.log('rows' + rows);
	//create grid

	for (let x = 0; x < rows; x ++){ // creates rows
		let row = gridContainer.insertRow(x);
		for (let y = 0; y < cols; y++){ // creates cols
			// add col 
			let col = row.insertCell(y);
			// listen for click event
			col.addEventListener('mousedown', changeBckgrndColor)
		}
	}
	
}


function changeBckgrndColor(cell){
	//change color
	cell.target.style.backgroundColor = cellColor.value;
	console.log('2' + cellColor + cell);


}
