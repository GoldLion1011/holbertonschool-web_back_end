// an instance of express and a route for GET /.

const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

const port = 7865;
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

app.get('/cart/:id([0-9]*)', (req, res) => {
  const cartId = req.params.id;

  if (isNaN(cartId)) {
    res.status(400).send('Invalid cart ID. Cart ID must be a number.');
  } else {
    res.send(`Payment methods for cart ${cartId}`);
  }
});

module.exports = app;
