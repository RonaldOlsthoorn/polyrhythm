# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: polyrhythm/polyrhythm.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='polyrhythm/polyrhythm.proto',
  package='polyrhythm',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bpolyrhythm/polyrhythm.proto\x12\npolyrhythm\"&\n\x08\x46raction\x12\x0b\n\x03num\x18\x01 \x01(\x05\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\x05\"V\n\x08Position\x12\x12\n\x05value\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12,\n\x0erepresentation\x18\x02 \x01(\x0b\x32\x14.polyrhythm.FractionB\x08\n\x06_value\">\n\x05\x43olor\x12\t\n\x01r\x18\x01 \x01(\x05\x12\t\n\x01g\x18\x02 \x01(\x05\x12\t\n\x01\x62\x18\x03 \x01(\x05\x12\x0e\n\x01\x61\x18\x04 \x01(\x05H\x00\x88\x01\x01\x42\x04\n\x02_a\">\n\x04Note\x12&\n\x08position\x18\x01 \x01(\x0b\x32\x14.polyrhythm.Position\x12\x0e\n\x06volume\x18\x02 \x01(\x02\"|\n\x06Rhythm\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nsound_path\x18\x02 \x01(\t\x12\x1f\n\x05notes\x18\x03 \x03(\x0b\x32\x10.polyrhythm.Note\x12%\n\x05\x63olor\x18\x04 \x01(\x0b\x32\x11.polyrhythm.ColorH\x00\x88\x01\x01\x42\x08\n\x06_color\"z\n\nPolyRhythm\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x0etime_signature\x18\x02 \x01(\x0b\x32\x14.polyrhythm.Fraction\x12\x0b\n\x03\x62pm\x18\x03 \x01(\x05\x12#\n\x07rhythms\x18\x04 \x03(\x0b\x32\x12.polyrhythm.Rhythmb\x06proto3'
)




_FRACTION = _descriptor.Descriptor(
  name='Fraction',
  full_name='polyrhythm.Fraction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='polyrhythm.Fraction.num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='denom', full_name='polyrhythm.Fraction.denom', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=81,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='polyrhythm.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='polyrhythm.Position.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='representation', full_name='polyrhythm.Position.representation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_value', full_name='polyrhythm.Position._value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=83,
  serialized_end=169,
)


_COLOR = _descriptor.Descriptor(
  name='Color',
  full_name='polyrhythm.Color',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='r', full_name='polyrhythm.Color.r', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='g', full_name='polyrhythm.Color.g', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='polyrhythm.Color.b', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='a', full_name='polyrhythm.Color.a', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_a', full_name='polyrhythm.Color._a',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=171,
  serialized_end=233,
)


_NOTE = _descriptor.Descriptor(
  name='Note',
  full_name='polyrhythm.Note',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='polyrhythm.Note.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volume', full_name='polyrhythm.Note.volume', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=235,
  serialized_end=297,
)


_RHYTHM = _descriptor.Descriptor(
  name='Rhythm',
  full_name='polyrhythm.Rhythm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='polyrhythm.Rhythm.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sound_path', full_name='polyrhythm.Rhythm.sound_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notes', full_name='polyrhythm.Rhythm.notes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='polyrhythm.Rhythm.color', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_color', full_name='polyrhythm.Rhythm._color',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=299,
  serialized_end=423,
)


_POLYRHYTHM = _descriptor.Descriptor(
  name='PolyRhythm',
  full_name='polyrhythm.PolyRhythm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='polyrhythm.PolyRhythm.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_signature', full_name='polyrhythm.PolyRhythm.time_signature', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bpm', full_name='polyrhythm.PolyRhythm.bpm', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rhythms', full_name='polyrhythm.PolyRhythm.rhythms', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=425,
  serialized_end=547,
)

_POSITION.fields_by_name['representation'].message_type = _FRACTION
_POSITION.oneofs_by_name['_value'].fields.append(
  _POSITION.fields_by_name['value'])
_POSITION.fields_by_name['value'].containing_oneof = _POSITION.oneofs_by_name['_value']
_COLOR.oneofs_by_name['_a'].fields.append(
  _COLOR.fields_by_name['a'])
_COLOR.fields_by_name['a'].containing_oneof = _COLOR.oneofs_by_name['_a']
_NOTE.fields_by_name['position'].message_type = _POSITION
_RHYTHM.fields_by_name['notes'].message_type = _NOTE
_RHYTHM.fields_by_name['color'].message_type = _COLOR
_RHYTHM.oneofs_by_name['_color'].fields.append(
  _RHYTHM.fields_by_name['color'])
_RHYTHM.fields_by_name['color'].containing_oneof = _RHYTHM.oneofs_by_name['_color']
_POLYRHYTHM.fields_by_name['time_signature'].message_type = _FRACTION
_POLYRHYTHM.fields_by_name['rhythms'].message_type = _RHYTHM
DESCRIPTOR.message_types_by_name['Fraction'] = _FRACTION
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['Color'] = _COLOR
DESCRIPTOR.message_types_by_name['Note'] = _NOTE
DESCRIPTOR.message_types_by_name['Rhythm'] = _RHYTHM
DESCRIPTOR.message_types_by_name['PolyRhythm'] = _POLYRHYTHM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Fraction = _reflection.GeneratedProtocolMessageType('Fraction', (_message.Message,), {
  'DESCRIPTOR' : _FRACTION,
  '__module__' : 'polyrhythm.polyrhythm_pb2'
  # @@protoc_insertion_point(class_scope:polyrhythm.Fraction)
  })
_sym_db.RegisterMessage(Fraction)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'polyrhythm.polyrhythm_pb2'
  # @@protoc_insertion_point(class_scope:polyrhythm.Position)
  })
_sym_db.RegisterMessage(Position)

Color = _reflection.GeneratedProtocolMessageType('Color', (_message.Message,), {
  'DESCRIPTOR' : _COLOR,
  '__module__' : 'polyrhythm.polyrhythm_pb2'
  # @@protoc_insertion_point(class_scope:polyrhythm.Color)
  })
_sym_db.RegisterMessage(Color)

Note = _reflection.GeneratedProtocolMessageType('Note', (_message.Message,), {
  'DESCRIPTOR' : _NOTE,
  '__module__' : 'polyrhythm.polyrhythm_pb2'
  # @@protoc_insertion_point(class_scope:polyrhythm.Note)
  })
_sym_db.RegisterMessage(Note)

Rhythm = _reflection.GeneratedProtocolMessageType('Rhythm', (_message.Message,), {
  'DESCRIPTOR' : _RHYTHM,
  '__module__' : 'polyrhythm.polyrhythm_pb2'
  # @@protoc_insertion_point(class_scope:polyrhythm.Rhythm)
  })
_sym_db.RegisterMessage(Rhythm)

PolyRhythm = _reflection.GeneratedProtocolMessageType('PolyRhythm', (_message.Message,), {
  'DESCRIPTOR' : _POLYRHYTHM,
  '__module__' : 'polyrhythm.polyrhythm_pb2'
  # @@protoc_insertion_point(class_scope:polyrhythm.PolyRhythm)
  })
_sym_db.RegisterMessage(PolyRhythm)


# @@protoc_insertion_point(module_scope)
