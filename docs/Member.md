# Member

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The Member&#x27;s role in the Workspace. | 
**entity_type** | **str** | A string description of this resource. | 
**disabled** | **bool** | True/false boolean indicating whether the Member has been disabled within the Workspace. | 
**global_id** | **str** |  | 
**state** | **str** | The user state, one of partial, full, disabled, or imported.  A partial user is disabled, has no means to log in, and is not an import user.  A full user is enabled and has a means to log in.  A disabled user is disabled and has a means to log in.  An import user is disabled, has no means to log in, and is marked as an import user. | 
**updated_at** | **datetime** | The time/date the Member was last updated. | 
**created_without_invite** | **bool** | Whether this member was created as a placeholder entity. | 
**group_ids** | **list[str]** | The Member&#x27;s group ids | 
**id** | **str** | The Member&#x27;s ID in Shortcut. | 
**profile** | [**Profile**](Profile.md) |  | 
**created_at** | **datetime** | The time/date the Member was created. | 
**replaced_by** | **str** | The id of the member that replaces this one when merged. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

