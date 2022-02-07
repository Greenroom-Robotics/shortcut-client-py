# UpdateStoryContents

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the story. | [optional] 
**entity_type** | **str** | A string description of this resource. | [optional] 
**labels** | [**list[CreateLabelParams]**](CreateLabelParams.md) | An array of labels to be populated by the template. | [optional] 
**story_type** | **str** | The type of story (feature, bug, chore). | [optional] 
**custom_fields** | [**list[CustomFieldValueParams]**](CustomFieldValueParams.md) | An array of maps specifying a CustomField ID and CustomFieldEnumValue ID that represents an assertion of some value for a CustomField. | [optional] 
**linked_files** | [**list[LinkedFile]**](LinkedFile.md) | An array of linked files attached to the story. | [optional] 
**file_ids** | **list[int]** | An array of the attached file IDs to be populated. | [optional] 
**name** | **str** | The name of the story. | [optional] 
**epic_id** | **int** | The ID of the epic the to be populated. | [optional] 
**external_links** | **list[str]** | An array of external links to be populated. | [optional] 
**iteration_id** | **int** | The ID of the iteration the to be populated. | [optional] 
**tasks** | [**list[EntityTemplateTask]**](EntityTemplateTask.md) | An array of tasks to be populated by the template. | [optional] 
**label_ids** | **list[int]** | An array of label ids attached to the story. | [optional] 
**group_id** | **str** | The ID of the group to be populated. | [optional] 
**workflow_state_id** | **int** | The ID of the workflow state the story is currently in. | [optional] 
**follower_ids** | **list[str]** | An array of UUIDs for any Members listed as Followers. | [optional] 
**owner_ids** | **list[str]** | An array of UUIDs of the owners of this story. | [optional] 
**estimate** | **int** | The numeric point estimate to be populated. | [optional] 
**files** | [**list[UploadedFile]**](UploadedFile.md) | An array of files attached to the story. | [optional] 
**project_id** | **int** | The ID of the project the story belongs to. | [optional] 
**linked_file_ids** | **list[int]** | An array of the linked file IDs to be populated. | [optional] 
**deadline** | **datetime** | The due date of the story. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

