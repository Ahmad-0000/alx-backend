import { createQueue } from 'kue';

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  for (const jobData of jobs) {
    const job = queue.create('8-job', jobData);
    job.on('enqueue', () => {
      console.log('Notification job created: ', job.id);
    });

   job.on('completed', () => {
     console.log(`Notification job ${job.id} completed`)
   });

   job.on('failed', (error) => {
     console.log(`Notification job ${job.id} failed: ${error}`);
   });

   job.on('progress', (progress) => {
     console.log(`Notification job ${job.id} ${progress}% complete`);
   });
   job.save();
  }
}

export default createPushNotificationsJobs;
