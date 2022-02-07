# UpdateEpic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The Epic&#x27;s description. | [optional] 
**archived** | **bool** | A true/false boolean indicating whether the Epic is in archived state. | [optional] 
**labels** | [**list[CreateLabelParams]**](CreateLabelParams.md) | An array of Labels attached to the Epic. | [optional] 
**completed_at_override** | **datetime** | A manual override for the time/date the Epic was completed. | [optional] 
**name** | **str** | The Epic&#x27;s name. | [optional] 
**planned_start_date** | **datetime** | The Epic&#x27;s planned start date. | [optional] 
**state** | **str** | &#x60;Deprecated&#x60; The Epic&#x27;s state (to do, in progress, or done); will be ignored when &#x60;epic_state_id&#x60; is set. | [optional] 
**milestone_id** | **int** | The ID of the Milestone this Epic is related to. | [optional] 
**requested_by_id** | **str** | The ID of the member that requested the epic. | [optional] 
**epic_state_id** | **int** | The ID of the Epic State. | [optional] 
**started_at_override** | **datetime** | A manual override for the time/date the Epic was started. | [optional] 
**group_id** | **str** | The ID of the group to associate with the epic. | [optional] 
**follower_ids** | **list[str]** | An array of UUIDs for any Members you want to add as Followers on this Epic. | [optional] 
**owner_ids** | **list[str]** | An array of UUIDs for any members you want to add as Owners on this Epic. | [optional] 
**before_id** | **int** | The ID of the Epic we want to move this Epic before. | [optional] 
**after_id** | **int** | The ID of the Epic we want to move this Epic after. | [optional] 
**deadline** | **datetime** | The Epic&#x27;s deadline. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

