# Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Full text of the Task. | 
**entity_type** | **str** | A string description of this resource. | 
**story_id** | **int** | The unique identifier of the parent Story. | 
**mention_ids** | **list[str]** | Deprecated: use member_mention_ids. | 
**member_mention_ids** | **list[str]** | An array of UUIDs of Members mentioned in this Task. | 
**completed_at** | **datetime** | The time/date the Task was completed. | 
**updated_at** | **datetime** | The time/date the Task was updated. | 
**group_mention_ids** | **list[str]** | An array of UUIDs of Groups mentioned in this Task. | 
**owner_ids** | **list[str]** | An array of UUIDs of the Owners of this Task. | 
**external_id** | **str** | This field can be set to another unique ID. In the case that the Task has been imported from another tool, the ID in the other tool can be indicated here. | 
**id** | **int** | The unique ID of the Task. | 
**position** | **int** | The number corresponding to the Task&#x27;s position within a list of Tasks on a Story. | 
**complete** | **bool** | True/false boolean indicating whether the Task has been completed. | 
**created_at** | **datetime** | The time/date the Task was created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

