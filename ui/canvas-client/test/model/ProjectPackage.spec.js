/**
 * Canvas API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd() + '/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd() + '/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.CanvasApi);
  }
})(this, function (expect, CanvasApi) {
  'use strict';

  var instance;

  beforeEach(function () {
    instance = new CanvasApi.ProjectPackage();
  });

  var getProperty = function (object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function') return object[getter]();
    else return object[property];
  };

  var setProperty = function (object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function') object[setter](value);
    else object[property] = value;
  };

  describe('ProjectPackage', function () {
    it('should create an instance of ProjectPackage', function () {
      // uncomment below and update the code to test ProjectPackage
      //var instance = new CanvasApi.ProjectPackage();
      //expect(instance).to.be.a(CanvasApi.ProjectPackage);
    });

    it('should have the property name (base name: "name")', function () {
      // uncomment below and update the code to test the property name
      //var instance = new CanvasApi.ProjectPackage();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function () {
      // uncomment below and update the code to test the property type
      //var instance = new CanvasApi.ProjectPackage();
      //expect(instance).to.be();
    });

    it('should have the property inputs (base name: "inputs")', function () {
      // uncomment below and update the code to test the property inputs
      //var instance = new CanvasApi.ProjectPackage();
      //expect(instance).to.be();
    });

    it('should have the property outputs (base name: "outputs")', function () {
      // uncomment below and update the code to test the property outputs
      //var instance = new CanvasApi.ProjectPackage();
      //expect(instance).to.be();
    });

    it('should have the property parameters (base name: "parameters")', function () {
      // uncomment below and update the code to test the property parameters
      //var instance = new CanvasApi.ProjectPackage();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function () {
      // uncomment below and update the code to test the property id
      //var instance = new CanvasApi.ProjectPackage();
      //expect(instance).to.be();
    });

    it('should have the property projectId (base name: "project_id")', function () {
      // uncomment below and update the code to test the property projectId
      //var instance = new CanvasApi.ProjectPackage();
      //expect(instance).to.be();
    });

    it('should have the property deployStatus (base name: "deploy_status")', function () {
      // uncomment below and update the code to test the property deployStatus
      //var instance = new CanvasApi.ProjectPackage();
      //expect(instance).to.be();
    });

    it('should have the property outputData (base name: "output_data")', function () {
      // uncomment below and update the code to test the property outputData
      //var instance = new CanvasApi.ProjectPackage();
      //expect(instance).to.be();
    });

    it('should have the property parameterData (base name: "parameter_data")', function () {
      // uncomment below and update the code to test the property parameterData
      //var instance = new CanvasApi.ProjectPackage();
      //expect(instance).to.be();
    });
  });
});
