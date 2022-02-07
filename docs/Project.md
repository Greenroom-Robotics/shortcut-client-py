# Project

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | The Shortcut application url for the Project. | 
**description** | **str** | The description of the Project. | 
**archived** | **bool** | True/false boolean indicating whether the Project is in an Archived state. | 
**entity_type** | **str** | A string description of this resource. | 
**days_to_thermometer** | **int** | The number of days before the thermometer appears in the Story summary. | 
**color** | **str** | The color associated with the Project in the Shortcut member interface. | 
**workflow_id** | **int** | The ID of the workflow the project belongs to. | 
**name** | **str** | The name of the Project | 
**start_time** | **datetime** | The date at which the Project was started. | 
**updated_at** | **datetime** | The time/date that the Project was last updated. | 
**follower_ids** | **list[str]** | An array of UUIDs for any Members listed as Followers. | 
**external_id** | **str** | This field can be set to another unique ID. In the case that the Project has been imported from another tool, the ID in the other tool can be indicated here. | 
**id** | **int** | The unique ID of the Project. | 
**show_thermometer** | **bool** | Configuration to enable or disable thermometers in the Story summary. | 
**team_id** | **int** | The ID of the team the project belongs to. | 
**iteration_length** | **int** | The number of weeks per iteration in this Project. | 
**abbreviation** | **str** | The Project abbreviation used in Story summaries. Should be kept to 3 characters at most. | 
**stats** | [**ProjectStats**](ProjectStats.md) |  | 
**created_at** | **datetime** | The time/date that the Project was created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

