// brand (String)
// motor (String)
// color (String)
// Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
// Add a method named cloneCar. This method should return a new object of the class.
// Hint: Symbols in ES6

class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  get brand() {
    return this._brand;
  }

  get motor() {
    return this._motor;
  }

  get color() {
    return this._color;
  }

  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    return new this.constructor[Symbol.species]();
  }
}

export default Car;
