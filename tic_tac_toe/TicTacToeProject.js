// Grabbing table cells
var button = document.querySelector('#button');
var cells = document.querySelectorAll('td');

// Event logic
// Clearing the board
function clearBoard() { 
    for (let i = 0; i < cells.length; i++) {
        cells[i].textContent = '';
    }
}
button.addEventListener('click', clearBoard);

// Changing the marker
function changeCell() {
    if (this.textContent === '') {
        this.textContent = 'X';
    }   else if (this.textContent === 'X') {
        this.textContent = 'O';
    }   else {
        this.textContent = '';
    }
}

for (let i = 0; i < cells.length; i++) {
    cells[i].addEventListener('click', changeCell)
}
