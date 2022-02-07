# History

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed_at** | **str** | The date when the change occurred. | 
**primary_id** | **int** | The ID of the primary entity that has changed, if applicable. | [optional] 
**references** | **list[object]** | An array of objects affected by the change. Reference objects provide basic information for the entities reference in the history actions. Some have specific fields, but they always contain an id, entity_type, and a name. | [optional] 
**actions** | **list[object]** | An array of actions that were performed for the change. | 
**member_id** | **str** | The ID of the member who performed the change. | [optional] 
**external_id** | **str** | The ID of the webhook that handled the change. | [optional] 
**id** | **str** | The ID representing the change for the story. | 
**version** | **str** | The version of the change format. | 
**webhook_id** | **str** | The ID of the webhook that handled the change. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

