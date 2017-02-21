from .serializers import ReimbursementSerializer, ReimbursementGetSerializer, AdminSerializer
from .models import Reimbursement
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from django.db.models import Sum, Count
# Create your views here.


@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication, BasicAuthentication))
def reimbursement_list(request):
    """
    List all reimbursements, or create a new reimbursement.
    """

    if request.method == 'GET':
        """
        Admin Access
        """
        if request.user.is_superuser:
            reimbursement = Reimbursement.objects.all().order_by('user')
            serializer = AdminSerializer(reimbursement, many=True)
            total_reimbursement_amount = Reimbursement.objects.filter(reimbursed_flag=False).aggregate(
                total_pending_reimbursement=Sum('amount'))
            total_reimbursement_amount.update([("details", serializer.data)])
            return Response(total_reimbursement_amount)

        """
        User Access
        """
        reimbursement = Reimbursement.objects.filter(user=request.user)
        user = request.user
        serializer = ReimbursementGetSerializer(reimbursement, many=True)
        total_reimbursement_amount = Reimbursement.objects.filter(user=user).aggregate(
            total_reimbursement=Sum('amount'))
        pending = Reimbursement.objects.filter(user=user, reimbursed_flag=False).aggregate(
            total_pending=Count('amount'))

        total_reimbursement_amount.update(pending)
        total_reimbursement_amount.update([("details", serializer.data)])

        return Response(total_reimbursement_amount)

    elif request.method == 'POST':
        serializer = ReimbursementSerializer(data=request.data)
        if serializer.is_valid():
            # Inspect validated field data.
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes((TokenAuthentication, BasicAuthentication))
def reimbursement_detail(request, pk):
    """
    Get a specific reimbursement
    """
    try:
        if request.user.is_superuser:
            reimbursements = Reimbursement.objects.get(pk=pk)
        else:
            reimbursements = Reimbursement.objects.filter(user=request.user).get(pk=pk)
    except Reimbursement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="Either this is not your reimbursement or it doesn't exist")

    if request.method == 'GET':
        """
        Allow Admin full access
        """
        if request.user.is_superuser:
            serializer = AdminSerializer(reimbursements)
            return Response(serializer.data)

        """
        User access
        """
        serializer = ReimbursementGetSerializer(reimbursements)
        return Response(serializer.data)



@api_view(['GET'])
@authentication_classes((TokenAuthentication, BasicAuthentication))
def pending_reimbursement(request):

    """
    Get the list and count of pending reimbursement of a user
    """
    if request.method == 'GET':
        """
        Admin Access
        """
        if request.user.is_superuser:
            total_reimbursement_amount = Reimbursement.objects.filter(reimbursed_flag=False).aggregate(
                total_pending_reimbursement=Sum('amount'))
            pending = Reimbursement.objects.filter(user=user, reimbursed_flag=False).aggregate(
                total_pending=Count('amount'))
            total_reimbursement_amount.update(pending)
            return Response(total_reimbursement_amount)

        """
        User Access
        """
        user = request.user
        total_reimbursement_amount = Reimbursement.objects.filter(user=user,reimbursed_flag=False).aggregate(
            total_pending_reimbursement=Sum('amount'))
        pending = Reimbursement.objects.filter(user=user, reimbursed_flag=False).aggregate(
            total_pending=Count('amount'))

        total_reimbursement_amount.update(pending)
  
        return Response(total_reimbursement_amount)
