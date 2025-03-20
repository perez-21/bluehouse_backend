class Building {
  constructor(sqft) {
    /*if (this.constructor === Building) {
      throw new Error("Class is of abstract type and cant' be instantiated");
    }*/

    // shouldn't abstract functions not be instantiable?
    this._sqft = sqft;

    if (
      this.evacuationWarningMessage === undefined &&
      this.constructor !== Building
    ) {
      throw new Error('evacuationWarningMessage method must be implemented');
    }
  }

  get sqft() {
    return this._sqft;
  }
}

export default Building;
