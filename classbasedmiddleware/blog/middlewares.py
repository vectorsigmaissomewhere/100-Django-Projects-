class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization")
    
    def __call__(self, request):
        # code that runs before calling view 
        print("This is before view")
        response = self.get_response(request)
        print("This is after view")
        return response 