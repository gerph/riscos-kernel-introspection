#!/usr/bin/python
"""
Build the C sources that define the layout of registers in the Register Dump Areas.

Taken from RISC OS Pyromaniac and butchered.
"""

import osplatformfeatures


class ArchRegister(object):
    """
    Register mapping for this architecture.
    """
    desctype = 'register'

    def __init__(self, regnumber, name, bitwidth, excoffset, regtype, synthetic=False, bitalignment=0):
        self.number = regnumber
        self.synthetic = synthetic
        self.name = name
        self.bitwidth = bitwidth
        self.excoffset = excoffset
        self.bitalignment = bitalignment

        """
        Register types:
            g:  general purpose register
            s:  stack register
            f:  processor flags
            p:  program counter
            l:  link register/generic register
        """
        self.regtype = regtype

    def __repr__(self):
        return "<{}({}: {} ({}), width={}, offset={})>".format(self.__class__.__name__,
                                                               self.number, self.name, self.regtype,
                                                               self.bitwidth, self.excoffset)

class ArchRegisterFlag(object):
    """
    Flag mapping within a register, for this architecture
    """
    desctype = 'flag'

    def __init__(self, bit, bitwidth, name, value=None, header_values=False, last=False):
        self.bit = bit
        self.bitwidth = bitwidth
        self.name = name
        self.value = value
        self.header_values = header_values
        self.last = last


class AArch32(object):
    name = "aarch32"
    archnum = osplatformfeatures.CPUArchitecture_AArch32
    archregs = [
            ArchRegister(0, 'r0', 32, 4 * 0, 'g'),
            ArchRegister(1, 'r1', 32, 4 * 1, 'g'),
            ArchRegister(2, 'r2', 32, 4 * 2, 'g'),
            ArchRegister(3, 'r3', 32, 4 * 3, 'g'),
            ArchRegister(4, 'r4', 32, 4 * 4, 'g'),
            ArchRegister(5, 'r5', 32, 4 * 5, 'g'),
            ArchRegister(6, 'r6', 32, 4 * 6, 'g'),
            ArchRegister(7, 'r7', 32, 4 * 7, 'g'),
            ArchRegister(8, 'r8', 32, 4 * 8, 'g'),
            ArchRegister(9, 'r9', 32, 4 * 9, 'g'),
            ArchRegister(10, 'r10', 32, 4 * 10, 'g'),
            ArchRegister(11, 'r11', 32, 4 * 11, 'g'),
            ArchRegister(12, 'r12', 32, 4 * 12, 'g'),
            ArchRegister(13, 'sp', 32, 4 * 13, 's'),
            ArchRegister(14, 'lr', 32, 4 * 14, 'l'),
            ArchRegister(15, 'pc', 32, 4 * 15, 'p', bitalignment=2),
            ArchRegister(16, 'CPSR', 32, 4 * 16, 'f'),

            ArchRegisterFlag(0, 4, "Mode", header_values=True),
            ArchRegisterFlag(0, 4, "USR", value=0x0),
            ArchRegisterFlag(0, 4, "FIQ", value=0x1),
            ArchRegisterFlag(0, 4, "IRQ", value=0x2),
            ArchRegisterFlag(0, 4, "SVC", value=0x3),
            ArchRegisterFlag(0, 4, "0100", value=0x4),
            ArchRegisterFlag(0, 4, "0101", value=0x5),
            ArchRegisterFlag(0, 4, "MON", value=0x6),
            ArchRegisterFlag(0, 4, "ABT", value=0x7),
            ArchRegisterFlag(0, 4, "1000", value=0x8),
            ArchRegisterFlag(0, 4, "1001", value=0x9),
            ArchRegisterFlag(0, 4, "HYP", value=0xA),
            ArchRegisterFlag(0, 4, "UND", value=0xB),
            ArchRegisterFlag(0, 4, "1100", value=0xC),
            ArchRegisterFlag(0, 4, "1101", value=0xD),
            ArchRegisterFlag(0, 4, "1110", value=0xE),
            ArchRegisterFlag(0, 4, "SYS", value=0xF, last=True),

            ArchRegisterFlag(4, 1, "Bitness", header_values=True),
            ArchRegisterFlag(4, 1, "26bit", value=0),
            ArchRegisterFlag(4, 1, "32bit", value=1, last=True),

            ArchRegisterFlag(5, 1, "Encoding", header_values=True),
            ArchRegisterFlag(5, 1, "ARM", value=0),
            ArchRegisterFlag(5, 1, "Thm", value=1, last=True),

            ArchRegisterFlag(6, 1, 'f'),
            ArchRegisterFlag(7, 1, 'i'),
            ArchRegisterFlag(8, 1, 'a'),
            ArchRegisterFlag(9, 1, 'e'),
            ArchRegisterFlag(27, 1, 'q'),
            ArchRegisterFlag(28, 1, 'v'),
            ArchRegisterFlag(29, 1, 'c'),
            ArchRegisterFlag(30, 1, 'z'),
            ArchRegisterFlag(31, 1, 'n'),

#            ArchRegister(17, 'SPSR', 32, None, 'f'),
        ]


