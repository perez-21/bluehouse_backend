function hasValuesFromArray(someSet, arr) {
  let is = true;
  arr.forEach((element) => {
    if (!someSet.has(element)) {
      is = false;
    }
  });
  return is;
}

export default hasValuesFromArray;
