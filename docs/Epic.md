# Epic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | The Shortcut application url for the Epic. | 
**description** | **str** | The Epic&#x27;s description. | 
**archived** | **bool** | True/false boolean that indicates whether the Epic is archived or not. | 
**started** | **bool** | A true/false boolean indicating if the Epic has been started. | 
**entity_type** | **str** | A string description of this resource. | 
**labels** | [**list[LabelSlim]**](LabelSlim.md) | An array of Labels attached to the Epic. | 
**mention_ids** | **list[str]** | Deprecated: use member_mention_ids. | 
**member_mention_ids** | **list[str]** | An array of Member IDs that have been mentioned in the Epic description. | 
**project_ids** | **list[int]** | The IDs of Projects related to this Epic. | 
**stories_without_projects** | **int** | The number of stories in this epic which are not associated with a project. | 
**completed_at_override** | **datetime** | A manual override for the time/date the Epic was completed. | 
**productboard_plugin_id** | **str** | The ID of the associated productboard integration. | 
**started_at** | **datetime** | The time/date the Epic was started. | 
**completed_at** | **datetime** | The time/date the Epic was completed. | 
**name** | **str** | The name of the Epic. | 
**global_id** | **str** |  | 
**completed** | **bool** | A true/false boolean indicating if the Epic has been completed. | 
**comments** | [**list[ThreadedComment]**](ThreadedComment.md) | A nested array of threaded comments. | 
**productboard_url** | **str** | The URL of the associated productboard feature. | 
**planned_start_date** | **datetime** | The Epic&#x27;s planned start date. | 
**state** | **str** | &#x60;Deprecated&#x60; The workflow state that the Epic is in. | 
**milestone_id** | **int** | The ID of the Milestone this Epic is related to. | 
**requested_by_id** | **str** | The ID of the Member that requested the epic. | 
**epic_state_id** | **int** | The ID of the Epic State. | 
**label_ids** | **list[int]** | An array of Label ids attached to the Epic. | 
**started_at_override** | **datetime** | A manual override for the time/date the Epic was started. | 
**group_id** | **str** |  | 
**updated_at** | **datetime** | The time/date the Epic was updated. | 
**group_mention_ids** | **list[str]** | An array of Group IDs that have been mentioned in the Epic description. | 
**productboard_id** | **str** | The ID of the associated productboard feature. | 
**follower_ids** | **list[str]** | An array of UUIDs for any Members you want to add as Followers on this Epic. | 
**owner_ids** | **list[str]** | An array of UUIDs for any members you want to add as Owners on this new Epic. | 
**external_id** | **str** | This field can be set to another unique ID. In the case that the Epic has been imported from another tool, the ID in the other tool can be indicated here. | 
**id** | **int** | The unique ID of the Epic. | 
**position** | **int** | The Epic&#x27;s relative position in the Epic workflow state. | 
**productboard_name** | **str** | The name of the associated productboard feature. | 
**deadline** | **datetime** | The Epic&#x27;s deadline. | 
**stats** | [**EpicStats**](EpicStats.md) |  | 
**created_at** | **datetime** | The time/date the Epic was created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

