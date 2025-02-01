import { createClient } from 'redis';
import kue from 'kue';
import { promisify } from 'util';
import express from 'express';

const client = createClient();
const asyncGet = promisify(client.get).bind(client);
let reservationEnabled = true;

function reserveSeat(number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats () {
  return await asyncGet('available_seats');
}

reserveSeat(50);

const queue = kue.createQueue();
const processorQueue = kue.createQueue();

const server = express();

server.get('/available_seats', async (req, res) => {
  res.json({numberOfAvailableSeats: await getCurrentAvailableSeats()});
});

server.get('/reserve_seat', (req, res) => {
  if (reservationEnabled === false) {
    res.json({ "status": "Reservation are blocked" });
  } else {
    const job = queue.create('reserve_seat').save((error) => {
      if (!error) {
        res.json({ "status": "Reservation in process" });
      } else {
        res.json({ "status": "Reservation failed" });
      }
    });
    job.on('complete', (result) => {
      console.log(`Seat reservation job ${job.id} completed`);
    });
    job.on('failed', (errorMessage) => {
      console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
    });
  }
});

server.get('/process', async (req, res) => {
  await processorQueue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    if (+availableSeats - 1 === 0) {
      reservationEnabled = false;
    } else if (+availableSeats - 1 < 0) {
      done(new Error('Not enough seats available'));
    }
    reserveSeat(availableSeats - 1);
    done();
  });
  res.json({ "status": "Queue processing" });
});

server.listen(1245);
