from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . models import Books
from . serializers import BooksSerializer


@api_view(['GET','POST'])
def book_view(request):
    if  request.method == "GET":
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET','DELETE','PUT'])
def book_detail_view(request,pk):
    
    try:
        book = Books.objects.get(pk=pk)
    except Books.DoesNotExist:
        return Response({"error": "Book Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "GET":
        serializer = BooksSerializer(book)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        


    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
















# @api_view(['POST'])
# def book_add(request):






# @api_view(['POST'])
# def book_add(request):
#     title = request.data.get("title")
#     author = request.data.get("author")
#     price = request.data.get("price")

#     book = Books.objects.create(title=title,author=author,price=price)
#     print(book)

#     return Response(book)




