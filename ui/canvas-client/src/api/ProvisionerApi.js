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

import ApiClient from '../ApiClient';
import AppSchemasProvisionerProjectPackageProjectPackageUpdate from '../model/AppSchemasProvisionerProjectPackageProjectPackageUpdate';
import HTTPValidationError from '../model/HTTPValidationError';

/**
 * Provisioner service.
 * @module api/ProvisionerApi
 * @version 0.1.0
 */
export default class ProvisionerApi {
  /**
   * Constructs a new ProvisionerApi.
   * @alias module:api/ProvisionerApi
   * @class
   * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
   * default to {@link module:ApiClient#instance} if unspecified.
   */
  constructor(apiClient) {
    this.apiClient = apiClient || ApiClient.instance;
  }

  /**
   * Callback function to receive the result of the updateProjectPackageProvisionerProjectsProjectIdPackagesPackageIdPatch operation.
   * @callback module:api/ProvisionerApi~updateProjectPackageProvisionerProjectsProjectIdPackagesPackageIdPatchCallback
   * @param {String} error Error message, if any.
   * @param {Object} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * Update Project Package
   * @param {String} projectId The ID of the project
   * @param {String} packageId The ID of the package
   * @param {String} xCanvasToken
   * @param {module:model/AppSchemasProvisionerProjectPackageProjectPackageUpdate} appSchemasProvisionerProjectPackageProjectPackageUpdate
   * @param {module:api/ProvisionerApi~updateProjectPackageProvisionerProjectsProjectIdPackagesPackageIdPatchCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link Object}
   */
  updateProjectPackageProvisionerProjectsProjectIdPackagesPackageIdPatch(
    projectId,
    packageId,
    xCanvasToken,
    appSchemasProvisionerProjectPackageProjectPackageUpdate,
    callback
  ) {
    let postBody = appSchemasProvisionerProjectPackageProjectPackageUpdate;
    // verify the required parameter 'projectId' is set
    if (projectId === undefined || projectId === null) {
      throw new Error(
        "Missing the required parameter 'projectId' when calling updateProjectPackageProvisionerProjectsProjectIdPackagesPackageIdPatch"
      );
    }
    // verify the required parameter 'packageId' is set
    if (packageId === undefined || packageId === null) {
      throw new Error(
        "Missing the required parameter 'packageId' when calling updateProjectPackageProvisionerProjectsProjectIdPackagesPackageIdPatch"
      );
    }
    // verify the required parameter 'xCanvasToken' is set
    if (xCanvasToken === undefined || xCanvasToken === null) {
      throw new Error(
        "Missing the required parameter 'xCanvasToken' when calling updateProjectPackageProvisionerProjectsProjectIdPackagesPackageIdPatch"
      );
    }
    // verify the required parameter 'appSchemasProvisionerProjectPackageProjectPackageUpdate' is set
    if (
      appSchemasProvisionerProjectPackageProjectPackageUpdate === undefined ||
      appSchemasProvisionerProjectPackageProjectPackageUpdate === null
    ) {
      throw new Error(
        "Missing the required parameter 'appSchemasProvisionerProjectPackageProjectPackageUpdate' when calling updateProjectPackageProvisionerProjectsProjectIdPackagesPackageIdPatch"
      );
    }

    let pathParams = {
      project_id: projectId,
      package_id: packageId,
    };
    let queryParams = {};
    let headerParams = {
      'x-canvas-token': xCanvasToken,
    };
    let formParams = {};

    let authNames = [];
    let contentTypes = ['application/json'];
    let accepts = ['application/json'];
    let returnType = Object;
    return this.apiClient.callApi(
      '/provisioner/projects/{project_id}/packages/{package_id}',
      'PATCH',
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback
    );
  }
}