class AArch64(object):
    name = "aarch64"
    archnum = osplatformfeatures.CPUArchitecture_AArch64
    archregs = [
            ArchRegister(0, 'x0', 64, 8 * 0, 'g'),
            ArchRegister(1, 'x1', 64, 8 * 1, 'g'),
            ArchRegister(2, 'x2', 64, 8 * 2, 'g'),
            ArchRegister(3, 'x3', 64, 8 * 3, 'g'),
            ArchRegister(4, 'x4', 64, 8 * 4, 'g'),
            ArchRegister(5, 'x5', 64, 8 * 5, 'g'),
            ArchRegister(6, 'x6', 64, 8 * 6, 'g'),
            ArchRegister(7, 'x7', 64, 8 * 7, 'g'),
            ArchRegister(8, 'x8', 64, 8 * 8, 'g'),
            ArchRegister(9, 'x9', 64, 8 * 9, 'g'),
            ArchRegister(10, 'x10', 64, 8 * 10, 'g'),
            ArchRegister(11, 'x11', 64, 8 * 11, 'g'),
            ArchRegister(12, 'x12', 64, 8 * 12, 'g'),
            ArchRegister(13, 'x13', 64, 8 * 13, 'g'),
            ArchRegister(14, 'x14', 64, 8 * 14, 'g'),
            ArchRegister(15, 'x15', 64, 8 * 15, 'g'),
            ArchRegister(16, 'x16', 64, 8 * 16, 'g'),
            ArchRegister(17, 'x17', 64, 8 * 17, 'g'),
            ArchRegister(18, 'x18', 64, 8 * 18, 'g'),
            ArchRegister(19, 'x19', 64, 8 * 19, 'g'),
            ArchRegister(20, 'x20', 64, 8 * 20, 'g'),
            ArchRegister(21, 'x21', 64, 8 * 21, 'g'),
            ArchRegister(22, 'x22', 64, 8 * 22, 'g'),
            ArchRegister(23, 'x23', 64, 8 * 23, 'g'),
            ArchRegister(24, 'x24', 64, 8 * 24, 'g'),
            ArchRegister(25, 'x25', 64, 8 * 25, 'g'),
            ArchRegister(26, 'x26', 64, 8 * 26, 'g'),
            ArchRegister(27, 'x27', 64, 8 * 27, 'g'),
            ArchRegister(28, 'x28', 64, 8 * 28, 'g'),
            ArchRegister(29, 'x29', 64, 8 * 29, 'g'),
            ArchRegister(30, 'lr', 64, 8 * 30, 'l'),
            ArchRegister(31, 'xzr', 64, 8 * 31, 'g'),

            ArchRegister(32, 'sp', 64, 8 * 32, 's', bitalignment=4),
            ArchRegister(33, 'pc', 64, 8 * 33, 'p', bitalignment=2),
            ArchRegister(34, 'PSTATE', 32, 8 * 34, 'f'),

            ArchRegisterFlag(0, 4, "M32", header_values=True),
            ArchRegisterFlag(0, 4, "USR", value=0x0),
            ArchRegisterFlag(0, 4, "FIQ", value=0x1),
            ArchRegisterFlag(0, 4, "IRQ", value=0x2),
            ArchRegisterFlag(0, 4, "SVC", value=0x3),
            ArchRegisterFlag(0, 4, "0100", value=0x4),
            ArchRegisterFlag(0, 4, "0101", value=0x5),
            ArchRegisterFlag(0, 4, "MON", value=0x6),
            ArchRegisterFlag(0, 4, "ABT", value=0x7),
            ArchRegisterFlag(0, 4, "1000", value=0x8),
            ArchRegisterFlag(0, 4, "1001", value=0x9),
            ArchRegisterFlag(0, 4, "HYP", value=0xA),
            ArchRegisterFlag(0, 4, "UND", value=0xB),
            ArchRegisterFlag(0, 4, "1100", value=0xC),
            ArchRegisterFlag(0, 4, "1101", value=0xD),
            ArchRegisterFlag(0, 4, "1110", value=0xE),
            ArchRegisterFlag(0, 4, "SYS", value=0xF, last=True),

            ArchRegisterFlag(2, 2, "EL", header_values=True),

            ArchRegisterFlag(4, 1, "Bitness", header_values=True),
            ArchRegisterFlag(4, 1, "64bit", value=0),
            ArchRegisterFlag(4, 1, "32bit", value=1, last=True),

            ArchRegisterFlag(6, 1, 'f'),
            ArchRegisterFlag(7, 1, 'i'),
            ArchRegisterFlag(8, 1, 's'),
            ArchRegisterFlag(9, 1, 'd'),

            ArchRegisterFlag(20, 1, 'l'),
            ArchRegisterFlag(21, 1, 't'),

            ArchRegisterFlag(28, 1, 'v'),
            ArchRegisterFlag(29, 1, 'c'),
            ArchRegisterFlag(30, 1, 'z'),
            ArchRegisterFlag(31, 1, 'n'),

            # FIXME: Include VFP registers ?
        ]


