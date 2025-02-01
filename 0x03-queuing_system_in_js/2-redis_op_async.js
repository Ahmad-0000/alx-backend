import { createClient, print }  from 'redis';
import { promisify } from 'util';

const client = createClient();
const asyncGet = promisify(client.get).bind(client);

client.on('connect', () => { 
  console.log('Redis client connected to the server')
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`)
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue (schoolName) {
  try {
    const value = await asyncGet(schoolName);
    console.log(value);
  } catch (error) {
    console.error(error);
  }
}

async function main () {
  await displaySchoolValue('ALX');
  await setNewSchool('ALXSanFrancisco', '100');
  await displaySchoolValue('ALXSanFrancisco');
}

main();
