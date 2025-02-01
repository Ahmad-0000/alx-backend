import { createQueue } from 'kue';

const process_notification_code_2 = createQueue();
const blackList = ['4153518780', '4153518781'];

const job = process_notification_code_2.process('7-job', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
  

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  /* job.on('progress', (progress) => {
    console.log(`${progress}% complete`);
  });

  job.on('failed', (error) => {
    console.log(error);
  }); */

  if (blackList.indexOf(phoneNumber) !== -1) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
  
