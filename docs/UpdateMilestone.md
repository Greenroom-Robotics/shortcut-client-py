# UpdateMilestone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The Milestone&#x27;s description. | [optional] 
**completed_at_override** | **datetime** | A manual override for the time/date the Milestone was completed. | [optional] 
**name** | **str** | The name of the Milestone. | [optional] 
**state** | **str** | The workflow state that the Milestone is in. | [optional] 
**started_at_override** | **datetime** | A manual override for the time/date the Milestone was started. | [optional] 
**categories** | [**list[CreateCategoryParams]**](CreateCategoryParams.md) | An array of IDs of Categories attached to the Milestone. | [optional] 
**before_id** | **int** | The ID of the Milestone we want to move this Milestone before. | [optional] 
**after_id** | **int** | The ID of the Milestone we want to move this Milestone after. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

