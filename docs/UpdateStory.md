# UpdateStory

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the story. | [optional] 
**archived** | **bool** | True if the story is archived, otherwise false. | [optional] 
**labels** | [**list[CreateLabelParams]**](CreateLabelParams.md) | An array of labels attached to the story. | [optional] 
**pull_request_ids** | **list[int]** | An array of IDs of Pull/Merge Requests attached to the story. | [optional] 
**story_type** | **str** | The type of story (feature, bug, chore). | [optional] 
**custom_fields** | [**list[CustomFieldValueParams]**](CustomFieldValueParams.md) | A map specifying a CustomField ID and CustomFieldEnumValue ID that represents an assertion of some value for a CustomField. | [optional] 
**move_to** | **str** | One of \&quot;first\&quot; or \&quot;last\&quot;. This can be used to move the given story to the first or last position in the workflow state. | [optional] 
**file_ids** | **list[int]** | An array of IDs of files attached to the story. | [optional] 
**completed_at_override** | **datetime** | A manual override for the time/date the Story was completed. | [optional] 
**name** | **str** | The title of the story. | [optional] 
**epic_id** | **int** | The ID of the epic the story belongs to. | [optional] 
**external_links** | **list[str]** | An array of External Links associated with this story. | [optional] 
**branch_ids** | **list[int]** | An array of IDs of Branches attached to the story. | [optional] 
**commit_ids** | **list[int]** | An array of IDs of Commits attached to the story. | [optional] 
**requested_by_id** | **str** | The ID of the member that requested the story. | [optional] 
**iteration_id** | **int** | The ID of the iteration the story belongs to. | [optional] 
**started_at_override** | **datetime** | A manual override for the time/date the Story was started. | [optional] 
**group_id** | **str** | The ID of the group to associate with this story | [optional] 
**workflow_state_id** | **int** | The ID of the workflow state to put the story in. | [optional] 
**follower_ids** | **list[str]** | An array of UUIDs of the followers of this story. | [optional] 
**owner_ids** | **list[str]** | An array of UUIDs of the owners of this story. | [optional] 
**before_id** | **int** | The ID of the story we want to move this story before. | [optional] 
**estimate** | **int** | The numeric point estimate of the story. Can also be null, which means unestimated. | [optional] 
**after_id** | **int** | The ID of the story we want to move this story after. | [optional] 
**project_id** | **int** | The ID of the project the story belongs to. | [optional] 
**linked_file_ids** | **list[int]** | An array of IDs of linked files attached to the story. | [optional] 
**deadline** | **datetime** | The due date of the story. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

