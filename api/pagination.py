from rest_framework import pagination
from rest_framework.response import Response

class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'current_page_num': self.page.number,  #hozirgi turgan sahifaning raqamini ko`rsatadi
            'total_pages': self.page.paginator.num_pages, # umumiy sahifalar soni haqidagi ma`lumot chiqaradi
            'items_per_page': len(self.page), # bir sahifada nechta obyektlar mavjudligini ko`rsatadi
            'results': data
        })