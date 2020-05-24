from rest_framework.pagination import PageNumberPagination

from goods.serializer import GoodsSerializer
from .models import Goods
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .fiters import GoodsFilter



# class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView):
#     '商品列表页'
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer

    # def get(self,request,*args,**kwargs):
    #     return self.list(request,*args,**kwargs)
class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 10
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'p'
    #最多能显示多少页
    max_page_size = 100

# class GoodsListView(generics.ListAPIView):
#     '商品列表页'
#     pagination_class = GoodsPagination
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer


class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    '商品列表页,分页，搜索，过滤，排序'

    #这里必须要定义一个默认的排序,否则会报错
    queryset = Goods.objects.all().order_by('id')
    # 分页
    pagination_class = GoodsPagination
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)

    # 设置filter的类为我们自定义的类
    filter_class = GoodsFilter
    search_fields = ('name','goods_brief','goods_desc')
    order_fields = ('sold_num','add_time')

