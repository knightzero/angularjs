var app = angular.module('Todo', ['ng.django.websocket'])
    .config(function(djangoWebsocketProvider) {
        djangoWebsocketProvider.prefix('/ws');
    })
.controller('MyFormController', function($scope, $http, djangoWebsocket) {
    djangoWebsocket.connect($scope, ['subscribe-broadcast'], 'subscribe_data');
    $scope.loadtodos = function () {
        $scope.todos = []
        $http.get('/api/todo/?format=json').success(function(data) {
            $scope.todos = data.results;
        });
    }
    $scope.$watchCollection('subscribe_data',function(){
            $scope.loadtodos()
            $scope.subscribe_data = {}
        })
    $scope.loadtodos()
    $scope.getTotalTodos = function() {
        return $scope.todos.length;
    }
    
    $scope.clearCompleted = function () {
        _.each($scope.todos, function(data) {
            if (data.done) {
                $http.delete('/api/todo/' + data.id + '/')
            }
        });
        $scope.todos = _.where($scope.todos, {done:false});
    }
    
    $scope.addTodo = function () {
        $http.post('/api/todo/', {text:$scope.formTodoText, done:false}).success(function(data) {
            $scope.todos.push(data);
            $scope.formTodoText = '';
        });
    }
});