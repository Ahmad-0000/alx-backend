const redis = require('redis');

const client = redis.createClient();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));

client.hset('ALX', 'Portland', '50', redis.print);
client.hset('ALX', 'Seattle', '80', redis.print);
client.hset('ALX', 'New York', '20', redis.print);
client.hset('ALX', 'Bogota', '20', redis.print);
client.hset('ALX', 'Cali', '40', redis.print);
client.hset('ALX', 'Paris', '2', redis.print);

client.hgetall('ALX', (error, response) => {
  if (error) {
    console.error(error);
  } else if (response) {
    console.log(response);
  }
});
