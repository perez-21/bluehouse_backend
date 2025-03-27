function createInt8TypedArray(length, position, value) {
  if (position > length) {
    throw Error('Position outside range');
  }
  const int8view = new Int8Array(new ArrayBuffer(length));
  int8view[position] = value;

  return int8view.buffer;
}

export default createInt8TypedArray;
