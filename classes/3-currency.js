class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }

  set name(name) {
    this._name = name;
  }

  set code(code) {
    this._code = code;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}

export default Currency;
