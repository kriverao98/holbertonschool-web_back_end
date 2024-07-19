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

  // Abstract method to ensure subclasses implement evacuationWarningMessage
  // eslint-disable-next-line class-methods-use-this
  evacuationWarningMessage() {
    throw new Error('evacuationWarningMessage must be implemented by subclass');
  }
}
