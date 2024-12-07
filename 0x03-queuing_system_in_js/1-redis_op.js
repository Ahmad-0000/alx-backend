const redis = require('redis');

const client = redis.createClient();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue (schoolName) {
  const value = client.get(schoolName, (error, replay) => {
    if (error) {
      console.log(error);
    } else {
      console.log(replay);
    }
  });
}

displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
