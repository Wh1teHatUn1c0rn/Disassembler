import capstone


def disassemble(file_path):
    with open(file_path, "rb") as f:
        code = f.read()

    md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
    for i in md.disasm(code, 0x1000):
        print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))


disassemble("/path/to/binary_file")
