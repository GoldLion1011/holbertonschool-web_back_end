// Do not call list in Kue

const kue = require('kue');
const queue = kue.createQueue({
  concurrency: 2
});

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
];

const blacklistedNumbers = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    done(error);
    return;
  }

  job.progress(50);

  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
};

jobs.forEach((jobData) => {
  const job = queue.create('push_notification_code_2', jobData).save(function (err) {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

  job.on('complete', function () {
    console.log(`Notification job ${job.id} completed`);
  });

  job.on('failed', function (err) {
    console.log(`Notification job ${job.id} failed: ${err}`);
  });

  job.on('progress', function (progress) {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });

  queue.process('push_notification_code_2', function (job, done) {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
  });
});

console.log('Creating notification jobs...');
