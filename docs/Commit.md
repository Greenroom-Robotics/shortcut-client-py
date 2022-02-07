# Commit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | A string description of this resource. | 
**author_id** | **str** | The ID of the Member that authored the Commit, if known. | 
**hash** | **str** | The Commit hash. | 
**updated_at** | **datetime** | The time/date the Commit was updated. | 
**merged_branch_ids** | **list[int]** | The IDs of the Branches the Commit has been merged into. | 
**id** | **int** | The unique ID of the Commit. | 
**url** | **str** | The URL of the Commit. | 
**author_email** | **str** | The email address of the VCS user that authored the Commit. | 
**timestamp** | **datetime** | The time/date the Commit was pushed. | 
**author_identity** | [**Identity**](Identity.md) |  | 
**repository_id** | **int** | The ID of the Repository that contains the Commit. | 
**created_at** | **datetime** | The time/date the Commit was created. | 
**message** | **str** | The Commit message. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

