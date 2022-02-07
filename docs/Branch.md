# Branch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | A string description of this resource. | 
**deleted** | **bool** | A true/false boolean indicating if the Branch has been deleted. | 
**name** | **str** | The name of the Branch. | 
**persistent** | **bool** | A true/false boolean indicating if the Branch is persistent; e.g. master. | 
**updated_at** | **datetime** | The time/date the Branch was updated. | 
**pull_requests** | [**list[PullRequest]**](PullRequest.md) | An array of PullRequests attached to the Branch (there is usually only one). | 
**merged_branch_ids** | **list[int]** | The IDs of the Branches the Branch has been merged into. | 
**id** | **int** | The unique ID of the Branch. | 
**url** | **str** | The URL of the Branch. | 
**repository_id** | **int** | The ID of the Repository that contains the Branch. | 
**created_at** | **datetime** | The time/date the Branch was created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

