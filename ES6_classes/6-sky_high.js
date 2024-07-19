import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);

    // Type checks
    if (typeof floors !== 'number') {
      throw new TypeError('floors should be a number');
    }

    this._floors = floors;
  }

  // Getter for sqft
  get sqft() {
    return this._sqft;
  }

  // Getter for floors
  get floors() {
    return this._floors;
  }

  // Override the evacuationWarningMessage method
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
