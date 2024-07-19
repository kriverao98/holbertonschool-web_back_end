const cloneSymbol = Symbol('clone');

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  [cloneSymbol]() {
    return new this.constructor(this._brand, this._motor, this._color);
  }

  cloneCar() {
    return this[cloneSymbol]();
  }

  // Getters for each attribute
  get brand() {
    return this._brand;
  }

  get motor() {
    return this._motor;
  }

  get color() {
    return this._color;
  }
}