class Memory(object):
    def __init__(self, size, address=0):
        self.address = address
        self.size = size
        self.words = {}
        self.strings = {}

    def write_word(self, value, offset=0):
        self.words[self.address + offset] = value

    def write_string(self, value, offset=0):
        self.strings[self.address + offset] = value

    def __getitem__(self, index):
        return MemoryAlias(self, address=index)

    def hcode(self, varname):
        lines = []
        lines.append('typedef struct %s_s %s_t;' % (varname, varname))
        lines.append('extern const %s_t %s;' % (varname, varname))
        return lines

    def ccode(self, word_type, word_length, varname):
        words_size = (max(self.words.keys()) + word_length)
        nwords = int(words_size / word_length)
        highest_string = max(self.strings.keys())
        stringbytes = highest_string + len(self.strings[highest_string]) + 1 - words_size
        lines = []
        lines.append('typedef struct %s_s {' % (varname,))
        lines.append('    %s words[%i];' % (word_type, nwords))
        lines.append('    char strings[%i];' % (stringbytes,))
        lines.append('} %s_t;' % (varname,))
        lines.append('')
        lines.append('const %s_t %s = {' % (varname, varname))
        lines.append('    {')
        for offset in range(0, nwords):
            value = self.words.get(offset * word_length)
            if value is None:
                lines.append('        0, /* Not defined */')
            else:
                if word_length == 4:
                    lines.append('        0x%08X,' % (value & 0xFFFFFFFF,))
                elif word_length == 8:
                    lines.append('        0x%016X,' % (value & 0xFFFFFFFFFFFFFFFF,))
                else:
                    print("Unsupported word length?")
        lines[-1] = lines[-1].replace(',', '')

        lines.append('    },')
        stringbase = nwords * word_length
        end = stringbase + stringbytes
        offset = stringbase
        while offset < end:
            string = self.strings.get(offset)
            if string is None:
                lines.append('    "\0" /* Padding? */')
                offset += 1
            else:
                lines.append('    "%s\\0"' % (string,))
                offset += len(string) + 1
        lines.append('};')
        return lines


class MemoryAlias(Memory):
    def __init__(self, baseobject, address):
        super(MemoryAlias, self).__init__(baseobject.size - address, address)
        self.baseobject = baseobject
        self.words = baseobject.words
        self.strings = baseobject.strings


