class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Brother Initialization")
    
    def __call__(self, request):
        # code that runs before calling view 
        print("This is Brother before view")
        response = self.get_response(request)
        print("This is Brother after view")
        return response 
    
class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Father Initialization")
    
    def __call__(self, request):
        # code that runs before calling view 
        print("This is Father before view")
        response = self.get_response(request)
        print("This is Father after view")
        return response 
    
class MommyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Mommy Initialization")
    
    def __call__(self, request):
        # code that runs before calling view 
        print("This is Mommy before view")
        response = self.get_response(request)
        print("This is Mommy after view")
        return response 