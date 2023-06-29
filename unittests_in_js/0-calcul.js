// Rounds two numbers and returns the sum
// Parameters: a, b
// Return: sum of a and b rounded

const calculateNumber = (a, b) => { Math.round(a) + Math.round(b);
  if (isNaN(a) || isNaN(b)) throw TypeError('Parameters must be numbers');
  return calculateNumber(a, b);
};

module.exports = calculateNumber;
