from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.db.models import Q
import json
from .models import Order, ProductOrder, Payment


class OrderDetailView(View):
    def get(self, request, id):
        order = get_object_or_404(Order, id=id)
        json_response = {
            'customer': order.customer.username,
            'courier': order.courier.username if order.courier else None,
            'status': order.status,
            'total_price': float(order.total_price),
            'created_at': order.created_at,
            'updated_at': order.updated_at,
        }
        return JsonResponse(json_response)


class OrderListView(View):
    def get(self, request):
        orders = Order.objects.all()
        json_responses = []
        for order in orders:
            json_response = {
                'id': order.id,
                'customer': order.customer.username,
                'status': order.status,
                'total_price': float(order.total_price),
                'created_at': order.created_at,
            }
            json_responses.append(json_response)
        return JsonResponse(json_responses, safe=False)


class OrderDeleteView(View):
    def delete(self, request, id):
        order = get_object_or_404(Order, id=id)
        order_id = order.id
        order.delete()
        json_response = {
            'message': f'Order "{order_id}" has been successfully deleted.'
        }
        return JsonResponse(json_response, status=200)


class OrderUpdateView(View):
    def put(self, request, id):
        order = get_object_or_404(Order, id=id)
        data = json.loads(request.body)

        if 'status' in data and data['status'] in dict(Order.STATUS_CHOICES):
            order.status = data['status']
        if 'total_price' in data:
            order.total_price = data['total_price']

        order.save()
        json_response = {
            'message': f'Order "{order.id}" has been successfully updated.'
        }
        return JsonResponse(json_response, status=200)


class OrderPartialUpdateView(View):
    def patch(self, request, id):
        order = get_object_or_404(Order, id=id)
        data = json.loads(request.body)

        if 'status' in data and data['status'] in dict(Order.STATUS_CHOICES):
            order.status = data['status']
        if 'total_price' in data:
            order.total_price = data['total_price']

        order.save()
        json_response = {
            'message': f'Order "{order.id}" has been partially updated.'
        }
        return JsonResponse(json_response, status=200)


class PaymentCreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            order = Order.objects.get(id=data['order_id'])
            payment = Payment.objects.create(
                order=order,
                amount=data['amount'],
                method=data['method'],
                status=data.get('status', 'pending')
            )
            json_response = {
                'message': f'Payment for order "{order.id}" created successfully.',
                'payment_id': payment.id,
                'status': payment.status
            }
            return JsonResponse(json_response, status=201)
        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found.'}, status=404)


class PaymentRefundView(View):
    def post(self, request, id):
        payment = get_object_or_404(Payment, id=id)
        if payment.status != 'completed':
            return JsonResponse({"error": "Only completed payments can be refunded."}, status=400)

        payment.status = 'refunded'
        payment.save()
        json_response = {
            'message': f'Payment "{payment.id}" has been successfully refunded.'
        }
        return JsonResponse(json_response, status=200)
