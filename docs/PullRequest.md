# PullRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | A string description of this resource. | 
**closed** | **bool** | True/False boolean indicating whether the VCS pull request has been closed. | 
**merged** | **bool** | True/False boolean indicating whether the VCS pull request has been merged. | 
**num_added** | **int** | Number of lines added in the pull request, according to VCS. | 
**branch_id** | **int** | The ID of the branch for the particular pull request. | 
**number** | **int** | The pull request&#x27;s unique number ID in VCS. | 
**branch_name** | **str** | The name of the branch for the particular pull request. | 
**target_branch_name** | **str** | The name of the target branch for the particular pull request. | 
**num_commits** | **int** | The number of commits on the pull request. | 
**title** | **str** | The title of the pull request. | 
**updated_at** | **datetime** | The time/date the pull request was created. | 
**draft** | **bool** | True/False boolean indicating whether the VCS pull request is in the draft state. | 
**id** | **int** | The unique ID associated with the pull request in Shortcut. | 
**vcs_labels** | [**list[PullRequestLabel]**](PullRequestLabel.md) | An array of PullRequestLabels attached to the PullRequest. | [optional] 
**url** | **str** | The URL for the pull request. | 
**num_removed** | **int** | Number of lines removed in the pull request, according to VCS. | 
**review_status** | **str** | The status of the review for the pull request. | [optional] 
**num_modified** | **int** | Number of lines modified in the pull request, according to VCS. | 
**build_status** | **str** | The status of the Continuous Integration workflow for the pull request. | [optional] 
**target_branch_id** | **int** | The ID of the target branch for the particular pull request. | 
**repository_id** | **int** | The ID of the repository for the particular pull request. | 
**created_at** | **datetime** | The time/date the pull request was created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

