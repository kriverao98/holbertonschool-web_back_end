export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number') {
      throw new TypeError('size should be a number');
    }
    if (typeof location !== 'string') {
      throw new TypeError('location should be a string');
    }
    this._size = size;
    this._location = location;
  }

  // Getter for size
  get size() {
    return this._size;
  }

  // Getter for location
  get location() {
    return this._location;
  }

  // Method to convert class instance to Number
  valueOf() {
    return this._size;
  }

  // Method to convert class instance to String
  toString() {
    return this._location;
  }
}
