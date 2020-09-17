from flask import request, jsonify
from flask_restful import Resource
from ..models import tables


class SocialAction(Resource):
    def get(delf, name):
        social_action = tables.SocialActions.query.filter_by(name=name).first()
        try:
            response = {
                'id': social_action.id,
                'nome': social_action.name,
                'instituição': social_action.institution,
                'bairro': social_action.neighborhood,
                'cidade': social_action.city,
                'endereço': social_action.address,
                'descrição': social_action.description
            }
        except AttributeError:
            response = {
                'status': 'error',
                'msg': 'Ação social não encontrada'
            }
        return response

    def put(delf, name):
        social_action = tables.SocialActions.query.filter_by(name=name).first()
        data = request.json
        if 'nome' in data:
            social_action.name = data['nome']
        if 'instituição' in data:
            social_action.institution = data['instituição']
        if 'bairro' in data:
            social_action.neighborhood = data['bairro']
        if 'cidade' in data:
            social_action.city = data['cidade']
        if 'endereço' in data:
            social_action.address = data['endereço']
        if 'descrição' in data:
            social_action.description = data['descrição']

        social_action.save()
        response = {
            'id': social_action.id,
            'nome': social_action.name,
            'instituição': social_action.institution,
            'bairro': social_action.neighborhood,
            'cidade': social_action.city,
            'endereço': social_action.address,
            'descrição': social_action.description
        }
        return response

    def delete(self, name):
        try:
            social_action = tables.SocialActions.query.filter_by(
                name=name).first()
            status = 'success'
            msg = 'Ação social {} excluída com sucesso'.format(
                social_action.name)
            social_action.delete()
        except AttributeError:
            status = 'error'
            msg = 'Ação social com o nome {} não encontrado'.format(name)
        return jsonify({'status': status, 'mensagem': msg})


class AllActions(Resource):
    def get(delf):
        social_actions = tables.SocialActions.query.all()
        response = [{'id': i.id, 'nome': i.name, 'instituição': i.institution,
                     'bairro': i.neighborhood, 'cidade': i.city, 'endereço': i.address, 'descrição': i.description} for i in social_actions]
        return jsonify(response)
    def post(delf):
        data = request.json
        social_action = tables.SocialActions(
            name=data['nome'], institution=data['instituição'], neighborhood=data['bairro'], city=data['cidade'], address=data['endereço'], description=data['descrição'])
        social_action.save()
        response = {
            'id': social_action.id,
            'nome': social_action.name,
            'instituição': social_action.institution,
            'bairro': social_action.neighborhood,
            'cidade': social_action.city,
            'endereço': social_action.address,
            'descrição': social_action.description
        }
        return response
