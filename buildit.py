
import struct
import io
from ppci import ir, api
from textx.metamodel import metamodel_from_file


def parse():
    woot = metamodel_from_file('woot.tx')
    model = woot.model_from_file('test.say')

    module = ir.Module('main')
    func = ir.Procedure('main')
    module.add_function(func)
    block = ir.Block('entry')
    func.add_block(block)
    func.entry = block

    for statement in model.statements:
        text = statement.text
        data = struct.pack('<i', len(text)) + text.encode('ascii')
        text_val = ir.LiteralData(data, 'text')
        block.add_instruction(text_val)
        block.add_instruction(ir.ProcedureCall('crt_print', [text_val]))

    block.add_instruction(ir.Exit())

    return module


def generate_code(module):
    """ Generate code """
    march = 'x86_64'
    obj1 = api.ir_to_object([module], march)
    obj2 = api.asm('crt0.asm', march)
    obj3 = api.c3c(['crt0.c3'], [], march)
    obj = api.link([obj1, obj2, obj3])

    with open('test.oj', 'w') as f:
        obj.save(f)
    # api.objcopy(obj, 'code', 'elf', 'test.elf')


if __name__ == '__main__':
    module = parse()
    generate_code(module)

