# CanvasApi.PackagesApi

All URIs are relative to _http://localhost_

| Method                                                                                                                                                              | HTTP request                                                       | Description             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------- |
| [**createProjectPackageProjectsProjectIdPackagesPost**](PackagesApi.md#createProjectPackageProjectsProjectIdPackagesPost)                                           | **POST** /projects/{project_id}/packages/                          | Create Project Package  |
| [**deleteProjectPackageProjectsProjectIdPackagesPackageIdDelete**](PackagesApi.md#deleteProjectPackageProjectsProjectIdPackagesPackageIdDelete)                     | **DELETE** /projects/{project_id}/packages/{package_id}            | Delete Project Package  |
| [**deployProjectPackageProjectsProjectIdPackagesPackageIdDeployPost**](PackagesApi.md#deployProjectPackageProjectsProjectIdPackagesPackageIdDeployPost)             | **POST** /projects/{project_id}/packages/{package_id}/deploy       | Deploy Project Package  |
| [**destroyProjectPackageProjectsProjectIdPackagesPackageIdDestroyDelete**](PackagesApi.md#destroyProjectPackageProjectsProjectIdPackagesPackageIdDestroyDelete)     | **DELETE** /projects/{project_id}/packages/{package_id}/destroy    | Destroy Project Package |
| [**getProjectPackageProjectsProjectIdPackagesPackageIdGet**](PackagesApi.md#getProjectPackageProjectsProjectIdPackagesPackageIdGet)                                 | **GET** /projects/{project_id}/packages/{package_id}               | Get Project Package     |
| [**listProjectPackagesProjectsProjectIdPackagesGet**](PackagesApi.md#listProjectPackagesProjectsProjectIdPackagesGet)                                               | **GET** /projects/{project_id}/packages/                           | List Project Packages   |
| [**updateProjectPackageProjectsProjectIdPackagesPackageIdPatch**](PackagesApi.md#updateProjectPackageProjectsProjectIdPackagesPackageIdPatch)                       | **PATCH** /projects/{project_id}/packages/{package_id}             | Update Project Package  |
| [**updateProjectPackageProvisionerProjectsProjectIdPackagesPackageIdPatch**](PackagesApi.md#updateProjectPackageProvisionerProjectsProjectIdPackagesPackageIdPatch) | **PATCH** /provisioner/projects/{project_id}/packages/{package_id} | Update Project Package  |

## createProjectPackageProjectsProjectIdPackagesPost

> ProjectPackage createProjectPackageProjectsProjectIdPackagesPost(projectId, projectPackageCreate)

Create Project Package

### Example

```javascript
import CanvasApi from 'canvas_api';

let apiInstance = new CanvasApi.PackagesApi();
let projectId = 'projectId_example'; // String | The ID of the project
let projectPackageCreate = new CanvasApi.ProjectPackageCreate(); // ProjectPackageCreate |
apiInstance.createProjectPackageProjectsProjectIdPackagesPost(
  projectId,
  projectPackageCreate,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log('API called successfully. Returned data: ' + data);
    }
  }
);
```

### Parameters

| Name                     | Type                                                | Description           | Notes |
| ------------------------ | --------------------------------------------------- | --------------------- | ----- |
| **projectId**            | **String**                                          | The ID of the project |
| **projectPackageCreate** | [**ProjectPackageCreate**](ProjectPackageCreate.md) |                       |

### Return type

[**ProjectPackage**](ProjectPackage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## deleteProjectPackageProjectsProjectIdPackagesPackageIdDelete

> Object deleteProjectPackageProjectsProjectIdPackagesPackageIdDelete(projectId, packageId)

Delete Project Package

### Example

```javascript
import CanvasApi from 'canvas_api';

let apiInstance = new CanvasApi.PackagesApi();
let projectId = 'projectId_example'; // String | The ID of the project
let packageId = 'packageId_example'; // String | The ID of the package
apiInstance.deleteProjectPackageProjectsProjectIdPackagesPackageIdDelete(
  projectId,
  packageId,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log('API called successfully. Returned data: ' + data);
    }
  }
);
```

### Parameters

| Name          | Type       | Description           | Notes |
| ------------- | ---------- | --------------------- | ----- |
| **projectId** | **String** | The ID of the project |
| **packageId** | **String** | The ID of the package |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## deployProjectPackageProjectsProjectIdPackagesPackageIdDeployPost

> ProjectPackage deployProjectPackageProjectsProjectIdPackagesPackageIdDeployPost(projectId, packageId)

Deploy Project Package

### Example

```javascript
import CanvasApi from 'canvas_api';

let apiInstance = new CanvasApi.PackagesApi();
let projectId = 'projectId_example'; // String | The ID of the project
let packageId = 'packageId_example'; // String | The ID of the package
apiInstance.deployProjectPackageProjectsProjectIdPackagesPackageIdDeployPost(
  projectId,
  packageId,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log('API called successfully. Returned data: ' + data);
    }
  }
);
```

### Parameters

| Name          | Type       | Description           | Notes |
| ------------- | ---------- | --------------------- | ----- |
| **projectId** | **String** | The ID of the project |
| **packageId** | **String** | The ID of the package |

### Return type

[**ProjectPackage**](ProjectPackage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## destroyProjectPackageProjectsProjectIdPackagesPackageIdDestroyDelete

> ProjectPackage destroyProjectPackageProjectsProjectIdPackagesPackageIdDestroyDelete(projectId, packageId)

Destroy Project Package

### Example

```javascript
import CanvasApi from 'canvas_api';

let apiInstance = new CanvasApi.PackagesApi();
let projectId = 'projectId_example'; // String | The ID of the project
let packageId = 'packageId_example'; // String | The ID of the package
apiInstance.destroyProjectPackageProjectsProjectIdPackagesPackageIdDestroyDelete(
  projectId,
  packageId,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log('API called successfully. Returned data: ' + data);
    }
  }
);
```

### Parameters

| Name          | Type       | Description           | Notes |
| ------------- | ---------- | --------------------- | ----- |
| **projectId** | **String** | The ID of the project |
| **packageId** | **String** | The ID of the package |

### Return type

[**ProjectPackage**](ProjectPackage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## getProjectPackageProjectsProjectIdPackagesPackageIdGet

> ProjectPackage getProjectPackageProjectsProjectIdPackagesPackageIdGet(projectId, packageId)

Get Project Package

### Example

```javascript
import CanvasApi from 'canvas_api';

let apiInstance = new CanvasApi.PackagesApi();
let projectId = 'projectId_example'; // String | The ID of the project
let packageId = 'packageId_example'; // String | The ID of the package
apiInstance.getProjectPackageProjectsProjectIdPackagesPackageIdGet(
  projectId,
  packageId,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log('API called successfully. Returned data: ' + data);
    }
  }
);
```

### Parameters

| Name          | Type       | Description           | Notes |
| ------------- | ---------- | --------------------- | ----- |
| **projectId** | **String** | The ID of the project |
| **packageId** | **String** | The ID of the package |

### Return type

[**ProjectPackage**](ProjectPackage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## listProjectPackagesProjectsProjectIdPackagesGet

> [ProjectPackage] listProjectPackagesProjectsProjectIdPackagesGet(projectId, opts)

List Project Packages

### Example

```javascript
import CanvasApi from 'canvas_api';

let apiInstance = new CanvasApi.PackagesApi();
let projectId = 'projectId_example'; // String | The ID of the project
let opts = {
  skip: 0, // Number |
  limit: 100, // Number |
};
apiInstance.listProjectPackagesProjectsProjectIdPackagesGet(
  projectId,
  opts,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log('API called successfully. Returned data: ' + data);
    }
  }
);
```

### Parameters

| Name          | Type       | Description           | Notes                       |
| ------------- | ---------- | --------------------- | --------------------------- |
| **projectId** | **String** | The ID of the project |
| **skip**      | **Number** |                       | [optional] [default to 0]   |
| **limit**     | **Number** |                       | [optional] [default to 100] |

### Return type

[**[ProjectPackage]**](ProjectPackage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## updateProjectPackageProjectsProjectIdPackagesPackageIdPatch

> ProjectPackage updateProjectPackageProjectsProjectIdPackagesPackageIdPatch(projectId, packageId, appSchemasProjectPackageProjectPackageUpdate)

Update Project Package

### Example

```javascript
import CanvasApi from 'canvas_api';

let apiInstance = new CanvasApi.PackagesApi();
let projectId = 'projectId_example'; // String | The ID of the project
let packageId = 'packageId_example'; // String | The ID of the package
let appSchemasProjectPackageProjectPackageUpdate =
  new CanvasApi.AppSchemasProjectPackageProjectPackageUpdate(); // AppSchemasProjectPackageProjectPackageUpdate |
apiInstance.updateProjectPackageProjectsProjectIdPackagesPackageIdPatch(
  projectId,
  packageId,
  appSchemasProjectPackageProjectPackageUpdate,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log('API called successfully. Returned data: ' + data);
    }
  }
);
```

### Parameters

| Name                                             | Type                                                                                                | Description           | Notes |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------- | --------------------- | ----- |
| **projectId**                                    | **String**                                                                                          | The ID of the project |
| **packageId**                                    | **String**                                                                                          | The ID of the package |
| **appSchemasProjectPackageProjectPackageUpdate** | [**AppSchemasProjectPackageProjectPackageUpdate**](AppSchemasProjectPackageProjectPackageUpdate.md) |                       |

### Return type

[**ProjectPackage**](ProjectPackage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## updateProjectPackageProvisionerProjectsProjectIdPackagesPackageIdPatch

> Object updateProjectPackageProvisionerProjectsProjectIdPackagesPackageIdPatch(projectId, packageId, xCanvasToken, appSchemasProvisionerProjectPackageProjectPackageUpdate)

Update Project Package

### Example

```javascript
import CanvasApi from 'canvas_api';

let apiInstance = new CanvasApi.PackagesApi();
let projectId = 'projectId_example'; // String | The ID of the project
let packageId = 'packageId_example'; // String | The ID of the package
let xCanvasToken = 'xCanvasToken_example'; // String |
let appSchemasProvisionerProjectPackageProjectPackageUpdate =
  new CanvasApi.AppSchemasProvisionerProjectPackageProjectPackageUpdate(); // AppSchemasProvisionerProjectPackageProjectPackageUpdate |
apiInstance.updateProjectPackageProvisionerProjectsProjectIdPackagesPackageIdPatch(
  projectId,
  packageId,
  xCanvasToken,
  appSchemasProvisionerProjectPackageProjectPackageUpdate,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log('API called successfully. Returned data: ' + data);
    }
  }
);
```

### Parameters

| Name                                                        | Type                                                                                                                      | Description           | Notes |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------- | ----- |
| **projectId**                                               | **String**                                                                                                                | The ID of the project |
| **packageId**                                               | **String**                                                                                                                | The ID of the package |
| **xCanvasToken**                                            | **String**                                                                                                                |                       |
| **appSchemasProvisionerProjectPackageProjectPackageUpdate** | [**AppSchemasProvisionerProjectPackageProjectPackageUpdate**](AppSchemasProvisionerProjectPackageProjectPackageUpdate.md) |                       |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json
