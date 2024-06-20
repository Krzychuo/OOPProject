class Observer:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Observer, cls).__new__(cls, *args, **kwargs) 
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.subscribtions = {}

    def subscribe(self, name, obj):
        if not name in self.subscribtions:
            self.subscribtions[name] = []
        self.subscribtions[name].append(obj)
    
    def notify(self, name, **kwargs):
        for subscriber in self.subscribtions[name]:
            subscriber(**kwargs)
