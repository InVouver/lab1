# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        spisokFIO = ['Иван Сидоров', 'Петр Иванов', 'Николай Зайцев', 'Александр Овечкин', 'Сергей Мозякин',
                     'Илья Ковальчук', 'Павел Дацюк', 'Александр Радулов', 'Семен Петров','Игорь Акинфеев']
        import random
        spisokMO = []
        spisokPS = []
        spisokIT = []
        spisokBOS = []
        spisokSPORT = []

        inf=[]
        otl=[]
        otch=[]

        for i in range(len(spisokFIO)):
            spisokMO.append(random.randint(2, 5))
            spisokPS.append(random.randint(2, 5))
            spisokIT.append(random.randint(2, 5))
            spisokBOS.append(random.randint(2, 5))
            spisokSPORT.append(random.randint(2, 5))
            k=(spisokMO[i] + spisokPS[i] + spisokIT[i] + spisokBOS[i] + spisokSPORT[i]) / 5
            
            spis = {
                'id': i+1,
                'fio': spisokFIO[i],
                'mo': spisokMO[i],
                'ps': spisokPS[i],
                'it': spisokIT[i],
                'bos': spisokBOS[i],
                'sport': spisokSPORT[i],
                'average': k
            }
            inf.append(spis)
            if k==5:
                otl.append(spisokFIO[i])

            if k < 3:
                otch.append(spisokFIO[i])



        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': inf,

                'excellent_students': otl,
                'bad_students': otch
            }
        )
        return context



