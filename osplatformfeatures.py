"""
Constants for OS_PlatformFeatures from RISC OS Pyromaniac
"""

# Architecture register block constants
CPUArchitecture_AArch32 = 0
CPUArchitecture_AArch64 = 1
CPUArchitecture_X64 = 2

CPURegisterType_Register = (0<<24)
CPURegisterType_Flag = (1<<24)
CPURegisterType = (15<<24)
CPURegisterTypeShift = 24

# Field values in register type definitions
CPURegisterTypeRegister_ID = ((1<<24) - 1)

# Field values in flag type definitions
CPURegisterTypeFlag_BaseBit = (255<<0)
CPURegisterTypeFlag_BaseBitShift = 0
CPURegisterTypeFlag_Value = (0x3FFF<<8)
CPURegisterTypeFlag_ValueShift = 8
CPURegisterTypeFlag_Name = (0<<22)
CPURegisterTypeFlag_NameWithValues = (1<<22)
CPURegisterTypeFlag_ValueEnd = (2<<22)
CPURegisterTypeFlag_ValueWithMore = (3<<22)
CPURegisterTypeFlag_FieldMask = (3<<22)

CPURegisterFlag_BitWidth = (4095<<0)
CPURegisterFlag_BitWidthShift = 0
CPURegisterFlag_TypeGeneral = 0
CPURegisterFlag_TypeStack = 1
CPURegisterFlag_TypeLink = 2
CPURegisterFlag_TypePC = 3
CPURegisterFlag_TypeFlags = 4
CPURegisterFlag_Type = (15<<12)
CPURegisterFlag_Type_Shift = 12
CPURegisterFlag_BitAlignment = (15<<16)
CPURegisterFlag_BitAlignmentShift = 16
