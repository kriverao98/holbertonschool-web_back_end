export default class Building {
  constructor(sqft) {
  // Type checks
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft should be a number');
    }

    this._sqft = sqft;
  }

  // Getter for sqft
  get sqft() {
    return this._sqft;
  }

  // Method to ensure subclasses implement evacuationWarningMessage
  evacuationWarningMessage() {
    if (this.constructor === Building) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    throw new Error('evacuationWarningMessage must be implemented by subclass');
  }
}
