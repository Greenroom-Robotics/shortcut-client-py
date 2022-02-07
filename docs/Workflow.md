# Workflow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the workflow. | 
**entity_type** | **str** | A string description of this resource. | 
**project_ids** | **list[float]** | An array of IDs of projects within the Workflow. | 
**states** | [**list[WorkflowState]**](WorkflowState.md) | A map of the states in this Workflow. | 
**name** | **str** | The name of the workflow. | 
**updated_at** | **datetime** | The date the Workflow was updated. | 
**auto_assign_owner** | **bool** | Indicates if an owner is automatically assigned when an unowned story is started. | 
**id** | **int** | The unique ID of the Workflow. | 
**team_id** | **int** | The ID of the team the workflow belongs to. | 
**created_at** | **datetime** | The date the Workflow was created. | 
**default_state_id** | **int** | The unique ID of the default state that new Stories are entered into. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

