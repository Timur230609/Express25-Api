from rest_framework.pagination import PageNumberPagination

class StorePaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 2
    max_page_size = 100