"use strict";

var sayHello = function() {
    return "hello";
};

// Test case
describe("sayHello.js", function() {
    it('should returns string "hello"', function() {
        expect(sayHello()).toBe("hello");
        expect(sayHello()).not.toBe("bye");
    });
});
