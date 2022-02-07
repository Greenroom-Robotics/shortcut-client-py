# SearchStories

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** | A true/false boolean indicating whether the Story is in archived state. | [optional] 
**owner_id** | **str** | An array of UUIDs for any Users who may be Owners of the Stories. | [optional] 
**story_type** | **str** | The type of Stories that you want returned. | [optional] 
**epic_ids** | **list[int]** | The Epic IDs that may be associated with the Stories. | [optional] 
**project_ids** | **list[int]** | The IDs for the Projects the Stories may be assigned to. | [optional] 
**updated_at_end** | **datetime** | Stories should have been updated before this date. | [optional] 
**completed_at_end** | **datetime** | Stories should have been completed before this date. | [optional] 
**workflow_state_types** | **list[str]** | The type of Workflow State the Stories may be in. | [optional] 
**deadline_end** | **datetime** | Stories should have a deadline before this date. | [optional] 
**created_at_start** | **datetime** | Stories should have been created after this date. | [optional] 
**epic_id** | **int** | The Epic IDs that may be associated with the Stories. | [optional] 
**label_name** | **str** | The name of any associated Labels. | [optional] 
**requested_by_id** | **str** | The UUID of any Users who may have requested the Stories. | [optional] 
**iteration_id** | **int** | The Iteration ID that may be associated with the Stories. | [optional] 
**label_ids** | **list[int]** | The Label IDs that may be associated with the Stories. | [optional] 
**group_id** | **str** | The Group ID that is associated with the Stories | [optional] 
**workflow_state_id** | **int** | The unique IDs of the specific Workflow States that the Stories should be in. | [optional] 
**iteration_ids** | **list[int]** | The Iteration IDs that may be associated with the Stories. | [optional] 
**created_at_end** | **datetime** | Stories should have been created before this date. | [optional] 
**deadline_start** | **datetime** | Stories should have a deadline after this date. | [optional] 
**group_ids** | **list[str]** | The Group IDs that are associated with the Stories | [optional] 
**owner_ids** | **list[str]** | An array of UUIDs for any Users who may be Owners of the Stories. | [optional] 
**external_id** | **str** | An ID or URL that references an external resource. Useful during imports. | [optional] 
**includes_description** | **bool** | Whether to include the story description in the response. | [optional] 
**estimate** | **int** | The number of estimate points associate with the Stories. | [optional] 
**project_id** | **int** | The IDs for the Projects the Stories may be assigned to. | [optional] 
**completed_at_start** | **datetime** | Stories should have been completed after this date. | [optional] 
**updated_at_start** | **datetime** | Stories should have been updated after this date. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

