# coding: utf-8

from django.conf.urls import patterns, url

urlpatterns = patterns('project.system',
   url(r'^consulta', 'views.consulta'),
   url(r'^inicio-pagamento/(?P<cpf>\d+)/', 'views.inicio_pagamento'),
   

   url(r'^emissao/(?P<id>\d+)/', 'views.emissao'),
   url(r'^processo/digitar/', 'views.digitar'),
   url(r'^gerar_boleto/(?P<id>\d+)/', 'views.gerar_boleto_pagamento'),

   url(r'^tr_mensal/consulta/', 'tr_mensal.consulta'),
   url(r'^tr_mensal/cadastro/', 'tr_mensal.cadastro'),
   url(r'^tr_mensal/edicao/(?P<id>\d+)/', 'tr_mensal.edicao'),

   )
