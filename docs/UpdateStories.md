# UpdateStories

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** | If the Stories should be archived or not. | [optional] 
**story_ids** | **list[int]** | The Ids of the Stories you wish to update. | 
**story_type** | **str** | The type of story (feature, bug, chore). | [optional] 
**custom_fields** | [**list[CustomFieldValueParams]**](CustomFieldValueParams.md) | A map specifying a CustomField ID and CustomFieldEnumValue ID that represents an assertion of some value for a CustomField. | [optional] 
**move_to** | **str** | One of \&quot;first\&quot; or \&quot;last\&quot;. This can be used to move the given story to the first or last position in the workflow state. | [optional] 
**follower_ids_add** | **list[str]** | The UUIDs of the new followers to be added. | [optional] 
**epic_id** | **int** | The ID of the epic the story belongs to. | [optional] 
**external_links** | **list[str]** | An array of External Links associated with this story. | [optional] 
**follower_ids_remove** | **list[str]** | The UUIDs of the followers to be removed. | [optional] 
**requested_by_id** | **str** | The ID of the member that requested the story. | [optional] 
**iteration_id** | **int** | The ID of the iteration the story belongs to. | [optional] 
**labels_add** | [**list[CreateLabelParams]**](CreateLabelParams.md) | An array of labels to be added. | [optional] 
**group_id** | **str** | The Id of the Group the Stories should belong to. | [optional] 
**workflow_state_id** | **int** | The ID of the workflow state to put the stories in. | [optional] 
**before_id** | **int** | The ID of the story that the stories are to be moved before. | [optional] 
**estimate** | **int** | The numeric point estimate of the story. Can also be null, which means unestimated. | [optional] 
**after_id** | **int** | The ID of the story that the stories are to be moved below. | [optional] 
**owner_ids_remove** | **list[str]** | The UUIDs of the owners to be removed. | [optional] 
**project_id** | **int** | The ID of the Project the Stories should belong to. | [optional] 
**labels_remove** | [**list[CreateLabelParams]**](CreateLabelParams.md) | An array of labels to be removed. | [optional] 
**deadline** | **datetime** | The due date of the story. | [optional] 
**owner_ids_add** | **list[str]** | The UUIDs of the new owners to be added. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

