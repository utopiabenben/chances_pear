from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # 自定义动作示例
    @action(detail=True, methods=['get'])
    def contact_info(self, request, pk=None):
        customer = self.get_object()
        data = {
            "contact_person": customer.contact_person,
            "contact_email": customer.contact_email,
            "phone": customer.phone
        }
        return Response(data)

# Create your views here.
