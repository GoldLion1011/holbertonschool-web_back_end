// Deep equality & Post integration testing

const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
  const cartId = req.params.id;

  if (isNaN(cartId)) {
    res.status(404).send('Invalid cart ID. Cart ID must be a number.');
  } else {
    res.send(`Payment methods for cart ${cartId}`);
  }
});

app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

app.post('/login', (req, res) => {
  const { userName } = req.body;
  res.send(`Welcome ${userName}`);
});

const port = 7865;
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;
