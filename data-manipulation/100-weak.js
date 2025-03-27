const weakMap = new WeakMap();

function queryAPI(endpoint) {
  if (weakMap.has(endpoint)) {
    if (weakMap.get(endpoint) >= 5) {
      throw Error('Endpoint load is high');
    }
    weakMap.set(endpoint, weakMap.get(endpoint) + 1);
  } else {
    weakMap.set(endpoint, 1);
  }
}

export { weakMap, queryAPI };
