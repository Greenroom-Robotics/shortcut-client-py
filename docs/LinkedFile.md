# LinkedFile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the file. | 
**entity_type** | **str** | A string description of this resource. | 
**story_ids** | **list[int]** | The IDs of the stories this file is attached to. | 
**mention_ids** | **list[str]** | Deprecated: use member_mention_ids. | 
**member_mention_ids** | **list[str]** | The members that are mentioned in the description of the file. | 
**name** | **str** | The name of the linked file. | 
**thumbnail_url** | **str** | The URL of the file thumbnail, if the integration provided it. | 
**type** | **str** | The integration type (e.g. google, dropbox, box). | 
**size** | **int** | The filesize, if the integration provided it. | 
**uploader_id** | **str** | The UUID of the member that uploaded the file. | 
**content_type** | **str** | The content type of the image (e.g. txt/plain). | 
**updated_at** | **datetime** | The time/date the LinkedFile was updated. | 
**group_mention_ids** | **list[str]** | The groups that are mentioned in the description of the file. | 
**id** | **int** | The unique identifier for the file. | 
**url** | **str** | The URL of the file. | 
**created_at** | **datetime** | The time/date the LinkedFile was created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

