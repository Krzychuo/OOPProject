class Observer:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Observer, cls).__new__(cls, *args, **kwargs) 
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.__subscriptions = {}

    def subscribe(self, name, obj):
        if not name in self.__subscriptions:
            self.__subscriptions[name] = []
        self.__subscriptions[name].append(obj)
    
    def notify(self, name, **kwargs):
        for subscriber in self.__subscriptions[name]:
            subscriber(**kwargs)

    def remove(self, name):
        if name in self.__subscriptions:
            del self.__subscriptions
        else:
            raise KeyError(f"No event with name {name}")
