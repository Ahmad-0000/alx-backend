import { createQueue } from 'kue';


const jobData = {
  phoneNumber: '0119436789',
  message: 'Hello'
};
const push_notification_code = createQueue();
const job = push_notification_code.create('job', jobData);

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

job.save(function (error) {
  if (!error) {
    console.log('Notification job created: ', job.id);
  }
});
