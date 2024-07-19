export default class Airport {
  constructor(name, code) {
    if (typeof name !== 'string') {
      throw new TypeError('name should be a string');
    }
    if (typeof code !== 'string') {
      throw new TypeError('code should be a string');
    }
    this._name = name;
    this._code = code;
  }

  // Getter for name
  get name() {
    return this._name;
  }

  // Getter for code
  get code() {
    return this._code;
  }

  // Override toString method
  toString() {
    return `[object ${this._code}]`;
  }
}
