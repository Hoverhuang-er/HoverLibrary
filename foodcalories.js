var chalk = require('chalk');
var prompt = require('sync-prompt').prompt;

var gender; 
var weight = 0;
var food = [];
var totalCals = [];
var sumCals = 0;

cals = parseInt(cals)

gender = prompt('(m)ale or (f)emale? ')
weight = prompt('Weight in pounds: ')

weight = parseInt(weight)

var input

while(input != 'q'){
  var meal = prompt('What did you eat? ')
  var cals = prompt('How many calories was it? ')
  cals = parseInt(cals)
  food.push(meal)
//  console.log(food)
//  console.log(cals)
  totalCals.push(cals)

 input = prompt('Press any key to enter another food or (q)uit: ')
}

console.log('Here is all the food you ate: ' + chalk.red(food))
//console.log(totalCals)
var i
for(  i = 0; i < totalCals.length; i++){
  sumCals += totalCals[i]
}

console.log('You consumed ' + chalk.red(sumCals) + ' calories')

var gain
gain = parseFloat(gain)
if(gender === 'm' && sumCals >= 4000){
  gain = (sumCals/4000)
  }else if(gender === 'f' && sumCals >= 3000){
  gain = (sumCals/3000)
  }


console.log('You gained ' + chalk.red(gain.toFixed(1)) + ' pounds. You now weigh ' + chalk.red((weight+gain).toFixed(1)))
