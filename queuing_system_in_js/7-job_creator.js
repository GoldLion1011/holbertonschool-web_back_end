// Still more fun with Kue :p

const kue = require('kue');
const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

jobs.forEach((job) => {
  const jobName = 'push_notification_code_2';
  const newJob = queue.create(jobName, job).save((error) => {
    if (!error) console.log(`Notification job created: ${newJob.id}`);
  });
  newJob.on('complete', () => console.log(`Notification job ${newJob.id} completed`));
  newJob.on('failed', (error) => console.log(`Notification job ${newJob.id} failed: ${error}`));
  newJob.on('progress', (progress) => console.log(`Notification job ${newJob.id} ${progress}% complete`));
}
);

// jobs.forEach((jobData) => {
//   const job = queue.create('push_notification_code_2', jobData)
//     .save(function (err) {
//       if (!err) {
//         console.log(`Notification job created: ${job.id}`);
//       }
//     });

//   job.on('complete', function () {
//     console.log(`Notification job ${job.id} completed`);
//   });

//   job.on('failed', function (err) {
//     console.log(`Notification job ${job.id} failed: ${err}`);
//   });

//   job.on('progress', function (progress) {
//     console.log(`Notification job ${job.id} ${progress}% complete`);
//   });
// });

// console.log('Creating notification jobs...');