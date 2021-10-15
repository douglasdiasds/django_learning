Conceito das URL e Métodos do Django


class XPTO(views.ModelViewSet):
    serializer_class = bla // São herdados do modelviewset e o conjunto de mixins
    queryset = Objeto.objects.all() // São herdados do modelviewset e o conjunto de mixins

    Na Keeps normalmente sobrescrevemos (overwrite) os métodos que definem o serializer class e o queryset, que são:
    get_queryset()
    get_serializer_class()


Quando eu vou definir uma URL (ou resource, ou uma URI, ...) eu preciso informar quais métodos estão disponíveis
conforme verbo HTTP:

Sempre será um par de chaves {HTTP-VERB: ViewSet Metodo}

path('', StudentViewSet.as_view(QUAIS_METODOS??), name='student-list')

OS METODOS SAO:

'get': 'list',
'get': 'retrieve'
'put': 'update',
'patch': 'update'.
'delete': 'destroy'.
'post': 'create'

TODO list:
    - criar um serviço para calcular o tempo de uma missão baseado nos tempos do conteúdos ✓
    - chamar o serviço acima usando django.signals(observable) ✓
    - criar um serviço de matrícula para validar:
        - se o existe matrícula em andamento, não permitir uma nova matrícula ✓
        - criar um serviço para finalizar a matrícula ✓
        - se a nota for menor que 0.7 reprovar a matrícular ao finalizarz ✓
        - reiniciar uma matrícula (remover data de conclusão e nota):
            - matrícula só pode ser reinicializada se tiver concluída
            - matrícula só pode ser reinicializada se o curso não é obrigatório
