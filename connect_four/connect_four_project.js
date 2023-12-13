// project overview

// start, alert for player names 1 and 2
// match the screen to look like project overview
// player picks column and it drops to the bottom
// player wins when 4 in a row, or catsgame
// reset button to start over

alert('Welcome to Connect Four! Player One will be red, and Player Two will be blue.')
var playerOneName = prompt('Player One (red), please enter your name: ')
var playerTwoName = prompt('Player Two (blue), please enter your name: ')

// variables
// Player turn states
var playerOneTurn = true
var playerTwoTurn = false

// column states
var colOne = 6
var colTwo = 6
var colThree = 6
var colFour = 6
var colFive = 6
var colSix = 6
var colSeven = 6

var circle = $('.circle')

// on click
$('.col1').on('click', function() {
    if (playerOneTurn === true) {
        $('.col1').eq(colOne-1).addClass('turnRed')
        colOne--
    } else if (playerTwoTurn === true) {
        $('.col1').eq(colOne-1).addClass('turnBlue')
        colOne--
    }
    playerTurns()
    turnPrompt()
})

$('.col2').on('click', function() {
    if (playerOneTurn === true) {
        $('.col2').eq(colTwo-1).addClass('turnRed')
        colTwo--
    } else if (playerTwoTurn === true) {
        $('.col2').eq(colTwo-1).addClass('turnBlue')
        colTwo--
    }
    playerTurns()
    turnPrompt()
})

$('.col3').on('click', function() {
    if (playerOneTurn === true) {
        $('.col3').eq(colThree-1).addClass('turnRed')
        colThree--
    } else if (playerTwoTurn === true) {
        $('.col3').eq(colThree-1).addClass('turnBlue')
        colThree--
    }
    playerTurns()
    turnPrompt()
})

$('.col4').on('click', function() {
    if (playerOneTurn === true) {
        $('.col4').eq(colFour-1).addClass('turnRed')
        colFour--
    } else if (playerTwoTurn === true) {
        $('.col4').eq(colFour-1).addClass('turnBlue')
        colFour--
    }
    playerTurns()
    turnPrompt()
})

$('.col5').on('click', function() {
    if (playerOneTurn === true) {
        $('.col5').eq(colFive-1).addClass('turnRed')
        colFive--
    } else if (playerTwoTurn === true) {
        $('.col5').eq(colFive-1).addClass('turnBlue')
        colFive--
    }
    playerTurns()
    turnPrompt()
})

$('.col6').on('click', function() {
    if (playerOneTurn === true) {
        $('.col6').eq(colSix-1).addClass('turnRed')
        colSix--
    } else if (playerTwoTurn === true) {
        $('.col6').eq(colSix-1).addClass('turnBlue')
        colSix--
    }
    playerTurns()
    turnPrompt()
})

$('.col7').on('click', function() {
    if (playerOneTurn === true) {
        $('.col7').eq(colSeven-1).addClass('turnRed')
        colSeven--
    } else if (playerTwoTurn === true) {
        $('.col7').eq(colSeven-1).addClass('turnBlue')
        colSeven--
    }
    playerTurns()
    turnPrompt()
})

// other functions
function playerTurns() {
    if (playerOneTurn === true) {
        playerOneTurn = false
        playerTwoTurn = true
    } else if (playerTwoTurn === true) {
        playerTwoTurn = false
        playerOneTurn = true
    }
}

function turnPrompt() {
    if (playerOneTurn === true) {
        $('#turnPrompt').text(playerOneName + ' (Red)\'s turn. (Click a column to drop a piece.)')
    } else if (playerTwoTurn === true) {
        $('#turnPrompt').text(playerTwoName + ' (Blue)\'s turn. (Click a column to drop a piece.)')
    }
}


function checkWin() {
    // check if board full with no winner
    if (colOne <= 0 && colTwo <= 0 && colThree <= 0 && colFour <= 0 && colFive <= 0 && colSix <= 0 && colSeven <= 0) {
        alert('Catsgame! No winner, refresh webpage to play again.')
    }
    // check if 4 in a row horizontally
    // check if 4 in a row vertically
    // check if 4 in a row diagonally
}
