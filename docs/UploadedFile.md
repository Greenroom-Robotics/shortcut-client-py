# UploadedFile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the file. | 
**entity_type** | **str** | A string description of this resource. | 
**story_ids** | **list[int]** | The unique IDs of the Stories associated with this file. | 
**mention_ids** | **list[str]** | Deprecated: use member_mention_ids. | 
**member_mention_ids** | **list[str]** | The unique IDs of the Members who are mentioned in the file description. | 
**name** | **str** | The optional User-specified name of the file. | 
**thumbnail_url** | **str** | The url where the thumbnail of the file can be found in Shortcut. | 
**size** | **int** | The size of the file. | 
**uploader_id** | **str** | The unique ID of the Member who uploaded the file. | 
**content_type** | **str** | Free form string corresponding to a text or image file. | 
**updated_at** | **datetime** | The time/date that the file was updated. | 
**filename** | **str** | The name assigned to the file in Shortcut upon upload. | 
**group_mention_ids** | **list[str]** | The unique IDs of the Groups who are mentioned in the file description. | 
**external_id** | **str** | This field can be set to another unique ID. In the case that the File has been imported from another tool, the ID in the other tool can be indicated here. | 
**id** | **int** | The unique ID for the file. | 
**url** | **str** | The URL for the file. | 
**created_at** | **datetime** | The time/date that the file was created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

