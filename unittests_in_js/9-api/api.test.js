// Testing using Chai and Mocha

const { expect } = require('chai');
const request = require('request');

describe('API test', () => {
  it('Tests the GET / route', (done) => {
    request('http://localhost:7865', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should return correct status code when :id is a number', (done) => {
    request('http://localhost:7865/cart/12', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return 404 status code when :id is NaN', (done) => {
    request('http://localhost:7865/cart/anything', (error, response, body) => {
      expect(response.statusCode).to.equal(400);
      done();
    });
  });
});
