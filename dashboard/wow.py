

# class CreateClientView(APIView):
#     def post(self, request):
#         serializer = UserRegistrationSerializer(data=request.data) 
#         if serializer.is_valid(raise_exception=True):

#             try:
#                 url = "http://18.207.205.10/auth/user/create"
#                 data= {
#                 "first_name": serializer.validated_data['first_name'],
#                 "last_name": serializer.validated_data['last_name'],
#                 "email": serializer.validated_data['email'],
#                 "phone": serializer.validated_data['phone'],
#                 "password": serializer.validated_data['password'],
#                 "product_code": serializer.validated_data['product_code'],
#                 "client": serializer.validated_data['client'],
#                 "role": serializer.validated_data['role'],
#                 }

#                 response = requests.post(url=url, data=data)
#                 status = response.status_code
#                 if status == 400:
#                     return Response({'message': 'user already exists'}, status=400)
#                 else:
#                     serializer.create(validate_data=serializer.validated_data)
#                 return Response(response)
#             except requests.exceptions.InvalidSchema:
#                 print("The URL you provided is not a valid URL. Please check the URL and try again.")
#         return ValidationError
                
        
        
