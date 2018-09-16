app = angular.module 'chatbot.api', ['ngResource']

app.factory 'UserChatbot', ['$resource', ($resource) -> 
	$resource '/api/chatbot/:userid', userid: '@userid'
]
