# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: persona.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rpersona.proto\"\x97\x01\n\x07Persona\x12\x12\n\nlocal_name\x18\x01 \x01(\t\x12\x13\n\x0bmac_address\x18\x02 \x01(\t\x12\x10\n\x08node_num\x18\x03 \x01(\x05\x12\x12\n\npublic_key\x18\x04 \x01(\x0c\x12\x13\n\x0bprivate_key\x18\x05 \x01(\x0c\x12\x0b\n\x03uid\x18\x06 \x01(\x0c\x12\x0c\n\x04mask\x18\x07 \x01(\x0c\x12\r\n\x05owned\x18\x08 \x01(\x08\"H\n\x06Wallet\x12\x1d\n\x0bmy_personas\x18\x01 \x03(\x0b\x32\x08.Persona\x12\x1f\n\rpeer_personas\x18\x02 \x03(\x0b\x32\x08.Personab\x06proto3')



_PERSONA = DESCRIPTOR.message_types_by_name['Persona']
_WALLET = DESCRIPTOR.message_types_by_name['Wallet']
Persona = _reflection.GeneratedProtocolMessageType('Persona', (_message.Message,), {
  'DESCRIPTOR' : _PERSONA,
  '__module__' : 'persona_pb2'
  # @@protoc_insertion_point(class_scope:Persona)
  })
_sym_db.RegisterMessage(Persona)

Wallet = _reflection.GeneratedProtocolMessageType('Wallet', (_message.Message,), {
  'DESCRIPTOR' : _WALLET,
  '__module__' : 'persona_pb2'
  # @@protoc_insertion_point(class_scope:Wallet)
  })
_sym_db.RegisterMessage(Wallet)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PERSONA._serialized_start=18
  _PERSONA._serialized_end=169
  _WALLET._serialized_start=171
  _WALLET._serialized_end=243
# @@protoc_insertion_point(module_scope)
