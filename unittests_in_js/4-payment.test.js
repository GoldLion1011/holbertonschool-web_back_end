// Test suite for Sinon spy

const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('checks if the math used in sendPaymentRequestToApi(100, 20) is the same as Utils.calculateNumber("SUM", 100, 20)', () => {
    const calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const consoleSpy = sinon.spy(console, 'log');

    const res = sendPaymentRequestToApi(100, 20);

    expect(calculateNumberStub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(consoleSpy.calledWithExactly('The total is: 10')).to.be.true;
    expect(Utils.calculateNumber('SUM', 100, 20)).to.equal(10);
    expect(res).to.equal(10);

    calculateNumberStub.restore();
    consoleSpy.restore();
  });
});
