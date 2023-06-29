// Rounds two numbers and returns a value based on type

const calculateNumber = (type, a, b) => { 

  if (isNaN(a) || isNaN(b)) throw TypeError('Parameters must be numbers');

  if (type === 'SUM')
    return Math.round(a) + Math.round(b);
  if (type === 'SUBTRACT')
    return Math.round(a) - Math.round(b);
  if (type === 'DIVIDE') {
    if (Math.round(b) === 0) return 'Error';
    return Math.round(a) / Math.round(b);
  }
};

module.exports = calculateNumber;
