import { createQueue } from 'kue';

const queue = createQueue();
function sendNotification (phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('job', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
});
