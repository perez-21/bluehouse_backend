function cleanSet(aSet, startString) {
  const filteredStrings = [];
  aSet.forEach((element) => {
    if (element.startsWith(startString)) {
      let endString = element.slice(startString.length);
      filteredStrings.push(endString);
    }
  });

  return filteredStrings.join('-');
}
export default cleanSet;
