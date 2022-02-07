# ThreadedComment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | The Shortcut application url for the Comment. | 
**entity_type** | **str** | A string description of this resource. | 
**deleted** | **bool** | True/false boolean indicating whether the Comment is deleted. | 
**mention_ids** | **list[str]** | Deprecated: use member_mention_ids. | 
**author_id** | **str** | The unique ID of the Member that authored the Comment. | 
**member_mention_ids** | **list[str]** | An array of Member IDs that have been mentioned in this Comment. | 
**comments** | [**list[ThreadedComment]**](ThreadedComment.md) | A nested array of threaded comments. | 
**updated_at** | **datetime** | The time/date the Comment was updated. | 
**group_mention_ids** | **list[str]** | An array of Group IDs that have been mentioned in this Comment. | 
**external_id** | **str** | This field can be set to another unique ID. In the case that the Comment has been imported from another tool, the ID in the other tool can be indicated here. | 
**id** | **int** | The unique ID of the Comment. | 
**created_at** | **datetime** | The time/date the Comment was created. | 
**text** | **str** | The text of the Comment. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

