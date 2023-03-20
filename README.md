# DjangoApp
## Background
This project is based on translation app which is part of assignment given to me. Its work is to store the translated version of simple ‘English’ texts of different articles to several Indian Languages. It has been designed in ‘Django’ framework and the database being used is ‘sqlite3’.  
	
### User credentials
1. Username - kunal, password - kunal, It is a super user and there are no groups assigned to this user. It is created to check basic admin functionalities like creating/modifying/deleting users, groups and raw entries in projects and sentences tables. 
2. Username - manager1, password - kunal021, It is a user which belongs to manager group. It is created to add new projects assign it to annotators, view all the existing projects.
3. Username - annotator1, password - kunal021, It is a user which belongs to annotator group. It is created to add new projects and view all the existing projects assigned to it.
4. Username - annotator2, password - kunal021, It is a user which belongs to annotator group. It is created to add new projects and view all the existing projects assigned to it.

### API’s
1. admin/ - (Method: GET) - Fetches the admin page(Predefined from Django)
2. project/ - (Method: GET) - Fetches all projects
3. project/ - (Method: POST) - Creates new project
4. projectcreated/ - (Method: GET) - It is re-directed after project is created. The user can either create a new project or list all active projects or log out directly. 
5. sentences/<int:projectId>/ - (Method: GET) - Fetches all sentences 
6. sentences/<int:projectId>/ - (Method: POST) - Saves the translated sentences.
7. listprojects/ -  (Method: GET) - It shows the list of all projects
8. sentenceupdated/ - (Method: GET) - It is re-directed after a translated sentence is updated.
9. logout/ - (Method: GET) - Log out the user (Predefined from Django)
10. ‘’ - (Method: GET) - It shows the list of all projects

### Models 
There are two models,
1. Project, which contains a PID as primary key, articleTitle, targetLanguage and annotator(The user who can edit this project).
2. Sentence, which contains a ProjectID as foreign key, sentenceId, originalSentence and translatedSentence.

### Apps
There are two apps created other than default apps, they are, projects and sentences.

## Flow
The overall flow is, first the user logs it from the home page. Then, the user can directly go to the dashboard by clicking on "view site" from top right and view all active projects that were assigned to him if the user is an annotator else if he is a manager he can view all projects. Next, The user can either create a new project(if it belongs to manager group) or edit a project assigned to him. After, editing the user can click on submit which will save the translations and the users can redirect to create a new project or move to the list of projects. The user can also log out from any page directly.

## Security
1. Any user who is not logged in cannot access any API.
2. Any user who does not belong to a manager group cannot create a new project.
3. Any user who is not been annotated a project cannot view or edit or update it. 

## Completed tasks(list)
Frontend task 1, Backend task 1, Backend task 2, Backend task 3, Frontend task 2, Backend task 4, Frontend task 3, Bonus-1, Bonus-2.
