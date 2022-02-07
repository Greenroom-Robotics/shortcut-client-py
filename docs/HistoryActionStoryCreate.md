# HistoryActionStoryCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | The application URL of the Story. | 
**description** | **str** | The description of the Story. | [optional] 
**started** | **bool** | Whether or not the Story has been started. | [optional] 
**entity_type** | **str** | The type of entity referenced. | 
**task_ids** | **list[int]** | An array of Task IDs on this Story. | [optional] 
**story_type** | **str** | The type of Story; either feature, bug, or chore. | 
**name** | **str** | The name of the Story. | 
**completed** | **bool** | Whether or not the Story is completed. | [optional] 
**blocker** | **bool** | Whether or not the Story is blocking another Story. | [optional] 
**epic_id** | **int** | The Epic ID for this Story. | [optional] 
**requested_by_id** | **str** | The ID of the Member that requested the Story. | [optional] 
**iteration_id** | **int** | The Iteration ID the Story is in. | [optional] 
**label_ids** | **list[int]** | An array of Labels IDs attached to the Story. | [optional] 
**workflow_state_id** | **int** | An array of Workflow State IDs attached to the Story. | [optional] 
**object_story_link_ids** | **list[int]** | An array of Story IDs that are the object of a Story Link relationship. | [optional] 
**follower_ids** | **list[str]** | An array of Member IDs for the followers of the Story. | [optional] 
**owner_ids** | **list[str]** | An array of Member IDs that are the owners of the Story. | [optional] 
**id** | **int** | The ID of the entity referenced. | 
**estimate** | **int** | The estimate (or point value) for the Story. | [optional] 
**subject_story_link_ids** | **list[int]** | An array of Story IDs that are the subject of a Story Link relationship. | [optional] 
**action** | **str** | The action of the entity referenced. | 
**blocked** | **bool** | Whether or not the Story is blocked by another Story. | [optional] 
**project_id** | **int** | The Project ID of the Story is in. | [optional] 
**deadline** | **str** | The timestamp representing the Story&#x27;s deadline. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

