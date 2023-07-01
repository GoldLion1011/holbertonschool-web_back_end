// 

const { expect } = require('chai');
const request = require('request');
const app = require('./api');

describe('API test', () => {
  it('Tests the GET / route', (done) => {
    const port = 7865;
    const url = `http://localhost:${port}`;

    request(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});