class RegisterDumpInfo(object):

    def __init__(self, arch):
        self.arch = arch
        self._descriptor = None

    def descriptor(self):
        if self._descriptor is None:
            descriptor_size = 16 + (16 * len(self.arch.archregs)) + 4
            strings_size = sum(len(ar.name) + 1 for ar in self.arch.archregs)
            descriptor = Memory(descriptor_size + strings_size)

            archnum = self.arch.archnum
            descriptor.write_word(archnum, offset=0)
            descriptor.write_word(4, offset=4)      # Min instruction length (FIXME)
            descriptor.write_word(4, offset=8)      # Max instruction length (FIXME)
            # Dump size is filled in once we've walked the table
            dump_size = 0
            ardesc = descriptor[16]
            stroffset = descriptor_size
            last_reg_was_flags = False
            for ar in self.arch.archregs:
                if ar.desctype == 'register':
                    deftype = (osplatformfeatures.CPURegisterType_Register << osplatformfeatures.CPURegisterTypeShift) | ar.number

                    nameoffset = stroffset
                    descriptor.write_string(ar.name, offset=stroffset)
                    stroffset += len(ar.name) + 1
                    if ar.excoffset is not None:
                        dumpoffset = ar.excoffset
                        dumpsize = int((ar.bitwidth + 7) / 8)
                        dumpend = dumpoffset + dumpsize
                        #print("%r is at offset &%x, width &%x" % (ar, dumpoffset, dumpsize))
                        dump_size = max(dump_size, dumpend)
                    else:
                        dumpoffset = -1

                    flags = ar.bitwidth
                    last_reg_was_flags = False
                    if ar.regtype == 'g':
                        flags |= osplatformfeatures.CPURegisterFlag_TypeGeneral << osplatformfeatures.CPURegisterFlag_Type_Shift
                    elif ar.regtype == 's':
                        flags |= osplatformfeatures.CPURegisterFlag_TypeStack << osplatformfeatures.CPURegisterFlag_Type_Shift
                    elif ar.regtype == 'l':
                        flags |= osplatformfeatures.CPURegisterFlag_TypeLink << osplatformfeatures.CPURegisterFlag_Type_Shift
                    elif ar.regtype == 'p':
                        flags |= osplatformfeatures.CPURegisterFlag_TypePC << osplatformfeatures.CPURegisterFlag_Type_Shift
                    elif ar.regtype == 'f':
                        flags |= osplatformfeatures.CPURegisterFlag_TypeFlags << osplatformfeatures.CPURegisterFlag_Type_Shift
                        last_reg_was_flags = True

                    flags |= ar.bitalignment << osplatformfeatures.CPURegisterFlag_BitAlignmentShift

                    ardesc.write_word(deftype, offset=0)
                    ardesc.write_word(nameoffset, offset=4)
                    ardesc.write_word(dumpoffset, offset=8)
                    ardesc.write_word(flags, offset=12)

                elif ar.desctype == 'flag':
                    if not last_reg_was_flags:
                        # FIXME: Malformed register description list. Report it?
                        continue

                    deftype = osplatformfeatures.CPURegisterType_Flag
                    deftype |= ar.bit << osplatformfeatures.CPURegisterTypeFlag_BaseBitShift
                    if ar.value is not None:
                        if ar.last:
                            deftype |= osplatformfeatures.CPURegisterTypeFlag_ValueEnd
                        else:
                            deftype |= osplatformfeatures.CPURegisterTypeFlag_ValueWithMore
                        deftype |= ar.value << osplatformfeatures.CPURegisterTypeFlag_ValueShift
                    else:
                        if ar.header_values:
                            deftype |= osplatformfeatures.CPURegisterTypeFlag_NameWithValues
                        else:
                            deftype |= osplatformfeatures.CPURegisterTypeFlag_Name

                    nameoffset = stroffset
                    descriptor.write_string(ar.name, offset=stroffset)
                    stroffset += len(ar.name) + 1

                    flags = ar.bitwidth

                    ardesc.write_word(deftype, offset=0)
                    ardesc.write_word(nameoffset, offset=4)
                    ardesc.write_word(0, offset=8)
                    ardesc.write_word(flags, offset=12)

                ardesc.address += 16

            # Terminator word
            ardesc.write_word(-1)

            descriptor.write_word(dump_size, offset=12)     # Register dump size
            self._descriptor = descriptor

        return self._descriptor


def generate_c_files(arch, cfilename, hfilename):
    cpuregs = RegisterDumpInfo(arch)
    descriptor = cpuregs.descriptor()

    ccode = descriptor.ccode('uint32_t', 4, 'cpuregisters_' + arch.name)
    with open(cfilename, 'w') as fh:
        fh.write("/* Autogenerated CPU registers for %s */\n" % (arch.name,))
        fh.write("\n")
        fh.write("#include <stdint.h>\n")
        fh.write("\n")
        for line in ccode:
            fh.write("%s\n" % (line,))

    hcode = descriptor.hcode('cpuregisters_' + arch.name)
    with open(hfilename, 'w') as fh:
        fh.write("/* Autogenerated CPU registers for %s */\n" % (arch.name,))
        fh.write("\n")
        fh.write("#ifndef CPUREGISTERS_%s_H\n" % (arch.name,))
        fh.write("#define CPUREGISTERS_%s_H\n" % (arch.name,))
        fh.write("\n")
        fh.write("#include <stdint.h>\n")
        fh.write("\n")
        for line in hcode:
            fh.write("%s\n" % (line,))
        fh.write("\n")
        fh.write("#endif\n")


generate_c_files(AArch32(), "c/cpuregisters_aarch32", "h/cpuregisters_aarch32")
generate_c_files(AArch64(), "c/cpuregisters_aarch64", "h/cpuregisters_aarch64")

if False:
    aarch64 = AArch64()
    cpuregs64 = RegisterDumpInfo(aarch64)
    descriptor64 = cpuregs64.descriptor()
