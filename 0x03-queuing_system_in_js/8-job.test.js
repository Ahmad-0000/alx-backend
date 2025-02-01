import createPushNotificationsJobs from './8-job.js';
import { createQueue } from 'kue';
import { expect } from 'chai';

const queue = createQueue();

before(() => {
  queue.testMode.enter();
});

afterEach(() => {
  queue.testMode.clear();
});

after(() => {
  queue.testMode.exit();
});

it('display a error message if jobs is not an array', () => {
  try {
    createPushNotificationsJobs({'data': 'random' ,'data2': 'random'}, queue);
  } catch (error) {
    expect(error.message).to.equal('Jobs is not an array');
  }
});

it('create two new jobs to the queue', () => {
  createPushNotificationsJobs([{'data': 'random'}, {'data': 'random'}], queue);
  expect(queue.testMode.jobs.length).to.equal(2);
});
