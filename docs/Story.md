# Story

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** | The Shortcut application url for the Story. | 
**description** | **str** | The description of the story. | 
**archived** | **bool** | True if the story has been archived or not. | 
**started** | **bool** | A true/false boolean indicating if the Story has been started. | 
**story_links** | [**list[TypedStoryLink]**](TypedStoryLink.md) | An array of story links attached to the Story. | 
**entity_type** | **str** | A string description of this resource. | 
**labels** | [**list[LabelSlim]**](LabelSlim.md) | An array of labels attached to the story. | 
**mention_ids** | **list[str]** | Deprecated: use member_mention_ids. | 
**member_mention_ids** | **list[str]** | An array of Member IDs that have been mentioned in the Story description. | 
**story_type** | **str** | The type of story (feature, bug, chore). | 
**custom_fields** | [**list[StoryCustomField]**](StoryCustomField.md) | An array of CustomField value assertions for the story. | [optional] 
**linked_files** | [**list[LinkedFile]**](LinkedFile.md) | An array of linked files attached to the story. | 
**workflow_id** | **int** | The ID of the workflow the story belongs to. | 
**completed_at_override** | **datetime** | A manual override for the time/date the Story was completed. | 
**started_at** | **datetime** | The time/date the Story was started. | 
**completed_at** | **datetime** | The time/date the Story was completed. | 
**name** | **str** | The name of the story. | 
**completed** | **bool** | A true/false boolean indicating if the Story has been completed. | 
**comments** | [**list[StoryComment]**](StoryComment.md) | An array of comments attached to the story. | 
**blocker** | **bool** | A true/false boolean indicating if the Story is currently a blocker of another story. | 
**branches** | [**list[Branch]**](Branch.md) | An array of Git branches attached to the story. | 
**epic_id** | **int** | The ID of the epic the story belongs to. | 
**story_template_id** | **str** | The ID of the story template used to create this story, or null if not created using a template. | 
**external_links** | **list[str]** | An array of external links (strings) associated with a Story | 
**previous_iteration_ids** | **list[int]** | The IDs of the iteration the story belongs to. | 
**requested_by_id** | **str** | The ID of the Member that requested the story. | 
**iteration_id** | **int** | The ID of the iteration the story belongs to. | 
**tasks** | [**list[Task]**](Task.md) | An array of tasks connected to the story. | 
**label_ids** | **list[int]** | An array of label ids attached to the story. | 
**started_at_override** | **datetime** | A manual override for the time/date the Story was started. | 
**group_id** | **str** | The ID of the group associated with the story. | 
**workflow_state_id** | **int** | The ID of the workflow state the story is currently in. | 
**updated_at** | **datetime** | The time/date the Story was updated. | 
**pull_requests** | [**list[PullRequest]**](PullRequest.md) | An array of Pull/Merge Requests attached to the story. | 
**group_mention_ids** | **list[str]** | An array of Group IDs that have been mentioned in the Story description. | 
**follower_ids** | **list[str]** | An array of UUIDs for any Members listed as Followers. | 
**owner_ids** | **list[str]** | An array of UUIDs of the owners of this story. | 
**external_id** | **str** | This field can be set to another unique ID. In the case that the Story has been imported from another tool, the ID in the other tool can be indicated here. | 
**id** | **int** | The unique ID of the Story. | 
**lead_time** | **int** | The lead time (in seconds) of this story when complete. | [optional] 
**estimate** | **int** | The numeric point estimate of the story. Can also be null, which means unestimated. | 
**commits** | [**list[Commit]**](Commit.md) | An array of commits attached to the story. | 
**files** | [**list[UploadedFile]**](UploadedFile.md) | An array of files attached to the story. | 
**position** | **int** | A number representing the position of the story in relation to every other story in the current project. | 
**blocked** | **bool** | A true/false boolean indicating if the Story is currently blocked. | 
**project_id** | **int** | The ID of the project the story belongs to. | 
**deadline** | **datetime** | The due date of the story. | 
**stats** | [**StoryStats**](StoryStats.md) |  | 
**cycle_time** | **int** | The cycle time (in seconds) of this story when complete. | [optional] 
**created_at** | **datetime** | The time/date the Story was created. | 
**moved_at** | **datetime** | The time/date the Story was last changed workflow-state. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

