// Rounds two numbers and returns the sum
// Parameters: a, b
// Return: sum of a and b rounded

const calculateNumber = (a, b) => { 
  if (isNaN(a) || isNaN(b)) throw TypeError('Parameters must be numbers');
  return Math.round(a) + Math.round(b);
};

module.exports = calculateNumber;
