#!/usr/bin/node
// Class Rectangle That Defines a rectangle & defines 2 args Width & height

module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }
};
