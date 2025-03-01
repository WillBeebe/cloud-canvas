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
/**
 * Enum class CredentialType.
 * @enum {}
 * @readonly
 */
export default class CredentialType {
  /**
   * value: "SERVICE_ACCOUNT_KEY"
   * @const
   */
  SERVICE_ACCOUNT_KEY = 'SERVICE_ACCOUNT_KEY';

  /**
   * value: "SECRET"
   * @const
   */
  SECRET = 'SECRET';

  /**
   * Returns a <code>CredentialType</code> enum value from a Javascript object name.
   * @param {Object} data The plain JavaScript object containing the name of the enum value.
   * @return {module:model/CredentialType} The enum <code>CredentialType</code> value.
   */
  static constructFromObject(object) {
    return object;
  }
}
