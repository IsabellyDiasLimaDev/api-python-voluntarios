from flask import request, jsonify
from flask_restful import Resource
from ..models import tables


class Voluntary(Resource):
    def get(self, name):
        voluntary = tables.Volunteers.query.filter_by(name=name).first()
        try:
            response = {
                'nome': voluntary.name,
                'sobrenome': voluntary.lastname,
                'bairro': voluntary.neighborhood,
                'cidade': voluntary.city,
                'id': voluntary.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'msg': 'Voluntário(a) não encontrado(a)'
            }
        return response

    def put(self, name):
        voluntary = tables.Volunteers.query.filter_by(name=name).first()
        data = request.json
        if 'nome' in data:
            voluntary.name = data['nome']
        if 'sobrenome' in data:
            voluntary.lastname = data['sobrenome']
        if 'bairro' in data:
            voluntary.neighborhood = data['bairro']
        if 'cidade' in data:
            voluntary.city = data['cidade']
        voluntary.save()
        response = {
            'id':voluntary.id,
            'nome': voluntary.name,
            'sobrenome': voluntary.lastname,
            'bairro': voluntary.neighborhood,
            'cidade': voluntary.city
        }
        return response

    def delete(self, name):
        try:
            voluntary = tables.Volunteers.query.filter_by(name=name).first()
            status = 'success'
            msg = 'Voluntário(a) {} excluído(a) com sucesso'.format(
                voluntary.name)
            voluntary.delete()
        except AttributeError:
            status = 'error'
            msg = 'Voluntário(a) com o nome {} não encontrado'.format(name)
        return jsonify({'status': status, 'mensagem': msg})


class AllVolunteers(Resource):
    def get(self):
        volunteers = tables.Volunteers.query.all()
        response = [{'id': i.id, 'nome': i.name, 'sobrenome': i.lastname,
                     'bairro': i.neighborhood, 'cidade': i.city} for i in volunteers]
        return  jsonify(response)
    
    def post(self):
        data = request.json
        voluntary = tables.Volunteers(name=data['nome'],lastname=data['sobrenome'],neighborhood=data['bairro'],city=data['cidade'])
        voluntary.save()
        response = {
            'id':voluntary.id,
            'nome': voluntary.name,
            'sobrenome': voluntary.lastname,
            'bairro': voluntary.neighborhood,
            'cidade': voluntary.city
        }
        return response