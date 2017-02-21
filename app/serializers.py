from rest_framework import serializers
from .models import Reimbursement, User


class ReimbursementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reimbursement
        fields = ('amount', 'description', 'attachment')


class ReimbursementGetSerializer(serializers.ModelSerializer):
    total_amount = serializers.IntegerField(read_only=True)

    class Meta:
        model = Reimbursement
        fields = ('total_amount', 'id', 'amount', 'description', 'attachment', 'reimbursed_flag', 'date_created',)


class AdminSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Reimbursement
        fields = (
            'username', 'id', 'amount', 'description', 'attachment', 'reimbursed_flag', 'date_created',)

    def get_username(self, obj):
        return obj.user.username

