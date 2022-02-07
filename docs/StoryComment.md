# StoryComment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | The Shortcut application url for the Comment. | 
**entity_type** | **str** | A string description of this resource. | 
**deleted** | **bool** | True/false boolean indicating whether the Comment has been deleted. | 
**story_id** | **int** | The ID of the Story on which the Comment appears. | 
**mention_ids** | **list[str]** | Deprecated: use member_mention_ids. | 
**author_id** | **str** | The unique ID of the Member who is the Comment&#x27;s author. | 
**member_mention_ids** | **list[str]** | The unique IDs of the Member who are mentioned in the Comment. | 
**updated_at** | **datetime** | The time/date when the Comment was updated. | 
**group_mention_ids** | **list[str]** | The unique IDs of the Group who are mentioned in the Comment. | 
**external_id** | **str** | This field can be set to another unique ID. In the case that the Comment has been imported from another tool, the ID in the other tool can be indicated here. | 
**parent_id** | **int** | The ID of the parent Comment this Comment is threaded under. | [optional] 
**id** | **int** | The unique ID of the Comment. | 
**position** | **int** | The Comments numerical position in the list from oldest to newest. | 
**reactions** | [**list[StoryReaction]**](StoryReaction.md) | A set of Reactions to this Comment. | 
**created_at** | **datetime** | The time/date when the Comment was created. | 
**text** | **str** | The text of the Comment. In the case that the Comment has been deleted, this field can be set to nil. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

