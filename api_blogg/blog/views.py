from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import (
    Categoria, Noticia, ArticuloSeccion, Nutricion,
    DietaComida, ComentarioComunidad, RespuestaComentario
)
from .serializers import (
    CategoriaSerializer, NoticiaSerializer, ArticuloSeccionSerializer,
    NutricionSerializer, DietaComidaSerializer, ComentarioComunidadSerializer,
    RespuestaComentarioSerializer
)


# ============================================
# CATEGORÍAS
# ============================================
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'status': 200,
            'message': 'Petición exitosa',
            'data': serializer.data
        })

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'status': 201,
                'message': 'Registro creado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'status': 400,
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                'success': True,
                'status': 200,
                'message': 'Petición exitosa',
                'data': serializer.data
            })
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'status': 200,
                    'message': 'Registro actualizado exitosamente',
                    'data': serializer.data
                })
            return Response({
                'success': False,
                'status': 400,
                'message': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.activo = False
            instance.save()
            return Response({
                'success': True,
                'status': 200,
                'message': 'Registro desactivado exitosamente'
            })
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)


# ============================================
# NOTICIAS
# ============================================
class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'status': 200,
            'message': 'Petición exitosa',
            'data': serializer.data
        })

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'status': 201,
                'message': 'Registro creado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'status': 400,
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                'success': True,
                'status': 200,
                'message': 'Petición exitosa',
                'data': serializer.data
            })
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'status': 200,
                    'message': 'Registro actualizado exitosamente',
                    'data': serializer.data
                })
            return Response({
                'success': False,
                'status': 400,
                'message': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.activo = False
            instance.save()
            return Response({
                'success': True,
                'status': 200,
                'message': 'Registro desactivado exitosamente'
            })
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)


# ============================================
# ARTÍCULOS SECCIONES
# ============================================
class ArticuloSeccionViewSet(viewsets.ModelViewSet):
    queryset = ArticuloSeccion.objects.all()
    serializer_class = ArticuloSeccionSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'status': 200,
            'message': 'Petición exitosa',
            'data': serializer.data
        })

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'status': 201,
                'message': 'Registro creado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'status': 400,
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                'success': True,
                'status': 200,
                'message': 'Petición exitosa',
                'data': serializer.data
            })
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'status': 200,
                    'message': 'Registro actualizado exitosamente',
                    'data': serializer.data
                })
            return Response({
                'success': False,
                'status': 400,
                'message': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.activo = False
            instance.save()
            return Response({
                'success': True,
                'status': 200,
                'message': 'Registro desactivado exitosamente'
            })
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)


# ============================================
# NUTRICIÓN
# ============================================
class NutricionViewSet(viewsets.ModelViewSet):
    queryset = Nutricion.objects.all()
    serializer_class = NutricionSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'status': 200,
            'message': 'Petición exitosa',
            'data': serializer.data
        })

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'status': 201,
                'message': 'Registro creado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'status': 400,
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                'success': True,
                'status': 200,
                'message': 'Petición exitosa',
                'data': serializer.data
            })
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'status': 200,
                    'message': 'Registro actualizado exitosamente',
                    'data': serializer.data
                })
            return Response({
                'success': False,
                'status': 400,
                'message': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.activo = False
            instance.save()
            return Response({
                'success': True,
                'status': 200,
                'message': 'Registro desactivado exitosamente'
            })
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)


# ============================================
# DIETA COMIDAS
# ============================================
class DietaComidaViewSet(viewsets.ModelViewSet):
    queryset = DietaComida.objects.all()
    serializer_class = DietaComidaSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'status': 200,
            'message': 'Petición exitosa',
            'data': serializer.data
        })

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'status': 201,
                'message': 'Registro creado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'status': 400,
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                'success': True,
                'status': 200,
                'message': 'Petición exitosa',
                'data': serializer.data
            })
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'status': 200,
                    'message': 'Registro actualizado exitosamente',
                    'data': serializer.data
                })
            return Response({
                'success': False,
                'status': 400,
                'message': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.activo = False
            instance.save()
            return Response({
                'success': True,
                'status': 200,
                'message': 'Registro desactivado exitosamente'
            })
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)


# ============================================
# COMENTARIOS COMUNIDAD
# ============================================
class ComentarioComunidadViewSet(viewsets.ModelViewSet):
    queryset = ComentarioComunidad.objects.all()
    serializer_class = ComentarioComunidadSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'status': 200,
            'message': 'Petición exitosa',
            'data': serializer.data
        })

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'status': 201,
                'message': 'Registro creado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'status': 400,
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                'success': True,
                'status': 200,
                'message': 'Petición exitosa',
                'data': serializer.data
            })
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'status': 200,
                    'message': 'Registro actualizado exitosamente',
                    'data': serializer.data
                })
            return Response({
                'success': False,
                'status': 400,
                'message': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.activo = False
            instance.save()
            return Response({
                'success': True,
                'status': 200,
                'message': 'Registro desactivado exitosamente'
            })
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)


# ============================================
# RESPUESTAS COMENTARIO
# ============================================
class RespuestaComentarioViewSet(viewsets.ModelViewSet):
    queryset = RespuestaComentario.objects.all()
    serializer_class = RespuestaComentarioSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'status': 200,
            'message': 'Petición exitosa',
            'data': serializer.data
        })

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'status': 201,
                'message': 'Registro creado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'status': 400,
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                'success': True,
                'status': 200,
                'message': 'Petición exitosa',
                'data': serializer.data
            })
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'status': 200,
                    'message': 'Registro actualizado exitosamente',
                    'data': serializer.data
                })
            return Response({
                'success': False,
                'status': 400,
                'message': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.activo = False
            instance.save()
            return Response({
                'success': True,
                'status': 200,
                'message': 'Registro desactivado exitosamente'
            })
        except Exception:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)