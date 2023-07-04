// Creating an object with job data using Kue

const kue = require('kue');
const queue = kue.createQueue();

// Create an object with job data
const jobData = {
  phoneNumber: '1234567890',
  message: "Hello, we have been trying to reach you regarding your car's extended warranty!",
};

// Create the queue named push_notification_code
const pushNotificationQueue = queue.create('push_notification_code', jobData);

// Save the job to the queue
pushNotificationQueue.save(function (error) {
  if (error) {
    console.error('Failed to save job:', error);
  } else {
    console.log(`Notification job created: ${pushNotificationQueue.id}`);
  }

  // Close the Redis connection and exit the process
  // queue.shutdown(5000, function (err) {
  //   console.log('Notification job completed');
  //   process.exit(0);
  // });
});
