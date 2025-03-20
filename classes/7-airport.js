class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  get code() {
    return this._code;
  }
  toString() {
    return this.code;
  }
}

export default Airport;
