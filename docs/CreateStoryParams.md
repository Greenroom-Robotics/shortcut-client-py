# CreateStoryParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the story. | [optional] 
**archived** | **bool** | Controls the story&#x27;s archived state. | [optional] 
**story_links** | [**list[CreateStoryLinkParams]**](CreateStoryLinkParams.md) | An array of story links attached to the story. | [optional] 
**labels** | [**list[CreateLabelParams]**](CreateLabelParams.md) | An array of labels attached to the story. | [optional] 
**story_type** | **str** | The type of story (feature, bug, chore). | [optional] 
**custom_fields** | [**list[CustomFieldValueParams]**](CustomFieldValueParams.md) | A map specifying a CustomField ID and CustomFieldEnumValue ID that represents an assertion of some value for a CustomField. | [optional] 
**file_ids** | **list[int]** | An array of IDs of files attached to the story. | [optional] 
**completed_at_override** | **datetime** | A manual override for the time/date the Story was completed. | [optional] 
**name** | **str** | The name of the story. | 
**comments** | [**list[CreateStoryCommentParams]**](CreateStoryCommentParams.md) | An array of comments to add to the story. | [optional] 
**epic_id** | **int** | The ID of the epic the story belongs to. | [optional] 
**story_template_id** | **str** | The id of the story template used to create this story, if applicable. | [optional] 
**external_links** | **list[str]** | An array of External Links associated with this story. | [optional] 
**requested_by_id** | **str** | The ID of the member that requested the story. | [optional] 
**iteration_id** | **int** | The ID of the iteration the story belongs to. | [optional] 
**tasks** | [**list[CreateTaskParams]**](CreateTaskParams.md) | An array of tasks connected to the story. | [optional] 
**started_at_override** | **datetime** | A manual override for the time/date the Story was started. | [optional] 
**group_id** | **str** | The id of the group to associate with this story. | [optional] 
**workflow_state_id** | **int** | The ID of the workflow state the story will be in. | [optional] 
**updated_at** | **datetime** | The time/date the Story was updated. | [optional] 
**follower_ids** | **list[str]** | An array of UUIDs of the followers of this story. | [optional] 
**owner_ids** | **list[str]** | An array of UUIDs of the owners of this story. | [optional] 
**external_id** | **str** | This field can be set to another unique ID. In the case that the Story has been imported from another tool, the ID in the other tool can be indicated here. | [optional] 
**estimate** | **int** | The numeric point estimate of the story. Can also be null, which means unestimated. | [optional] 
**project_id** | **int** | The ID of the project the story belongs to. | [optional] 
**linked_file_ids** | **list[int]** | An array of IDs of linked files attached to the story. | [optional] 
**deadline** | **datetime** | The due date of the story. | [optional] 
**created_at** | **datetime** | The time/date the Story was created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

