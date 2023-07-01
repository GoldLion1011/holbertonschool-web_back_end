// 

const { expect } = require('chai');
const request = require('request');
//const app = require('./api');

describe('API test', () => {
  it('Tests the GET / route', (done) => {
    request('http://localhost:7865', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});
