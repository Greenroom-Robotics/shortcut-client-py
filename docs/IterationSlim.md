# IterationSlim

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | The Shortcut application url for the Iteration. | 
**entity_type** | **str** | A string description of this resource | 
**labels** | [**list[Label]**](Label.md) | An array of labels attached to the iteration. | 
**mention_ids** | **list[str]** | Deprecated: use member_mention_ids. | 
**member_mention_ids** | **list[str]** | An array of Member IDs that have been mentioned in the Story description. | 
**name** | **str** | The name of the iteration. | 
**label_ids** | **list[int]** | An array of label ids attached to the iteration. | 
**updated_at** | **datetime** | The instant when this iteration was last updated. | 
**group_mention_ids** | **list[str]** | An array of Group IDs that have been mentioned in the Story description. | 
**end_date** | **datetime** | The date this iteration begins. | 
**follower_ids** | **list[str]** | An array of UUIDs for any Members listed as Followers. | 
**group_ids** | **list[str]** | An array of UUIDs for any Groups you want to add as Followers. Currently, only one Group association is presented in our web UI. | 
**start_date** | **datetime** | The date this iteration begins. | 
**status** | **str** | The status of the iteration. Values are either \&quot;unstarted\&quot;, \&quot;started\&quot;, or \&quot;done\&quot;. | 
**id** | **int** | The ID of the iteration. | 
**stats** | [**IterationStats**](IterationStats.md) |  | 
**created_at** | **datetime** | The instant when this iteration was created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

