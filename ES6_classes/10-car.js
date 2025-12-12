const cloneSymbol = Symbol('clone');

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const Cls = this.constructor;
    return new Cls(this._brand, this._motor, this._color);
  }
}