from rest_framework import serializers
from .models import Subject, Teacher


class SubjectSerializer(serializers.ModelSerializer):
    """课程数据序列化器"""
    id = serializers.IntegerField

    class Meta:
        model = Subject
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
