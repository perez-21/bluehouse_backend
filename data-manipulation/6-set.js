function setFromArray(arr) {
  let aSet = new Set();
  arr.forEach((element) => {
    aSet.add(element);
  });
  return aSet;
}

export default setFromArray;
