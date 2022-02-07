# shortcut_client_py.DefaultApi

All URIs are relative to *https://api.app.shortcut.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_category**](DefaultApi.md#create_category) | **POST** /api/v3/categories | Create Category
[**create_entity_template**](DefaultApi.md#create_entity_template) | **POST** /api/v3/entity-templates | Create Entity Template
[**create_epic**](DefaultApi.md#create_epic) | **POST** /api/v3/epics | Create Epic
[**create_epic_comment**](DefaultApi.md#create_epic_comment) | **POST** /api/v3/epics/{epic-public-id}/comments | Create Epic Comment
[**create_epic_comment_comment**](DefaultApi.md#create_epic_comment_comment) | **POST** /api/v3/epics/{epic-public-id}/comments/{comment-public-id} | Create Epic Comment Comment
[**create_group**](DefaultApi.md#create_group) | **POST** /api/v3/groups | Create Group
[**create_iteration**](DefaultApi.md#create_iteration) | **POST** /api/v3/iterations | Create Iteration
[**create_label**](DefaultApi.md#create_label) | **POST** /api/v3/labels | Create Label
[**create_linked_file**](DefaultApi.md#create_linked_file) | **POST** /api/v3/linked-files | Create Linked File
[**create_milestone**](DefaultApi.md#create_milestone) | **POST** /api/v3/milestones | Create Milestone
[**create_multiple_stories**](DefaultApi.md#create_multiple_stories) | **POST** /api/v3/stories/bulk | Create Multiple Stories
[**create_project**](DefaultApi.md#create_project) | **POST** /api/v3/projects | Create Project
[**create_story**](DefaultApi.md#create_story) | **POST** /api/v3/stories | Create Story
[**create_story_comment**](DefaultApi.md#create_story_comment) | **POST** /api/v3/stories/{story-public-id}/comments | Create Story Comment
[**create_story_link**](DefaultApi.md#create_story_link) | **POST** /api/v3/story-links | Create Story Link
[**create_story_reaction**](DefaultApi.md#create_story_reaction) | **POST** /api/v3/stories/{story-public-id}/comments/{comment-public-id}/reactions | Create Story Reaction
[**create_task**](DefaultApi.md#create_task) | **POST** /api/v3/stories/{story-public-id}/tasks | Create Task
[**delete_category**](DefaultApi.md#delete_category) | **DELETE** /api/v3/categories/{category-public-id} | Delete Category
[**delete_entity_template**](DefaultApi.md#delete_entity_template) | **DELETE** /api/v3/entity-templates/{entity-template-public-id} | Delete Entity Template
[**delete_epic**](DefaultApi.md#delete_epic) | **DELETE** /api/v3/epics/{epic-public-id} | Delete Epic
[**delete_epic_comment**](DefaultApi.md#delete_epic_comment) | **DELETE** /api/v3/epics/{epic-public-id}/comments/{comment-public-id} | Delete Epic Comment
[**delete_file**](DefaultApi.md#delete_file) | **DELETE** /api/v3/files/{file-public-id} | Delete File
[**delete_iteration**](DefaultApi.md#delete_iteration) | **DELETE** /api/v3/iterations/{iteration-public-id} | Delete Iteration
[**delete_label**](DefaultApi.md#delete_label) | **DELETE** /api/v3/labels/{label-public-id} | Delete Label
[**delete_linked_file**](DefaultApi.md#delete_linked_file) | **DELETE** /api/v3/linked-files/{linked-file-public-id} | Delete Linked File
[**delete_milestone**](DefaultApi.md#delete_milestone) | **DELETE** /api/v3/milestones/{milestone-public-id} | Delete Milestone
[**delete_multiple_stories**](DefaultApi.md#delete_multiple_stories) | **DELETE** /api/v3/stories/bulk | Delete Multiple Stories
[**delete_project**](DefaultApi.md#delete_project) | **DELETE** /api/v3/projects/{project-public-id} | Delete Project
[**delete_story**](DefaultApi.md#delete_story) | **DELETE** /api/v3/stories/{story-public-id} | Delete Story
[**delete_story_comment**](DefaultApi.md#delete_story_comment) | **DELETE** /api/v3/stories/{story-public-id}/comments/{comment-public-id} | Delete Story Comment
[**delete_story_link**](DefaultApi.md#delete_story_link) | **DELETE** /api/v3/story-links/{story-link-public-id} | Delete Story Link
[**delete_story_reaction**](DefaultApi.md#delete_story_reaction) | **DELETE** /api/v3/stories/{story-public-id}/comments/{comment-public-id}/reactions | Delete Story Reaction
[**delete_task**](DefaultApi.md#delete_task) | **DELETE** /api/v3/stories/{story-public-id}/tasks/{task-public-id} | Delete Task
[**disable_groups**](DefaultApi.md#disable_groups) | **PUT** /api/v3/groups/disable | Disable Groups
[**disable_iterations**](DefaultApi.md#disable_iterations) | **PUT** /api/v3/iterations/disable | Disable Iterations
[**disable_story_templates**](DefaultApi.md#disable_story_templates) | **PUT** /api/v3/entity-templates/disable | Disable Story Templates
[**enable_groups**](DefaultApi.md#enable_groups) | **PUT** /api/v3/groups/enable | Enable Groups
[**enable_iterations**](DefaultApi.md#enable_iterations) | **PUT** /api/v3/iterations/enable | Enable Iterations
[**enable_story_templates**](DefaultApi.md#enable_story_templates) | **PUT** /api/v3/entity-templates/enable | Enable Story Templates
[**get_category**](DefaultApi.md#get_category) | **GET** /api/v3/categories/{category-public-id} | Get Category
[**get_current_member_info**](DefaultApi.md#get_current_member_info) | **GET** /api/v3/member | Get Current Member Info
[**get_entity_template**](DefaultApi.md#get_entity_template) | **GET** /api/v3/entity-templates/{entity-template-public-id} | Get Entity Template
[**get_epic**](DefaultApi.md#get_epic) | **GET** /api/v3/epics/{epic-public-id} | Get Epic
[**get_epic_comment**](DefaultApi.md#get_epic_comment) | **GET** /api/v3/epics/{epic-public-id}/comments/{comment-public-id} | Get Epic Comment
[**get_epic_workflow**](DefaultApi.md#get_epic_workflow) | **GET** /api/v3/epic-workflow | Get Epic Workflow
[**get_external_link_stories**](DefaultApi.md#get_external_link_stories) | **GET** /api/v3/external-link/stories | Get External Link Stories
[**get_file**](DefaultApi.md#get_file) | **GET** /api/v3/files/{file-public-id} | Get File
[**get_group**](DefaultApi.md#get_group) | **GET** /api/v3/groups/{group-public-id} | Get Group
[**get_iteration**](DefaultApi.md#get_iteration) | **GET** /api/v3/iterations/{iteration-public-id} | Get Iteration
[**get_label**](DefaultApi.md#get_label) | **GET** /api/v3/labels/{label-public-id} | Get Label
[**get_linked_file**](DefaultApi.md#get_linked_file) | **GET** /api/v3/linked-files/{linked-file-public-id} | Get Linked File
[**get_member**](DefaultApi.md#get_member) | **GET** /api/v3/members/{member-public-id} | Get Member
[**get_milestone**](DefaultApi.md#get_milestone) | **GET** /api/v3/milestones/{milestone-public-id} | Get Milestone
[**get_project**](DefaultApi.md#get_project) | **GET** /api/v3/projects/{project-public-id} | Get Project
[**get_repository**](DefaultApi.md#get_repository) | **GET** /api/v3/repositories/{repo-public-id} | Get Repository
[**get_story**](DefaultApi.md#get_story) | **GET** /api/v3/stories/{story-public-id} | Get Story
[**get_story_comment**](DefaultApi.md#get_story_comment) | **GET** /api/v3/stories/{story-public-id}/comments/{comment-public-id} | Get Story Comment
[**get_story_link**](DefaultApi.md#get_story_link) | **GET** /api/v3/story-links/{story-link-public-id} | Get Story Link
[**get_task**](DefaultApi.md#get_task) | **GET** /api/v3/stories/{story-public-id}/tasks/{task-public-id} | Get Task
[**get_workflow**](DefaultApi.md#get_workflow) | **GET** /api/v3/workflows/{workflow-public-id} | Get Workflow
[**list_categories**](DefaultApi.md#list_categories) | **GET** /api/v3/categories | List Categories
[**list_category_milestones**](DefaultApi.md#list_category_milestones) | **GET** /api/v3/categories/{category-public-id}/milestones | List Category Milestones
[**list_entity_templates**](DefaultApi.md#list_entity_templates) | **GET** /api/v3/entity-templates | List Entity Templates
[**list_epic_comments**](DefaultApi.md#list_epic_comments) | **GET** /api/v3/epics/{epic-public-id}/comments | List Epic Comments
[**list_epic_stories**](DefaultApi.md#list_epic_stories) | **GET** /api/v3/epics/{epic-public-id}/stories | List Epic Stories
[**list_epics**](DefaultApi.md#list_epics) | **GET** /api/v3/epics | List Epics
[**list_files**](DefaultApi.md#list_files) | **GET** /api/v3/files | List Files
[**list_group_stories**](DefaultApi.md#list_group_stories) | **GET** /api/v3/groups/{group-public-id}/stories | List Group Stories
[**list_groups**](DefaultApi.md#list_groups) | **GET** /api/v3/groups | List Groups
[**list_iteration_stories**](DefaultApi.md#list_iteration_stories) | **GET** /api/v3/iterations/{iteration-public-id}/stories | List Iteration Stories
[**list_iterations**](DefaultApi.md#list_iterations) | **GET** /api/v3/iterations | List Iterations
[**list_label_epics**](DefaultApi.md#list_label_epics) | **GET** /api/v3/labels/{label-public-id}/epics | List Label Epics
[**list_label_stories**](DefaultApi.md#list_label_stories) | **GET** /api/v3/labels/{label-public-id}/stories | List Label Stories
[**list_labels**](DefaultApi.md#list_labels) | **GET** /api/v3/labels | List Labels
[**list_linked_files**](DefaultApi.md#list_linked_files) | **GET** /api/v3/linked-files | List Linked Files
[**list_members**](DefaultApi.md#list_members) | **GET** /api/v3/members | List Members
[**list_milestone_epics**](DefaultApi.md#list_milestone_epics) | **GET** /api/v3/milestones/{milestone-public-id}/epics | List Milestone Epics
[**list_milestones**](DefaultApi.md#list_milestones) | **GET** /api/v3/milestones | List Milestones
[**list_projects**](DefaultApi.md#list_projects) | **GET** /api/v3/projects | List Projects
[**list_repositories**](DefaultApi.md#list_repositories) | **GET** /api/v3/repositories | List Repositories
[**list_stories**](DefaultApi.md#list_stories) | **GET** /api/v3/projects/{project-public-id}/stories | List Stories
[**list_workflows**](DefaultApi.md#list_workflows) | **GET** /api/v3/workflows | List Workflows
[**search**](DefaultApi.md#search) | **GET** /api/v3/search | Search
[**search_epics**](DefaultApi.md#search_epics) | **GET** /api/v3/search/epics | Search Epics
[**search_stories**](DefaultApi.md#search_stories) | **GET** /api/v3/search/stories | Search Stories
[**search_stories_old**](DefaultApi.md#search_stories_old) | **POST** /api/v3/stories/search | Search Stories (Old)
[**story_history**](DefaultApi.md#story_history) | **GET** /api/v3/stories/{story-public-id}/history | Story History
[**unlink_productboard_from_epic**](DefaultApi.md#unlink_productboard_from_epic) | **POST** /api/v3/epics/{epic-public-id}/unlink-productboard | Unlink Productboard from Epic
[**update_category**](DefaultApi.md#update_category) | **PUT** /api/v3/categories/{category-public-id} | Update Category
[**update_entity_template**](DefaultApi.md#update_entity_template) | **PUT** /api/v3/entity-templates/{entity-template-public-id} | Update Entity Template
[**update_epic**](DefaultApi.md#update_epic) | **PUT** /api/v3/epics/{epic-public-id} | Update Epic
[**update_epic_comment**](DefaultApi.md#update_epic_comment) | **PUT** /api/v3/epics/{epic-public-id}/comments/{comment-public-id} | Update Epic Comment
[**update_file**](DefaultApi.md#update_file) | **PUT** /api/v3/files/{file-public-id} | Update File
[**update_group**](DefaultApi.md#update_group) | **PUT** /api/v3/groups/{group-public-id} | Update Group
[**update_iteration**](DefaultApi.md#update_iteration) | **PUT** /api/v3/iterations/{iteration-public-id} | Update Iteration
[**update_label**](DefaultApi.md#update_label) | **PUT** /api/v3/labels/{label-public-id} | Update Label
[**update_linked_file**](DefaultApi.md#update_linked_file) | **PUT** /api/v3/linked-files/{linked-file-public-id} | Update Linked File
[**update_milestone**](DefaultApi.md#update_milestone) | **PUT** /api/v3/milestones/{milestone-public-id} | Update Milestone
[**update_multiple_stories**](DefaultApi.md#update_multiple_stories) | **PUT** /api/v3/stories/bulk | Update Multiple Stories
[**update_project**](DefaultApi.md#update_project) | **PUT** /api/v3/projects/{project-public-id} | Update Project
[**update_story**](DefaultApi.md#update_story) | **PUT** /api/v3/stories/{story-public-id} | Update Story
[**update_story_comment**](DefaultApi.md#update_story_comment) | **PUT** /api/v3/stories/{story-public-id}/comments/{comment-public-id} | Update Story Comment
[**update_story_link**](DefaultApi.md#update_story_link) | **PUT** /api/v3/story-links/{story-link-public-id} | Update Story Link
[**update_task**](DefaultApi.md#update_task) | **PUT** /api/v3/stories/{story-public-id}/tasks/{task-public-id} | Update Task
[**upload_files**](DefaultApi.md#upload_files) | **POST** /api/v3/files | Upload Files

# **create_category**
> Category create_category(body)

Create Category

Create Category allows you to create a new Category in Shortcut.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateCategory() # CreateCategory | 

try:
    # Create Category
    api_response = api_instance.create_category(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCategory**](CreateCategory.md)|  | 

### Return type

[**Category**](Category.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity_template**
> EntityTemplate create_entity_template(body)

Create Entity Template

Create a new entity template for the Workspace.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateEntityTemplate() # CreateEntityTemplate | Request paramaters for creating an entirely new entity template.

try:
    # Create Entity Template
    api_response = api_instance.create_entity_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_entity_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEntityTemplate**](CreateEntityTemplate.md)| Request paramaters for creating an entirely new entity template. | 

### Return type

[**EntityTemplate**](EntityTemplate.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_epic**
> Epic create_epic(body)

Create Epic

Create Epic allows you to create a new Epic in Shortcut.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateEpic() # CreateEpic | 

try:
    # Create Epic
    api_response = api_instance.create_epic(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_epic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEpic**](CreateEpic.md)|  | 

### Return type

[**Epic**](Epic.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_epic_comment**
> ThreadedComment create_epic_comment(body, epic_public_id)

Create Epic Comment

This endpoint allows you to create a threaded Comment on an Epic.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateEpicComment() # CreateEpicComment | 
epic_public_id = 789 # int | The ID of the associated Epic.

try:
    # Create Epic Comment
    api_response = api_instance.create_epic_comment(body, epic_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_epic_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEpicComment**](CreateEpicComment.md)|  | 
 **epic_public_id** | **int**| The ID of the associated Epic. | 

### Return type

[**ThreadedComment**](ThreadedComment.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_epic_comment_comment**
> ThreadedComment create_epic_comment_comment(body, epic_public_id, comment_public_id)

Create Epic Comment Comment

This endpoint allows you to create a nested Comment reply to an existing Epic Comment.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateCommentComment() # CreateCommentComment | 
epic_public_id = 789 # int | The ID of the associated Epic.
comment_public_id = 789 # int | The ID of the parent Epic Comment.

try:
    # Create Epic Comment Comment
    api_response = api_instance.create_epic_comment_comment(body, epic_public_id, comment_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_epic_comment_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCommentComment**](CreateCommentComment.md)|  | 
 **epic_public_id** | **int**| The ID of the associated Epic. | 
 **comment_public_id** | **int**| The ID of the parent Epic Comment. | 

### Return type

[**ThreadedComment**](ThreadedComment.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> Group create_group(body)

Create Group

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateGroup() # CreateGroup | 

try:
    # Create Group
    api_response = api_instance.create_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateGroup**](CreateGroup.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iteration**
> Iteration create_iteration(body)

Create Iteration

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateIteration() # CreateIteration | 

try:
    # Create Iteration
    api_response = api_instance.create_iteration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iteration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateIteration**](CreateIteration.md)|  | 

### Return type

[**Iteration**](Iteration.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_label**
> Label create_label(body)

Create Label

Create Label allows you to create a new Label in Shortcut.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateLabelParams() # CreateLabelParams | Request parameters for creating a Label on a Shortcut Story.

try:
    # Create Label
    api_response = api_instance.create_label(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLabelParams**](CreateLabelParams.md)| Request parameters for creating a Label on a Shortcut Story. | 

### Return type

[**Label**](Label.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_linked_file**
> LinkedFile create_linked_file(body)

Create Linked File

Create Linked File allows you to create a new Linked File in Shortcut.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateLinkedFile() # CreateLinkedFile | 

try:
    # Create Linked File
    api_response = api_instance.create_linked_file(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_linked_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLinkedFile**](CreateLinkedFile.md)|  | 

### Return type

[**LinkedFile**](LinkedFile.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_milestone**
> Milestone create_milestone(body)

Create Milestone

Create Milestone allows you to create a new Milestone in Shortcut.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateMilestone() # CreateMilestone | 

try:
    # Create Milestone
    api_response = api_instance.create_milestone(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_milestone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMilestone**](CreateMilestone.md)|  | 

### Return type

[**Milestone**](Milestone.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multiple_stories**
> list[StorySlim] create_multiple_stories(body)

Create Multiple Stories

Create Multiple Stories allows you to create multiple stories in a single request using the same syntax as [Create Story](https://shortcut.com/api/#create-story).

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateStories() # CreateStories | 

try:
    # Create Multiple Stories
    api_response = api_instance.create_multiple_stories(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_multiple_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateStories**](CreateStories.md)|  | 

### Return type

[**list[StorySlim]**](StorySlim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> Project create_project(body)

Create Project

Create Project is used to create a new Shortcut Project.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateProject() # CreateProject | 

try:
    # Create Project
    api_response = api_instance.create_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProject**](CreateProject.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_story**
> Story create_story(body)

Create Story

Create Story is used to add a new story to your Shortcut.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateStoryParams() # CreateStoryParams | Request parameters for creating a story.

try:
    # Create Story
    api_response = api_instance.create_story(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_story: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateStoryParams**](CreateStoryParams.md)| Request parameters for creating a story. | 

### Return type

[**Story**](Story.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_story_comment**
> StoryComment create_story_comment(body, story_public_id)

Create Story Comment

Create Comment allows you to create a Comment on any Story.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateStoryComment() # CreateStoryComment | 
story_public_id = 789 # int | The ID of the Story that the Comment is in.

try:
    # Create Story Comment
    api_response = api_instance.create_story_comment(body, story_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_story_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateStoryComment**](CreateStoryComment.md)|  | 
 **story_public_id** | **int**| The ID of the Story that the Comment is in. | 

### Return type

[**StoryComment**](StoryComment.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_story_link**
> StoryLink create_story_link(body)

Create Story Link

Story Links (called Story Relationships in the UI) allow you create semantic relationships between two stories. The parameters read like an active voice grammatical sentence:  subject -> verb -> object.  The subject story acts on the object Story; the object story is the direct object of the sentence.  The subject story \"blocks\", \"duplicates\", or \"relates to\" the object story.  Examples: - \"story 5 blocks story 6” -- story 6 is now \"blocked\" until story 5 is moved to a Done workflow state. - \"story 2 duplicates story 1” -- Story 2 represents the same body of work as Story 1 (and should probably be archived). - \"story 7 relates to story 3”

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateStoryLink() # CreateStoryLink | 

try:
    # Create Story Link
    api_response = api_instance.create_story_link(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_story_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateStoryLink**](CreateStoryLink.md)|  | 

### Return type

[**StoryLink**](StoryLink.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_story_reaction**
> list[StoryReaction] create_story_reaction(body, story_public_id, comment_public_id)

Create Story Reaction

Create a reaction to a story comment.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateOrDeleteStoryReaction() # CreateOrDeleteStoryReaction | 
story_public_id = 789 # int | The ID of the Story that the Comment is in.
comment_public_id = 789 # int | The ID of the Comment.

try:
    # Create Story Reaction
    api_response = api_instance.create_story_reaction(body, story_public_id, comment_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_story_reaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrDeleteStoryReaction**](CreateOrDeleteStoryReaction.md)|  | 
 **story_public_id** | **int**| The ID of the Story that the Comment is in. | 
 **comment_public_id** | **int**| The ID of the Comment. | 

### Return type

[**list[StoryReaction]**](StoryReaction.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task**
> Task create_task(body, story_public_id)

Create Task

Create Task is used to create a new task in a Story.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateTask() # CreateTask | 
story_public_id = 789 # int | The ID of the Story that the Task will be in.

try:
    # Create Task
    api_response = api_instance.create_task(body, story_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTask**](CreateTask.md)|  | 
 **story_public_id** | **int**| The ID of the Story that the Task will be in. | 

### Return type

[**Task**](Task.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category**
> delete_category(category_public_id)

Delete Category

Delete Category can be used to delete any Category.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
category_public_id = 789 # int | The unique ID of the Category.

try:
    # Delete Category
    api_instance.delete_category(category_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_public_id** | **int**| The unique ID of the Category. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity_template**
> delete_entity_template(entity_template_public_id)

Delete Entity Template

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
entity_template_public_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique ID of the entity template.

try:
    # Delete Entity Template
    api_instance.delete_entity_template(entity_template_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_entity_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_template_public_id** | [**str**](.md)| The unique ID of the entity template. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_epic**
> delete_epic(epic_public_id)

Delete Epic

Delete Epic can be used to delete the Epic. The only required parameter is Epic ID.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
epic_public_id = 789 # int | The unique ID of the Epic.

try:
    # Delete Epic
    api_instance.delete_epic(epic_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_epic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **epic_public_id** | **int**| The unique ID of the Epic. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_epic_comment**
> delete_epic_comment(epic_public_id, comment_public_id)

Delete Epic Comment

This endpoint allows you to delete a Comment from an Epic.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
epic_public_id = 789 # int | The ID of the associated Epic.
comment_public_id = 789 # int | The ID of the Comment.

try:
    # Delete Epic Comment
    api_instance.delete_epic_comment(epic_public_id, comment_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_epic_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **epic_public_id** | **int**| The ID of the associated Epic. | 
 **comment_public_id** | **int**| The ID of the Comment. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(file_public_id)

Delete File

Delete File deletes a previously uploaded file.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
file_public_id = 789 # int | The File’s unique ID.

try:
    # Delete File
    api_instance.delete_file(file_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_public_id** | **int**| The File’s unique ID. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iteration**
> delete_iteration(iteration_public_id)

Delete Iteration

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
iteration_public_id = 789 # int | The unique ID of the Iteration.

try:
    # Delete Iteration
    api_instance.delete_iteration(iteration_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iteration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iteration_public_id** | **int**| The unique ID of the Iteration. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_label**
> delete_label(label_public_id)

Delete Label

Delete Label can be used to delete any Label.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
label_public_id = 789 # int | The unique ID of the Label.

try:
    # Delete Label
    api_instance.delete_label(label_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_public_id** | **int**| The unique ID of the Label. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_linked_file**
> delete_linked_file(linked_file_public_id)

Delete Linked File

Delete Linked File can be used to delete any previously attached Linked-File.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
linked_file_public_id = 789 # int | The unique identifier of the linked file.

try:
    # Delete Linked File
    api_instance.delete_linked_file(linked_file_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_linked_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_file_public_id** | **int**| The unique identifier of the linked file. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_milestone**
> delete_milestone(milestone_public_id)

Delete Milestone

Delete Milestone can be used to delete any Milestone.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
milestone_public_id = 789 # int | The ID of the Milestone.

try:
    # Delete Milestone
    api_instance.delete_milestone(milestone_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_milestone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **milestone_public_id** | **int**| The ID of the Milestone. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_multiple_stories**
> delete_multiple_stories(body)

Delete Multiple Stories

Delete Multiple Stories allows you to delete multiple archived stories at once.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.DeleteStories() # DeleteStories | 

try:
    # Delete Multiple Stories
    api_instance.delete_multiple_stories(body)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_multiple_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteStories**](DeleteStories.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_public_id)

Delete Project

Delete Project can be used to delete a Project. Projects can only be deleted if all associated Stories are moved or deleted. In the case that the Project cannot be deleted, you will receive a 422 response.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
project_public_id = 789 # int | The unique ID of the Project.

try:
    # Delete Project
    api_instance.delete_project(project_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_public_id** | **int**| The unique ID of the Project. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_story**
> delete_story(story_public_id)

Delete Story

Delete Story can be used to delete any Story.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
story_public_id = 789 # int | The ID of the Story.

try:
    # Delete Story
    api_instance.delete_story(story_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_story: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_public_id** | **int**| The ID of the Story. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_story_comment**
> delete_story_comment(story_public_id, comment_public_id)

Delete Story Comment

Delete a Comment from any story.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
story_public_id = 789 # int | The ID of the Story that the Comment is in.
comment_public_id = 789 # int | The ID of the Comment.

try:
    # Delete Story Comment
    api_instance.delete_story_comment(story_public_id, comment_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_story_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_public_id** | **int**| The ID of the Story that the Comment is in. | 
 **comment_public_id** | **int**| The ID of the Comment. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_story_link**
> delete_story_link(story_link_public_id)

Delete Story Link

Removes the relationship between the stories for the given Story Link.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
story_link_public_id = 789 # int | The unique ID of the Story Link.

try:
    # Delete Story Link
    api_instance.delete_story_link(story_link_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_story_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_link_public_id** | **int**| The unique ID of the Story Link. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_story_reaction**
> delete_story_reaction(body, story_public_id, comment_public_id)

Delete Story Reaction

Delete a reaction from any story comment.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.CreateOrDeleteStoryReaction() # CreateOrDeleteStoryReaction | 
story_public_id = 789 # int | The ID of the Story that the Comment is in.
comment_public_id = 789 # int | The ID of the Comment.

try:
    # Delete Story Reaction
    api_instance.delete_story_reaction(body, story_public_id, comment_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_story_reaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrDeleteStoryReaction**](CreateOrDeleteStoryReaction.md)|  | 
 **story_public_id** | **int**| The ID of the Story that the Comment is in. | 
 **comment_public_id** | **int**| The ID of the Comment. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> delete_task(story_public_id, task_public_id)

Delete Task

Delete Task can be used to delete any previously created Task on a Story.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
story_public_id = 789 # int | The unique ID of the Story this Task is associated with.
task_public_id = 789 # int | The unique ID of the Task.

try:
    # Delete Task
    api_instance.delete_task(story_public_id, task_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_public_id** | **int**| The unique ID of the Story this Task is associated with. | 
 **task_public_id** | **int**| The unique ID of the Task. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_groups**
> disable_groups()

Disable Groups

Disables Groups for the current workspace2

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # Disable Groups
    api_instance.disable_groups()
except ApiException as e:
    print("Exception when calling DefaultApi->disable_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_iterations**
> disable_iterations()

Disable Iterations

Disables Iterations for the current workspace

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # Disable Iterations
    api_instance.disable_iterations()
except ApiException as e:
    print("Exception when calling DefaultApi->disable_iterations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_story_templates**
> disable_story_templates()

Disable Story Templates

Disables the Story Template feature for the Workspace.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # Disable Story Templates
    api_instance.disable_story_templates()
except ApiException as e:
    print("Exception when calling DefaultApi->disable_story_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_groups**
> enable_groups()

Enable Groups

Enables Groups for the current workspace2

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # Enable Groups
    api_instance.enable_groups()
except ApiException as e:
    print("Exception when calling DefaultApi->enable_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_iterations**
> enable_iterations()

Enable Iterations

Enables Iterations for the current workspace

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # Enable Iterations
    api_instance.enable_iterations()
except ApiException as e:
    print("Exception when calling DefaultApi->enable_iterations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_story_templates**
> enable_story_templates()

Enable Story Templates

Enables the Story Template feature for the Workspace.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # Enable Story Templates
    api_instance.enable_story_templates()
except ApiException as e:
    print("Exception when calling DefaultApi->enable_story_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category**
> Category get_category(category_public_id)

Get Category

Get Category returns information about the selected Category.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
category_public_id = 789 # int | The unique ID of the Category.

try:
    # Get Category
    api_response = api_instance.get_category(category_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_public_id** | **int**| The unique ID of the Category. | 

### Return type

[**Category**](Category.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_member_info**
> MemberInfo get_current_member_info()

Get Current Member Info

Returns information about the authenticated member.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # Get Current Member Info
    api_response = api_instance.get_current_member_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_current_member_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MemberInfo**](MemberInfo.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_template**
> EntityTemplate get_entity_template(entity_template_public_id)

Get Entity Template

Get Entity Template returns information about a given entity template.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
entity_template_public_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique ID of the entity template.

try:
    # Get Entity Template
    api_response = api_instance.get_entity_template(entity_template_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_entity_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_template_public_id** | [**str**](.md)| The unique ID of the entity template. | 

### Return type

[**EntityTemplate**](EntityTemplate.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_epic**
> Epic get_epic(epic_public_id)

Get Epic

Get Epic returns information about the selected Epic.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
epic_public_id = 789 # int | The unique ID of the Epic.

try:
    # Get Epic
    api_response = api_instance.get_epic(epic_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_epic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **epic_public_id** | **int**| The unique ID of the Epic. | 

### Return type

[**Epic**](Epic.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_epic_comment**
> ThreadedComment get_epic_comment(epic_public_id, comment_public_id)

Get Epic Comment

This endpoint returns information about the selected Epic Comment.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
epic_public_id = 789 # int | The ID of the associated Epic.
comment_public_id = 789 # int | The ID of the Comment.

try:
    # Get Epic Comment
    api_response = api_instance.get_epic_comment(epic_public_id, comment_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_epic_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **epic_public_id** | **int**| The ID of the associated Epic. | 
 **comment_public_id** | **int**| The ID of the Comment. | 

### Return type

[**ThreadedComment**](ThreadedComment.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_epic_workflow**
> EpicWorkflow get_epic_workflow()

Get Epic Workflow

Returns the Epic Workflow for the Workspace.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # Get Epic Workflow
    api_response = api_instance.get_epic_workflow()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_epic_workflow: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EpicWorkflow**](EpicWorkflow.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_link_stories**
> list[StorySlim] get_external_link_stories(body)

Get External Link Stories

Get Stories which have a given External Link associated with them.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.GetExternalLinkStoriesParams() # GetExternalLinkStoriesParams | 

try:
    # Get External Link Stories
    api_response = api_instance.get_external_link_stories(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_external_link_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetExternalLinkStoriesParams**](GetExternalLinkStoriesParams.md)|  | 

### Return type

[**list[StorySlim]**](StorySlim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> UploadedFile get_file(file_public_id)

Get File

Get File returns information about the selected UploadedFile.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
file_public_id = 789 # int | The File’s unique ID.

try:
    # Get File
    api_response = api_instance.get_file(file_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_public_id** | **int**| The File’s unique ID. | 

### Return type

[**UploadedFile**](UploadedFile.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(group_public_id)

Get Group

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
group_public_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique ID of the Group.

try:
    # Get Group
    api_response = api_instance.get_group(group_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_public_id** | [**str**](.md)| The unique ID of the Group. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_iteration**
> Iteration get_iteration(iteration_public_id)

Get Iteration

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
iteration_public_id = 789 # int | The unique ID of the Iteration.

try:
    # Get Iteration
    api_response = api_instance.get_iteration(iteration_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_iteration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iteration_public_id** | **int**| The unique ID of the Iteration. | 

### Return type

[**Iteration**](Iteration.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_label**
> Label get_label(label_public_id)

Get Label

Get Label returns information about the selected Label.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
label_public_id = 789 # int | The unique ID of the Label.

try:
    # Get Label
    api_response = api_instance.get_label(label_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_public_id** | **int**| The unique ID of the Label. | 

### Return type

[**Label**](Label.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_file**
> LinkedFile get_linked_file(linked_file_public_id)

Get Linked File

Get File returns information about the selected Linked File.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
linked_file_public_id = 789 # int | The unique identifier of the linked file.

try:
    # Get Linked File
    api_response = api_instance.get_linked_file(linked_file_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_linked_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_file_public_id** | **int**| The unique identifier of the linked file. | 

### Return type

[**LinkedFile**](LinkedFile.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member**
> Member get_member(body, member_public_id)

Get Member

Returns information about a Member.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.GetMember() # GetMember | 
member_public_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Member's unique ID.

try:
    # Get Member
    api_response = api_instance.get_member(body, member_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetMember**](GetMember.md)|  | 
 **member_public_id** | [**str**](.md)| The Member&#x27;s unique ID. | 

### Return type

[**Member**](Member.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_milestone**
> Milestone get_milestone(milestone_public_id)

Get Milestone

Get Milestone returns information about a chosen Milestone.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
milestone_public_id = 789 # int | The ID of the Milestone.

try:
    # Get Milestone
    api_response = api_instance.get_milestone(milestone_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_milestone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **milestone_public_id** | **int**| The ID of the Milestone. | 

### Return type

[**Milestone**](Milestone.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(project_public_id)

Get Project

Get Project returns information about the selected Project.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
project_public_id = 789 # int | The unique ID of the Project.

try:
    # Get Project
    api_response = api_instance.get_project(project_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_public_id** | **int**| The unique ID of the Project. | 

### Return type

[**Project**](Project.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository**
> Repository get_repository(repo_public_id)

Get Repository

Get Repository returns information about the selected Repository.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
repo_public_id = 789 # int | The unique ID of the Repository.

try:
    # Get Repository
    api_response = api_instance.get_repository(repo_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_public_id** | **int**| The unique ID of the Repository. | 

### Return type

[**Repository**](Repository.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_story**
> Story get_story(story_public_id)

Get Story

Get Story returns information about a chosen Story.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
story_public_id = 789 # int | The ID of the Story.

try:
    # Get Story
    api_response = api_instance.get_story(story_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_story: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_public_id** | **int**| The ID of the Story. | 

### Return type

[**Story**](Story.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_story_comment**
> StoryComment get_story_comment(story_public_id, comment_public_id)

Get Story Comment

Get Comment is used to get Comment information.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
story_public_id = 789 # int | The ID of the Story that the Comment is in.
comment_public_id = 789 # int | The ID of the Comment.

try:
    # Get Story Comment
    api_response = api_instance.get_story_comment(story_public_id, comment_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_story_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_public_id** | **int**| The ID of the Story that the Comment is in. | 
 **comment_public_id** | **int**| The ID of the Comment. | 

### Return type

[**StoryComment**](StoryComment.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_story_link**
> StoryLink get_story_link(story_link_public_id)

Get Story Link

Returns the stories and their relationship for the given Story Link.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
story_link_public_id = 789 # int | The unique ID of the Story Link.

try:
    # Get Story Link
    api_response = api_instance.get_story_link(story_link_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_story_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_link_public_id** | **int**| The unique ID of the Story Link. | 

### Return type

[**StoryLink**](StoryLink.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> Task get_task(story_public_id, task_public_id)

Get Task

Returns information about a chosen Task.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
story_public_id = 789 # int | The unique ID of the Story this Task is associated with.
task_public_id = 789 # int | The unique ID of the Task.

try:
    # Get Task
    api_response = api_instance.get_task(story_public_id, task_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_public_id** | **int**| The unique ID of the Story this Task is associated with. | 
 **task_public_id** | **int**| The unique ID of the Task. | 

### Return type

[**Task**](Task.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow**
> Workflow get_workflow(workflow_public_id)

Get Workflow

Get Workflow returns information about a chosen Workflow.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
workflow_public_id = 789 # int | The ID of the Workflow.

try:
    # Get Workflow
    api_response = api_instance.get_workflow(workflow_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_public_id** | **int**| The ID of the Workflow. | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_categories**
> list[Category] list_categories()

List Categories

List Categories returns a list of all Categories and their attributes.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # List Categories
    api_response = api_instance.list_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Category]**](Category.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_category_milestones**
> list[Milestone] list_category_milestones(category_public_id)

List Category Milestones

List Category Milestones returns a list of all Milestones with the Category.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
category_public_id = 789 # int | The unique ID of the Category.

try:
    # List Category Milestones
    api_response = api_instance.list_category_milestones(category_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_category_milestones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_public_id** | **int**| The unique ID of the Category. | 

### Return type

[**list[Milestone]**](Milestone.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entity_templates**
> list[EntityTemplate] list_entity_templates()

List Entity Templates

List all the entity templates for the Workspace.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # List Entity Templates
    api_response = api_instance.list_entity_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_entity_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EntityTemplate]**](EntityTemplate.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_epic_comments**
> list[ThreadedComment] list_epic_comments(epic_public_id)

List Epic Comments

Get a list of all Comments on an Epic.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
epic_public_id = 789 # int | The unique ID of the Epic.

try:
    # List Epic Comments
    api_response = api_instance.list_epic_comments(epic_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_epic_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **epic_public_id** | **int**| The unique ID of the Epic. | 

### Return type

[**list[ThreadedComment]**](ThreadedComment.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_epic_stories**
> list[StorySlim] list_epic_stories(body, epic_public_id)

List Epic Stories

Get a list of all Stories in an Epic.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.GetEpicStories() # GetEpicStories | 
epic_public_id = 789 # int | The unique ID of the Epic.

try:
    # List Epic Stories
    api_response = api_instance.list_epic_stories(body, epic_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_epic_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetEpicStories**](GetEpicStories.md)|  | 
 **epic_public_id** | **int**| The unique ID of the Epic. | 

### Return type

[**list[StorySlim]**](StorySlim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_epics**
> list[EpicSlim] list_epics(body)

List Epics

List Epics returns a list of all Epics and their attributes.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.ListEpics() # ListEpics | 

try:
    # List Epics
    api_response = api_instance.list_epics(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_epics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListEpics**](ListEpics.md)|  | 

### Return type

[**list[EpicSlim]**](EpicSlim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> list[UploadedFile] list_files()

List Files

List Files returns a list of all UploadedFiles in the workspace.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # List Files
    api_response = api_instance.list_files()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_files: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UploadedFile]**](UploadedFile.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_stories**
> list[StorySlim] list_group_stories(body, group_public_id)

List Group Stories

List the Stories assigned to the Group. (By default, limited to 1,000).

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.ListGroupStories() # ListGroupStories | 
group_public_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique ID of the Group.

try:
    # List Group Stories
    api_response = api_instance.list_group_stories(body, group_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_group_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListGroupStories**](ListGroupStories.md)|  | 
 **group_public_id** | [**str**](.md)| The unique ID of the Group. | 

### Return type

[**list[StorySlim]**](StorySlim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> list[Group] list_groups()

List Groups

A group in our API maps to a \"Team\" within the Shortcut Product. A Team is a collection of Users that can be associated to Stories, Epics, and Iterations within Shortcut.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # List Groups
    api_response = api_instance.list_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Group]**](Group.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_iteration_stories**
> list[StorySlim] list_iteration_stories(body, iteration_public_id)

List Iteration Stories

Get a list of all Stories in an Iteration.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.GetIterationStories() # GetIterationStories | 
iteration_public_id = 789 # int | The unique ID of the Iteration.

try:
    # List Iteration Stories
    api_response = api_instance.list_iteration_stories(body, iteration_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_iteration_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetIterationStories**](GetIterationStories.md)|  | 
 **iteration_public_id** | **int**| The unique ID of the Iteration. | 

### Return type

[**list[StorySlim]**](StorySlim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_iterations**
> list[IterationSlim] list_iterations()

List Iterations

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # List Iterations
    api_response = api_instance.list_iterations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_iterations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[IterationSlim]**](IterationSlim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_label_epics**
> list[EpicSlim] list_label_epics(label_public_id)

List Label Epics

List all of the Epics with the Label.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
label_public_id = 789 # int | The unique ID of the Label.

try:
    # List Label Epics
    api_response = api_instance.list_label_epics(label_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_label_epics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_public_id** | **int**| The unique ID of the Label. | 

### Return type

[**list[EpicSlim]**](EpicSlim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_label_stories**
> list[StorySlim] list_label_stories(body, label_public_id)

List Label Stories

List all of the Stories with the Label.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.GetLabelStories() # GetLabelStories | 
label_public_id = 789 # int | The unique ID of the Label.

try:
    # List Label Stories
    api_response = api_instance.list_label_stories(body, label_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_label_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetLabelStories**](GetLabelStories.md)|  | 
 **label_public_id** | **int**| The unique ID of the Label. | 

### Return type

[**list[StorySlim]**](StorySlim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_labels**
> list[Label] list_labels(body)

List Labels

List Labels returns a list of all Labels and their attributes.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.ListLabels() # ListLabels | 

try:
    # List Labels
    api_response = api_instance.list_labels(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListLabels**](ListLabels.md)|  | 

### Return type

[**list[Label]**](Label.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_linked_files**
> list[LinkedFile] list_linked_files()

List Linked Files

List Linked Files returns a list of all Linked-Files and their attributes.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # List Linked Files
    api_response = api_instance.list_linked_files()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_linked_files: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LinkedFile]**](LinkedFile.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_members**
> list[Member] list_members(body)

List Members

Returns information about members of the Workspace.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.ListMembers() # ListMembers | 

try:
    # List Members
    api_response = api_instance.list_members(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListMembers**](ListMembers.md)|  | 

### Return type

[**list[Member]**](Member.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_milestone_epics**
> list[EpicSlim] list_milestone_epics(milestone_public_id)

List Milestone Epics

List all of the Epics within the Milestone.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
milestone_public_id = 789 # int | The ID of the Milestone.

try:
    # List Milestone Epics
    api_response = api_instance.list_milestone_epics(milestone_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_milestone_epics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **milestone_public_id** | **int**| The ID of the Milestone. | 

### Return type

[**list[EpicSlim]**](EpicSlim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_milestones**
> list[Milestone] list_milestones()

List Milestones

List Milestones returns a list of all Milestones and their attributes.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # List Milestones
    api_response = api_instance.list_milestones()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_milestones: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Milestone]**](Milestone.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> list[Project] list_projects()

List Projects

List Projects returns a list of all Projects and their attributes.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # List Projects
    api_response = api_instance.list_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Project]**](Project.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repositories**
> list[Repository] list_repositories()

List Repositories

List Repositories returns a list of all Repositories and their attributes.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # List Repositories
    api_response = api_instance.list_repositories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_repositories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Repository]**](Repository.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stories**
> list[StorySlim] list_stories(body, project_public_id)

List Stories

List Stories returns a list of all Stories in a selected Project and their attributes.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.GetProjectStories() # GetProjectStories | 
project_public_id = 789 # int | The unique ID of the Project.

try:
    # List Stories
    api_response = api_instance.list_stories(body, project_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetProjectStories**](GetProjectStories.md)|  | 
 **project_public_id** | **int**| The unique ID of the Project. | 

### Return type

[**list[StorySlim]**](StorySlim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflows**
> list[Workflow] list_workflows()

List Workflows

Returns a list of all Workflows in the Workspace.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))

try:
    # List Workflows
    api_response = api_instance.list_workflows()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_workflows: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Workflow]**](Workflow.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SearchResults search(body)

Search

Search lets you search Epics and Stories based on desired parameters. Since ordering of the results can change over time (due to search ranking decay, new Epics and Stories being created), the `next` value from the previous response can be used as the path and query string for the next page to ensure stable ordering.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.Search() # Search | 

try:
    # Search
    api_response = api_instance.search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Search**](Search.md)|  | 

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_epics**
> EpicSearchResults search_epics(body)

Search Epics

Search Epics lets you search Epics based on desired parameters. Since ordering of stories can change over time (due to search ranking decay, new Epics being created), the `next` value from the previous response can be used as the path and query string for the next page to ensure stable ordering.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.Search() # Search | 

try:
    # Search Epics
    api_response = api_instance.search_epics(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_epics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Search**](Search.md)|  | 

### Return type

[**EpicSearchResults**](EpicSearchResults.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_stories**
> StorySearchResults search_stories(body)

Search Stories

Search Stories lets you search Stories based on desired parameters. Since ordering of stories can change over time (due to search ranking decay, new stories being created), the `next` value from the previous response can be used as the path and query string for the next page to ensure stable ordering.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.Search() # Search | 

try:
    # Search Stories
    api_response = api_instance.search_stories(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Search**](Search.md)|  | 

### Return type

[**StorySearchResults**](StorySearchResults.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_stories_old**
> list[StorySlim] search_stories_old(body)

Search Stories (Old)

Search Stories lets you search Stories based on desired parameters.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.SearchStories() # SearchStories | 

try:
    # Search Stories (Old)
    api_response = api_instance.search_stories_old(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_stories_old: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchStories**](SearchStories.md)|  | 

### Return type

[**list[StorySlim]**](StorySlim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **story_history**
> list[History] story_history(story_public_id)

Story History

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
story_public_id = 789 # int | The ID of the Story.

try:
    # Story History
    api_response = api_instance.story_history(story_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->story_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_public_id** | **int**| The ID of the Story. | 

### Return type

[**list[History]**](History.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_productboard_from_epic**
> unlink_productboard_from_epic(epic_public_id)

Unlink Productboard from Epic

This endpoint allows you to unlink a productboard epic.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
epic_public_id = 789 # int | The unique ID of the Epic.

try:
    # Unlink Productboard from Epic
    api_instance.unlink_productboard_from_epic(epic_public_id)
except ApiException as e:
    print("Exception when calling DefaultApi->unlink_productboard_from_epic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **epic_public_id** | **int**| The unique ID of the Epic. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category**
> Category update_category(body, category_public_id)

Update Category

Update Category allows you to replace a Category name with another name. If you try to name a Category something that already exists, you will receive a 422 response.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateCategory() # UpdateCategory | 
category_public_id = 789 # int | The unique ID of the Category you wish to update.

try:
    # Update Category
    api_response = api_instance.update_category(body, category_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCategory**](UpdateCategory.md)|  | 
 **category_public_id** | **int**| The unique ID of the Category you wish to update. | 

### Return type

[**Category**](Category.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity_template**
> EntityTemplate update_entity_template(body, entity_template_public_id)

Update Entity Template

Update an entity template's name or its contents.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateEntityTemplate() # UpdateEntityTemplate | Request parameters for changing either a template's name or any of
  the attributes it is designed to pre-populate.
entity_template_public_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique ID of the template to be updated.

try:
    # Update Entity Template
    api_response = api_instance.update_entity_template(body, entity_template_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_entity_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateEntityTemplate**](UpdateEntityTemplate.md)| Request parameters for changing either a template&#x27;s name or any of
  the attributes it is designed to pre-populate. | 
 **entity_template_public_id** | [**str**](.md)| The unique ID of the template to be updated. | 

### Return type

[**EntityTemplate**](EntityTemplate.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_epic**
> Epic update_epic(body, epic_public_id)

Update Epic

Update Epic can be used to update numerous fields in the Epic. The only required parameter is Epic ID, which can be found in the Shortcut UI.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateEpic() # UpdateEpic | 
epic_public_id = 789 # int | The unique ID of the Epic.

try:
    # Update Epic
    api_response = api_instance.update_epic(body, epic_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_epic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateEpic**](UpdateEpic.md)|  | 
 **epic_public_id** | **int**| The unique ID of the Epic. | 

### Return type

[**Epic**](Epic.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_epic_comment**
> ThreadedComment update_epic_comment(body, epic_public_id, comment_public_id)

Update Epic Comment

This endpoint allows you to update a threaded Comment on an Epic.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateComment() # UpdateComment | 
epic_public_id = 789 # int | The ID of the associated Epic.
comment_public_id = 789 # int | The ID of the Comment.

try:
    # Update Epic Comment
    api_response = api_instance.update_epic_comment(body, epic_public_id, comment_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_epic_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateComment**](UpdateComment.md)|  | 
 **epic_public_id** | **int**| The ID of the associated Epic. | 
 **comment_public_id** | **int**| The ID of the Comment. | 

### Return type

[**ThreadedComment**](ThreadedComment.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file**
> UploadedFile update_file(body, file_public_id)

Update File

Update File updates the properties of an UploadedFile (but not its content).

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateFile() # UpdateFile | 
file_public_id = 789 # int | The unique ID assigned to the file in Shortcut.

try:
    # Update File
    api_response = api_instance.update_file(body, file_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateFile**](UpdateFile.md)|  | 
 **file_public_id** | **int**| The unique ID assigned to the file in Shortcut. | 

### Return type

[**UploadedFile**](UploadedFile.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> Group update_group(body, group_public_id)

Update Group

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateGroup() # UpdateGroup | 
group_public_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique ID of the Group.

try:
    # Update Group
    api_response = api_instance.update_group(body, group_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateGroup**](UpdateGroup.md)|  | 
 **group_public_id** | [**str**](.md)| The unique ID of the Group. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iteration**
> Iteration update_iteration(body, iteration_public_id)

Update Iteration

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateIteration() # UpdateIteration | 
iteration_public_id = 789 # int | The unique ID of the Iteration.

try:
    # Update Iteration
    api_response = api_instance.update_iteration(body, iteration_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iteration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateIteration**](UpdateIteration.md)|  | 
 **iteration_public_id** | **int**| The unique ID of the Iteration. | 

### Return type

[**Iteration**](Iteration.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_label**
> Label update_label(body, label_public_id)

Update Label

Update Label allows you to replace a Label name with another name. If you try to name a Label something that already exists, you will receive a 422 response.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateLabel() # UpdateLabel | 
label_public_id = 789 # int | The unique ID of the Label you wish to update.

try:
    # Update Label
    api_response = api_instance.update_label(body, label_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateLabel**](UpdateLabel.md)|  | 
 **label_public_id** | **int**| The unique ID of the Label you wish to update. | 

### Return type

[**Label**](Label.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_linked_file**
> LinkedFile update_linked_file(body, linked_file_public_id)

Update Linked File

Updated Linked File allows you to update properties of a previously attached Linked-File.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateLinkedFile() # UpdateLinkedFile | 
linked_file_public_id = 789 # int | The unique identifier of the linked file.

try:
    # Update Linked File
    api_response = api_instance.update_linked_file(body, linked_file_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_linked_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateLinkedFile**](UpdateLinkedFile.md)|  | 
 **linked_file_public_id** | **int**| The unique identifier of the linked file. | 

### Return type

[**LinkedFile**](LinkedFile.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_milestone**
> Milestone update_milestone(body, milestone_public_id)

Update Milestone

Update Milestone can be used to update Milestone properties.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateMilestone() # UpdateMilestone | 
milestone_public_id = 789 # int | The ID of the Milestone.

try:
    # Update Milestone
    api_response = api_instance.update_milestone(body, milestone_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_milestone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateMilestone**](UpdateMilestone.md)|  | 
 **milestone_public_id** | **int**| The ID of the Milestone. | 

### Return type

[**Milestone**](Milestone.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_multiple_stories**
> list[StorySlim] update_multiple_stories(body)

Update Multiple Stories

Update Multiple Stories allows you to make changes to numerous stories at once.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateStories() # UpdateStories | 

try:
    # Update Multiple Stories
    api_response = api_instance.update_multiple_stories(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_multiple_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateStories**](UpdateStories.md)|  | 

### Return type

[**list[StorySlim]**](StorySlim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(body, project_public_id)

Update Project

Update Project can be used to change properties of a Project.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateProject() # UpdateProject | 
project_public_id = 789 # int | The unique ID of the Project.

try:
    # Update Project
    api_response = api_instance.update_project(body, project_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateProject**](UpdateProject.md)|  | 
 **project_public_id** | **int**| The unique ID of the Project. | 

### Return type

[**Project**](Project.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_story**
> Story update_story(body, story_public_id)

Update Story

Update Story can be used to update Story properties.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateStory() # UpdateStory | 
story_public_id = 789 # int | The unique identifier of this story.

try:
    # Update Story
    api_response = api_instance.update_story(body, story_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_story: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateStory**](UpdateStory.md)|  | 
 **story_public_id** | **int**| The unique identifier of this story. | 

### Return type

[**Story**](Story.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_story_comment**
> StoryComment update_story_comment(body, story_public_id, comment_public_id)

Update Story Comment

Update Comment replaces the text of the existing Comment.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateStoryComment() # UpdateStoryComment | 
story_public_id = 789 # int | The ID of the Story that the Comment is in.
comment_public_id = 789 # int | The ID of the Comment

try:
    # Update Story Comment
    api_response = api_instance.update_story_comment(body, story_public_id, comment_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_story_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateStoryComment**](UpdateStoryComment.md)|  | 
 **story_public_id** | **int**| The ID of the Story that the Comment is in. | 
 **comment_public_id** | **int**| The ID of the Comment | 

### Return type

[**StoryComment**](StoryComment.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_story_link**
> StoryLink update_story_link(body, story_link_public_id)

Update Story Link

Updates the stories and/or the relationship for the given Story Link.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateStoryLink() # UpdateStoryLink | 
story_link_public_id = 789 # int | The unique ID of the Story Link.

try:
    # Update Story Link
    api_response = api_instance.update_story_link(body, story_link_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_story_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateStoryLink**](UpdateStoryLink.md)|  | 
 **story_link_public_id** | **int**| The unique ID of the Story Link. | 

### Return type

[**StoryLink**](StoryLink.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> Task update_task(body, story_public_id, task_public_id)

Update Task

Update Task can be used to update Task properties.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
body = shortcut_client_py.UpdateTask() # UpdateTask | 
story_public_id = 789 # int | The unique identifier of the parent Story.
task_public_id = 789 # int | The unique identifier of the Task you wish to update.

try:
    # Update Task
    api_response = api_instance.update_task(body, story_public_id, task_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTask**](UpdateTask.md)|  | 
 **story_public_id** | **int**| The unique identifier of the parent Story. | 
 **task_public_id** | **int**| The unique identifier of the Task you wish to update. | 

### Return type

[**Task**](Task.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_files**
> list[UploadedFile] upload_files(story_id, file0, file1, file2, file3)

Upload Files

Upload Files uploads one or many files and optionally associates them with a story.    Use the multipart/form-data content-type to upload.    Each `file` key should contain a separate file.    Each UploadedFile's name comes from the Content-Disposition header \"filename\" directive for that field.

### Example
```python
from __future__ import print_function
import time
import shortcut_client_py
from shortcut_client_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = shortcut_client_py.Configuration()
configuration.api_key['Shortcut-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Shortcut-Token'] = 'Bearer'

# create an instance of the API class
api_instance = shortcut_client_py.DefaultApi(shortcut_client_py.ApiClient(configuration))
story_id = 789 # int | 
file0 = 'file0_example' # str | 
file1 = 'file1_example' # str | 
file2 = 'file2_example' # str | 
file3 = 'file3_example' # str | 

try:
    # Upload Files
    api_response = api_instance.upload_files(story_id, file0, file1, file2, file3)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_id** | **int**|  | 
 **file0** | **str**|  | 
 **file1** | **str**|  | 
 **file2** | **str**|  | 
 **file3** | **str**|  | 

### Return type

[**list[UploadedFile]**](UploadedFile.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

