from rest_framework import serializers

from .models import PackageRelease, Project
from .pypi import version_exists, latest_version


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ["name", "version"]
        extra_kwargs = {"version": {"required": False}}

    def validate(self, data):
        # TODO

        # Validar o pacote, checar se ele existe na versão especificada.
        # Buscar a última versão caso ela não seja especificada pelo usuário.
        # Subir a exceção `serializers.ValidationError()` se o pacote não
        # for válido.

        name = data.get('name', '')
        version = data.get('version', '')

        if version:
            exist = version_exists(name, version)

            if exist:
                return data
            else:
                raise serializers.ValidationError({"error": "One or more packages doesn't exist"})
        else:
            latest = latest_version(name)

            if latest:
                data['version'] = latest
                return data
            else:
                raise serializers.ValidationError({"error": "One or more packages doesn't exist"})



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "packages"]

    packages = PackageSerializer(many=True)

    def create(self, validated_data):
        # TODO
        # Salvar o projeto e seus pacotes associados.
        #
        # Algumas referência para uso de models do Django:
        # - https://docs.djangoproject.com/en/3.2/topics/db/models/
        # - https://www.django-rest-framework.org/api-guide/serializers/#saving-instances
        # com
        packages = validated_data["packages"]

        projeto = Project.objects.create(name=validated_data["name"])  

        for package in packages:
            PackageRelease.objects.create(project=projeto, name=package['name'], version=package['version'])


        return projeto
