# Disassembler

This code reads the binary file, creates a disassembler object using the capstone.Cs() function and then uses the
disasm() method to disassemble the code.

The output is a list of instructions, each containing the address, mnemonic and operands of the instruction.

Keep in mind that this is just an example and the code is not complete and you may have to adjust the parameters in capstone.

Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32) to match the architecture of the malware you are analyzing.

Also, it is important to note that disassembling the malware is just one step of the malware analysis process, and a complete analysis would also include additional techniques such as dynamic analysis, memory analysis and reverse engineering.
