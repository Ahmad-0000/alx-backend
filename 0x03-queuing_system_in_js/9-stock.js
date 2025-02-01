import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const redisClient = createClient();
const asyncHGetAll = promisify(redisClient.hgetall).bind(redisClient);
const app = express();
const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  }
];

function getItemById(id) {
  return listProducts.filter((product) => product.id === id)[0];
}

app.get('/list_products', (req, res) => {
  const resArray = [];
  for (const product of listProducts) {
    const obj = {};
    obj.itemId = product.id;
    obj.itemName = product.name;
    obj.price = product.price;
    obj.initialAvailableQuantity = product.stock;
    resArray.push(obj);
  }
  res.json(resArray);
});

function reserveStockById (itemId, stock) {
  for (const k in stock) {
    if (stock.hasOwnProperty(k)) {
      redisClient.hset(`item.${itemId}`, k, stock[k], () => {});
    }
  }
}

async function getCurrentReservedStockById (itemId) {
  return await asyncHGetAll(`item.${itemId}`);
}



for (const product of listProducts) {
  const obj = {};
  obj.itemId = product.id;
  obj.itemName = product.name;
  obj.price = product.price;
  obj.initialAvailableQuantity = product.stock;
  reserveStockById(obj.itemId, obj);
}

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const value = await getCurrentReservedStockById(itemId);
  if (!value) {
    res.json({"status": "Product not found"});
  } else {
    res.json(value);
  }
});

app.get('/reserve_product/:itemId', (req, res) => {
  const itemId = req.params.itemId;
  const item = listProducts.filter((item) => item.id === +itemId)[0];
  if (!item) {
    res.json({"status":"Product not found"});
  } else {
    if (item.stock > 0) {
      reserveStockById(itemId, item);
      res.json({"status":"Reservation confirmed","itemId": itemId});
    } else {
      res.json({"status":"Reservation confirmed","itemId": itemId});
    }
  }
});

app.listen(1245);
