export default class Car {
  constructor(brand, motor, color) {
    this.brand = brand;
    this.motor = motor;
    this.color = color;
  }

  cloneCar() {
    return Object.assign(Object.create(Object.getPrototypeOf(this)), {
      _brand: undefined,
      _motor: undefined,
      _color: undefined,
    });
  }
}
