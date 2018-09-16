app = angular.module 'chatbot.app.resource', ['chatbot.api']

app.controller 'ChatbotController', ['$scope', 'UserChatbot', ($scope, UserChatbot) ->
	$scope.messages = UserChatbot.query()
]
